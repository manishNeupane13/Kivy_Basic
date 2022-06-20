from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

kv = """
<InfoLine>:
    size_hint_y: None
    height: 48
    Label:
        text: root.label_text
    Button:
        text: root.button_text
        on_release: print(f'Button: {self.text} pressed')
    
BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'BoxLayout in a ScrollView'
        size_hint_y: None
        height: 48
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        scroll_type:['bars', 'content']
        bar_width: 20
        BoxLayout:
            orientation: 'vertical'
            id: sv_box
            size_hint_y: None
            height: self.minimum_height
            Label:
                text:"Hello"
            InfoLine:
            InfoLine:
                label_text: 'Test'
                button_text: 'Initialized in kv'
               
"""


class InfoLine(BoxLayout):
    label_text = StringProperty('default')
    button_text = StringProperty('default')


class ScrollBoxApp(App):
    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        for i in range(100):
            self.root.ids.sv_box.add_widget(
                InfoLine(label_text=f'Label {i}', button_text=f'Button {i}'))


ScrollBoxApp().run()
