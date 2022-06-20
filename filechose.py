from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class MyLayout(Widget):
    Builder.load_file('filechose.kv')
    def selected(self,filename):
        try:

            self.ids.my_image.source=filename[0]
            # print(filename)
        except:

            pass
        
    
class img(App):
    def build(self):
        return MyLayout()
if __name__=="__main__":
    img().run()