from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

KV = """
<Home>:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Home'
                        left_action_items: [["menu", lambda x: nav_draw.set_state()]]
                        elevation: 8
                    MDLabel:
                        text: 'Welcome'
                        #font_style: 'H1'
                        halign: 'center'
                        font_size: 100
                        bold: True


        MDNavigationDrawer:
            id: nav_draw
            BoxLayout:
                orientation: 'vertical'

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Enquiry Menu"
                            on_press:
                                nav_draw.set_state('close')
                                #root.manager.current = 'new'

                            IconLeftWidget:
                                icon: 'file-document-box-plus'

                        OneLineIconListItem:
                            text: "Help"
                            on_press:
                                nav_draw.set_state('close')
                                #root.manager.current = 'view'

                            IconLeftWidget:
                                icon: 'book-open'

"""


class Home(Screen):
    pass


class EnqiryMenu(Screen):
    pass


class Inquire(MDApp):

    def build(self):
        Builder.load_string(KV)
        return Home()


Inquire().run()
