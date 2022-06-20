
from main_database import fetech_firestore_doc_db
from types import BuiltinFunctionType
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.datatables import MDDataTable
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
Window.size = 650, 750


class View_route(MDApp):
    def build(self):
        return Builder.load_file('view.kv')

    def showTable(self):
        location_name=self.root.ids.location.text
        route_name=self.root.ids.route.text
        # result = fetech_firestore_doc_db(
        #     # 'Kathmandu', 'Kalanki-TIA')
        #     # "Kathmandu", "Kalanki-TIA ")
        # location_name,route_name)
        # print(result)
        # for x, y in result.to_dict().items():
        #     print(x,y)

        result = fetech_firestore_doc_db(location_name,route_name)
        # column_data = [(x, dp(20)) for x, y in result.to_dict().items()]
        # layout = AnchorLayout()
        data_tables =MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Stop Number ", dp(40)),
                ("Stop Name", dp(40))
            ],

            row_data=[(x, y) for x, y in result.to_dict().items()],
        )
        self.root.ids.table_box.add_widget(data_tables)
       



View_route().run()
