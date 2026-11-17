from collections.abc import Mapping
# from worlds.AutoWorld import World
from rule_builder.cached_world import CachedRuleBuilderWorld
from . import options as gd_options
from . import items, locations, rules, web_world, regions
from typing import Any

class GDWorld(CachedRuleBuilderWorld):
    """Jump and fly your way through danger in this rhythm-based action platformer! 
    Geometry Dash is a platformer devoloped by RobTop and released on August 13th, 2013 on mobile devices
    and on December 22nd, 2014 on Steam."""
    #taken from steam

    # The name of the game (duh)
    game = "Geometry Dash"

    # Define how the game will be displayed on the website
    web = web_world.GDWebWorld()

    # Associate the options defined in options.py
    options_dataclass = gd_options.GDOptions
    options: gd_options.GDOptions

    # Define static dictionaries for better readability and reusability
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    # Generate the world
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self):
        rules.set_all_rules(self)

        self.multiworld.completion_condition[self.player] = (
            lambda state: state.has("Game Beaten", self.player)
        )

    def create_items(self):
        items.create_all_items(self)

    # Create item method for other files (used in items.py)
    def create_item(self, name: str) -> items.GDItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    topology_present = False
    gd_base_id = 130820130
    startinglevelslist = ["Stereo Madness"]

    # TODO: Add possible starting levels
    # Currently, AP always starts with Stero Madness, however the player can choose
    # to start with a certain number of levels later on (from Stereo Madness to Time Machine)

    def fill_slot_data(self) -> Mapping[str, Any]:
        # gotta do all this because apcpp dont got bools it seems
        # Haven't seen apcpp yet so will leave this untouched for now
        # if self.options.coins.value:
        #     coinsVal = 1
        # else:
        #     coinsVal = 0
        # if self.options.check_shop.value:
        #     checkShopVal = 1
        # else:
        #     checkShopVal = 0
        ultimateVal = 1 if self.options.ultimate else 0
        coinLocksVal = 1 if self.options.coin_locks else 0
        return {
            "ultimate": ultimateVal,
            "death_link": self.options.death_link.value,
            "death_link_amnesty": self.options.death_link_amnesty.value,
            "coin_locks": coinLocksVal,
            "goal_requirement": self.options.goal_requirement.value,
            # "speed": self.options.speed.value,
            # "start_levels": self.options.start_levels.value,
            # "startinglevels": startinglevelslist,
            # "coins": coinsVal,
            # "check_shop": checkShopVal,
        }