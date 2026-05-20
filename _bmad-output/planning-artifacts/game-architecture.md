---
title: 'Game Architecture'
project: 'dual-world-time-puzzle'
date: '2026-05-19'
author: 'Sue'
version: '1.0'
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9]
status: 'complete'
engine: 'Godot 4.6.2 stable'
platform: 'PC / Steam; Web demo'

# Source Documents
gdd: 'D:\ProgramData\git\repository\github\huaqingai\dual-world-time-puzzle\_bmad-output\planning-artifacts\gdds\gdd-dual-world-time-puzzle-2026-05-19\gdd.md'
epics: 'D:\ProgramData\git\repository\github\huaqingai\dual-world-time-puzzle\_bmad-output\planning-artifacts\gdds\gdd-dual-world-time-puzzle-2026-05-19\epics.md'
ux: 'D:\ProgramData\git\repository\github\huaqingai\dual-world-time-puzzle\_bmad-output\planning-artifacts\ux-design-specification.md'
brief: 'D:\ProgramData\git\repository\github\huaqingai\dual-world-time-puzzle\_bmad-output\game-brief.md'
---

# Game Architecture

## Executive Summary

**微光花园 / Seedlight Garden** architecture is designed for Godot 4.6.2 stable with GDScript, targeting PC / Steam and a Web demo.

**Key Architectural Decisions:**

- Use a global `WorldStateManager` state machine for `Withered`, `Bloom`, and `Switching`, with state-responsive puzzle objects subscribing to typed signals.
- Use local JSON saves with schema versioning for planted seeds, center garden restoration, completed rooms, and settings.
- Use Godot Resources for editable game data and packed scenes for entity creation, keeping room, seed, restoration, hint, and UI systems in clearly separated folders.

**Project Structure:** Hybrid organization with 8 core systems mapped to explicit locations.

**Implementation Patterns:** 10 patterns defined to ensure AI agent consistency, including 3 project-specific patterns for world-state response, seed carry/plant flow, and restoration flags.

**Ready for:** Epic implementation phase.

## Document Status

This architecture document was created through the GDS Architecture Workflow.

**Steps Completed:** 9 of 9 (Complete)

---

## Architecture Summary

Seedlight Garden uses Godot 4.6.2 stable with GDScript for a 2D room-based cozy puzzle targeting PC and Web demo. The architecture centers on a global world-state state machine, consistent state-responsive puzzle objects, local JSON progression, and strict scene/script/data organization so AI agents can implement systems without inventing incompatible patterns.

---

## Project Context

### Game Overview

**微光花园 / Seedlight Garden** - 休闲俯视角双世界花园解谜游戏。玩家控制迷路的小精灵，在“枯萎 / 盛放”状态之间切换，观察路径和对象变化，收集发光种子，并通过种植让中心花园逐步恢复生命、颜色和声音。

### Technical Scope

**Platform:** PC / Steam；Web demo 用于试玩、传播和早期反馈；移动端仅作为后续验证方向  
**Genre:** Cozy puzzle / 2D top-down room-based puzzle  
**Project Level:** Medium complexity solo-indie vertical slice first

### Core Systems

| System | Complexity | GDD Reference |
| --- | --- | --- |
| Player movement and room shell | Medium | Game Mechanics / Controls and Input |
| Dual-world state machine | High | World switch, Withered / Bloom / Switching |
| State-responsive puzzle objects | High | Vine bridge, flower door, exit flower, seed |
| Seed collection and restoration | Medium | Core Gameplay Loop, Player Progression |
| Visual/audio feedback orchestration | High | Art and Audio Direction, Feedback Pillar |
| Player assistance and hints | Medium | Player Assistance |
| Progress persistence | Medium | Seed planting, center garden permanent changes |
| PC/Web build pipeline | Medium | Technical Specifications, Platform Details |

### Technical Requirements

