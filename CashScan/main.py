
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.button import Button

from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.graphics import Color, Rectangle
from kivy.uix.camera import Camera

##### Window Size
Config.set('graphics', 'width', '540')
Config.set('graphics', 'height', '920')
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'position', 'auto')


###################### Costume ###############################


#######################   Main Screen ##########################################################################################################################
############################################################################################################################################################################
class CameraScreen(FloatLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        #self.add_widget(Label(text='Main Screen'))
        self.orientation = 'vertical'
        self.screen_manager = screen_manager

        with self.canvas.before:
            Color(240, 240, 240, 1)
            self.rect = Rectangle(size=(self.width, self.height), pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.camera = Camera(resolution=(540, 920), play=True)
        self.add_widget(self.camera)


        ### Settings Button ###
        btn = Button(size_hint=(None, None),
                     size=(110, 110),
                     pos_hint={'x': 0.82, 'y': 0.90},
                     background_normal='assets/settings.png',
                     background_down = 'assets/settings_png',
                     border = (0, 0, 0, 0),
                     background_color=(1, 1, 1, 1)
                     )

        btn.bind(on_press=self.go_to_settings)
        self.add_widget(btn)

        record_btn = Button(size_hint=(None, None),
                            size=(110, 110),
                            pos_hint={'x': 0.72, 'y': 0.07},
                            background_normal='assets/record.png',
                            background_down = 'assets/record_png',
                            border = (0, 0, 0, 0),
                            background_color=(1, 1, 1, 1)
                            )

        record_btn.bind(on_press=self.go_to_record)
        self.add_widget(record_btn)

        ## Capture/Record Button ####
        capture_btn = Button(size_hint=(None, None),
                             size=(150, 150),
                             pos_hint={'x': 0.37, 'y': 0.05},
                             background_normal='assets/capture.png',
                             background_down = 'assets/capture_png',
                             border = (0, 0, 0, 0),
                             background_color=(1, 1, 1, 1)
                             )

        #capture_btn.bind(on_press=self.capture_image)
        self.add_widget(capture_btn)


    def capture_image(self,instance):
        self.camera.export_to_jpg("image.jpg")
        print("Image saved as 'Image.jpg'.")

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_to_settings(self, instance):
        self.screen_manager.transition = SlideTransition(direction="left")
        self.screen_manager.current = "settings"

    def go_to_record(self, instance):
        self.screen_manager.transition = SlideTransition(direction="right")
        self.screen_manager.current = "record"



###############################################################################################################################################################################
##############################################################################################################################################################################

class RecordScreen(FloatLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.screen_manager = screen_manager

        with self.canvas.before:
            Color(240, 240, 240, 1)
            self.rect = Rectangle(size=(self.width, self.height), pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        #self.camera1 = Camera(resolution=(480,640), play=True)
        #self.add_widget(self.camera1)


        ### Settings Button ###
        btn = Button(size_hint=(None, None),
                     size=(110, 110),
                     pos_hint={'x': 0.82, 'y': 0.90},
                     background_normal='assets/settings.png',
                     background_down = 'assets/settings_png',
                     border = (0, 0, 0, 0),
                     background_color=(1, 1, 1, 1)
                     )
        btn.bind(on_press=self.go_to_settings)
        self.add_widget(btn)


        camera_btn = Button(size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.09, 'y': 0.09},
                            background_normal='assets/camera.png',
                            background_down='assets/camera.png',
                            border=(0, 0, 0, 0),
                            background_color=(1, 1, 1, 1)
                            )

        camera_btn.bind(on_press=self.go_to_camera)
        self.add_widget(camera_btn)

        ## Capture/Record Button ####
        record_btn = Button(size_hint=(None, None),
                             size=(150, 150),
                             pos_hint={'x': 0.37, 'y': 0.05},
                             background_normal = 'assets/capture.png',
                             background_down = 'assets/capture.png',
                             border = (0, 0, 0, 0),
                             background_color = (1, 1, 1, 1)
        )
        #capture_btn.bind(on_press=self.toggle_recording)
        self.add_widget(record_btn)




    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_to_settings(self, instance):
        self.screen_manager.transition = SlideTransition(direction="left")
        self.screen_manager.current = "settings"

    def go_to_camera(self, instance):
        self.screen_manager.transition = SlideTransition(direction="left")
        self.screen_manager.current = "camera"


########################## Settings Screen #############################################################################################################
############################################################################################################################################################################
class SettingScreen(FloatLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        #### BG COLOR
        with self.canvas.before:
            Color(240, 240, 240, 1)
            self.rect = Rectangle(size=(self.width, self.height), pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)




###########################    BACk Button   ###################################
        back_btn = Button(size_hint=(None, None),
                          size=(110, 110),
                          pos_hint={'x': 0.01, 'y': 0.88},
                          background_normal='assets/back.png',
                          background_down='assets/back.png',
                          border=(0, 0, 0, 0),
                          background_color=(1, 1, 1, 1)
                          )

        back_btn.bind(on_press=self.go_to_camera)
        self.add_widget(back_btn)

#################################### Settings Buttons #########

###################   VOLUME BUTTON #############################################
#################################################################################
        volume_btn = Button(size_hint=(None, None),
                            size=(150, 150),
                            pos_hint={'x': 0.18, 'y': 0.70},
                            background_normal='assets/volume.png',
                            background_down='assets/volume.png',
                            border=(0, 0, 0, 0),
                            background_color=(1, 1, 1, 1)
                            )

        volume_btn.bind(on_press=self.go_to_volume)  ##gO TO
        self.add_widget(volume_btn)

#############################   FLIP CAMERA BUTTON ###########################
##############################################################################
        flip_btn = Button(size_hint=(None, None),
                          size=(150, 150),
                          pos_hint={'x': 0.18, 'y': 0.45},
                          background_normal='assets/flip_camera.png',
                          background_down='assets/flip_camera.png',
                          border=(0, 0, 0, 0),
                          background_color=(1, 1, 1, 1)
                          )
        #flip_btn.bind(on_press=self.go_to_flip)  ##gO TO
        self.add_widget(flip_btn)


#############################   FLASH CAMERA BUTTON #############################
#################################################################################
        flash_btn = Button(size_hint=(None, None),
                           size=(150, 150),
                           pos_hint={'x': 0.60, 'y': 0.70},
                           background_normal='assets/flash.png',
                           background_down='assets/flash.png',
                           border=(0, 0, 0, 0),
                           background_color=(1, 1, 1, 1)
                           )

        flash_btn.bind(on_press=self.go_to_flash)  ##gO TO
        self.add_widget(flash_btn)


#############################   LANGUAGE BUTTON #################################
#################################################################################
        language_btn = Button(size_hint=(None, None),
                           size=(150, 150),
                           pos_hint={'x': 0.60, 'y': 0.45},
                              background_normal='assets/language.png',
                              background_down='assets/language.png',
                              border=(0, 0, 0, 0),
                              background_color=(1, 1, 1, 1)
                              )

        language_btn.bind(on_press=self.go_to_language)  ##gO TO
        self.add_widget(language_btn)




#############################   MANUAL BUTTON ###################################
#################################################################################
        manual_btn = Button(size_hint=(None, None),
                              size=(240, 240),
                              pos_hint={'x': 0.35, 'y': 0.15},
                            background_normal='assets/manual.png',
                            background_down='assets/manual.png',
                            border=(0, 0, 0, 0),
                            background_color=(1, 1, 1, 1)
                            )

        manual_btn.bind(on_press=self.go_to_guide)  ##gO TO
        self.add_widget(manual_btn)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


    def go_to_camera(self, instance):
        self.screen_manager.transition = SlideTransition(direction="right")
        self.screen_manager.current = "camera"

    def go_to_language(self, instance):
        self.screen_manager.transition = SlideTransition(direction="left")
        self.screen_manager.current = "language"

    def go_to_flash(self, instance):
        self.screen_manager.transition = SlideTransition(direction="left")
        self.screen_manager.current = "flash"

    #def go_to_flip(self, instance):
        #self.screen_manager.transition = SlideTransition(direction="left")
        #self.screen_manager.current = "flip"

    def go_to_volume(self, instance):
        self.screen_manager.transition = SlideTransition(direction="left")
        self.screen_manager.current = "volume"

    def go_to_guide(self, instance):
        self.screen_manager.transition = SlideTransition(direction="left")
        self.screen_manager.current = "guide"

######################################  FLASH SCREEN ##################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################################

class FlashScreen(FloatLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Flash Camera',
                              color =(0,0,0,1),
                              pos_hint={'x': 0.01, 'y': 0.30},
                              font_size=50
                              ))
        self.screen_manager = screen_manager
        ## BG Color
        with self.canvas.before:
            Color(240, 240, 240, 1)
            self.rect = Rectangle(size=(self.width, self.height), pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        back_btn = Button(size_hint=(None, None),
                          size=(110, 110),
                          pos_hint={'x': 0.01, 'y': 0.88},
                          background_normal='assets/back.png',
                          background_down='assets/back.png',
                          border=(0, 0, 0, 0),
                          background_color=(1, 1, 1, 1)
                          )


        back_btn.bind(on_press=self.go_to_settings)

        self.add_widget(back_btn)


    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


    def go_to_settings(self, instance):
        self.screen_manager.transition = SlideTransition(direction="right")
        self.screen_manager.current = "settings"







######################################  VOLUME SCREEN ##################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################################

class VolumeScreen(FloatLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Volume',
                              color =(0,0,0,1),
                              pos_hint={'x': 0.01, 'y': 0.30},
                              font_size=50
                              ))
        self.screen_manager = screen_manager
        ## BG Color
        with self.canvas.before:
            Color(240, 240, 240, 1)
            self.rect = Rectangle(size=(self.width, self.height), pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        back_btn = Button(size_hint=(None, None),
                          size=(110, 110),
                          pos_hint={'x': 0.01, 'y': 0.88},
                          background_normal='assets/back.png',
                          background_down='assets/back.png',
                          border=(0, 0, 0, 0),
                          background_color=(1, 1, 1, 1)
                          )

        back_btn.bind(on_press=self.go_to_settings)

        self.add_widget(back_btn)



    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


    def go_to_settings(self, instance):
        self.screen_manager.transition = SlideTransition(direction="right")
        self.screen_manager.current = "settings"






######################################  MANUAL SCREEN ##################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################################

class GuideScreen(FloatLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Guide',
                              color =(0,0,0,1),
                              pos_hint={'x': 0.01, 'y': 0.30},
                              font_size=50
                              ))
        self.screen_manager = screen_manager
        ## BG Color
        with self.canvas.before:
            Color(240, 240, 240, 1)
            self.rect = Rectangle(size=(self.width, self.height), pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        back_btn = Button(size_hint=(None, None),
                          size=(110, 110),
                          pos_hint={'x': 0.01, 'y': 0.88},
                          background_normal='assets/back.png',
                          background_down='assets/back.png',
                          border=(0, 0, 0, 0),
                          background_color=(1, 1, 1, 1)
                          )

        back_btn.bind(on_press=self.go_to_settings)

        self.add_widget(back_btn)



    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


    def go_to_settings(self, instance):
        self.screen_manager.transition = SlideTransition(direction="right")
        self.screen_manager.current = "settings"


########################### LANGUAGE SCREEN ############################################################################################################################################################
#####################################################################################################################################################################################################3
class LanguageScreen(FloatLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Language',
                              color =(0,0,0,1),
                              pos_hint={'x': 0.01, 'y': 0.30},
                              font_size=50
                              ))

        self.screen_manager = screen_manager
        ## BG Color
        with self.canvas.before:
            Color(240, 240,240, 1)
            self.rect = Rectangle(size=(self.width, self.height), pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        back_btn = Button(size_hint=(None, None),
                          size=(110, 110),
                          pos_hint={'x': 0.01, 'y': 0.88},
                          background_normal='assets/back.png',
                          background_down='assets/back.png',
                          border=(0, 0, 0, 0),
                          background_color=(1, 1, 1, 1)
                          )

        back_btn.bind(on_press=self.go_to_settings)

        self.add_widget(back_btn)

    def go_to_settings(self, instance):
        self.screen_manager.transition = SlideTransition(direction="right")
        self.screen_manager.current = "settings"

################## LANGUAGE CHOICE BUTTONS ##################
        language1_btn = Button(text='English',
                              size_hint=(None, None),
                              size =(470,80),
                              font_size=40,
                              color=(1,1,1,1),
                              pos_hint={'x': 0.15, 'y': 0.65},
                              background_normal='',
                              background_color=(0, 0, 0, 1))

        language2_btn = Button(text='Tagalog',
                              size_hint=(None, None),
                              size =(467,80),
                              font_size=40,
                              color=(1,1,1,1),
                              pos_hint={'x': 0.15, 'y': 0.48},
                              background_normal='',
                              background_color=(0, 0, 0, 1))

        language3_btn = Button(text='Bisaya',
                              size_hint=(None, None),
                              size =(467,80),
                              font_size=40,
                              color=(1,1,1,1),
                              pos_hint={'x': 0.15, 'y': 0.30},
                              background_normal='',
                              background_color=(0, 0, 0, 1))

        self.add_widget(language3_btn)
        self.add_widget(language2_btn)
        self.add_widget(language1_btn)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


###################### Screen Manager #####################################
class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        camera_screen = Screen(name='camera')
        camera_screen.add_widget(CameraScreen(self))

        record_screen = Screen(name='record')
        record_screen.add_widget(RecordScreen(self))

        settings_screen = Screen(name='settings')
        settings_screen.add_widget(SettingScreen(self))

        language_screen = Screen(name='language')
        language_screen.add_widget(LanguageScreen(self))

        flash_screen = Screen(name='flash')
        flash_screen.add_widget(FlashScreen(self))

        volume_screen = Screen(name='volume')
        volume_screen.add_widget(VolumeScreen(self))

        guide_screen = Screen(name='guide')
        guide_screen.add_widget(GuideScreen(self))

        self.add_widget(camera_screen)
        self.add_widget(record_screen)
        self.add_widget(settings_screen)
        self.add_widget(language_screen)
        self.add_widget(flash_screen)
        self.add_widget(volume_screen)
        self.add_widget(guide_screen)


###################### LOOP ###########################
class CashScan(App):
    def build(self):
        sm = ScreenManagement()
        return sm


if __name__ == '__main__':
    app = CashScan()
    app.run()
