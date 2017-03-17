import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder

class VKMenu(Screen):
    def on_save_btn_release(self,text_input):
        text = Label(text = "Data form patient {} was saved".format(text_input))
        pop_up = Popup(title="Update", content=text, size_hint=(.7, .7))
        pop_up.open()

class Analysis(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("vk.kv")

class VKApp(App):

    def build(self):
        return presentation
    
if __name__ == '__main__':
    VKApp().run()
