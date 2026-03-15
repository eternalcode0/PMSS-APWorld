from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll, HasAny, HasGroupUnique, Rule, True_

from . import items, locations, regions
from .names import ItemName as I
from .names import LocationName as L
from .names import RegionName as R

if TYPE_CHECKING:
    from .world import PMSSWorld


def set_all_rules(world: PMSSWorld):
    world.set_completion_rule(HasGroupUnique(items.GROUP_ROYAL_STICKER, 5))
    connect_regions(world)
    set_location_rules(world)


def connect_regions(world: PMSSWorld):
    region_map = regions.get_region_map(world)
    for from_region, connections in REGION_RULES.items():
        for to_region, rule in connections.items():
            world.create_entrance(region_map[from_region], region_map[to_region], rule)


def set_location_rules(world: PMSSWorld):
    location_map = locations.get_location_map(world)
    for location, rule in LOCATION_RULES.items():
        world.set_rule(location_map[location], rule)


w11_wooden_bridge = HasAll(I.PAPERIZATION, I.SCRAP_WOODEN_BRIDGE)
w15_shop = Has(I.SCRAP_WHITE_GATE)


REGION_RULES: dict[R, dict[R, Rule]] = {
    R.DECALBURG_FESTIVAL_1: {
        R.DECALBURG: Has(I.HAMMER),
    },
    R.DECALBURG: {
        R.DECALBURG_FESTIVAL_1: True_(),
        R.WORLD_MAP: True_(),
    },
    R.WORLD_MAP: {
        R.SURFSHINE_HARBOR: Has(I.SURFSHINE_HARBOR),
        R.DECALBURG: True_(),
        R.WORLD_1_1: True_(),
        R.WORLD_1_2: Has(I.COMET_PIECE_1_2),
        R.WORLD_1_3: Has(I.COMET_PIECE_1_3),
        R.WORLD_1_4: Has(I.COMET_PIECE_1_4),
        R.WORLD_1_5: Has(I.COMET_PIECE_1_5),
        R.WORLD_1_6: Has(I.COMET_PIECE_1_6),

        # R.WORLD_2_1: True_(),
        # R.WORLD_3_1: True_(),
    },
}  # fmt:off