- Use a shared room map with state-driven object changes rather than loading two separate worlds.
- Central world state should support `Withered`, `Bloom`, and `Switching`; switching must lock repeat input during the 0.45-0.75s transition.
- Puzzle objects must respond to world state through visuals, collision, interaction availability, animation, and audio.
- Critical object states cannot rely on color alone; shape, outline, animation, glow, or sound must also change.
- PC target is 1080p stable 60 FPS; Web demo should target 60 FPS on mainstream desktop browsers, with 30 FPS as acceptable lower bound on weaker devices.
- Keyboard and controller support are required for the first version; touch controls are deferred.

### Complexity Drivers

- Dual-world object synchronization: visual state, collision state, animation, audio, and interaction state must stay coherent.
- Readability-driven architecture: objects need explicit states and debug-friendly transitions so AI agents do not implement one-off behavior.
- Feedback timing: world switch, vine bridge, flower door, seed follow, exit flower, and planting ritual all need coordinated timing.
- Web export constraints: asset size, load time, shader/effect cost, and audio loading must stay controlled.
- Solo + AI production: file structure, naming conventions, asset import rules, and scene patterns need to be strict enough to prevent inconsistent implementation.

### Technical Risks

- World switching becomes only a palette swap instead of a readable state transformation.
- Puzzle object logic fragments into bespoke scripts, making later rooms hard to extend.
- Collision and visuals desynchronize during switching.
- Audio/animation polish is delayed too long, weakening the core feedback loop.
- Web demo load/performance budget is missed because asset and effect constraints are not defined early.
- AI-generated assets create style inconsistency unless import and visual-state rules are documented.

---

## Engine & Framework

### Selected Engine

**Godot** v4.6.2 stable

**Version Verification Date:** 2026-05-19

**Rationale:** Godot 4.6.2 is a strong fit for a solo-developed 2D cozy puzzle with PC and Web demo targets. It provides a lightweight scene/node workflow, mature 2D physics, GDScript iteration speed, input mapping, audio buses, animation tooling, and practical exports without requiring a heavy commercial engine stack. Because Godot 4 C# does not currently support Web export, the project should use GDScript for gameplay code.

### Project Initialization

Start from an empty Godot project rather than a generic starter template. Existing public starters skew toward platformers, shooters, or broad boilerplate, while this project needs a small, explicit architecture around world state, puzzle object responses, feedback orchestration, and Web export constraints.

```bash
godot --editor --path .
```

### Engine-Provided Architecture

| Component | Solution | Notes |
| --------- | -------- | ----- |
| 2D Rendering | Godot 2D renderer | Use Compatibility renderer for Web-first reliability unless effects require Forward+ validation. |
| Physics | `CharacterBody2D`, `StaticBody2D`, `Area2D`, collision layers | Used for player movement, room bounds, bridge passability, triggers, and interactions. |
| Animation | `AnimationPlayer`, `AnimationTree`, tweens | Used for world switch transitions, object state changes, seed follow, and planting ritual timing. |
| Audio | Audio buses and audio players | Use buses for Withered/Bloom ambience, SFX, and music-layer control. |
| Input | Input Map | Map movement, world switch, interact, reset, and pause for keyboard and controller. |
| Scene Management | Node tree, packed scenes, autoloads | Use reusable object scenes and autoload singletons for world state and progression. |
| Resource Pipeline | Godot import system | Define import conventions for sprites, audio, particles, and Web-friendly compression. |
| Build System | Godot export presets | Maintain PC and Web export presets from the start of the vertical slice. |

### Remaining Architectural Decisions

The following decisions must be made explicitly:

- World state model: `Withered`, `Bloom`, and `Switching`, including transition guards.
- State-responsive object contract for bridges, doors, seeds, exit flowers, hints, and future puzzle objects.
- Collision and interaction update timing during world switches.
- Feedback event flow for visual, audio, particle, camera, and UI reactions.
- Scene and directory conventions for AI-assisted implementation consistency.
- Save/progression model for planted seeds and center garden restoration.
- Web demo performance and asset budget rules.
- Debug tooling for world state, object state, collision state, and progression flags.

