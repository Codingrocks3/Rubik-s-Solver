import unittest
from cube import Cube, SOLVED_CUBE_LIST, GREEN, RED

class CubeTestCase(unittest.TestCase):
    def test_algorithm_double_turns(self):
        for move in ["U", "L", "F", "R", "D", "B"]:
            with self.subTest(move=move):
                before = [face.copy() for face in self.cube.cube_state]
                self.cube.algorithm(f"{move} {move}")
                double = [face.copy() for face in self.cube.cube_state]
                self.cube = Cube()
                self.cube.algorithm(f"{move}2")
                self.assertEqual(self.cube.cube_state, double)

    def test_algorithm_middle_slices_raise(self):
        for move in ["M", "M'", "E", "E'", "S", "S'"]:
            with self.assertRaises(NotImplementedError):
                self.cube.algorithm(move)
    def setUp(self):
        self.cube = Cube()

    def test_cube_starts_solved(self):
        self.assertTrue(self.cube.solved)
        self.assertEqual(self.cube.cube_state, SOLVED_CUBE_LIST)

    def test_clockwise_rotation_changes_cube(self):
        before = [face.copy() for face in self.cube.cube_state]
        self.cube.clockwise(GREEN)
        self.assertNotEqual(self.cube.cube_state, before)

    def test_counterclockwise_rotation_changes_cube(self):
        before = [face.copy() for face in self.cube.cube_state]
        self.cube.counterclockwise(GREEN)
        self.assertNotEqual(self.cube.cube_state, before)

    def test_rotation_and_reverse_restore_cube(self):
        before = [face.copy() for face in self.cube.cube_state]
        self.cube.clockwise(RED)
        self.cube.counterclockwise(RED)
        self.assertEqual(self.cube.cube_state, before)

    def test_algorithm_rotations(self):
        before = [face.copy() for face in self.cube.cube_state]
        self.cube.algorithm("U U'")
        self.assertEqual(self.cube.cube_state, before)

        before = [face.copy() for face in self.cube.cube_state]
        self.cube.algorithm("L L'")
        self.assertEqual(self.cube.cube_state, before)

        before = [face.copy() for face in self.cube.cube_state]
        self.cube.algorithm("F F'")
        self.assertEqual(self.cube.cube_state, before)

        before = [face.copy() for face in self.cube.cube_state]
        self.cube.algorithm("R R'")
        self.assertEqual(self.cube.cube_state, before)

        before = [face.copy() for face in self.cube.cube_state]
        self.cube.algorithm("D D'")
        self.assertEqual(self.cube.cube_state, before)

        before = [face.copy() for face in self.cube.cube_state]
        self.cube.algorithm("B B'")
        self.assertEqual(self.cube.cube_state, before)

    def test_algorithm_invalid_input(self):
        with self.assertRaises(ValueError):
            self.cube.algorithm("X")

if __name__ == '__main__':
    unittest.main()