LOCATION_RULES = {
    L.DECALBURG_SHOP_JUMP: True_(),
    L.DECALBURG_SHOP_IRON_JUMP: Has(I.COMET_PIECE_1_6),
    L.DECALBURG_SHOP_HOPSLIPPER: Has(I.COMET_PIECE_1_2),
    L.DECALBURG_SHOP_LINE_JUMP: Has(I.COMET_PIECE_1_2),
    L.DECALBURG_SHOP_HAMMER: True_(),
    L.DECALBURG_SHOP_EEKHAMMER: Has(I.COMET_PIECE_1_2),
    L.DECALBURG_SHOP_HURLHAMMER: Has(I.COMET_PIECE_1_6),
    L.DECALBURG_SHOP_SLAPHAMMER: Has(I.COMET_PIECE_1_2),
    L.DECALBURG_SHOP_BAAHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 2),
    L.DECALBURG_SHOP_BURNHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 2),
    L.DECALBURG_SHOP_CHILLHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 2),
    L.DECALBURG_SHOP_SPIKE_HELMET: Has(I.COMET_PIECE_1_6),
    L.DECALBURG_SHOP_POW_BLOCK: Has(I.COMET_PIECE_1_6),
    L.DECALBURG_SHOP_SHELL: Has(I.COMET_PIECE_1_6),
    L.DECALBURG_SHOP_SHINY_SHELL: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_MUSHROOM: True_(),
    L.DECALBURG_SHOP_SHINY_MUSHROOM: HasGroupUnique(items.GROUP_ROYAL_STICKER, 1),
    L.DECALBURG_SHOP_FLASHY_MUSHROOM: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_JUMP: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_IRON_JUMP: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_HOPSLIPPER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_LINE_JUMP: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_HAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_EEKHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_HURLHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_SLAPHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_BAAHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_BURNHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    L.DECALBURG_SHOP_BIG_SHINY_CHILLHAMMER: HasGroupUnique(items.GROUP_ROYAL_STICKER, 3),
    # It's preferable to add a region after the bridge to reduce the rule used for it.
    # Regions get messy quickly if that's done for every scenario though so if it's preferred to keep the region graph
    # small it should be done rarely. On the flipside avoiding duplicated rules with extra regions "typically" speeds up
    # generation, UT and other location accessibility traversals.
    L.W11_BRIDGE_ROOM_UPGRADE_BLOCK: w11_wooden_bridge,
    L.W11_THIRD_ROOM_UPGRADE_BLOCK: w11_wooden_bridge,
    L.W11_THIRD_ROOM_STICKER_SCISSORS_CAVE: w11_wooden_bridge,
    L.W11_THIRD_ROOM_THING_CAVE: w11_wooden_bridge,
    L.W11_THIRD_ROOM_BLOCK_CAVE1: w11_wooden_bridge,
    L.W11_THIRD_ROOM_BLOCK_CAVE2: w11_wooden_bridge,
    L.W11_THIRD_ROOM_BLOCK_CAVE3: w11_wooden_bridge,
    L.W11_THIRD_ROOM_STICKER_RIGHT_WALL: w11_wooden_bridge,
    L.W11_THIRD_ROOM_STICKER_NEAR_SECRET_DOOR: w11_wooden_bridge,
    L.W11_THIRD_ROOM_THING_SECRET_CAVE: w11_wooden_bridge,
    L.W11_THIRD_ROOM_STICKER_WALL_STEPS_1: w11_wooden_bridge,
    L.W11_THIRD_ROOM_STICKER_WALL_STEPS_2: w11_wooden_bridge,
    L.W11_THIRD_ROOM_BLOCK_STEP_1: w11_wooden_bridge,
    L.W11_THIRD_ROOM_BLOCK_STEP_2: w11_wooden_bridge,
    L.W11_THIRD_ROOM_BLOCK_STEP_3: w11_wooden_bridge,
    L.W11_THIRD_ROOM_STICKER_SIGN: w11_wooden_bridge,
    L.W11_THIRD_ROOM_BLOCK_SIGN: w11_wooden_bridge,
    L.W11_LAST_ROOM_STICKER_FENCE: w11_wooden_bridge,
    L.W11_LAST_ROOM_COMET_PIECE: w11_wooden_bridge,
    L.W11_LAST_ROOM_COMET_PIECE: w11_wooden_bridge,
    L.W11_THIRD_ROOM_THING_SECRET_CAVE: Has(I.STICKER_SECRET_DOOR),
    L.W12_WINDY_ROOM_TOAD_GIFT: HasAny(I.STICKER_FIRE_FLOWER, I.STICKER_ICE_FLOWER),
    L.W12_SECRET_ROOM_LEFT_BLOCK: Has(I.STICKER_SECRET_DOOR),
    L.W12_SECRET_ROOM_MIDDLE_BLOCK: Has(I.STICKER_SECRET_DOOR),
    L.W12_SECRET_ROOM_RIGHT_BLOCK: Has(I.STICKER_SECRET_DOOR),
    L.W12_COMET_ROOM_COMET_PIECE: True_(),
    L.W13_STOLEN_COMET_ROOM_COMET_PIECE: Has(I.SCRAP_COMET_PIECE),
    L.W13_SECRET_WATERFALL_COMET_PIECE: True_(),
    L.W13_UNDERGROUND_BED_SECRET_DOOR: Has(I.STICKER_SECRET_DOOR),
    L.W14_COMET_ROOM_COMET_PIECE: Has(I.SCRAP_GREEN_WARP_PIPE),
    L.W15_SHOP_ROOM_HIDDEN_BLOCK_LEFT: w15_shop,
    L.W15_SHOP_ROOM_HIDDEN_BLOCK_RIGHT: w15_shop,
    L.W15_COMET_ROOM_COMET_PIECE: w15_shop,
    L.W16_WINDY_ROOM_THING_SECRET_ROOM: Has(I.STICKER_SECRET_DOOR),
    L.W16_COVERED_SPIKES_ROOM_BLOCK: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_COVERED_SPIKES_ROOM_HIDDEN_LUIGI: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_SPIRAL_STAIR_ROOM_UPGRADE_BLOCK: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_SPIRAL_STAIR_ROOM_BLOCK_1: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_SPIRAL_STAIR_ROOM_BLOCK_2: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_SPIRAL_STAIR_ROOM_BRICK_BLOCK: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_SPIRAL_STAIR_ROOM_BLOCK_3: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_SPIRAL_STAIR_ROOM_BLOCK_4: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_SPIRAL_STAIR_ROOM_HIDDEN_BLOCK: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_SPIRAL_STAIR_ROOM_BLOCK_5: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_TOP_ROOM_THING: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_TOP_ROOM_BLOCK: Has(I.SCRAP_BLOCK_SWITCH),
    L.W16_BOSS_ROYAL_STICKER: Has(I.SCRAP_BLOCK_SWITCH) & Has(I.THING_SCISSORS) & HasGroupUnique(items.GROUP_THINGS, 3),
    L.W16_BOSS_PAGE: Has(I.SCRAP_BLOCK_SWITCH) & Has(I.THING_SCISSORS) & HasGroupUnique(items.GROUP_THINGS, 3),
}
