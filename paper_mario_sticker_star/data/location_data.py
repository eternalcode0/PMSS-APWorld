from dataclasses import dataclass
from typing import Any

from ..names import ItemName as I
from ..names import LocationName as L
from ..names import RegionName as R
from . import RandomizationType


@dataclass
class LocationData:
    code: int  # Use as the location id
    name: L
    region: R
    """What region does the the location belong to"""
    item: I
    """What vanilla item is traditionally here. Only used if the location isn't shuffled """
    groups: frozenset = frozenset()
    """What location groups does this get added to"""
    setting: str | RandomizationType = RandomizationType.RANDOM
    """What condition is required for the location to be randomized"""


# Convenience strings so that the dictionaries don't have to use quotes everywhere
code = "code"
name = "name"
region = "region"
item = "item"
groups = "groups"
setting = "setting"


GROUP_WORLD_BOSS = "World Boss"
GROUP_SHOP = "Shop Purchase"
GROUP_DECALBURG_SHOP = "Decalburg Shop"
GROUP_WHAMMINO_SHOP = "Whammino Mountain Shop"


LOCATION_DICT_LIST: list[dict[str, Any]] = [
    #region Decalburg
    { name: L.DECALBURG_FESTIVAL_1_HAMMER_TOAD
    , code: 1
    , region: R.DECALBURG_FESTIVAL_1
    , item: I.HAMMER
    },
    { name: L.DECALBURG_FESTIVAL_1_JUMP_TOAD
    , code: 2
    , region: R.DECALBURG_FESTIVAL_1
    , item: I.STICKER_JUMP
    },
    { name: L.DECALBURG_FESTIVAL_1_RIGHT_BOOTH
    , code: 3
    , region: R.DECALBURG_FESTIVAL_1
    , item: I.STICKER_HAMMER
    },
    { name: L.DECALBURG_FESTIVAL_1_LEFT_BOXES
    , code: 4
    , region: R.DECALBURG_FESTIVAL_1
    , item: I.STICKER_EEKHAMMER
    },
    { name: L.DECALBURG_SHOP_JUMP
    , code: 5
    , region: R.DECALBURG
    , item: I.STICKER_JUMP
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_IRON_JUMP
    , code: 6
    , region: R.DECALBURG
    , item: I.STICKER_IRON_JUMP
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_HOPSLIPPER
    , code: 7
    , region: R.DECALBURG
    , item: I.STICKER_HOPSLIPPER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_LINE_JUMP
    , code: 8
    , region: R.DECALBURG
    , item: I.STICKER_LINE_JUMP
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_HAMMER
    , code: 9
    , region: R.DECALBURG
    , item: I.STICKER_HAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_EEKHAMMER
    , code: 10
    , region: R.DECALBURG
    , item: I.STICKER_EEKHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_HURLHAMMER
    , code: 11
    , region: R.DECALBURG
    , item: I.STICKER_HURLHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_SLAPHAMMER
    , code: 12
    , region: R.DECALBURG
    , item: I.STICKER_SLAPHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BAAHAMMER
    , code: 13
    , region: R.DECALBURG
    , item: I.STICKER_BAAHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BURNHAMMER
    , code: 14
    , region: R.DECALBURG
    , item: I.STICKER_BURNHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_CHILLHAMMER
    , code: 15
    , region: R.DECALBURG
    , item: I.STICKER_CHILLHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_SPIKE_HELMET
    , code: 16
    , region: R.DECALBURG
    , item: I.STICKER_SPIKE_HELMET
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_POW_BLOCK
    , code: 17
    , region: R.DECALBURG
    , item: I.STICKER_POW_BLOCK
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_SHELL
    , code: 18
    , region: R.DECALBURG
    , item: I.STICKER_SHELL
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_SHINY_SHELL
    , code: 19
    , region: R.DECALBURG
    , item: I.STICKER_SHINY_SHELL
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_MUSHROOM
    , code: 20
    , region: R.DECALBURG
    , item: I.STICKER_MUSHROOM
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_SHINY_MUSHROOM
    , code: 21
    , region: R.DECALBURG
    , item: I.STICKER_SHINY_MUSHROOM
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_FLASHY_MUSHROOM
    , code: 22
    , region: R.DECALBURG
    , item: I.STICKER_FLASHY_MUSHROOM
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_JUMP
    , code: 23
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_JUMP
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_IRON_JUMP
    , code: 24
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_IRON_JUMP
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_HOPSLIPPER
    , code: 25
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_HOPSLIPPER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_LINE_JUMP
    , code: 26
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_LINE_JUMP
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_HAMMER
    , code: 27
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_HAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_EEKHAMMER
    , code: 28
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_EEKHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_HURLHAMMER
    , code: 29
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_HURLHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_SLAPHAMMER
    , code: 30
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_SLAPHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_BAAHAMMER
    , code: 31
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_BAAHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_BURNHAMMER
    , code: 32
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_BURNHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_SHOP_BIG_SHINY_CHILLHAMMER
    , code: 33
    , region: R.DECALBURG
    , item: I.STICKER_BIG_SHINY_CHILLHAMMER
    , groups: {GROUP_SHOP, GROUP_DECALBURG_SHOP}
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.DECALBURG_TOWN_BACK_LEFT_BUSHES
    , code: 34
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_BACK_LEFT_DIRT_PATCH
    , code: 35
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_LEFT_HOUSE
    , code: 36
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_INSIDE_FENCE_NEAR_BUSH
    , code: 37
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_INSIDE_LEFT_HOUSE
    , code: 38
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_INSIDE_MIDDLE_HOUSE
    , code: 39
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_BLOCK_BEHIND_HOUSES
    , code: 40
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_STICKER_BEHIND_HOUSES
    , code: 41
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_STICKER_RIGHT_HOUSE
    , code: 42
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_STICKER_RIGHT_BACK_BUSH
    , code: 43
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_BLOCK_TOP_RIGHT_HOUSE
    , code: 44
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_BLOCK_INSIDE_BOXES
    , code: 45
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_SQAURE_STICKER_SHOP_WALL
    , code: 46
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_SQAURE_FOUNTAIN_SCRAP
    , code: 47
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_SQAURE_FREE_STICKERS
    , code: 48
    , region: R.DECALBURG
    , item: I.STICKER_SANDAL
    },
    { name: L.DECALBURG_TOWN_BACK_ALLEY_TOAD
    , code: 49
    , region: R.DECALBURG
    , item: I.STICKER_POISON_MUSHROOM
    , setting: RandomizationType.VANILLA_EVENT
    },
    #endregion
    #region 1-1: Warm Fuzzy Plains
    { name: L.W11_FIRST_ROOM_FIRST_BLOCK
    , code: 50
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_FIRST_ROOM_STICKER_FIRST_WALL
    , code: 51
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_FIRST_ROOM_BLOCK_RAISED_LEDGE
    , code: 52
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_FIRST_ROOM_STICKER_UPPER_FENCE
    , code: 53
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_FIRST_ROOM_STICKER_ON_SIGN
    , code: 54
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_BRIDGE_ROOM_PAPERIZATION
    , code: 55
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_BRIDGE_ROOM_BRIDGE_SCRAP
    , code: 56
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_BRIDGE_ROOM_UPGRADE_BLOCK
    , code: 57
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_UPGRADE_BLOCK
    , code: 58
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_STICKER_SCISSORS_CAVE
    , code: 59
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_THING_CAVE
    , code: 60
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_BLOCK_CAVE1
    , code: 61
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_BLOCK_CAVE2
    , code: 62
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_BLOCK_CAVE3
    , code: 63
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_STICKER_RIGHT_WALL
    , code: 64
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_STICKER_NEAR_SECRET_DOOR
    , code: 65
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_THING_SECRET_CAVE
    , code: 66
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_STICKER_WALL_STEPS_1
    , code: 67
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_STICKER_WALL_STEPS_2
    , code: 68
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_BLOCK_STEP_1
    , code: 69
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_BLOCK_STEP_2
    , code: 70
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_BLOCK_STEP_3
    , code: 71
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_STICKER_SIGN
    , code: 72
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_THIRD_ROOM_BLOCK_SIGN
    , code: 73
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_LAST_ROOM_STICKER_FENCE
    , code: 74
    , region: R.WORLD_1_1
    , item: I.STICKER_SANDAL
    },
    { name: L.W11_LAST_ROOM_COMET_PIECE
    , code: 75
    , region: R.WORLD_1_1
    , item: I.COMET_PIECE_1_2
    , setting: RandomizationType.VANILLA_EVENT
    },
    #endregion
    #region 1-2: Bouquet Gardens
    { name: L.W12_FIRST_ROOM_STICKER_FIRST_FENCE
    , code: 76
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_FIRST_ROOM_STICKER_BLOCK_FORMATION
    , code: 77
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_FIRST_ROOM_BOTTOM_BLOCK_FORMATION
    , code: 78
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_FIRST_ROOM_HIDDEN_BLOCK
    , code: 79
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_FIRST_ROOM_RAISED_STICKER
    , code: 80
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_FIRST_ROOM_TOP_BLOCK_FORMATION
    , code: 81
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_WINDY_ROOM_TOAD_GIFT
    , code: 82
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_WINDY_ROOM_FAN_THING
    , code: 83
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_SECRET_ROOM_STICKER_BUSHES
    , code: 84
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_SECRET_ROOM_BLOCK
    , code: 85
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_LOWER_PATH_STICKER_LEFT_BUSHES
    , code: 86
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_LOWER_PATH_BLOCK_RIGHT
    , code: 87
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_LOWER_PATH_STICKER_RIGHT_BUSHES
    , code: 88
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_LOWER_PATH_STICKER_STAIRS
    , code: 89
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_LOWER_PATH_BLOCK_PEELED_STAIRS
    , code: 90
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_LOWER_PATH_STICKER_TOP_BUSHES
    , code: 91
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_PAST_WINDY_ROOM_BLOCK_NEAR_RECOVERY
    , code: 92
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_PAST_WINDY_ROOM_THING_CAT
    , code: 93
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_PAST_WINDY_ROOM_UPGRADE_BLOCK_RIGHT
    , code: 94
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_PAST_WINDY_ROOM_BLOCK_BLUE_FLOWERS
    , code: 95
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_RIGHT_WINDY_ROOM_UPGRADE_BLOCK
    , code: 96
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_GOOMBA_WHEEL_ROOM_STICKER_LEFT_ALCOVE
    , code: 97
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_GOOMBA_WHEEL_ROOM_STICKER_INSIDE_ALCOVE_1
    , code: 98
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_GOOMBA_WHEEL_ROOM_STICKER_INSIDE_ALCOVE_2
    , code: 99
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_GOOMBA_WHEEL_ROOM_STICKER_RIGHT_ALCOVE_1
    , code: 100
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_GOOMBA_WHEEL_ROOM_STICKER_RIGHT_ALCOVE_2
    , code: 101
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_GOOMBA_WHEEL_ROOM_BLOCK_RIGHT_SIDE
    , code: 102
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_GOOMBA_WHEEL_ROOM_STICKER_UPPER_BUSH
    , code: 103
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_GOOMBA_WHEEL_ROOM_STICKER_LOWER_BUSH
    , code: 104
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_COMET_ROOM_BLOCK_LEFT_1
    , code: 105
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_COMET_ROOM_BLOCK_LEFT_2
    , code: 106
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_COMET_ROOM_BLOCK_LEFT_3
    , code: 107
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_COMET_ROOM_STICKER_WHITE_FLOWERS
    , code: 108
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_COMET_ROOM_STICKER_SECRET_DOOR
    , code: 109
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_SECRET_ROOM_LEFT_BLOCK
    , code: 110
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_SECRET_ROOM_MIDDLE_BLOCK
    , code: 111
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_SECRET_ROOM_RIGHT_BLOCK
    , code: 112
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_COMET_ROOM_BLOCK_NEAR_STAIRS
    , code: 113
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_COMET_ROOM_STICKER_NEAR_STAIRS
    , code: 114
    , region: R.WORLD_1_2
    , item: I.STICKER_SANDAL
    },
    { name: L.W12_COMET_ROOM_COMET_PIECE
    , code: 115
    , region: R.WORLD_1_2
    , item: I.COMET_PIECE_1_3
    , setting: RandomizationType.VANILLA_EVENT
    },
    #endregion
    #region 1-3: Water's Edge Way
    { name: L.W13_FIRST_ROOM_BLOCK_BOTTOM_RIGHT
    , code: 116
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_FIRST_ROOM_HIDDEN_BLOCK_LEFT_FLOWER
    , code: 117
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_FIRST_ROOM_HIDDEN_BLOCK_RIGHT_FLOWER
    , code: 118
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_FIRST_ROOM_BLOCK_LEFT
    , code: 119
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_FIRST_ROOM_STICKER_TOP_STAIR_WELL
    , code: 120
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_FIRST_ROOM_STICKER_LEFT_WALL
    , code: 121
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_FIRST_ROOM_BLOCK_TOP_STAIRS
    , code: 122
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_FIRST_ROOM_STICKER_RIGHT_FENCING
    , code: 123
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_STOLEN_COMET_ROOM_ALBUM_PAGE
    , code: 124
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_STOLEN_COMET_ROOM_LEFT_BLOCK
    , code: 125
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_STOLEN_COMET_ROOM_MIDDLE_HIDDEN_BLOCK
    , code: 126
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_STOLEN_COMET_ROOM_RIGHT_BLOCK_1
    , code: 127
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_STOLEN_COMET_ROOM_RIGHT_BLOCK_2
    , code: 128
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_STOLEN_COMET_ROOM_RIGHT_BLOCK_3
    , code: 129
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_STOLEN_COMET_ROOM_COMET_PIECE
    , code: 130
    , region: R.WORLD_1_3
    , item: I.COMET_PIECE_1_4
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W13_WATERFALL_ROOM_STICKER_RIGHT_WATERFALL
    , code: 131
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_BLOCK_RIGHT_SIDE
    , code: 132
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_BLOCK_WATERFALL_ALCOVE
    , code: 133
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_STICKER_BOTTOM_STAIRS
    , code: 134
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_BLOCK_BOTTOM_STAIRS
    , code: 135
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_STICKER_BY_KOOPAS
    , code: 136
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_UPGRADE_BLOCK_BRIDGE
    , code: 137
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_SECRET_WATERFALL_COMET_PIECE
    , code: 138
    , region: R.WORLD_1_3
    , item: I.COMET_PIECE_1_5
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W13_BOWSER_HEAD_ROOM_STICKER_NEAR_FIRST_HOLE
    , code: 139
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_BOWSER_HEAD_ROOM_BLOCK_NEAR_FIRST_HOLE
    , code: 140
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_BOWSER_HEAD_ROOM_STICKER_NEAR_BLOCK
    , code: 141
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_BOWSER_HEAD_ROOM_STICKER_ON_STAIRS
    , code: 142
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_BOWSER_HEAD_ROOM_STICKER_TOP_STAIRS
    , code: 143
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_BOWSER_HEAD_ROOM_LEFT_BLOCK_TOP_STAIRS
    , code: 144
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_BOWSER_HEAD_ROOM_RIGHT_BLOCK_TOP_STIARS
    , code: 145
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_BOWSER_HEAD_ROOM_FAUCET
    , code: 146
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_BLOCK_AFTER_BOWSER_ROOM
    , code: 147
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_HIDDEN_BLOCK_FLOWERS
    , code: 148
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_WATERFALL_ROOM_STICKER_ON_PIPE
    , code: 149
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_UNDERGROUND_COMET_PIECE_SCRAP
    , code: 150
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_UNDERGROUND_STICKER_UNDER_PUDDLE
    , code: 151
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    { name: L.W13_UNDERGROUND_BED_SECRET_DOOR
    , code: 152
    , region: R.WORLD_1_3
    , item: I.STICKER_SANDAL
    },
    #endregion
    #region 1-4: Hither Thither Hill
    { name: L.W14_WINDMILL_ROOM_LEFT_BLOCK
    , code: 154
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_WINDMILL_ROOM_RIGHT_BLOCK
    , code: 155
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_WINDMILL_ROOM_STICKER_BUSH_1
    , code: 156
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_WINDMILL_ROOM_STICKER_BUSH_2
    , code: 157
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_UNDERGROUND_PATH_BLCOK_UNDER_PLATFORMS
    , code: 158
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_BLOCK
    , code: 159
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_STICKER_1
    , code: 160
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_STICKER_2
    , code: 161
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_STICKER_3
    , code: 162
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_STICKER_4
    , code: 163
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_STICKER_5
    , code: 164
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_STICKER_6
    , code: 165
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_STICKER_7
    , code: 166
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_CRYING_TOAD_ROOM_UPGRADE_BLOCK
    , code: 167
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_MISSING_PIPE_PATH_BLOCK
    , code: 168
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_COMET_ROOM_STICKER_AFTER_PATH
    , code: 169
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_UNDER_WINDMILL_BLOCK_RAISED_PLATFORMS
    , code: 170
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_UNDER_WINDMILL_SCRAP
    , code: 171
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_MISSING_PIPE_PATH_BIG_BUZZY_DROP
    , code: 172
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_COMET_ROOM_RAISED_BLOCK
    , code: 173
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_COMET_ROOM_LEFT_BLOCK
    , code: 174
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_COMET_ROOM_STICKER_BACK_WALL
    , code: 175
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_COMET_ROOM_SECRET_DOOR_THING
    , code: 176
    , region: R.WORLD_1_4
    , item: I.STICKER_SANDAL
    },
    { name: L.W14_COMET_ROOM_COMET_PIECE
    , code: 177
    , region: R.WORLD_1_4
    , item: I.COMET_PIECE_1_6
    , setting: RandomizationType.VANILLA_EVENT
    },
    #endregion
    #region 1-5: Whammino Mountain
    { name: L.W15_FIRST_ROOM_STICKER_WALL
    , code: 178
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_FIRST_ROOM_LEFT_BLOCK
    , code: 179
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_FIRST_ROOM_RIGHT_BLOCK
    , code: 180
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_FIRST_ROOM_STICKER_ROCK
    , code: 181
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_STARMAN_ROOM_FIRST_BLOCK
    , code: 182
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_STARMAN_ROOM_STICKER_ROCK
    , code: 183
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_STARMAN_ROOM_STICKER_STARMAN_1
    , code: 184
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_STARMAN_ROOM_STICKER_STARMAN_2
    , code: 185
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_SHOP_ROOM_STICKER_FENCE_1
    , code: 186
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_SHOP_ROOM_STICKER_FENCE_2
    , code: 187
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_SHOP_ROOM_STICKER_CLOUD
    , code: 188
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_STICKER_ROOM_ENTRANCE
    , code: 189
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_STICKER_UNDER_COMET
    , code: 190
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_BLOCK_UNDER_COMET
    , code: 191
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_BLOCK_BETWEEEN_KOOPA_SPINY
    , code: 192
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_BLOCK_NEAR_SHORTCUT
    , code: 193
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_BLOCK_HIDDEN_STAIRCASE_1
    , code: 194
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_BLOCK_HIDDEN_STAIRCASE_2
    , code: 195
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_BLOCK_HIDDEN_STAIRCASE_3
    , code: 196
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_STICKER_COIN_PLATFORM
    , code: 197
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_UNDERGROUND_PATH_THING_HIDDEN_DOOR
    , code: 198
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_STARMAN_ROOM_SCRAP
    , code: 199
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_SHOP_ROOM_HIDDEN_BLOCK_LEFT
    , code: 200
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_SHOP_ROOM_HIDDEN_BLOCK_RIGHT
    , code: 201
    , region: R.WORLD_1_5
    , item: I.STICKER_SANDAL
    },
    { name: L.W15_COMET_ROOM_COMET_PIECE
    , code: 202
    , region: R.WORLD_1_5
    , item: I.COMET_PIECE_1_6
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_JUMP
    , code: 203
    , region: R.WORLD_1_5
    , item: I.STICKER_JUMP
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_HAMMER
    , code: 204
    , region: R.WORLD_1_5
    , item: I.STICKER_HAMMER
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_POISON_MUSHROOM
    , code: 205
    , region: R.WORLD_1_5
    , item: I.STICKER_POISON_MUSHROOM
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_MUSHROOM
    , code: 206
    , region: R.WORLD_1_5
    , item: I.STICKER_MUSHROOM
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_FIRE_FLOWER
    , code: 207
    , region: R.WORLD_1_5
    , item: I.STICKER_FIRE_FLOWER
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_SHINY_FIRE_FLOWER
    , code: 208
    , region: R.WORLD_1_5
    , item: I.STICKER_SHINY_FIRE_FLOWER
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_FLASHY_FIRE_FLOWER
    , code: 209
    , region: R.WORLD_1_5
    , item: I.STICKER_FLASHY_FIRE_FLOWER
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_ICE_FLOWER
    , code: 210
    , region: R.WORLD_1_5
    , item: I.STICKER_ICE_FLOWER
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_SHINY_ICE_FLOWER
    , code: 211
    , region: R.WORLD_1_5
    , item: I.STICKER_SHINY_ICE_FLOWER
    , setting: RandomizationType.VANILLA_EVENT
    },
    { name: L.W15_SHOP_FLASHY_ICE_FLOWER
    , code: 212
    , region: R.WORLD_1_5
    , item: I.STICKER_FLASHY_ICE_FLOWER
    , setting: RandomizationType.VANILLA_EVENT
    },
    #endregion
    #region 1-6: Goomba Fortress
    { name: L.W16_BOMBS_ROOM_FIRST_LEFT_BLOCK
    , code: 213
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_BOMBS_ROOM_FIRST_RIGHT_BLOCK
    , code: 214
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_BOMBS_ROOM_STICKER_MIDDLE
    , code: 215
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_BOMBS_ROOM_BLOCK_BOTTOM_PLATFORM
    , code: 216
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_BOMBS_ROOM_BLOCK_HIDDEN_ROOM
    , code: 217
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_WINDY_ROOM_STICKER_LEFT_STAIRS
    , code: 218
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_WINDY_ROOM_THING_SECRET_ROOM
    , code: 219
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_WINDY_ROOM_BLOCK_RIGHT_STAIRS
    , code: 220
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_WINDY_ROOM_BRICK_BLOCK_RIGHT_STAIRS
    , code: 221
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_WINDY_ROOM_STICKER_RIGHT_STAIRS
    , code: 222
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_WINDY_ROOM_STICKER_TOP_STAIRS
    , code: 223
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_WINDY_ROOM_HIDDEN_BLOCK_1
    , code: 224
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_WINDY_ROOM_HIDDEN_BLOCK_2
    , code: 225
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_WINDY_ROOM_HIDDEN_BLOCK_3
    , code: 226
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_WINDY_ROOM_HIDDEN_BLOCK_4
    , code: 227
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_WINDY_ROOM_HIDDEN_BLOCK_5
    , code: 228
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_WINDY_ROOM_BLOCK
    , code: 229
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_BOMB_FENCE_ROOM_BLOCK_1
    , code: 230
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_BOMB_FENCE_ROOM_BLOCK_2
    , code: 231
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_BOMB_FENCE_ROOM_STICKER
    , code: 232
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_BOMB_FENCE_ROOM_STICKER_NEAR_TREE
    , code: 233
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_AFTER_BOMB_FENCE_ROOM_BLOCK_SWITCH_SCRAP
    , code: 234
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_COVERED_SPIKES_ROOM_BLOCK
    , code: 235
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_COVERED_SPIKES_ROOM_HIDDEN_LUIGI
    , code: 236
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_SPIRAL_STAIR_ROOM_UPGRADE_BLOCK
    , code: 237
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_SPIRAL_STAIR_ROOM_BLOCK_1
    , code: 238
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_SPIRAL_STAIR_ROOM_BLOCK_2
    , code: 239
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_SPIRAL_STAIR_ROOM_BRICK_BLOCK
    , code: 240
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_SPIRAL_STAIR_ROOM_BLOCK_3
    , code: 241
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_SPIRAL_STAIR_ROOM_BLOCK_4
    , code: 242
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_SPIRAL_STAIR_ROOM_HIDDEN_BLOCK
    , code: 243
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_SPIRAL_STAIR_ROOM_BLOCK_5
    , code: 244
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_TOP_ROOM_THING
    , code: 245
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_TOP_ROOM_BLOCK
    , code: 246
    , region: R.WORLD_1_6
    , item: I.STICKER_SANDAL
    },
    { name: L.W16_BOSS_ROYAL_STICKER
    , code: 247
    , region: R.WORLD_1_6
    , item: I.ROYAL_STICKER_RED
    , setting: RandomizationType.VANILLA_WORLD
    },
    { name: L.W16_BOSS_PAGE
    , code: 248
    , region: R.WORLD_1_6
    , item: I.ALBUM_PAGE
    },
    #endregion
]  # fmt:off

# Converts the dictionary above into LocationData
LOCATION_DATA = [LocationData(**dat) for dat in LOCATION_DICT_LIST]
