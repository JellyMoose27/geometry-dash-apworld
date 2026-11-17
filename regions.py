from __future__ import annotations
from typing import TYPE_CHECKING
from .locations import LOCATION_NAME_TO_ID
from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import GDWorld

LEVEL_NAMES = [
    "Stereo Madness",
    "Back On Track",
    "Polargeist",
    "Dry Out",
    "Base After Base",
    "Cant Let Go",
    "Jumper",
    "Time Machine",
    "Cycles",
    "xStep",
    "Clutterfunk",
    "Theory of Everything",
    "Electroman Adventures",
    "Clubstep",
    "Electrodynamix",
    "Hexagon Force",
    "Blast Processing",
    "Theory of Everything 2",
    "Geometrical Dominator",
    "Deadlocked",
    "Fingerdash",
    "Dash",
    "The Tower",
    "The Sewers",
    "The Cellar",
    "The Secret Hollow",
]

class Regions:
    MENU = "Menu"

    # Every level location gets its own region.
    LEVEL_REGIONS = tuple(name for name in LOCATION_NAME_TO_ID.keys() if name != "The Secret Hollow")

    GOAL_REGION = "The Secret Hollow"

    ALL_REGIONS = (MENU, *LEVEL_REGIONS, GOAL_REGION)

def create_and_connect_regions(world: GDWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: GDWorld) -> None:
    """Create the regions for the logic so that we can have locations."""

    # Create the regions using the Region class from BaseClasses
    regions = [
        Region(region_name, world.player, world.multiworld)
        for region_name in Regions.ALL_REGIONS
    ]

    # TODO: Add options to lock certain regions

    # Add regions to the multiworld so that AP knows they exists
    world.multiworld.regions += regions

def connect_regions(world: GDWorld) -> None:
    """Connect all regions to make the AP World."""
    menu = world.get_region(Regions.MENU)

    # Create entrances for every level so that the menu can always access them
    # as long as the player has the required items
    for level_name in LEVEL_NAMES:
        level_region = world.get_region(level_name)

        entrance = Entrance(
            world.player,
            f"Menu to {level_name}",
            parent=menu,
        )

        menu.exits.append(entrance)
        entrance.connect(level_region)