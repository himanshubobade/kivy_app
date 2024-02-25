'''
### LABEL  ####
from kivy.app import App #to launch app
from kivy.uix.label import Label #Label
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

class MainApp(App):
    def build(self):
        label = Label(text="Himanshu",font_size='20sp',color='black',bold=True,italic=True)
        return label

MainApp().run()
'''

'''
#### BUTTON ON PRESS ##########

from kivy.app import App #to launch app
from kivy.uix.label import Label #Label
from kivy.core.window import Window

from kivy.uix.button import Button

Window.clearcolor = (1,1,1,1)

class MainApp(App):
    def build(self):
        button = Button(text="Click",size_hint=(0.5,0.1),
                        font_size='20sp',pos_hint={'center_x':0.5,'center_y':0.3},
                        on_press=self.printpress,
                        on_release=self.printrelease)#button size percent
        return button
        #label = Label(text="Himanshu",font_size='20sp',color='black',bold=True,italic=True)
        #return label

    def printpress(self,obj):
        print("I'm clicked")

    def printrelease(self,obj):
        print("Button released")

MainApp().run()
'''

'''
#### Image dispalying ##########
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image # to add an image from system folder
from kivy.uix.image import AsyncImage # to import an image from an url

Window.clearcolor = (1,1,1,1)

class MainApp(App):
    def build(self):
        #img1 = Image(source='1.jpg')  # import image from system
        #return img1
        img2 = AsyncImage(source='https://akm-img-a-in.tosshub.com/businesstoday/images/story/202107/share_1200x675_092019020355_1-sixteen_nine.jpg?size=1200:675')
        return img2
MainApp().run()
'''

'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
Window.size = (360,600) #fixes window size.. for testing mobile interface

Window.clearcolor = (1,1,1,1)
class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',spacing=10,padding=50) #way widgets will arrange
        btn1 = Button(text='click')
        btn2 = Button(text='Sqeeze me')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout

MainApp().run()
'''
'''
###### Image and button and reseize  ###########
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
Window.size = (360,600) #fixes window size.. for testing mobile interface

Window.clearcolor = (1,1,1,1)
class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',spacing=10,padding=50) #way widgets will arrange
        img=Image(source='1.jpg')
        button = Button(text="Teddy",size_hint=(0.7,0.15),
                        width=100,
                        height = 50,
                        pos_hint={'center_x':0.5,'center_y':0})
        layout.add_widget(img)
        layout.add_widget(button)
        return layout

MainApp().run()
'''
'''
### GridLayout ##
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window
#Window.size = (360,600) #fixes window size.. for testing mobile interface

Window.clearcolor = (1,1,1,1)
class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2,row_force_default=True,row_default_height=40)
        btn1 = Button(text="button1",size_hint=(None,None),width=100,height=40)
        btn2 = Button(text="button2")
        btn3 = Button(text="button3",size_hint=(None,None),width=100,height=40)
        btn4 = Button(text="button4")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

MainApp().run()
'''
'''
### Nested GridLayout and text input #####
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
class MainApp(App):
    def build(self):
        layout= GridLayout(cols=2)
        self.weight = TextInput(text="Enter weight here")
        self.height = TextInput(text="Enter height here")
        submit = Button(text='Submit',on_press=self.submit)
        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)
        return layout
    def submit(self,obj):
        print("Weight is " + self.weight.text)
        print("Height is " + self.height.text)


MainApp().run()
'''


#############################################################################
#############################################################################
########################### K  I  V  Y - M  D ###############################
#############################################################################
#############################################################################
'''
## SYNTAX #######
from kivymd.app import MDApp

class DemoApp(MDApp):
    def build(self):
        return

DemoApp().run()
'''
'''
#### labels and text styles #######
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon

class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text="Hello",halign='center',theme_text_color='Custom',
                        text_color=(0,0,1,1),
                        font_style='H1')
        icon_label = MDIcon(icon='language-python',halign='center')
        return icon_label

DemoApp().run()
'''
'''
##### Themes and color palettes #########
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text="Hello",
                                pos_hint={'center_x':0.5,'center_y':0.5})
        icon_btn = MDIconButton(icon='android',
                                pos_hint={'center_x':0.5,'center_y':0.5})
        action_btn = MDFloatingActionButton(icon='android',
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #screen.add_widget(icon_btn)
        #screen.add_widget(btn_flat)
        screen.add_widget(action_btn)
        return screen

DemoApp().run()
'''
'''
#### Color palette ####
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Yellow'
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style="Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text="Hello",
                                pos_hint={'center_x':0.5,'center_y':0.5})
        screen.add_widget(btn_flat)
        return screen

DemoApp().run()
'''
'''
##### User Input with text field #######
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
#from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

username_helper="""
MDTextField:
    hint_text: "Enter username"
    helper_text:"or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right:"android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300
    
"""

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette="Green"
        #username = MDTextField(text='Enter a Username',
        #                       pos_hint={'center_x':0.5,'center_y':0.5},
        #                       size_hint_x=None,width=300)
        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen

DemoApp().run()
'''
'''
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from helpers import username_helper

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x':0.5,'center_y':0.5})
        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        screen.add_widget(button)
        return screen


DemoApp().run()
'''
'''
from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.button import Button
class MainApp(App):
    def build(self):
        #label = Label(text="Hello World")
        button = Button(text="Click me", size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'center_y':0.5})
        return button

MainApp().run()
'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

from kivy.core.window import Window
Window.size = (360,600) #fixes window size.. for testing mobile interface

Window.clearcolor = (1,1,1,1)
class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',spacing=10,padding=50) #way widgets will arrange
        img=Image(source='androidios.jpg')
        button = Button(text="Submit",size_hint=(0.7,0.15),
                        width=100,
                        height = 50,
                        pos_hint={'center_x':0.5,'center_y':0})
        layout.add_widget(img)
        layout.add_widget(button)
        return layout

MainApp().run()