import sys
import logging
from pathlib import Path
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from screens.focus import FocusScreen
from utils import SafePath, load_builder_files

# Load the KV files
safe_path = SafePath(Path("app/src/screens"))
focus_screen_path = "focus/focus_screen.kv"
all_paths = [focus_screen_path]
load_builder_files(Builder, safe_path, all_paths)

class MainScreen(Screen):
    pass

class NBloomSM(ScreenManager):
    pass

class NBloomApp(App):
    def build(self):
        sm = NBloomSM()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(FocusScreen(name="focus"))
        return sm


def catch_it(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            sys.exit(1)
    return wrapper

@catch_it
def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    
    logging.info("Program started")

    NBloomApp().run()

    logging.info("Program ended")
    sys.exit(0)

if __name__ == "__main__":
    main()