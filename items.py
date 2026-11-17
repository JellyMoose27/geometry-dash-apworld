from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import GDWorld

gd_base_id = 130820130

ITEM_NAME_TO_ID = {
    "Back On Track: Unlock": 0 + gd_base_id,
    "Polargeist: Unlock": 1 + gd_base_id,
    "Dry Out: Unlock": 2 + gd_base_id,
    "Base After Base: Unlock": 3 + gd_base_id,
    "Cant Let Go: Unlock": 4 + gd_base_id,
    "Jumper: Unlock": 5 + gd_base_id,
    "Time Machine: Unlock": 6 + gd_base_id,
    "Cycles: Unlock": 7 + gd_base_id,
    "xStep: Unlock": 8 + gd_base_id,
    "Clutterfunk: Unlock": 9 + gd_base_id,
    "Theory of Everything: Unlock": 10 + gd_base_id,
    "Electroman Adventures: Unlock": 11 + gd_base_id,
    "Clubstep: Unlock": 12 + gd_base_id,
    "Electrodynamix: Unlock": 13 + gd_base_id,
    "Hexagon Force: Unlock": 14 + gd_base_id,
    "Blast Processing: Unlock": 15 + gd_base_id,
    "Theory of Everything 2: Unlock": 16 + gd_base_id,
    "Geometrical Dominator: Unlock": 17 + gd_base_id,
    "Deadlocked: Unlock": 18 + gd_base_id,
    "Fingerdash: Unlock": 19 + gd_base_id,
    "Dash: Unlock": 20 + gd_base_id,
    "The Tower: Unlock": 21 + gd_base_id,
    "The Sewers: Unlock": 22 + gd_base_id,
    "The Cellar: Unlock": 23 + gd_base_id,
    "The Secret Hollow: Unlock": 24 + gd_base_id,

    "Ball Portal": 25 + gd_base_id,
    "UFO Portal": 26 + gd_base_id,
    "Wave Portal": 28 + gd_base_id,
    "Robot Portal": 29 + gd_base_id,
    "Spider Portal": 30 + gd_base_id,
    "Swing Portal": 31 + gd_base_id,

    "100 Mana Orbs": 32 + gd_base_id,
    "5 Diamonds": 33 + gd_base_id,
}

class GDItem(Item):
    game = "Geometry Dash"

# DEFAULT_ITEM_CLASSIFICATIONS = {
#     "100 Mana Orbs": ItemClassification.filler | ItemClassification.useful,
#     "5 Diamonds": ItemClassification.filler
# }

FILLER_ITEM_NAMES = {
    "100 Mana Orbs",
    "5 Diamonds",
}

# TODO: Add more filler items (or traps) and implement a better algorithm to randomize them 
def get_random_filler_item_name(world: GDWorld) -> str:
    return world.random.choice(list(FILLER_ITEM_NAMES))

def create_item_with_correct_classification(world: GDWorld, name: str) -> GDItem:
    # Create items by name with the correct classifications
    # classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # Unlocks and portals are progression items.
    if name.endswith("Unlock") or name.endswith("Portal"):
        classification = ItemClassification.progression
    else:
        classification = ItemClassification.filler

    return GDItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: GDWorld) -> None:
    """Submit all items into the multiworld item pool."""

    # Create items from the ITEM_NAME_TO_ID dict
    itempool: list[Item] = [
        world.create_item(name) for name in ITEM_NAME_TO_ID
        if name not in FILLER_ITEM_NAMES
    ]

    # Fetch the number of items created
    number_of_items = len(itempool)

    # Fetch the number of checks not filled with items yet
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Calculate the number of filler items needed for the unfilled checks
    number_of_filler_items_needed = number_of_unfilled_locations - number_of_items

    # Create the filler items and put them into the item pool
    itempool += [world.create_filler() for _ in range(number_of_filler_items_needed)]

    # Submit all created items into the multiworld item pool
    world.multiworld.itempool += itempool

    # TODO: Can probably add precollected items for easier runs, maybe depending on player's options
