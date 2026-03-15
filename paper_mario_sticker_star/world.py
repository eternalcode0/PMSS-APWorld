import json
import pkgutil
from collections.abc import Mapping
from typing import Any, ClassVar, TextIO

from BaseClasses import Item, ItemClassification, MultiWorld
from Options import Option, PerGameCommonOptions
from settings import Group, UserFilePath
from worlds.AutoWorld import WebWorld, World

from . import constants, items, locations, regions, rules, web_world
from .names import RegionName
from .options import PMSSOptions, exclude_options


# Settings are added to the host.yaml file
class PMSSSettings(Group):
    pass


class PMSSWorld(World):
    """
    Mario and a new ally named Kersti travel across the Mushroom Kingdom to retrieve the six Royal Stickers scattered by
    Bowser.
    """

    # Generic AP World stuffs
    settings: ClassVar[PMSSSettings]
    options_dataclass = PMSSOptions
    options: PMSSOptions
    web: ClassVar[WebWorld] = web_world.PMSSWebWorld()
    game = constants.GAME
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_groups = locations.LOCATION_GROUP_MAP
    item_name_groups = items.ITEM_GROUP_MAP
    origin_region_name = RegionName.DECALBURG_FESTIVAL_1

    # World specific stuffs
    slot_data: dict[str, Any]

    # Universal Tracker stuffs
    ut_can_gen_without_yaml = True
    is_ut: bool
    # Optional: Uncomment if your (emo/pop)tracker pack will be bundled with the apworld.
    # tracker_world: ClassVar[dict[str, Any]] = {
    #     "map_page_folder": "tracker",  # tracker folder relative to the root of the apworld
    #     "map_page_maps": "maps/maps.json",  # maps file under the `map_page_folder`
    #     "map_page_locations": "locations/locations.json",  # locations file under the `map_page_folder`
    # }

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.slot_data = {}

    # region APWorld Generation
    # sorted in execution order
    # Comments starting with `AP:` are a process run internall
    # Comments starting with `EX:` are an expectation the world must meet for generation to succeed

    def generate_early(self):
        # UT shenanigans
        self.is_ut = getattr(self.multiworld, "generation_is_fake", False)
        self.prepare_ut()
        if self.is_ut:
            # UT doesn't need to run the generate early since all its information should come from slot_data
            return

        # Override options if necessary
        # if self.options.total_mcguffins < self.options.mcguffins_required:
        #     self.options.total_mcguffins.value = self.options.mcguffins_required.value

        # Validate the options and throw errors if necessary

        # Populate slot data from options
        option_keys = [key for key in self.options.__dict__.keys() if key not in exclude_options]
        self.slot_data["options"] = self.options.as_dict(*option_keys)

    # AP: push start_inventory and start_inventory_from_pool into precollected_items

    def create_regions(self):
        regions.create_all_regions(self)
        self.rm = regions.get_region_map(self)
        self.lm = locations.get_location_map(self)
        # create_all_locations also gives the sum of each individual vanilla item from randomized locations
        # this lets us maintain a similar amount of filler to vanilla for randomized locations regardless of options
        self.filler_options = locations.create_all_locations(self)

    # EX: All non-event locations finalized

    def create_items(self):
        base_pool, filler_options = items.create_all_items(self)
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        filler_pool = self.random.choices(
            population=list(filler_options.keys()),
            weights=list(filler_options.values()),
            k=total_locations - len(base_pool),
        )
        filler_pool = [self.create_item(name) for name in filler_pool]
        self.multiworld.itempool.extend(base_pool)
        self.multiworld.itempool.extend(filler_pool)

    # AP: local_items overrides non_local_items

    def set_rules(self):
        rules.set_all_rules(self)

    def connect_entrances(self):
        pass

    # EX: All rules finalized
    # AP: location progress type assigned, excluded overrides priority
    # AP: locality for local_items and non_local_item set

    def generate_basic(self):
        # self.gen_diagram()
        pass

    # AP: remove start_inventory_from_pool from the pool
    # AP: process item_links
    # AP: item plando is processed

    def pre_fill(self):
        pass

    # EX: finalize item pool
    # AP: perform standard fill

    def post_fill(self):
        pass

    # EX: finalize randomization, no more calls to self.random
    # AP: process progression balancing
    # AP: perform accessibility check

    def generate_output(self, output_directory: str):
        # patch.output_patch(self, output_directory)
        self.gen_diagram()
        # pass

    def extend_hint_information(self, hint_data: dict[int, dict[int, str]]):
        pass

    def fill_slot_data(self):
        return self.slot_data

    # AP: playthrough is calculated

    def write_spoiler_header(self, spoiler_handle: TextIO):
        pass

    def write_spoiler(self, spoiler_handle: TextIO):
        pass

    def write_spoiler_end(self, spoiler_handle: TextIO):
        pass

    # AP: output zip
    # endregion

    # region Utility Methods

    def create_item(self, name: str) -> items.PMSSItem:
        return items.create_item(self, name)

    def create_event(self, name: str) -> items.PMSSItem:
        return items.PMSSItem(name, ItemClassification.progression, None, self.player)

    def get_pre_fill_items(self) -> list[Item]:
        return []

    def gen_diagram(self) -> None:
        from Utils import visualize_regions

        state = self.multiworld.get_all_state(False)
        state.update_reachable_regions(self.player)
        visualize_regions(
            self.get_region(self.origin_region_name),
            f"pmss_{self.player_name}.puml",
            show_other_regions=True,
            linetype_ortho=False,
            show_entrance_names=True,
            regions_to_highlight=set(state.reachable_regions[self.player]),
        )
        pass

    # endregion

    # region Universal Tracker

    def interpret_slot_data(self, slot_data: dict[str, Any]) -> dict[str, Any] | None:
        return slot_data

    def prepare_ut(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if not (re_gen_passthrough and self.game in re_gen_passthrough):
            return
        # Get the passed through slot data from the real generation
        slot_data: dict[str, Any] = re_gen_passthrough[self.game]

        slot_options: dict[str, Any] = slot_data.get("options", {})
        # Set all your options here instead of getting them from the yaml
        for key, value in slot_options.items():
            opt: Option | None = getattr(self.options, key, None)
            if opt is not None:
                # You can also set .value directly but that won't work if you have OptionSets
                setattr(self.options, key, opt.from_any(value))

    # endregion
