import json
import pkgutil

# Import some of the manifest data to be used throughout the world
manifest_data = pkgutil.get_data(__name__, "archipelago.json")
manifest: dict[str, str] = {}
if manifest_data:
    manifest: dict[str, str] = json.loads(manifest_data.decode())


GAME = manifest["game"]
VERSION = manifest["world_version"]
