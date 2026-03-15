from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class RequiredRoyalStickers(Range):
    """How many Royal Stickers are required to pass 6-1: Gate Cliff?"""

    display_name = "Required Royal Stickers"

    # I guess this could technically be 0, but wouldn't make for much of a rando if you didn't need any goal items.
    # Maybe if the map wasn't completely open and Entrance Rando was on?
    range_start = 1
    range_end = 5
    default = 5


class WorldMapMode(Choice):
    """
    How should traversing the world map work? World 6 will always be vanilla, requiring royal stickers to access.
    Vanilla is the only option that restricts level exits to working like they usually do, otherwise the world map is
    connected to every level from the beginning.

    - Vanilla: The only available levels at the start are Decalburg, Surfshine Harbor and the first level of World 1, 2,
      and 3. Comet Pieces unlock levels exactly as they do in the vanilla game.
    - Shuffled: You need each level's respective comet piece to enter it. Comet Pieces become locations/items shuffled
      amongst themselves. This also means the comet pieces will *not* be in the item pool.
    - Randomized: You need each level's respective comet piece to enter it. Comet Pieces become locations/items added to
      the multiworld item pool.
    - Open: Comet pieces aren't required to unlock levels, you can start every level without requirements.
    """

    display_name = "World Map Mode"

    option_vanilla = 0
    option_shuffled = 1
    option_randomized = 2
    option_open = 3

    default = option_open


class ShuffleThings(Choice):
    """
    Should Thing objects be randomized locations & items?

    - Shuffled: Things are shuffled between their usual locations, always within your own world.
    - Randomized: Things are added to the item pool to be placed anywhere.
    """

    # option_disabled = 0  # Would probably make for really boring logic but will keep it here as a placeholder
    option_shuffled = 1
    option_randomized = 2
    default = option_randomized


class ShuffleScraps(Choice):
    """Should Scrap objects be randomized locations & items?"""

    # option_disabled = 0  # Would probably make for really boring logic but will keep it here as a placeholder
    option_shuffled = 1
    option_randomized = 2
    default = option_randomized


class ShuffleBlocks(Choice):
    """Should Item/Coin blocks be randomized locations & items?"""

    option_disabled = 0b00
    option_visible = 0b01
    option_all = 0b10
    default = option_disabled

    @property
    def visible_randomized(self) -> bool:
        return self.value in {self.option_visible, self.option_all}

    @property
    def hidden_randomized(self) -> bool:
        return self.value == self.option_all


class ShuffleCoins(Choice):
    """Should coins be randomized locations?"""

    option_disabled = 0
    option_visible = 1
    option_all = 2
    default = option_disabled

    @property
    def visible_randomized(self) -> bool:
        return self.value in {self.option_visible, self.option_all}

    @property
    def hidden_randomized(self) -> bool:
        return self.value == self.option_all


class ShuffleStickers(Toggle):
    """Should peelable stickers be randomized locations?"""

    display_name = "Shuffle Stickers"


class ShuffleHPUpHearts(Toggle):
    """Should HP-Up Hearts be randomized locations & items?"""

    display_name = "Shuffle HP-Up Hearts"
    default = True


@dataclass
class PMSSOptions(PerGameCommonOptions):
    required_royal_stickers: RequiredRoyalStickers
    world_map_mode: WorldMapMode
    shuffle_things: ShuffleThings
    shuffle_scraps: ShuffleScraps
    shuffle_hp_up_hearts: ShuffleHPUpHearts
    shuffle_blocks: ShuffleBlocks
    shuffle_stickers: ShuffleStickers
    shuffle_coins: ShuffleCoins


exclude_options = [
    "progression_balancing",
    "accessibility",
    "local_items",
    "non_local_items",
    "start_inventory",
    "start_hints",
    "start_location_hints",
    "exclude_locations",
    "priority_locations",
    "item_links",
    "plando_items",
]


option_groups = [
    OptionGroup("World Access", [RequiredRoyalStickers, WorldMapMode]),
    OptionGroup(
        "Item & Location Shuffle",
        [ShuffleThings, ShuffleScraps, ShuffleHPUpHearts, ShuffleBlocks, ShuffleStickers, ShuffleCoins],
    ),
]

# Example option presets
option_presets = {
    # "easy": {
    #     "required_royal_stickers": 2,
    # },
}
