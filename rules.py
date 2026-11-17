from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll

from .locations import LOCATION_NAME_TO_ID
from .items import ITEM_NAME_TO_ID

if TYPE_CHECKING:
   from .world import GDWorld

LEVEL_PORTAL_REQUIREMENTS = {
    "Cycles": ("Ball Portal"),
    "xStep": ("Ball Portal"),
    "Clutterfunk": ("Ball Portal"),

    "Theory of Everything": ("Ball Portal", "UFO Portal"),
    "Electroman Adventures": ("Ball Portal", "UFO Portal"),
    "Clubstep": ("Ball Portal", "UFO Portal"),
    "Electrodynamix": ("Ball Portal", "UFO Portal"),

    "Hexagon Force": ("Ball Portal", "UFO Portal"),
    "Blast Processing": (
        "Ball Portal", "UFO Portal", "Wave Portal"
    ),
    "Theory of Everything 2": ("Ball Portal", "UFO Portal", "Wave Portal"),
    "Geometrical Dominator": (
        "Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"
    ),
    "Deadlocked": (
        "Ball Portal", "UFO Portal", "Wave Portal",
        "Robot Portal"
    ),
    "Fingerdash": (
        "UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"
    ),
    "Dash": (
        "Ball Portal", "Wave Portal", "Robot Portal",
        "Spider Portal", "Swing Portal"
    ),
    "The Cellar": ("Robot Portal"),
    "The Secret Hollow": ("Ball Portal"),
}


def set_all_rules(world: GDWorld) -> None:
    # level rules!
    set_all_entrance_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: GDWorld) -> None:
    """Set entrance rules so that the run can start properly"""
    # Set rules for transitions from the menu to the other regions
    for level_name in LOCATION_NAME_TO_ID:
        # Starting levels are accessible without an unlock item.
        entrance_name = f"Menu to {level_name}"

        if level_name in world.startinglevelslist:
            continue

        requirements = list(LEVEL_PORTAL_REQUIREMENTS.get(level_name, ()))

        unlock_item = f"{level_name}: Unlock"
        if unlock_item in ITEM_NAME_TO_ID:
            requirements.append(unlock_item)

        if requirements:
            world.set_rule(
                world.get_entrance(entrance_name),
                HasAll(*requirements),
            )

def set_completion_condition(world: GDWorld) -> None:

    # Default goal is to complete The Secret Hollow for now
    # TODO: Add more goals
    # TODO: Add a number of levels needed to be beaten in order to access The Secret Hollow (See Ultrakill AP)
    world.set_completion_rule(Has("Game Beaten"))

