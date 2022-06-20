from tkinter import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):
    user_name =ObjectProperty(None)
    user_password=ObjectProperty(None)
    
    def logger(self):
        user_name=self.user_name.text
        user_password=self.user_password.text
        print(f'user name :{user_name}, password :{user_password}')
    def clear(self):
        print("Helo'")


class mylang(App):
    def build(self):
        return MyGridLayout()

if __name__=='__main__':
    mylang().run()

