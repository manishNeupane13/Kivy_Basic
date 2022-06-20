from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# class MyGridLayout(Widget):

class Defaultdesign(Widget):
    Builder.load_file('default.kv')

class default(App):
    def build(self):
        return Builder.load_file('default.kv')
    

if __name__=="__main__":
    default().run()