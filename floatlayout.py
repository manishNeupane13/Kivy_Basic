from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class MyLayout(Widget):
    Builder.load_file('float.kv')
    pass
class img(App):
    def build(self):
        return MyLayout()
if __name__=="__main__":
    img().run()