from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from main_database import create_firestore_db


Window.size = 650, 750



class Route_List(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file("route.kv")

    def insert_db(self):
        bus_stops = {}
        dialog = None
        location_name = self.root.ids.location.text
        route_name = self.root.ids.route.text
        stops_key = self.root.ids.stops_keys.text
        stops_val = self.root.ids.stops_vals.text
        bus_stops[stops_key] = stops_val
        # inserting into database
        print("location", location_name, "route", route_name, bus_stops)
        try:
            create_firestore_db(location_name, route_name, bus_stops)
            self.dialog = MDDialog(
                title="Notificaton",
                text="...Insertion sucessfull...",
                # buttons=[
                #     MDFlatButton(text="Ok",on_release=self.dialog.dismiss())
                # ]
            )
            self.dialog.open()
        except:
            self.dialog = MDDialog(
                title="Notification ",
                text="...Insertion Unsucessfull...",
                # buttons=[
                #     MDFlatButton(text="Ok",on_release=self.dialog.dismiss())
                # ]
            )
            self.dialog.open()
            print("Database error")

    def clear(self):
        self.root.ids.location_name.text = " "
        self.root.ids.route_name.text = " "
        self.root.ids.stops_key.text = " "
        self.root.ids.stops_val.text = " "

    def navigation_draw(self):
        print("Meu icons ")


Route_List().run()