### AI Development Tools

Use MCP servers as optional but recommended AI development support:

| Tool | Repo | Install | Requirements |
| --- | --- | --- | --- |
| GoPeak Godot MCP | `HaD0Yun/Gopeak-godot-mcp` | Node.js MCP server via `npx -y gopeak` or global npm install | Godot 4.x, Node.js 18+ |
| Context7 | `upstash/context7` | MCP server via `npx -y @upstash/context7-mcp` or Docker | Node.js or Docker |

**GoPeak Godot MCP capabilities:**

- Find, launch, and manage Godot projects and editor execution.
- Create and modify scenes, nodes, GDScript files, resources, materials, shaders, and imports.
- Read logs, inspect live scene tree state, capture screenshots, and support runtime/debug workflows.
- Useful for AI-assisted scene inspection and implementation checks.

**Context7 capabilities:**

- Retrieve current Godot and library documentation during AI-assisted development.
- Reduce outdated API usage by grounding implementation in current docs.

---

## Architectural Decisions

### Decision Summary

| Category | Decision | Version | Rationale |
| --- | --- | --- | --- |
| Engine | Godot + GDScript | Godot 4.6.2 stable | 适合 2D、PC/Web、单人开发和快速迭代；GDScript 避免 Godot 4 C# Web 导出限制 |
| State Management | `WorldStateManager` Autoload + explicit state machine | N/A | 双世界状态是全局规则，但转换必须受控 |
| Puzzle Object Contract | `WorldStateResponder` component/base contract | N/A | 保证藤蔓桥、花门、出口花、种子等对象用一致方式响应世界状态 |
| Scene Structure | `Main -> Room -> Layers/Objects/Player/UI` | N/A | 保持 Godot 场景树清晰，方便 AI agent 复用 |
| Save System | Local JSON save with schema version | N/A | 当前只保存种子、中心花园恢复、设置；简单、可读、可迁移 |
| Asset Loading | Vertical slice preload; v1 scene-based room loading | N/A | 切片优先简单稳定，后续多房间再按房间加载 |
| Audio Architecture | Godot native Audio Bus | N/A | 足够支持 Withered/Bloom ambience、SFX、UI 和音乐层切换 |
| Input/UI | Godot InputMap + Control/CanvasLayer | N/A | 覆盖键盘、手柄、暂停、提示和设置需求 |

### State Management

**Approach:** `WorldStateManager` Autoload with explicit state machine.

The game uses one authoritative world state: `Withered`, `Bloom`, or `Switching`. Gameplay objects do not own the global state. They subscribe to world-state change signals and update their own visuals, collision, audio, and interaction availability.

### Puzzle Object Architecture

**Approach:** Shared `WorldStateResponder` contract.

All dual-world puzzle objects implement a common response surface:

- Receive world-state transition start/end.
- Expose current local object state.
- Update visuals and animation.
- Update collision and interaction availability.
- Optionally emit feedback events.

This prevents each room object from inventing a separate switching pattern.

### Data Persistence

**Save System:** Local JSON save file with schema version.

Save data includes planted seed IDs, center garden restoration flags, completed rooms, settings, and future migration version. Steam Cloud can be added later by syncing the same local save path.

### Asset Management

**Loading Strategy:** Preload vertical-slice assets; move to scene-based room loading for v1.

The vertical slice should avoid loading complexity. When content grows, each room becomes a loading boundary with explicit dependencies and a lightweight transition.

### Audio Architecture

**Approach:** Godot native audio buses.

Recommended buses:

- `Master`
- `Music`
- `Ambience`
- `SFX`
- `UI`

Withered/Bloom ambience should crossfade through the audio manager. Key object feedback stays as local SFX triggered by object events.

### Input and UI

