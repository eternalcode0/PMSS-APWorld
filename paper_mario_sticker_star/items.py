from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from BaseClasses import Item, ItemClassification

from .constants import GAME
from .names import ItemName as I

if TYPE_CHECKING:
    from .world import PMSSWorld


@dataclass(frozen=True)
class ItemData:
    name: I
    code: int = field(compare=True, hash=True)
    count: int = field(compare=False, default=1)
    groups: frozenset[str] = field(compare=False, default=frozenset())
    setting: str | None = field(compare=False, default=None)
    classification: ItemClassification = field(compare=False, default=ItemClassification.filler)


class PMSSItem(Item):
    game = GAME


def get_random_filler_item_name(world: "PMSSWorld") -> str:
    # Return a random filler item in the event the world runs out of items to fill
    # Should probably use something like world.random.choices to pick from all filler stickers or something
    return I.STICKER_SANDAL


def create_item(world: "PMSSWorld", name: str) -> PMSSItem:
    # Get the item's default classification from the item data below, if it's not listed assume it's filler
    item_data = ITEM_ENUM_TO_DATA.get(I(name))
    classification = item_data.classification if item_data is not None else ItemClassification.filler
    return PMSSItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: "PMSSWorld") -> tuple[list[PMSSItem], dict[str, int]]:
    # Create main item pool
    itempool: list[I] = [item.name for item in ITEM_DATA for _ in range(item.count)]
    return ([world.create_item(item_name) for item_name in itempool], {I.STICKER_SANDAL: 1})


ITEM_GROUPS_ENUM: dict[str, set[I]] = {
    "Royal Stickers": {
        I.ROYAL_STICKER_RED,
        I.ROYAL_STICKER_ORANGE,
        I.ROYAL_STICKER_GREEN,
        I.ROYAL_STICKER_BLUE,
        I.ROYAL_STICKER_PURPLE,
    },
}


# convenience strings because I hate putting quotes everywhere in dicts
name = "name"
code = "code"
count = "count"
groups = "groups"
setting = "setting"
classification = "classification"

# Item Groups
GROUP_ROYAL_STICKER = "Royal Stickers"
GROUP_THINGS = "Things"
GROUP_SCRAPS = "Scraps"
GROUP_UPGRADES = "Upgrades"
GROUP_STICKERS = "Stickers"


RAW_ITEM_DATA: list[dict[str, Any]] = [
    { name: I.STICKER_SANDAL
    , code: 1
    , count: 0
    , groups: {GROUP_STICKERS}
    , classification: ItemClassification.filler
    },
    { name: I.ROYAL_STICKER_RED
    , code: 2
    , count: 0
    , groups: {GROUP_ROYAL_STICKER}
    , setting: "royal_sticker"
    , classification: ItemClassification.progression_skip_balancing
    },
    { name: I.ROYAL_STICKER_ORANGE
    , code: 3
    , groups: {GROUP_ROYAL_STICKER}
    , setting: "royal_sticker"
    , classification: ItemClassification.progression_skip_balancing
    },
    { name: I.ROYAL_STICKER_BLUE
    , code: 4
    , groups: {GROUP_ROYAL_STICKER}
    , setting: "royal_sticker"
    , classification: ItemClassification.progression_skip_balancing
    },
    { name: I.ROYAL_STICKER_GREEN
    , code: 5
    , groups: {GROUP_ROYAL_STICKER}
    , setting: "royal_sticker"
    , classification: ItemClassification.progression_skip_balancing
    },
    { name: I.ROYAL_STICKER_PURPLE
    , code: 6
    , groups: {GROUP_ROYAL_STICKER}
    , setting: "royal_sticker"
    , classification: ItemClassification.progression_skip_balancing
    },
    { name: I.ROYAL_STICKER_GOLD
    , code: 7
    , count: 0
    , classification: ItemClassification.progression_skip_balancing
    },
    { name: I.HAMMER
    , code: 8
    , classification: ItemClassification.progression
    },
    { name: I.PAPERIZATION
    , code: 9
    , classification: ItemClassification.progression
    },
    { name: I.THING_SCISSORS
    , code: 10
    , classification: ItemClassification.progression
    , groups: {GROUP_THINGS}
    },
    { name: I.THING_FAN
    , code: 11
    , classification: ItemClassification.progression
    , groups: {GROUP_THINGS}
    },
    { name: I.THING_FAUCET
    , code: 12
    , classification: ItemClassification.progression
    , groups: {GROUP_THINGS}
    },
    { name: I.SCRAP_WOODEN_BRIDGE
    , code: 13
    , classification: ItemClassification.progression
    },
    { name: I.SCRAP_COMET_PIECE
    , code: 14
    , classification: ItemClassification.progression
    },
    { name: I.STICKER_SECRET_DOOR
    , code: 15
    , classification: ItemClassification.progression
    },
    { name: I.SCRAP_GREEN_WARP_PIPE
    , code: 16
    , classification: ItemClassification.progression
    },
    { name: I.THING_TRUMPET
    , code: 17
    , classification: ItemClassification.progression
    , groups: {GROUP_THINGS}
    },
    { name: I.SCRAP_WHITE_GATE
    , code: 18
    , classification: ItemClassification.progression
    , groups: {GROUP_SCRAPS}
    },
    { name: I.SCRAP_BLOCK_SWITCH
    , code: 19
    , classification: ItemClassification.progression
    , groups: {GROUP_SCRAPS}
    },
]  # fmt:off

ITEM_DATA: list[ItemData] = [ItemData(**data) for data in RAW_ITEM_DATA]
ITEM_ENUM_TO_DATA: dict[I, ItemData] = {data.name: data for data in ITEM_DATA}
ITEM_ENUM_TO_ID: dict[I, int] = {item: data.code for item, data in ITEM_ENUM_TO_DATA.items()}
# AP isn't a fan of StrEnums yet so we .value the name to get the raw string
ITEM_NAME_TO_ID: dict[str, int] = {name.value: code for name, code in ITEM_ENUM_TO_ID.items()}
ITEM_GROUPS: set[str] = {group for item in ITEM_DATA for group in item.groups}
# Generate the list of Item groups from each ItemData.groups
ITEM_GROUP_MAP: dict[str, set[str]] = {
    group: {item.name.value for item in ITEM_DATA if group in item.groups} for group in ITEM_GROUPS
}
