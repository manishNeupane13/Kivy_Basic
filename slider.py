from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


class MyLayout(Widget):
    Builder.load_file('slide.kv')
    def slide_it(self,*args):
        print(args[1])
        self.ids.label_demo.text=str(int(args[1]))
        self.ids.label_demo.font_size = str(int(args[1]))

        pass


class img(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    img().run()
