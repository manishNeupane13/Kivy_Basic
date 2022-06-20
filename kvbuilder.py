from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# class MyGridLayout(Widget):
#     Builder.load_file('builder_name.kv')
#     def press(self):
#         pass


class builder(App):
    user_name = ObjectProperty(None)
    user_password = ObjectProperty(None)

    def build(self):
        return Builder.load_file('builder_name.kv')

    def logger(self):
        user_name = self.user_name.text
        user_password = self.user_password.text
        print(f'user name :{user_name}, password :{user_password}')

    def clear(self):
        print("Helo'")
        # return MyGridLayout()


if __name__ == '__main__':
    builder().run()
