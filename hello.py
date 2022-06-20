
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="My name is Manish Neupane.",font_size=12)


if __name__=='__main__':
    MyApp().run()