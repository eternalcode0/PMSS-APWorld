from typing import TYPE_CHECKING

from BaseClasses import Region

from .names import RegionName

if TYPE_CHECKING:
    from .world import PMSSWorld


def create_all_regions(world: "PMSSWorld"):
    player = world.player
    multiworld = world.multiworld

    multiworld.regions.extend([Region(region_name, player, multiworld) for region_name in RegionName])


def get_region_map(world: "PMSSWorld", region_names: list[RegionName] | None = None) -> dict[RegionName, Region]:
    if region_names is None or len(region_names) == 0:
        region_names = list(RegionName)
    return {region_name: world.get_region(region_name) for region_name in region_names}
