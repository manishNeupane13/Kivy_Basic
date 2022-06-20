
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget

class Layoutdesign(Widget):
    Builder.load_file('boxlayout.kv')
    pass

class layoutApp(App):
    def build(self):
        return Layoutdesign()

if __name__=="__main__":
    layoutApp().run()

