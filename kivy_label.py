#Hello World!
#Initial test
print("Hello World")

import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        test_label = Label(text='Hello world', font_size='50sp')

        return test_label


if __name__ == '__main__':
    MyApp().run()