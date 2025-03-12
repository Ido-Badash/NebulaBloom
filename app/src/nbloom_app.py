from kivy.app import App
from widgets import MainWidget

class NBloomApp(App):
    def build(self):
        return MainWidget()