**Input:** Godot InputMap actions for movement, world switch, interact, reset, and pause.  
**UI:** Godot Control nodes under CanvasLayer for pause, settings, hint prompts, and debug overlays.

### Deferred Decisions

- Steam Cloud and Steam Input.
- GUT automated testing setup. Test automation is deferred until the first playable Godot skeleton exists; manual validation drives the vertical slice first.
- Editor validation tools.
- Advanced async loading.
- Full remapping UI.
- Steam achievements.

---

## Cross-cutting Concerns

These patterns apply to ALL systems and must be followed by every implementation.

### Error Handling

**Strategy:** Recoverable errors log a warning and use a safe fallback. Critical errors log an error and move the game into a safe state, such as pausing, resetting the current room, or returning the player to the room entrance.

**Rules:**

- Do not show raw technical errors to players.
- Recoverable object errors must not break the room if a fallback is possible.
- Critical progression/save errors must stop the risky operation and log enough context to debug.
- Never silently ignore failed world-state, save, or interaction operations.

**Example:**

```gdscript
func apply_world_state(state: WorldStateManager.WorldState) -> void:
    if animation_player == null:
        Log.warn("VineBridge", "Missing AnimationPlayer; applying collision fallback", {
            "node": get_path(),
            "state": state
        })
        collision_shape.disabled = state != WorldStateManager.WorldState.BLOOM
        return

    animation_player.play("bloom" if state == WorldStateManager.WorldState.BLOOM else "withered")
```

### Logging

**Format:** Structured plain text through a `Log` Autoload.  
**Destination:** Godot console during development; optional file/debug panel later.

**Log Levels:**

- `ERROR`: broken save, missing critical scene, impossible world state.
- `WARN`: missing optional node, fallback path used, recoverable data issue.
- `INFO`: room loaded, seed planted, restoration applied.
- `DEBUG`: state transitions, collision toggles, hint triggers.
- `TRACE`: disabled by default; only for local deep debugging.

**Example:**

```gdscript
Log.info("WorldState", "Switch started", {"from": "Withered", "to": "Bloom"})
Log.warn("SaveManager", "Unknown save version; attempting migration", {"version": save_version})
Log.error("RoomLoader", "Room scene missing", {"room_id": room_id, "path": scene_path})
```

### Configuration

**Approach:** Separate fixed constants, editable gameplay resources, player settings, and platform-specific export values.

**Configuration Structure:**

- Game constants: typed scripts, for values that should not be tuned in normal content work.
- Gameplay tuning: `.tres` Resources, for switch duration, hint delay, seed follow spacing, interaction radius.
- Player settings: local JSON, for volume, display, accessibility, input preferences.
- Platform settings: export preset notes and platform-specific constants.

**Example:**

```gdscript
@export var switch_duration: float = 0.6
@export var idle_hint_delay: float = 50.0
@export var seed_follow_distance: float = 28.0
```

### Event System

**Pattern:** Godot typed signals for local communication; `EventBus` Autoload only for cross-system events.

**Event Naming:** Past-tense snake_case for completed events.

**Global Events:**

- `world_state_changed(new_state, previous_state)`
- `seed_collected(seed_id, room_id)`
- `seed_planted(seed_id, garden_slot_id)`
- `room_completed(room_id)`
- `restoration_applied(restoration_id)`

**Example:**

```gdscript
# EventBus.gd
signal seed_collected(seed_id: String, room_id: String)
signal restoration_applied(restoration_id: String)

# Seed.gd
func collect() -> void:
    EventBus.seed_collected.emit(seed_id, room_id)
    queue_free()
```

### Debug Tools

**Available Tools:**

- Debug overlay showing FPS, current room, world state, switching flag, carried seed, planted seeds, and restoration flags.
- World-state hotkeys in development builds.
- Room reset and respawn-to-entrance command.
- Seed/progression flag inspector.
- Optional collision visibility toggle for puzzle objects.

**Activation:** Controlled by `debug_enabled`. Debug tools may exist in development and Web demo test builds, but release builds must hide debug commands and overlays by default.

