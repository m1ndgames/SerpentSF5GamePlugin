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
        kwargs["app_args"] = {"windowed":None,"ResX=640":None,"ResY=480":None,"NOSPLASH":None}

        super().__init__(**kwargs)

        self.api_class = SF5API
        self.api_instance = None

        self.frame_transformation_pipeline_string = "FLOAT"

    @property
    def screen_regions(self):
        regions = {
            "MENU_BUTTON_START": (283, 252, 297, 388),
            "MENU_BUTTON_TRAINING": (282, 101, 319, 258),
            "FIGHTZONE": (113, 1, 390, 639),
            "TIMER": (100, 299, 71, 341),
            "P1_HEALTH": (77, 297, 93, 51),
            "P1_TRIGGER": (405, 129, 399, 57),
            "P1_CA": (409, 71, 418, 185),
            "P2_HEALTH": (77, 341, 93, 590),
            "P2_TRIGGER": (399, 582, 405, 512),
            "P2_CA": (409, 567, 418, 456)
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