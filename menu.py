from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
Screen:
    GridLayout:
        cols:1
        pos_hint: {'center_x': 0.9, 'center_y': 0.1}
        spacing:40
        MDTextField:
            id:username
            pos_hint: {'center_x': .25, 'center_y': .6}
            size_hint_x: None
            width: "200dp"
            hint_text: "username"
            on_focus: if self.focus: app.menu.open()
        MDTextField:
            id:field
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: None
            width: "200dp"
            hint_text: "Password"
            on_focus: if self.focus: app.menu.open()
'''


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class Test(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        print(self.screen)
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(56),
                "text": f"Item {i}",
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            } for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.field,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        menu_items2 = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(56),
                "text": f"Item {i}",
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            } for i in range(1,5)]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.username,
            items=menu_items2,
            position="bottom",
            width_mult=4,
        )

        return self.screen
    def set_item(self, text__item):
        self.screen.ids.field.text = text__item
        print(self.root.ids.field.text)
        self.menu.dismiss()

    def set_item(self, text__item):
        self.screen.ids.username.text = text__item
        print(self.root.ids.username.text)
        self.menu.dismiss()


Test().run()

