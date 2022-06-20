from sqlite3 import DatabaseError
from tkinter import dialog
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
# from create import create_db, fetch_db, update_db, delete_db


Window.size = 650, 750


class Tab(ScrollView, MDTabsBase):
    '''Class implementing content for a tab.'''
    pass


class Route_List(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file("tab.kv")

    def insert_db(self):
        bus_stops = {}
        dialog = None
        location_name = self.root.ids.location.text
        route_name = self.root.ids.route.text
        stops_key = self.root.ids.keys.text
        stops_val = self.root.ids.vals.text
        # bus_stops[stops_key] = stops_val
        # inserting into database
        print(stops_val)
        #  route_name, bus_stops)
        # try:
        #     create_db(location_name, route_name, bus_stops)
        #     self.dialog = MDDialog(
        #         title="Notificaton",
        #         text="...Insertion sucessfull...",
        #         # buttons=[
        #         #     MDFlatButton(text="Ok",on_release=self.dialog.dismiss())
        #         # ]
        #     )
        #     self.dialog.open()
        # except DatabaseError as e:
        #     self.dialog = MDDialog(
        #         title="Notification ",
        #         text="...Insertion Unsucessfull...",
        #         # buttons=[
        #         #     MDFlatButton(text="Ok",on_release=self.dialog.dismiss())
        #         # ]
        #     )
        #     self.dialog.open()
        #     print("Database error", e)

    def clear(self):
        self.root.ids.location_name.text = " "
        self.root.ids.route_name.text = " "
        self.root.ids.stops_key.text = " "
        self.root.ids.stops_val.text = " "

    def navigation_draw(self):
        print("Meu icons ")


Route_List().run()
