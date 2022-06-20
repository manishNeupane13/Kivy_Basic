from kivymd.app import MDApp
# from farmermapview import FarmersMapView
from searchpopupmenu import SearchPopupMenu
from gpshelper import GPSHelper

class MainApp(MDApp):
    connection=None
    cursor=None
    search_menu=None

    def on_start(self):
        self.theme_cls.primary_palette='BlueGary'
        GPSHelper().run()

        self.search_menu=SearchPopupMenu()

if __name__=='__main__':
    MainApp().run()
