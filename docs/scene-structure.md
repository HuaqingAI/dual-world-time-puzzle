# Story 1.1 Scene Structure

The first playable shell starts at `res://scenes/main/main.tscn` and instances `res://scenes/rooms/room_001.tscn`.

`Room001` reserves the core boundaries required by later stories:

- `Ground` for the readable floor layer and main path.
- `Bounds` for visible room limits and collision placeholders.
- `PlayerSpawn` and `PlayerPlaceholder` for the future player scene replacement.
- `Objects` for puzzle object placeholders, currently including `DistantGoalPlaceholder`.
- `UI` as an empty canvas layer reserved for later HUD or prompt work.

The shell intentionally avoids autoloads, movement scripts, debug overlays, long tutorial text, and complex menus.
