from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.graphics import Color, Rectangle
from kivy.uix.camera import Camera

##### Window Size
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')
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

        self.camera = Camera(resolution=(480, 640), play=True)
        self.add_widget(self.camera)


        ### Settings Button ###
        btn = Button(size_hint=(None, None),
                     size=(70, 70),
                     pos_hint={'x': 0.86, 'y': 0.91},
                     background_normal='',
                     background_color=(0, 0, 0, 0)
                     )
        icon = Image(source='assets/settings.png',
                     size_hint=(None, None),
                     size=(60, 60),
                     pos=(521,915))
        btn.add_widget(icon)
        btn.bind(on_press=self.go_to_settings)
        self.add_widget(btn)

        record_btn = Button(size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.75, 'y': 0.09},
                            background_normal='',
                            background_color=(.7, .7, .7, 0))
        record_icon = Image(source='assets/record.png',
                            size_hint=(None, None),
                            size=(80, 80),
                            pos=(455,85)
                            )
        record_btn.add_widget(record_icon)
        record_btn.bind(on_press=self.go_to_record)
        self.add_widget(record_btn)

        ## Capture/Record Button ####
        capture_btn = Button(size_hint=(None, None),
                             size=(150, 150),
                             pos_hint={'x': 0.37, 'y': 0.05},
                             background_normal='',
                             background_color=(.7, .7, .7, 0))
        capture_btn_icon = Image(source='assets/capture.png',
                                 size_hint=(None, None),
                                 size=(140, 140),
                                 pos=(227,55)
                                 )
        capture_btn.add_widget(capture_btn_icon)
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
                     size=(70, 70),
                     pos_hint={'x': 0.86, 'y': 0.91},
                     background_normal='',
                     background_color=(0, 0, 0, 0)
                     )
        icon = Image(source='assets/settings.png',
                     size_hint=(None, None),
                     size=(60, 60),
                     pos=(521,915))
        btn.add_widget(icon)
        btn.bind(on_press=self.go_to_settings)
        self.add_widget(btn)


        camera_btn = Button(size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.09, 'y': 0.09},
                            background_normal='',
                            background_color=(.7, .7, .7, 0))
        camera_icon = Image(source='assets/camera.png',
                            size_hint=(None, None),
                            size=(70, 70),
                            pos=(58,90))
        camera_btn.add_widget(camera_icon)
        camera_btn.bind(on_press=self.go_to_camera)
        self.add_widget(camera_btn)

        ## Capture/Record Button ####
        record_btn = Button(size_hint=(None, None),
                             size=(150, 150),
                             pos_hint={'x': 0.37, 'y': 0.05},
                             background_normal='',
                             background_color=(.7, .7, .7, 0))
        record_btn_icon = Image(source='assets/capture.png',
                                 size_hint=(None, None),
                                 size=(140, 140),
                                 pos=(227,55)
                                 )
        record_btn.add_widget(record_btn_icon)
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
                          size=(70, 70),
                          pos_hint={'x': 0.02, 'y': 0.91},
                          background_normal='',
                          background_color=(0, 0, 0, 0)
                          )
        back_icon = Image(source='assets/back.png',
                          size_hint=(None, None),
                          size=(90, 90),
                          pos=(0,900)
                          )

        back_btn.add_widget(back_icon)
        back_btn.bind(on_press=self.go_to_camera)

        self.add_widget(back_btn)

#################################### Settings Buttons #########

###################   VOLUME BUTTON #############################################
#################################################################################
        volume_btn = Button(size_hint=(None, None),
                            size=(150, 150),
                            pos_hint={'x': 0.18, 'y': 0.70},
                            background_normal='',
                            background_color=(0, 0, 0, 0)
                            )

        volume_icon = Image(source='assets/volume.png',
                            size_hint=(None, None),
                            size=(140, 140),
                            pos=(112, 708)
                            )

        volume_btn.add_widget(volume_icon)
        volume_btn.bind(on_press=self.go_to_volume)  ##gO TO
        self.add_widget(volume_btn)

#############################   FLIP CAMERA BUTTON ###########################
##############################################################################
        flip_btn = Button(size_hint=(None, None),
                            size=(150, 150),
                            pos_hint={'x': 0.18, 'y': 0.45},
                            background_normal='',
                            background_color=(0, 0, 0, 0)
                            )

        flip_icon = Image(source='assets/flip_camera.png',
                            size_hint=(None, None),
                            size=(140, 140),
                            pos=(112, 455)
                            )

        flip_btn.add_widget(flip_icon)
        #flip_btn.bind(on_press=self.go_to_flip)  ##gO TO
        self.add_widget(flip_btn)


