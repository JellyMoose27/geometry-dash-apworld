from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class GDWebWorld(WebWorld):
    game = "Geometry Dash"
    theme = "ocean"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide for setting up Geometry Dash + Geode for the Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["1257Plays", "Jelly Moose"]
    )

    tutorials = [setup_en]
