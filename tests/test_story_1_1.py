import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
IGNORED_CSHARP_DIRS = {".git", ".agents", ".claude", "_bmad", "_bmad-output"}
VECTOR2_PATTERN = re.compile(r"Vector2\((-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\)")


def read_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def node_section(scene_text: str, node_name: str) -> str:
    match = re.search(
        rf'(?ms)^\[node name="{re.escape(node_name)}"[^\]]*\]\s*\n(?P<body>.*?)(?=^\[node |\Z)',
        scene_text,
    )
    if match is None:
        raise AssertionError(f"Missing node section: {node_name}")
    return match.group("body")


def node_vector2(scene_text: str, node_name: str, property_name: str) -> tuple[float, float]:
    section = node_section(scene_text, node_name)
    match = re.search(rf"^{re.escape(property_name)} = {VECTOR2_PATTERN.pattern}$", section, re.M)
    if match is None:
        raise AssertionError(f"{node_name} needs an explicit own {property_name} property.")
    return float(match.group(1)), float(match.group(2))


def assert_points_visible(
    test_case: unittest.TestCase,
    camera_position: tuple[float, float],
    camera_zoom: tuple[float, float],
    points: dict[str, tuple[float, float]],
) -> None:
    for width, height in [(1280, 720), (1600, 900), (1920, 1080)]:
        with test_case.subTest(resolution=f"{width}x{height}"):
            half_width = width / (2 * camera_zoom[0])
            half_height = height / (2 * camera_zoom[1])
            left = camera_position[0] - half_width
            right = camera_position[0] + half_width
            top = camera_position[1] - half_height
            bottom = camera_position[1] + half_height

            for point_name, (point_x, point_y) in points.items():
                with test_case.subTest(point=point_name):
                    test_case.assertGreaterEqual(point_x, left)
                    test_case.assertLessEqual(point_x, right)
                    test_case.assertGreaterEqual(point_y, top)
                    test_case.assertLessEqual(point_y, bottom)


def is_ignored_csharp_path(path: Path) -> bool:
    relative_parts = path.relative_to(REPO_ROOT).parts
    return any(part in IGNORED_CSHARP_DIRS for part in relative_parts)


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

        csharp_artifacts = [
            path
            for pattern in ("*.cs", "*.csproj")
            for path in REPO_ROOT.rglob(pattern)
            if not is_ignored_csharp_path(path)
        ]
        self.assertFalse(csharp_artifacts, "Story 1.1 must use GDScript, not C#.")

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

        player_position = node_vector2(room_scene, "PlayerPlaceholder", "position")
        goal_position = node_vector2(room_scene, "DistantGoalPlaceholder", "position")
        camera_position = node_vector2(room_scene, "Camera2D", "position")
        camera_zoom = node_vector2(room_scene, "Camera2D", "zoom")

        player_x = player_position[0]
        goal_x = goal_position[0]
        self.assertLess(player_x, 0, "Player should start near the left/entrance side of the room.")
        self.assertGreater(goal_x, 0, "Goal should sit farther along the main path.")
        self.assertGreater(goal_x - player_x, 600, "Player, path direction, and goal should read in one frame.")
        self.assertGreater(camera_zoom[0], 0)
        self.assertGreater(camera_zoom[1], 0)

        assert_points_visible(
            self,
            camera_position,
            camera_zoom,
            {
                "player": player_position,
                "goal": goal_position,
                "goal_top": (goal_position[0], goal_position[1] - 112),
                "goal_base": (goal_position[0], goal_position[1] + 184),
                "path_start": (-820, 40),
                "path_end": (860, 44),
            },
        )

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
        launch_files = [
            "project.godot",
            "scenes/main/main.tscn",
            "scenes/rooms/room_001.tscn",
        ]
        disallowed_visible_ui = [
            "[autoload]",
            'type="Label"',
            'type="RichTextLabel"',
            'type="Button"',
            'name="DebugOverlay"',
            'name="PauseMenu"',
            'name="TaskList"',
        ]

        for relative_path in launch_files:
            content = read_text(relative_path)
            for marker in disallowed_visible_ui:
                with self.subTest(relative_path=relative_path, marker=marker):
                    self.assertNotIn(marker, content)

        self.assertFalse(
            (REPO_ROOT / "scripts" / "autoloads").exists(),
            "Story 1.1 must not create autoload runtime managers.",
        )


if __name__ == "__main__":
    unittest.main()