**Mandatory Debug Display Fields:**

- `world_state`
- `is_switching`
- `current_room_id`
- `carried_seed_id`
- `planted_seed_ids`
- `restoration_flags`
- `fps`

---

## Project Structure

### Organization Pattern

**Pattern:** Hybrid

**Rationale:** Godot naturally separates scenes, scripts, resources, and imported assets. Inside those top-level folders, gameplay code is grouped by domain so AI agents can place world-state, puzzle-object, seed, restoration, hint, and UI work consistently.

### Directory Structure

```text
seedlight_garden/
├── project.godot
├── export_presets.cfg
├── addons/
├── assets/
│   ├── art/
│   │   ├── characters/
│   │   ├── rooms/
│   │   ├── puzzle_objects/
│   │   ├── seeds/
│   │   ├── restoration/
│   │   ├── vfx/
│   │   └── ui/
│   ├── audio/
│   │   ├── ambience/
│   │   ├── music/
│   │   ├── sfx/
│   │   └── ui/
│   └── fonts/
├── data/
│   ├── gameplay/
│   ├── rooms/
│   ├── seeds/
│   ├── restoration/
│   └── settings/
├── scenes/
│   ├── main/
│   ├── rooms/
│   ├── player/
│   ├── puzzle_objects/
│   ├── seeds/
│   ├── restoration/
│   ├── ui/
│   └── debug/
├── scripts/
│   ├── autoloads/
│   ├── core/
│   ├── gameplay/
│   │   ├── world_state/
│   │   ├── puzzle_objects/
│   │   ├── seeds/
│   │   ├── restoration/
│   │   ├── hints/
│   │   └── interaction/
│   ├── player/
│   ├── ui/
│   ├── debug/
│   ├── resources/
│   └── utils/
├── tests/
│   ├── unit/
│   └── integration/
└── docs/
```

### System Location Mapping

| System | Location | Responsibility |
| --- | --- | --- |
| WorldStateManager | `scripts/autoloads/world_state_manager.gd` | Owns `Withered`, `Bloom`, `Switching` state and transition signals |
| EventBus | `scripts/autoloads/event_bus.gd` | Publishes cross-system events |
| Log | `scripts/autoloads/log.gd` | Provides consistent structured logging |
| SaveManager | `scripts/autoloads/save_manager.gd` | Loads, validates, migrates, and writes local save JSON |
| AudioManager | `scripts/autoloads/audio_manager.gd` | Controls buses, ambience crossfades, and global audio state |
| Player | `scenes/player/`, `scripts/player/` | Movement, interaction scan, animation hooks |
| World-state responders | `scripts/gameplay/world_state/` | Shared contract and helpers for state-responsive objects |
| Puzzle objects | `scenes/puzzle_objects/`, `scripts/gameplay/puzzle_objects/` | Vine bridge, flower door, exit flower, and future room objects |
| Seeds | `scenes/seeds/`, `scripts/gameplay/seeds/`, `data/seeds/` | Seed pickup, following, planting data |
| Restoration | `scenes/restoration/`, `scripts/gameplay/restoration/`, `data/restoration/` | Center garden permanent restoration flags and visuals |
| Hints | `scripts/gameplay/hints/`, `scenes/ui/` | Passive cues, idle nudges, manual hints |
| UI | `scenes/ui/`, `scripts/ui/` | Pause, settings, hint prompts, menus |
| Debug | `scenes/debug/`, `scripts/debug/` | Debug overlay, state inspector, development commands |
| Rooms | `scenes/rooms/`, `data/rooms/` | Room scene composition and room metadata |

### Naming Conventions

#### Files

- Folders and files use `snake_case`.
- Scene files use `snake_case.tscn`, e.g. `vine_bridge.tscn`, `center_garden.tscn`.
- Script files use `snake_case.gd`, e.g. `world_state_manager.gd`.
- Resource files use `snake_case.tres`, e.g. `room_001.tres`, `seed_root_001.tres`.
- Asset files include domain and state where useful, e.g. `vine_bridge_bloom.png`, `flower_door_withered.png`.

