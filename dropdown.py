#image slider 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


class MyLayout(Widget):
    Builder.load_file('dropdown.kv')
    def spinner_clicked(self,value):
        self.ids.click_label.text=f' {value}'
   


class img(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    img().run()
