#image slider 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
#define screen of different forms

class Firstwindow(Screen):
    pass
class Secondwindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass


kv=Builder.load_file('multiscreen.kv')

   


class img(App):
    def build(self):
        return kv


if __name__ == "__main__":
    img().run()