#############################   FLASH CAMERA BUTTON #############################
#################################################################################
        flash_btn = Button(size_hint=(None, None),
                            size=(150, 150),
                            pos_hint={'x': 0.60, 'y': 0.70},
                            background_normal='',
                            background_color=(0, 0, 0, 0)
                            )

        flash_icon = Image(source='assets/flash.png',
                            size_hint=(None, None),
                            size=(150, 150),
                            pos=(370, 708)
                            )

        flash_btn.add_widget(flash_icon)
        flash_btn.bind(on_press=self.go_to_flash)  ##gO TO
        self.add_widget(flash_btn)


#############################   LANGUAGE BUTTON #################################
#################################################################################
        language_btn = Button(size_hint=(None, None),
                           size=(150, 150),
                           pos_hint={'x': 0.60, 'y': 0.45},
                           background_normal='',
                           background_color=(0, 0, 0, 0)
                           )

        language_icon = Image(source='assets/language.png',
                           size_hint=(None, None),
                           size=(140, 140),
                           pos=(365, 450)
                           )

        language_btn.add_widget(language_icon)
        language_btn.bind(on_press=self.go_to_language)  ##gO TO
        self.add_widget(language_btn)




#############################   MANUAL BUTTON ###################################
#################################################################################
        manual_btn = Button(size_hint=(None, None),
                              size=(240, 240),
                              pos_hint={'x': 0.32, 'y': 0.15},
                              background_normal='',
                              background_color=(0, 0, 0, 0)
                              )

        manual_icon = Image(source='assets/manual.png',
                              size_hint=(None, None),
                              size=(220, 220),
                              pos=(200, 150)
                              )

        manual_btn.add_widget(manual_icon)
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

        back3_btn = Button(size_hint=(None, None),
                          size=(70, 70),
                          pos_hint={'x': 0.02, 'y': 0.91},
                          background_normal='',
                          background_color=(0, 0, 0, 0)
                          )
        back3_icon = Image(source='assets/back.png',
                          size_hint=(None, None),
                          size=(90, 90),
                          pos=(0, 900)
                          )

        back3_btn.add_widget(back3_icon)
        back3_btn.bind(on_press=self.go_to_settings)

        self.add_widget(back3_btn)









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

        back4_btn = Button(size_hint=(None, None),
                          size=(70, 70),
                          pos_hint={'x': 0.02, 'y': 0.91},
                          background_normal='',
                          background_color=(0, 0, 0, 0)
                          )
        back4_icon = Image(source='assets/back.png',
                          size_hint=(None, None),
                          size=(90, 90),
                          pos=(0, 900)
                          )

        back4_btn.add_widget(back4_icon)
        back4_btn.bind(on_press=self.go_to_settings)

        self.add_widget(back4_btn)



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

        back5_btn = Button(size_hint=(None, None),
                          size=(70, 70),
                          pos_hint={'x': 0.02, 'y': 0.91},
                          background_normal='',
                          background_color=(0, 0, 0, 0)
                          )
        back5_icon = Image(source='assets/back.png',
                          size_hint=(None, None),
                          size=(90, 90),
                          pos=(0, 900)
                          )

        back5_btn.add_widget(back5_icon)
        back5_btn.bind(on_press=self.go_to_settings)

        self.add_widget(back5_btn)



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

        back2_btn = Button(size_hint=(None, None),
                          size=(70, 70),
                          pos_hint={'x': 0.02, 'y': 0.91},
                          background_normal='',
                          background_color=(0, 0, 0, 0)
                          )
        back2_icon = Image(source='assets/back.png',
                          size_hint=(None, None),
                          size=(90, 90),
                          pos=(0, 900)
                          )

        back2_btn.add_widget(back2_icon)
        back2_btn.bind(on_press=self.go_to_settings)

        self.add_widget(back2_btn)

    def go_to_settings(self, instance):
        self.screen_manager.transition = SlideTransition(direction="right")
        self.screen_manager.current = "settings"

################## LANGUAGE CHOICE BUTTONS ##################
        language1_btn = Button(text='English',
                              size_hint=(None, None),
                              size =(420,50),
                              font_size=30,
                              color=(1,1,1,1),
                              pos_hint={'x': 0.15, 'y': 0.55},
                              background_normal='',
                              background_color=(0, 0, 0, 1))

        language2_btn = Button(text='Tagalog',
                              size_hint=(None, None),
                              size =(420,50),
                              font_size=30,
                              color=(1,1,1,1),
                              pos_hint={'x': 0.15, 'y': 0.45},
                              background_normal='',
                              background_color=(0, 0, 0, 1))

        language3_btn = Button(text='Bisaya',
                              size_hint=(None, None),
                              size =(420,50),
                              font_size=30,
                              color=(1,1,1,1),
                              pos_hint={'x': 0.15, 'y': 0.35},
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