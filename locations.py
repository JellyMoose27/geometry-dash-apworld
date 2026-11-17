from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import GDWorld

# No idea why the GD's base id is needed here but I won't touch it
gd_base_id = 130820130

LOCATION_NAME_TO_ID = {
    "Stereo Madness": 0 + gd_base_id,
    "Back On Track": 1 + gd_base_id,
    "Polargeist": 2 + gd_base_id,
    "Dry Out": 3 + gd_base_id,
    "Base After Base": 4 + gd_base_id,
    "Cant Let Go": 5 + gd_base_id,
    "Jumper": 6 + gd_base_id,
    "Time Machine": 7 + gd_base_id,
    "Cycles": 8 + gd_base_id,
    "xStep": 9 + gd_base_id,
    "Clutterfunk": 10 + gd_base_id,
    "Theory of Everything": 11 + gd_base_id,
    "Electroman Adventures": 12 + gd_base_id,
    "Clubstep": 13 + gd_base_id,
    "Electrodynamix": 14 + gd_base_id,
    "Hexagon Force": 15 + gd_base_id,
    "Blast Processing": 16 + gd_base_id,
    "Theory of Everything 2": 17 + gd_base_id,
    "Geometrical Dominator": 18 + gd_base_id,
    "Deadlocked": 19 + gd_base_id,
    "Fingerdash": 20 + gd_base_id,
    "Dash": 21 + gd_base_id,
    "The Tower": 22 + gd_base_id,
    "The Sewers": 23 + gd_base_id,
    "The Cellar": 24 + gd_base_id,
    # Comment this out, will re-add it later on
    # "The Secret Hollow": 25 + gd_base_id,
    "Ultimate Clubstep": 26 + gd_base_id,
    "Ultimate Theory of Everything 2": 27 + gd_base_id,
    "Ultimate Deadlocked": 28 + gd_base_id,
    # Shop checks
    # **{
    #     f"Shop Item #{i}": 99 + i + gd_base_id
    #     for i in range(1, 43)
    # },

    # Coin checks
    **{
        f"{level_name} - Coin {coin_number}":
            (level_index + 1) * 1000 + coin_number + gd_base_id
        for level_index, level_name in enumerate([
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
            # "The Secret Hollow",
        ])
        for coin_number in range(1, 4)
    },
}

# unused until MoreGames is ported to 2.2081 (probably wont be so ill just not use this)
# There might be a way to extract these levels considering the achievements for them
# do exist in the base game. But don't quote me on this - Jelly Moose
# spinoff_locations = {
#     "The Seven Seas": 29 + gd_base_id,
#     "Viking Arena": 30 + gd_base_id,
#     "Airborne Robots": 31 + gd_base_id,
#     "Press Start": 32 + gd_base_id,
#     "Nock Em": 33 + gd_base_id,
#     "Power Trip": 34 + gd_base_id,
# }

# unused at the moment
possible_starting_levels = {
    "Stereo Madness": 0 + gd_base_id,
    "Back On Track": 1 + gd_base_id,
    "Polargeist": 2 + gd_base_id,
    "Dry Out": 3 + gd_base_id,
    "Base After Base": 4 + gd_base_id,
    "Cant Let Go": 5 + gd_base_id,
    "Jumper": 6 + gd_base_id,
    "Time Machine": 7 + gd_base_id,
}

class GDLocation(Location):
    game: str = "Geometry Dash"

# Helper method to fetch a dictionary of location names
def get_locations_by_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names if location_name in LOCATION_NAME_TO_ID}

# TODO: Implement a better helper method to fetch a dictionary
# of locations from a range (e.g Stereo Madness - Coin 1 to Time Machine - Coin 3)
def get_level_name_by_ids(start_id: int, end_id: int) -> dict[str, int | None]:
    return {
        name: location_id for name, location_id in LOCATION_NAME_TO_ID.items()
        if start_id <= location_id - gd_base_id <= end_id
    }

# TODO: Implement the same helper for level completion
def get_coin_locations(level_names: list[str]) -> dict[str, int]:
    location_names = [
        f"{level_name} - Coin {coin_number}"
        for level_name in level_names
        for coin_number in range(1, 4)
        if f"{level_name} - Coin {coin_number}" in LOCATION_NAME_TO_ID
    ]
    return {
        name: LOCATION_NAME_TO_ID[name]
        for name in location_names
    }

def create_all_locations(world: GDWorld) -> None:
    create_level_complete_locations(world)
    create_coin_collect_locations(world)
    # create_shop_locations(world)

def create_coin_collect_locations(world: GDWorld) -> None:
    """Place each level's coin checks in that level's region."""

    level_names = list(get_level_name_by_ids(0, 28).keys())

    for level_name in level_names:
        coin_locations = get_coin_locations([level_name])

        if coin_locations:
            world.get_region(level_name).add_locations(
                coin_locations,
                GDLocation,
            )

# unused for now
def create_shop_locations(world: GDWorld) -> None:
    menu = world.get_region("Menu")

    # Fetch items locations from the default Shop (Shop 1)
    shop_locations = {
        name: location_id
        for name, location_id in LOCATION_NAME_TO_ID.items()
        if name.startswith("Shop Item #")
    }

    menu.add_locations(
        shop_locations,
        GDLocation,
    )

def create_level_complete_locations(world: GDWorld) -> None:
    """Place each level-completion check in its own level region."""

    # The Secret Hollow is represented by the completion event below.
    # Are Ultimates counted as checks?
    if world.options.ultimate:
        level_locations = get_level_name_by_ids(0, 28)
    else:
        level_locations = get_level_name_by_ids(0, 25)

    for location_name, location_id in level_locations.items():
        world.get_region(location_name).add_locations(
            {location_name: location_id},
            GDLocation,
        )

    # Completing The Secret Hollow triggers the game goal.
    world.get_region("The Secret Hollow").add_event(
        "The Secret Hollow: Victory",
        "Game Beaten",
        location_type=GDLocation,
        item_type=items.GDItem,
    )
