import unittest
from cube import Cube, SOLVED_CUBE_LIST, GREEN, RED

class CubeTestCase(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()