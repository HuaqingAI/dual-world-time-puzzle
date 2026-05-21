import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


class Story11ProjectStructureTest(unittest.TestCase):
    def test_required_directories_exist(self) -> None:
        required_dirs = [
            "assets",
            "data",
            "docs",
            "scenes",
            "scenes/main",
            "scenes/rooms",
            "scenes/player",
            "scenes/puzzle_objects",
            "scenes/ui",
            "scenes/debug",
            "scripts",
            "scripts/player",
            "scripts/ui",
            "scripts/debug",
            "scripts/gameplay",
        ]

        for relative_path in required_dirs:
            with self.subTest(relative_path=relative_path):
                self.assertTrue(
                    (REPO_ROOT / relative_path).is_dir(),
                    f"Missing required directory: {relative_path}",
                )

    def test_project_godot_targets_story_engine_and_main_scene(self) -> None:
        project = read_text("project.godot")

        self.assertIn('config/features=PackedStringArray("4.6", "GL Compatibility")', project)
        self.assertIn('run/main_scene="res://scenes/main/main.tscn"', project)
        self.assertIn('renderer/rendering_method="gl_compatibility"', project)
        self.assertIn('renderer/rendering_method.mobile="gl_compatibility"', project)
        self.assertFalse(list(REPO_ROOT.glob("*.csproj")), "Story 1.1 must use GDScript, not C#.")

    def test_main_scene_loads_first_room(self) -> None:
        main_scene = read_text("scenes/main/main.tscn")

        self.assertRegex(main_scene, r'\[node name="Main" type="Node2D"\]')
        self.assertIn('path="res://scenes/rooms/room_001.tscn"', main_scene)
        self.assertIn('name="Room001"', main_scene)

    def test_room_scene_contains_required_shell_nodes(self) -> None:
        room_scene = read_text("scenes/rooms/room_001.tscn")
        required_node_names = [
            "Room001",
            "Ground",
            "Bounds",
            "PlayerSpawn",
            "PlayerPlaceholder",
            "Objects",
            "DistantGoalPlaceholder",
            "Camera2D",
            "UI",
        ]

        for node_name in required_node_names:
            with self.subTest(node_name=node_name):
                self.assertIn(f'name="{node_name}"', room_scene)

        self.assertRegex(room_scene, r'\[node name="Camera2D" type="Camera2D" parent="\."\]')
        self.assertIn("enabled = true", room_scene)

    def test_room_layout_places_player_path_and_goal_in_readable_composition(self) -> None:
        room_scene = read_text("scenes/rooms/room_001.tscn")

        player_match = re.search(
            r'\[node name="PlayerPlaceholder".*?\]\s+position = Vector2\((-?\d+), (-?\d+)\)',
            room_scene,
            re.S,
        )
        goal_match = re.search(
            r'\[node name="DistantGoalPlaceholder".*?\]\s+position = Vector2\((-?\d+), (-?\d+)\)',
            room_scene,
            re.S,
        )
        camera_match = re.search(
            r'\[node name="Camera2D".*?\]\s+position = Vector2\((-?\d+), (-?\d+)\).*?zoom = Vector2\(0\.(\d+), 0\.(\d+)\)',
            room_scene,
            re.S,
        )

        self.assertIsNotNone(player_match, "Player placeholder needs an explicit entrance position.")
        self.assertIsNotNone(goal_match, "Distant goal placeholder needs an explicit path-end position.")
        self.assertIsNotNone(camera_match, "Camera2D needs an explicit position and zoom below 1.0.")

        player_x = int(player_match.group(1))
        goal_x = int(goal_match.group(1))
        self.assertLess(player_x, 0, "Player should start near the left/entrance side of the room.")
        self.assertGreater(goal_x, 0, "Goal should sit farther along the main path.")
        self.assertGreater(goal_x - player_x, 600, "Player, path direction, and goal should read in one frame.")

        self.assertIn('name="MainPath"', room_scene)
        self.assertIn('name="RoomOutline"', room_scene)

    def test_goal_uses_shape_and_outline_not_color_only(self) -> None:
        room_scene = read_text("scenes/rooms/room_001.tscn")

        for visual_node in ["GoalHalo", "GoalCore", "GoalStem"]:
            with self.subTest(visual_node=visual_node):
                self.assertIn(f'name="{visual_node}"', room_scene)

        self.assertRegex(room_scene, r'\[node name="GoalHalo" type="Line2D"')
        self.assertRegex(room_scene, r'\[node name="GoalCore" type="Polygon2D"')

    def test_default_launch_has_no_debug_overlay_or_complex_ui(self) -> None:
        room_scene = read_text("scenes/rooms/room_001.tscn")
        disallowed_visible_ui = [
            'type="Label"',
            'type="RichTextLabel"',
            'type="Button"',
            'name="DebugOverlay"',
            'name="PauseMenu"',
            'name="TaskList"',
        ]

        for marker in disallowed_visible_ui:
            with self.subTest(marker=marker):
                self.assertNotIn(marker, room_scene)

        self.assertFalse(
            (REPO_ROOT / "scripts" / "autoloads").exists(),
            "Story 1.1 must not create autoload runtime managers.",
        )


if __name__ == "__main__":
    unittest.main()
