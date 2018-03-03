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
            "main_menu_training_button": (282, 101, 319, 258),
            "fight": (113, 0, 390, 640),
            "time": (100, 299, 71, 341),
            "p1_health": (77, 297, 93, 51),
            "p1_trigger": (405, 129, 399, 57),
            "p1_ca": (409, 71, 418, 185),
            "p2_health": (77, 341, 93, 590),
            "p2_trigger": (399, 582, 405, 512),
            "p2_ca": (409, 567, 418, 456)
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