from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty

class MyLayout(Widget):
    Builder.load_file('label.kv')
class Info(BoxLayout):
    label_text = StringProperty('default')
    button_text = StringProperty('default')


 
class img(App):
    def build(self):
        return MyLayout()

    def on_start(self):
        
        for i in range(1, 20):
            print(f'hwlloo: {i+1}')
            # self.ids.label_name.text= f'{i} hwlloo: {i+1}'
            self.root.ids.box1.add_widget(Info(label_text=f'Label {i}'))
    
    
if __name__=="__main__":
    img().run()