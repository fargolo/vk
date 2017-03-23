import kivy
kivy.require('1.9.1')

import subprocess

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from utils.raplysaattori.raplyzer import *

class Login(Screen):
    pass

class Session(Screen):
    pass

class Register(Screen):
    pass

class VKMenu(Screen):
    def on_save_btn_release(self,text_input):
        text = Label(text = "Data from patient {} was saved".format(text_input))
        pop_up = Popup(title="Update", content=text, size_hint=(.7, .7))
        # Insert function to save data do DB here (Twistar)
        pop_up.open()
    def on_send_btn_release(self,text_input):
        text = Label(text = "Data from patient {} was sent to server".format(text_input))
        pop_up = Popup(title="Update",content=text, size_hint=(.7, .7))
        # Insert function to send data to server here (Twistar)
        pop_up.open()

class Analysis(Screen):
    def on_phon_btn_release(self,input_id):
        local_lyr_dir = "transc" 
        int_id = int(input_id) - 1
        phon_output = read_lyrics(lyrics_dir = local_lyr_dir, language="en-us", lookback=15, patient_id=int_id)
        return phon_output
    def on_lsa_btn_release(self):
        subprocess.call ("utils/lsa.R")
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("vk.kv")

class VKApp(App):

    def build(self):
        return presentation
    
if __name__ == '__main__':
    VKApp().run()
