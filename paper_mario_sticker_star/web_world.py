from collections.abc import Sequence

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .constants import GAME
from .options import option_groups, option_presets


class PMSSWebWorld(WebWorld):
    game = GAME

    theme = "grassFlowers"

    option_groups = option_groups
    options_presets = option_presets

    rich_text_options_doc = True

    tutorials: Sequence[Tutorial] = [
        Tutorial(
            "Paper Mario Sticker Star Setup Guide",  # Tutorial Name
            "A guide to setting up Paper Mario Sticker Star for MultiWorld.",  # Description
            "English",  # Language
            "setup_en.md",  # File name under the world's /docs folder
            "setup/en",  # Link, unused?
            ["EternalCode"],  # Author
        )
    ]
