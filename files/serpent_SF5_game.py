from serpent.game import Game

from .api.api import SF5API

from serpent.utilities import Singleton
from serpent.input_controller import KeyboardKey

import time

class SerpentSF5Game(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"
        kwargs["window_name"] = "StreetFighterV"

        kwargs["app_id"] = 310950
        kwargs["app_args"] = {"windowed":None,"ResX=1280":None,"ResY=720":None,"NOSPLASH":None}

        super().__init__(**kwargs)

        self.api_class = SF5API
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:100x100|GRAYSCALE|FLOAT"

    @property
    def screen_regions(self):
        regions = {
            "MENU_BUTTON_START": (475, 505, 445, 775),
            "MENU_BUTTON_TRAINING": (517, 203, 444, 516),
            "MENU_STAGESELECT": (110, 780, 84, 500),
            "MENU_PLAYERSELECT": (449, 818, 424, 462),
            "FIGHTZONE": (109, 1, 657, 1279),
            "TIMER": (28, 683, 76, 597),
            "P1_HEALTH": (36, 594, 63, 102),
            "P2_HEALTH": (63, 685, 37, 1178),
            "P1_TRIGGER": (691, 259, 678, 114),
            "P2_TRIGGER": (690, 1021, 678, 1180),
            "P1_CA": (715, 369, 697, 143),
            "P2_CA": (715, 910, 698, 1136),
            "P1_DIZZY": (79, 446, 68, 594),
            "P2_DIZZY": (67, 833, 80, 685),
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets

    def after_launch(self):
        self.is_launched = True

        time.sleep(15)

        self.window_id = self.window_controller.locate_window(self.window_name)

        self.window_controller.move_window(self.window_id, 0, 0)
        self.window_controller.focus_window(self.window_id)

        self.window_geometry = self.extract_window_geometry()

        print(self.window_geometry)