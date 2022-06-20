#image slider 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel



class MyLayout(TabbedPanel):
    Builder.load_file('tabs.kv')
    pass
       


class img(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    img().run()
