
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class screen_layout(GridLayout):
    # initizalize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(screen_layout, self).__init__(**kwargs)
        # set the columns

        self.cols = 1
        # creating a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        # add widgets
        self.top_grid.add_widget(Label(text="NAME: "))
        # add input box
        self.name = TextInput(multiline=False,size_hint_x=None,width=500,size_hint_y=None,height=100)
        self.top_grid.add_widget(self.name)
        # add widgets
        self.top_grid.add_widget(Label(text="ADDRESS: "))
        # add input box
        self.address = TextInput(multiline=False, size_hint_x=None, width=500,size_hint_y=None,height=100)
        self.top_grid.add_widget(self.address)
        # add widgets
        self.top_grid.add_widget(Label(text="AGE: "))
        # add input box
        self.age = TextInput(multiline=False, size_hint_x=None, width=500,size_hint_y=None,height=100)
        self.top_grid.add_widget(self.age)
        # add widgets
        self.top_grid.add_widget(Label(text="NUMBER: "))
        # add input box
        self.number = TextInput(multiline=False, size_hint_x=None, width=500,size_hint_y=None,height=100)
        self.top_grid.add_widget(self.number)
        # add top grid into main grid
        self.add_widget(self.top_grid)
        # create submit
        self.submit = Button(text="SUBMIT", font_size=20,size_hint_y=None,height=50)
        # bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name=self.name.text
        age = self.age.text
        address = self.address.text
        number = self.number.text
        # printing to the terminal
        # print(f'hello {name}. Your are {age} years old living in {address}')

        self.add_widget(Label(text=f'He is mr {name}  who is {age} years old and lives in {address}. His contact number is {number}', font_size=22))


class button_app(App):
    def build(self):
        return screen_layout()


if __name__ == "__main__":
    button_app().run()
