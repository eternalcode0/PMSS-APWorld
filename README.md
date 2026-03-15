# Paper Mario Sticker Star: APWorld

## Development Notes

This was built with ZobeePlays's manual as a reference, all notes are made in regard to the differences between the two
versions:

I made a couple minor fixes to the logic that are probably needed in the future:

- The manual looked like it was connecting one level to another the same as the game's World Map actually looks, instead I made a "World Map" region that connects to each level directly and expected the player to have the respective "Comet Piece" to enter it. The comet pieces are kept vanilla so the logic is the same as the manual, however, this makes the region graph easier to traverse and lessens the amount of changes required if the game is ever made open world.
- The Gardener Toad in Bouquet Gardens required a progression Fire/Ice Flower sticker added to the pool but the player could technically spend/throw away the sticker in the pool if it wasn't on a repeatable location. To prevent this I turned Decalburg & Whammino Mountain shops into vanilla event locations to expect the player to purchase stickers from them for access. This seemed like the simplest way to get renewable stickers for now but any other method to farm stickers works too. For example, the romhack could provide an npc that gives any sticker you've previously obtained for free.

A couple other notes about what I did for the apworld:

- I started including some options that should be relatively simple for the apworld to add, I didn't consider how easy/hard it'd be for the romhack so some options may need to be removed. None of the options are hooked up at the moment since I can't dedicate that much time. If I get the time, I'll also provide an example for how I think the yaml options should update location/item data.
- I didn't decide what the filler pool should use so it's currently all Sandal Stickers :P the `create_all_items` function in the items file returns a dictionary of item name to weights if you want to customize it just change the data in that dictionary.
- I only half finished the location data, I planned on assigning all the vanilla items to each location for an eventual remote_items setting but didn't get that far. So right now the item attribute on location data only does something if the RandomizationType is set to VANILLA_EVENT or VANILLA_WORLD, otherwise it can be ignored.
- Since there wasn't World 6 locations for bowser or Gate cliff, I've defaulted goal to be gathering the 5 Royal Stickers. I also defaulted the Red royal sticker to be on the world 1 boss and the rest to be in the multiworld pool until their locations are done. Adjust the `count` attribute on the item data and the `setting` attribute on the location data to match whichever method you want.
