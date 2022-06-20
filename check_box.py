
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.properties import StringProperty


KV = '''
FloatLayout:
    MDLabel:
        size_hint: None, None
        size: "48dp", "48dp"
        text:"user"
        pos_hint: {'center_x': .75, 'center_y': .65}

    MDCheckbox:
        group:"usercategory"
        id:ch2
        text:"user"
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .75, 'center_y': .65}
        on_active:
            app.on_checkbox_active(*args)
            app.gender=self.text
    MDLabel:
        size_hint: None, None
        size: "48dp", "48dp"
        text:"driver"
        pos_hint: {'center_x': .5, 'center_y': .5}
    
    MDCheckbox:
        group:"usercategory"
        id:chk
        text:"driver"
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .5, 'center_y': .35}
        on_active:
            app.gender=self.text
            app.on_checkbox_active(*args)
'''


class Test(MDApp):
    gender=StringProperty("")
    def build(self):
        return Builder.load_string(KV)

    def on_checkbox_active(self, checkbox, value):
        # category = self.root.ids.ch2.text
        if value:
            # print(category)
            print('Gender',self.gender)
            print(value)
            print('The checkbox', checkbox, 'is active',
                  'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive',
                  'and', checkbox.state, 'state')


Test().run()
