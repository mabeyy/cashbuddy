from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.camera import Camera

# Set the window size
Window.size = (360, 640)

# Load the .kv file
Builder.load_file('camera_app.kv')

class MainScreen(Screen):        
    def go_to_settings(self, instance):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "settings"
    
    def on_flip(self, instance):
        print("Flipped!")
        
    def on_flash(self, instance):
        print("Flashed!")
    
    def captured(self, instance):
        print("Capture button pressed!")
    
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

class FlipCameraScreen(Screen):
    def go_to_settings(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "settings"
        
    def switch_callback(self, switchObject, switchValue):
        if(switchValue):
            print('Switch is ON:):):)')
        else:
            print('Switch is OFF:(:(:(')

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
        sm.add_widget(FlipCameraScreen(name='flip'))
        sm.add_widget(ManualScreen(name='manual'))
        return sm

if __name__ == '__main__':
    CameraApp().run()