#### Code Elements

| Element | Convention | Example |
| --- | --- | --- |
| Class names | `PascalCase` | `WorldStateManager` |
| Functions | `snake_case` | `apply_world_state()` |
| Variables | `snake_case` | `carried_seed_id` |
| Constants | `UPPER_SNAKE_CASE` | `DEFAULT_SWITCH_DURATION` |
| Signals | past-tense `snake_case` | `seed_collected` |
| Enum values | `UPPER_SNAKE_CASE` | `WITHERED`, `BLOOM`, `SWITCHING` |
| Private members | leading underscore | `_current_state` |

#### Game Assets

- Animation names use `snake_case`: `switch_to_bloom`, `bridge_unfold`, `seed_collect`.
- Audio files use domain + action: `world_switch_bloom.ogg`, `seed_collect_01.ogg`.
- Room IDs use stable numeric names: `room_001`, `room_002`.
- Seed IDs use family + number: `seed_root_001`.
- Restoration IDs use area + slot: `root_garden_slot_001`.

### Architectural Boundaries

- `scripts/autoloads/` contains only global services. Do not place room-specific logic there.
- Puzzle objects may read world state and emit events, but must not directly mutate save data or center garden restoration.
- Restoration systems consume seed/room completion events and update permanent garden state.
- UI requests gameplay changes through managers or EventBus; it must not directly edit puzzle object internals.
- Debug tools must not be required for gameplay to function.
- `assets/` stores source/imported media, `data/` stores editable game data, `scenes/` stores node compositions, and `scripts/` stores logic.

---

## Implementation Patterns

These patterns ensure consistent implementation across all AI agents.

### Novel Patterns

#### World State Response Pattern

**Purpose:** Ensure every object affected by Withered/Bloom switching updates visuals, collision, interaction, animation, and audio consistently.

**Components:**

- `WorldStateManager`: owns global state and emits transition signals.
- `WorldStateResponder`: base script or component used by state-responsive objects.
- Puzzle object scripts: override `apply_world_state()` for object-specific behavior.
- `FeedbackEmitter`: optional helper for visual/audio feedback events.

**Data Flow:**

1. Player requests world switch.
2. `WorldStateManager` enters `SWITCHING` and emits `world_switch_started`.
3. Responders lock interaction and play transition feedback.
4. `WorldStateManager` commits target state and emits `world_state_changed`.
5. Responders apply visuals, collision, interaction availability, and local audio.
6. `WorldStateManager` exits switching and emits `world_switch_finished`.

**Implementation Guide:**

```gdscript
class_name WorldStateResponder
extends Node2D

@export var active_in_bloom: bool = true
@onready var collision_shape: CollisionShape2D = $CollisionShape2D
@onready var animation_player: AnimationPlayer = $AnimationPlayer

func _ready() -> void:
    WorldStateManager.world_state_changed.connect(_on_world_state_changed)
    apply_world_state(WorldStateManager.current_state)

func _on_world_state_changed(new_state: WorldStateManager.WorldState, _previous_state: WorldStateManager.WorldState) -> void:
    apply_world_state(new_state)

func apply_world_state(state: WorldStateManager.WorldState) -> void:
    var is_active := state == WorldStateManager.WorldState.BLOOM if active_in_bloom else state == WorldStateManager.WorldState.WITHERED
    collision_shape.disabled = not is_active
    animation_player.play("active" if is_active else "inactive")
```

**Usage:** Use for vine bridges, flower doors, exit flowers, state-based hints, and any future object whose behavior changes between Withered and Bloom.

#### Seed Carry & Plant Pattern

**Purpose:** Treat seeds as emotional objects, not inventory items. A seed is collected, follows the player, then triggers restoration when planted.

