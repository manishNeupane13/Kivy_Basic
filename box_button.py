import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class screen_layout(GridLayout):
    #initizalize infinite keywords
    def __init__(self,**kwargs):
        #call grid layout constructor
        super(screen_layout,self).__init__(**kwargs)
        #set the columns
    
        self.cols=4
        #add widgets
        self.add_widget(Label(text="NAME: "))
        #add input box
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)
           #add widgets
        self.add_widget(Label(text="ADDRESS: "))
        #add input box
        self.address=TextInput(multiline=False)
        self.add_widget(self.address)
        #add widgets
        self.add_widget(Label(text="AGE: "))
        #add input box
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)
        #add widgets
        self.add_widget(Label(text="NUMBER: "))
        #add input box
        self.number = TextInput(multiline=False)
        self.add_widget(self.number)
        #create submit 
        self.submit=Button(text="SUBMIT",font_size=20)
        #bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    def press(self,instance):
        name=self.name.text
        age=self.age.text
        address=self.address.text
        number=self.number.text
        #printing to the terminal 
        # print(f'hello {name}. Your are {age} years old living in {address}')

        self.add_widget(Label(text=name,font_size=12))
        self.add_widget(Label(text=age,font_size=12))
        self.add_widget(Label(text=number,font_size=12))
        self.add_widget(Label(text=address,font_size=12))


class button_app(App):
    def build(self):
        return screen_layout()
if __name__=="__main__":
    button_app().run()