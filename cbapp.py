import cv2
from gtts import gTTS
import os
import platform
from queue import Queue
import threading
from queue import Queue
from roboflow import Roboflow
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.clock import Clock

# Initialize Roboflow and load model
rf = Roboflow(api_key="LtOWijXg0XxaIFvnHuZo")
model = rf.workspace().project("philippine-money-nbgvl-rgoa8").version(1).model

# Define label-to-value mapping
value_map = {
    "1": 1, "5": 5, "10": 10, "20": 20,
    "50": 50, "100": 100, "200": 200,
    "500": 500, "1000": 1000
}

# Set the window size
Window.size = (360, 640)

# Load the .kv file
Builder.load_file('app.kv')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.language = 'en'
        self.img = Image()
        self.capture = None
        self.update_interval = None  
        self.prediction_queue = Queue()
        self.running = True

        self.add_widget(self.img)  # Add the Image widget to the screen

        self.frame_thread = None
        self.stop_thread = False
        self.frame_count = 0
        self.frame_skip = 5
        self.processing_thread = None
    
    def change_language(self, language):
        self.language = language

    def on_enter(self):
        """Restart the camera and clock when entering the MainScreen."""
        if self.capture is None or not self.capture.isOpened():
            self.capture = cv2.VideoCapture(0)  
        if self.update_interval is None:  # If the update function is not scheduled, schedule it
            self.update_interval = Clock.schedule_interval(self.update, 1.0 / 30.0)  # Resume the update

        if not self.frame_thread or not self.frame_thread.is_alive():
            self.stop_thread = False
            self.frame_thread = threading.Thread(target=self.capture_and_process)
            self.frame_thread.start()

    def on_leave(self):
        """Stop the camera and clock when leaving the MainScreen."""
        if self.capture and self.capture.isOpened():
            self.capture.release()
        if self.update_interval:  # Unschedule the update if it's scheduled
            Clock.unschedule(self.update)
            self.update_interval = None  # Set to None after unscheduling
        self.stop_thread = True
        if self.frame_thread and self.frame_thread.is_alive():
            self.frame_thread.join()

    def capture_and_process(self):
        while not self.stop_thread:
            ret, frame = self.capture.read()
            if ret:
                # Flip the frame vertically (flip code 0)
                frame = cv2.flip(frame, 0)

                self.frame_count += 1
                if self.frame_count % self.frame_skip == 0:  # Skip frames to reduce processing load
                    # Resize the frame to reduce the resolution
                    frame_resized = cv2.resize(frame, (640, 360))  # Lower resolution for faster processing

                    # Add frame to queue for prediction
                    self.prediction_queue.put(frame_resized)

                    # Start prediction in a separate thread
                    if not self.processing_thread or not self.processing_thread.is_alive():
                        self.processing_thread = threading.Thread(target=self.process_predictions_in_background)
                        self.processing_thread.start()

    def process_predictions_in_background(self):
        if not self.prediction_queue.empty():
            frame = self.prediction_queue.get()

            # Save the current frame temporarily for prediction
            temp_image_path = "temp_frame.jpg"
            cv2.imwrite(temp_image_path, frame)

            # Perform prediction
            response = model.predict(temp_image_path, confidence=70, overlap=30).json()

            # Delete the temporary image file
            os.remove(temp_image_path)

            # Calculate total sum from predictions
            total_sum = self.process_predictions(response)

            # Generate and play speech
            if total_sum > 0:
                # Generate and play speech only if the sum is greater than 0
                self.play_text_to_speech(f'{total_sum} peso')

            # Draw bounding boxes on the image
            self.draw_bounding_boxes(frame, response)

            # Add processed frame to the queue for UI thread to update
            self.prediction_queue.put(frame)

    def update(self, dt):
        if not self.prediction_queue.empty():
            frame = self.prediction_queue.get()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
            self.img.texture = texture

    def process_predictions(self, response):
        total_sum = 0
        for pred in response['predictions']:
            total_sum += value_map.get(pred['class'], 0)
        return total_sum

    def play_text_to_speech(self, text):
        tts = gTTS(text, lang=self.language)
        temp_file = '/tmp/temp.mp3'
        tts.save(temp_file)
        os.system(f'mpg321 {temp_file}')
        os.remove(temp_file)

    def draw_bounding_boxes(self, frame, response):
        for pred in response['predictions']:
            x, y, w, h = int(pred['x']), int(pred['y']), int(pred['width']), int(pred['height'])
            label = pred['class']
            start, end = (x - w // 2, y - h // 2), (x + w // 2, y + h // 2)
            cv2.rectangle(frame, start, end, (0, 255, 0), 2)
            cv2.putText(frame, label, (start[0], start[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

    def on_stop(self):
        """Release the camera when the app is closed."""
        if self.capture and self.capture.isOpened():
            self.capture.release()
        if self.update_interval:  # Unschedule the update function if needed
            Clock.unschedule(self.update)

    def go_to_settings(self, instance):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "settings"

    def on_flip(self, instance):
        print("Flipped!")
        
    def on_flash(self, instance):
        print("Flashed!")

class SettingsScreen(Screen):
    def go_to_video(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "main"
        # Resume the camera and clock when returning to MainScreen
        self.manager.get_screen('main').on_enter()

    def adjust_volume(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "volume"

    def change_language(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "language"
        
    def manual_screen(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "manual"
        
class AdjustVolumeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.max_volume = 100
        self.min_volume = 0
        self.system_volume = self.get_system_volume()

        # Create the volume label
        self.volume_label = Label(
            text=f"Volume: {self.system_volume}%",
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.3}
        )
        self.add_widget(self.volume_label)

        # Bind key events and create buttons
        Window.bind(on_key_down=self.on_key_down)

    def get_system_volume(self):
        if platform.system() == "Windows":
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            from comtypes import CLSCTX_ALL
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = interface.QueryInterface(IAudioEndpointVolume)
            return int(volume.GetMasterVolumeLevelScalar() * 100)
        elif platform.system() == "Linux":
            result = os.popen("amixer -D pulse sget Master").read()
            return int(result.split('[')[1].split(']')[0].replace('%', '').strip())
        elif platform.system() == "Darwin":
            return int(os.popen("osascript -e 'output volume of (get volume settings)'").read().strip())
        return 100

    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        if key in (273, 274):  # Up and Down Arrow Keys
            self.adjust_volume(5 if key == 273 else -5)

    def adjust_volume(self, delta):
        self.system_volume = max(self.min_volume, min(self.system_volume + delta, self.max_volume))
        self.set_system_volume()
        self.update_volume_label()

    def set_system_volume(self):
        if platform.system() == "Windows":
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            from comtypes import CLSCTX_ALL
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = interface.QueryInterface(IAudioEndpointVolume)
            volume.SetMasterVolumeLevelScalar(self.system_volume / 100.0, None)
        elif platform.system() == "Linux":
            os.system(f"amixer -D pulse sset Master {self.system_volume}%")
        elif platform.system() == "Darwin":
            os.system(f"osascript -e 'set volume output volume {self.system_volume}'")

    def update_volume_label(self):
        self.volume_label.text = f"Volume: {self.system_volume}%"

    def go_to_settings(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "settings"

class ChangeLanguageScreen(Screen):
    def change_to_english(self, instance):
        self.manager.get_screen('main').change_language('en')

    def change_to_filipino(self, instance):
        self.manager.get_screen('main').change_language('tl')
        
    def go_to_settings(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "settings"

class ManualScreen(Screen):
    def go_to_settings(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "settings"

class CameraApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(AdjustVolumeScreen(name='volume'))
        sm.add_widget(ChangeLanguageScreen(name='language'))
        sm.add_widget(ManualScreen(name='manual'))
        return sm

if __name__ == '__main__':
    CameraApp().run()