**Components:**

- `Seed`: collectible room object.
- `SeedFollower`: player child node that displays carried seed visuals.
- `SeedData`: resource defining seed ID, family, visuals, and restoration target.
- `RestorationManager`: applies permanent garden state after planting.
- `SaveManager`: persists planted seed IDs and restoration flags.

**Data Flow:**

1. Player interacts with or touches `Seed`.
2. `Seed` emits `seed_collected`.
3. `SeedFollower` attaches seed visual to player.
4. Exit flower or planting point checks `SeedFollower.carried_seed_id`.
5. Planting emits `seed_planted`.
6. `RestorationManager` applies restoration and asks `SaveManager` to persist.

**Implementation Guide:**

```gdscript
func collect(actor: Node) -> void:
    if actor.seed_follower.has_seed():
        Log.warn("Seed", "Player already carries a seed", {"seed_id": seed_data.seed_id})
        return

    actor.seed_follower.attach_seed(seed_data)
    EventBus.seed_collected.emit(seed_data.seed_id, room_id)
    queue_free()
```

**Usage:** Use for all mainline seeds and future optional collectible seeds unless they have no planting behavior.

#### Restoration Flag Pattern

**Purpose:** Ensure center garden restoration is permanent and never lost by room reset.

**Components:**

- `RestorationData`: resource mapping seed IDs to garden slots and visuals.
- `RestorationManager`: owns runtime restoration state.
- `SaveManager`: persists restoration flags.
- `CenterGardenView`: displays restored/locked/unrestored visuals.

**Implementation Guide:**

```gdscript
func apply_restoration(restoration_id: String) -> void:
    if _restoration_flags.has(restoration_id):
        return

    _restoration_flags[restoration_id] = true
    EventBus.restoration_applied.emit(restoration_id)
    SaveManager.set_restoration_flag(restoration_id, true)
```

**Usage:** Use for all permanent center garden changes and any future room-completion permanent state.

### Communication Patterns

**Pattern:** Use the narrowest communication path that fits the relationship.

- Parent to child: direct call or exported node reference.
- Child to parent: signal.
- Sibling objects: parent mediator or signal connection.
- Cross-system events: `EventBus`.
- Global services: Autoload managers.

**Example:**

```gdscript
# Child emits.
signal interaction_completed(object_id: String)

# Parent connects.
flower_door.interaction_completed.connect(_on_object_interaction_completed)

# Global event only when multiple systems care.
EventBus.room_completed.emit(room_id)
```

### Entity Patterns

**Creation:** Use packed scene instantiation for gameplay entities. Use object pooling only for high-frequency transient VFX or particles if profiling proves it is needed.

**Example:**

```gdscript
@export var seed_scene: PackedScene

func spawn_seed(seed_data: SeedData, spawn_position: Vector2) -> Seed:
    var seed := seed_scene.instantiate() as Seed
    seed.seed_data = seed_data
    seed.global_position = spawn_position
    seeds_layer.add_child(seed)
    return seed
```

### State Patterns

**Pattern:** Use explicit state machines for global/gameplay-critical transitions and enums for simple local object state.

**Example:**

```gdscript
enum WorldState { WITHERED, BLOOM, SWITCHING }

func request_switch() -> void:
    if current_state == WorldState.SWITCHING:
        return

    var target := WorldState.BLOOM if current_state == WorldState.WITHERED else WorldState.WITHERED
    _begin_switch(target)
```

### Data Patterns

**Access:** Use `.tres` Resources for editable game definitions and `SaveManager` for persistent runtime data. No system except managers should read or write save files directly.

**Example:**

```gdscript
class_name SeedData
extends Resource

@export var seed_id: String
@export var family_id: String
@export var display_name: String
@export var restoration_id: String
@export var follower_texture: Texture2D
```

### Interaction Pattern

**Pattern:** Player detects interactable `Area2D` nodes and calls a shared `interact(actor)` method. Interactables decide whether they can act.

