import cv2
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

# Set the window size
Window.size = (360, 640)

# Load the .kv file
Builder.load_file('camera_app.kv')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.img = Image()
        # Open the webcam using OpenCV
        self.capture = cv2.VideoCapture(0)
        # Schedule the update function
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update at 30 FPS

        self.add_widget(self.img)  # Add the Image widget to the screen

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Flip the frame vertically (flip code 0)
            frame = cv2.flip(frame, 0)
            
            # Convert the image to texture for Kivy
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
            self.img.texture = texture

    def go_to_settings(self, instance):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "settings"
    
    def on_flip(self, instance):
        print("Flipped!")
        
    def on_flash(self, instance):
        print("Flashed!")
    
    def captured(self, instance):
        print("Capture button pressed!")

    def on_stop(self):
        # Release the webcam when the app is closed
        if self.capture.isOpened():
            self.capture.release()

class SettingsScreen(Screen):
    def go_to_video(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "main"
        
    def adjust_volume(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "volume"
    
    def change_language(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "language"
        
    def flip_camera(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "flip"
        
    def manual_screen(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "manual"

class AdjustVolumeScreen(Screen):
    def go_to_settings(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "settings"

class ChangeLanguageScreen(Screen):
    def go_to_settings(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "settings"

class ManualScreen(Screen):
    def go_to_settings(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
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
