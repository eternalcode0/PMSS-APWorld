from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items, regions
from .constants import GAME
from .data import RandomizationType, location_data
from .names import LocationName as L

if TYPE_CHECKING:
    from .world import PMSSWorld


class PMSSLocation(Location):
    game = GAME


def get_location_names_with_ids(location_names: list[L]) -> dict[str, int]:
    return {location_name: LOCATION_ENUM_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: "PMSSWorld"):
    region_map = regions.get_region_map(world)
    for location in location_data.LOCATION_DATA:
        rt = location.setting(world.options) if callable(location.setting) else location.setting
        if rt == RandomizationType.VANILLA_WORLD:
            loc = PMSSLocation(
                world.player, location.name, LOCATION_ENUM_TO_ID[location.name], region_map[location.region]
            )
            loc.place_locked_item(world.create_item(location.item))
            region_map[location.region].locations.append(loc)
        elif rt == RandomizationType.VANILLA_EVENT:
            region_map[location.region].add_event(location.name, location.item, None, PMSSLocation, items.PMSSItem)
        elif rt == RandomizationType.RANDOM:
            region_map[location.region].locations.append(
                PMSSLocation(
                    world.player, location.name, LOCATION_ENUM_TO_ID[location.name], region_map[location.region]
                )
            )


def get_location_map(world: "PMSSWorld", location_names: list[L] | None = None) -> dict[L, PMSSLocation]:
    if location_names is None or len(location_names) == 0:
        location_names = list(L)
    return {location.name: location for location in world.get_locations() if location.name in location_names}


BASE_LOCATION_ID = 0x1AC546
LOCATION_ENUM_TO_ID = {data.name: data.code + BASE_LOCATION_ID for data in location_data.LOCATION_DATA}
LOCATION_NAME_TO_ID = {name.value: num for name, num in LOCATION_ENUM_TO_ID.items()}
LOCATION_GROUPS = {group for loc in location_data.LOCATION_DATA for group in loc.groups}
LOCATION_GROUP_MAP = {
    group: {loc.name.value for loc in location_data.LOCATION_DATA if group in loc.groups and loc.region is not None}
    for group in LOCATION_GROUPS
}