**Example:**

```gdscript
class_name Interactable
extends Area2D

func can_interact(_actor: Node) -> bool:
    return true

func interact(_actor: Node) -> void:
    pass
```

### Lifecycle Pattern

**Pattern:** `_ready()` only caches node references, validates required children, connects signals, and applies initial state. It should not perform heavy gameplay decisions or file IO.

**Example:**

```gdscript
func _ready() -> void:
    _validate_required_nodes()
    WorldStateManager.world_state_changed.connect(_on_world_state_changed)
    apply_world_state(WorldStateManager.current_state)
```

### Consistency Rules

| Pattern | Convention | Enforcement |
| --- | --- | --- |
| World state response | All switchable objects implement `apply_world_state(state)` | Code review and base class |
| Seeds | Seeds use `SeedData` and `SeedFollower`; no inventory slot | Scene/script review |
| Restoration | Permanent changes go through `RestorationManager` | Save API boundary |
| Events | Global events only through typed `EventBus` signals | Naming and script review |
| Data | Definitions in `.tres`, saves in JSON | Directory and API boundaries |
| Entity creation | PackedScene instantiation by owner scene | Avoid global factories until needed |
| Lifecycle | `_ready()` is setup only | Code review |
| Debug | Debug state reads managers, never mutates without command method | Debug boundary |

---

## Architecture Validation

### Validation Summary

| Check | Result | Notes |
| --- | --- | --- |
| Decision Compatibility | PASS | Godot 4.6.2 + GDScript + Autoload/state machine + Resource/JSON persistence are coherent |
| GDD Coverage | PASS | Player movement, dual-world switching, puzzle objects, seeds, restoration, hints, PC/Web targets all have architectural support |
| Pattern Completeness | PASS | Communication, entity creation, state, data, interaction, lifecycle, error handling, logging, and debug patterns are defined with examples |
| Epic Mapping | PASS | E1-E7 map to project structure, systems, and implementation patterns |
| Document Completeness | PASS | Required sections exist, no placeholder/TODO markers found, version verification date recorded |

### Coverage Report

**Systems Covered:** 8/8  
**Patterns Defined:** 10 total: 3 novel patterns and 7 standard patterns  
**Decisions Made:** 8 core architectural decisions

### Issues Resolved

- Updated document status from Step 1 to Step 7.
- Added architecture summary.
- Added Godot version verification date: 2026-05-19.
- Clarified testing automation is deferred until the first playable Godot skeleton exists.

### Validation Date

2026-05-19

---

## Development Environment

### Prerequisites

- Godot 4.6.2 stable.
- GDScript for gameplay code.
- Node.js 18+ for optional MCP tooling.
- Git for source control.
- Export templates for PC and Web builds.

### AI Tooling (MCP Servers)

The following MCP servers were selected during architecture to enhance AI-assisted development:

| MCP Server | Purpose | Install Type |
| --- | --- | --- |
| GoPeak Godot MCP | Gives AI tools access to Godot project, scenes, scripts, resources, logs, screenshots, and runtime/debug workflows | Node.js MCP server |
| Context7 | Lets AI tools retrieve current Godot and library documentation | Node.js MCP server or Docker |

**Setup:**

```bash
npx -y gopeak
npx -y @upstash/context7-mcp
```

Configure your MCP client with the Godot executable path and the project path. Use GoPeak for Godot project inspection and Context7 for current documentation lookup.

### Setup Commands

```bash
mkdir seedlight_garden
cd seedlight_garden
godot --editor --path .
```

### First Steps

1. Create the directory structure from the Project Structure section.
2. Configure Godot autoloads for `WorldStateManager`, `EventBus`, `Log`, `SaveManager`, and `AudioManager`.
3. Configure MCP servers if using AI-assisted scene inspection and documentation lookup.
4. Create the first playable room skeleton using the World State Response, Seed Carry & Plant, and Restoration Flag patterns.
