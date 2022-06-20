#image slider 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


class MyLayout(Widget):
    Builder.load_file('checkbox.kv')
    def check_box_click(self,*args):
        print(args)
        if args[1]==True:
            self.ids.checkbox_result.text=f'You have selected : {self.ids.checkbox_label.text}'
        elif args[1]==False:
            self.ids.checkbox_result.text =f'You have selected : None '
            pass
        pass
   


class img(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    img().run()
