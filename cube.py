"""Implements a parent class for a Rubik's Cube with subclasses for faces and cubits
with functions to rotate (single rotation or full algorithm), display, and build a cube

Authors:
Kyran McCown
Kai Hogan
Blake Ogilvie
Mason Holly
Henry Fleming"""

import random
from copy import deepcopy

# Order of faces in list: Green, Red, White, Orange, Blue, Yellow
U = GREEN = 0
L = RED = 1
F = WHITE = 2
R = ORANGE = 3
D = BLUE = 4
B = YELLOW = 5


SOLVED_CUBE_LIST = [
    ["G", "G", "G",
     "G", "G", "G",
     "G", "G", "G"],  # Green face
    ["R", "R", "R",
     "R", "R", "R",
     "R", "R", "R"],  # Red face
    ["W", "W", "W",
     "W", "W", "W",
     "W", "W", "W"],  # White face
    ["O", "O", "O",
     "O", "O", "O",
     "O", "O", "O"],  # Orange face
    ["B", "B", "B",
     "B", "B", "B",
     "B", "B", "B"],  # Blue face
    ["Y", "Y", "Y",
     "Y", "Y", "Y",
     "Y", "Y", "Y"]   # Yellow face
]

POSSIBLE_MOVES = [
    "U", "U'", "U2",
    "D", "D'", "D2",
    "L", "L'", "L2",
    "R", "R'", "R2",
    "F", "F'", "F2",
    "B", "B'", "B2",
    "M", "M'", "M2",
    "E", "E'", "E2",
    "S", "S'", "S2"
]

class Cube:
    def __init__(self, cube_state=SOLVED_CUBE_LIST):
        self.cube_state = cube_state
        self.solved = self.cube_state == SOLVED_CUBE_LIST


    def face_clockwise(self, face: int):
        self.cube_state[face] = [
            self.cube_state[face][6], self.cube_state[face][3], self.cube_state[face][0],
            self.cube_state[face][7], self.cube_state[face][4], self.cube_state[face][1],
            self.cube_state[face][8], self.cube_state[face][5], self.cube_state[face][2]
        ]

    def face_counterclockwise(self, face: int):
        self.cube_state[face] = [
            self.cube_state[face][2], self.cube_state[face][5], self.cube_state[face][8],
            self.cube_state[face][1], self.cube_state[face][4], self.cube_state[face][7],
            self.cube_state[face][0], self.cube_state[face][3], self.cube_state[face][6]
        ]
    
    def u(self):
        self.face_clockwise(U)

        tmpW0 = self.cube_state[WHITE][0]
        tmpW1 = self.cube_state[WHITE][1]
        tmpW2 = self.cube_state[WHITE][2]

        self.cube_state[WHITE][0] = self.cube_state[ORANGE][0]
        self.cube_state[WHITE][1] = self.cube_state[ORANGE][1]
        self.cube_state[WHITE][2] = self.cube_state[ORANGE][2]

        self.cube_state[ORANGE][0] = self.cube_state[YELLOW][6]
        self.cube_state[ORANGE][1] = self.cube_state[YELLOW][7]
        self.cube_state[ORANGE][2] = self.cube_state[YELLOW][8]

        self.cube_state[YELLOW][6] = self.cube_state[RED][0]
        self.cube_state[YELLOW][7] = self.cube_state[RED][1]
        self.cube_state[YELLOW][8] = self.cube_state[RED][2]

        self.cube_state[RED][0] = tmpW0
        self.cube_state[RED][1] = tmpW1
        self.cube_state[RED][2] = tmpW2


    def u_prime(self):
        self.face_counterclockwise(U)

        tmpW0 = self.cube_state[WHITE][0]
        tmpW1 = self.cube_state[WHITE][1]
        tmpW2 = self.cube_state[WHITE][2]

        self.cube_state[WHITE][0] = self.cube_state[RED][0]
        self.cube_state[WHITE][1] = self.cube_state[RED][1]
        self.cube_state[WHITE][2] = self.cube_state[RED][2]

        self.cube_state[RED][0] = self.cube_state[YELLOW][6]
        self.cube_state[RED][1] = self.cube_state[YELLOW][7]
        self.cube_state[RED][2] = self.cube_state[YELLOW][8]

        self.cube_state[YELLOW][6] = self.cube_state[ORANGE][0]
        self.cube_state[YELLOW][7] = self.cube_state[ORANGE][1]
        self.cube_state[YELLOW][8] = self.cube_state[ORANGE][2]

        self.cube_state[ORANGE][0] = tmpW0
        self.cube_state[ORANGE][1] = tmpW1
        self.cube_state[ORANGE][2] = tmpW2

    def d(self):
        self.face_clockwise(D)

        tmpW6 = self.cube_state[WHITE][6]
        tmpW7 = self.cube_state[WHITE][7]
        tmpW8 = self.cube_state[WHITE][8]

        self.cube_state[WHITE][6] = self.cube_state[RED][6]
        self.cube_state[WHITE][7] = self.cube_state[RED][7]
        self.cube_state[WHITE][8] = self.cube_state[RED][8]

        self.cube_state[RED][6] = self.cube_state[YELLOW][0]
        self.cube_state[RED][7] = self.cube_state[YELLOW][1]
        self.cube_state[RED][8] = self.cube_state[YELLOW][2]

        self.cube_state[YELLOW][0] = self.cube_state[ORANGE][6]
        self.cube_state[YELLOW][1] = self.cube_state[ORANGE][7]
        self.cube_state[YELLOW][2] = self.cube_state[ORANGE][8]

        self.cube_state[ORANGE][6] = tmpW6
        self.cube_state[ORANGE][7] = tmpW7
        self.cube_state[ORANGE][8] = tmpW8

    def d_prime(self):
        self.face_counterclockwise(D)

        tmpW6 = self.cube_state[WHITE][6]
        tmpW7 = self.cube_state[WHITE][7]
        tmpW8 = self.cube_state[WHITE][8]

        self.cube_state[WHITE][6] = self.cube_state[ORANGE][6]
        self.cube_state[WHITE][7] = self.cube_state[ORANGE][7]
        self.cube_state[WHITE][8] = self.cube_state[ORANGE][8]

        self.cube_state[ORANGE][6] = self.cube_state[YELLOW][0]
        self.cube_state[ORANGE][7] = self.cube_state[YELLOW][1]
        self.cube_state[ORANGE][8] = self.cube_state[YELLOW][2]

        self.cube_state[YELLOW][0] = self.cube_state[RED][6]
        self.cube_state[YELLOW][1] = self.cube_state[RED][7]
        self.cube_state[YELLOW][2] = self.cube_state[RED][8]

        self.cube_state[RED][6] = tmpW6
        self.cube_state[RED][7] = tmpW7
        self.cube_state[RED][8] = tmpW8

    def r(self):
        self.face_clockwise(R)

        tmpG2 = self.cube_state[GREEN][2]
        tmpG5 = self.cube_state[GREEN][5]
        tmpG8 = self.cube_state[GREEN][8]

        self.cube_state[GREEN][2] = self.cube_state[YELLOW][2]
        self.cube_state[GREEN][5] = self.cube_state[YELLOW][5]
        self.cube_state[GREEN][8] = self.cube_state[YELLOW][8]

        self.cube_state[YELLOW][2] = self.cube_state[BLUE][8]
        self.cube_state[YELLOW][5] = self.cube_state[BLUE][5]
        self.cube_state[YELLOW][8] = self.cube_state[BLUE][2]

        self.cube_state[BLUE][2] = self.cube_state[WHITE][2]
        self.cube_state[BLUE][5] = self.cube_state[WHITE][5]
        self.cube_state[BLUE][8] = self.cube_state[WHITE][8]

        self.cube_state[WHITE][2] = tmpG2
        self.cube_state[WHITE][5] = tmpG5
        self.cube_state[WHITE][8] = tmpG8

    def r_prime(self):
        self.face_counterclockwise(R)

        tmpG2 = self.cube_state[GREEN][2]
        tmpG5 = self.cube_state[GREEN][5]
        tmpG8 = self.cube_state[GREEN][8]

        self.cube_state[GREEN][2] = self.cube_state[WHITE][2]
        self.cube_state[GREEN][5] = self.cube_state[WHITE][5]
        self.cube_state[GREEN][8] = self.cube_state[WHITE][8]

        self.cube_state[WHITE][2] = self.cube_state[BLUE][2]
        self.cube_state[WHITE][5] = self.cube_state[BLUE][5]
        self.cube_state[WHITE][8] = self.cube_state[BLUE][8]

        self.cube_state[BLUE][8] = self.cube_state[YELLOW][2]
        self.cube_state[BLUE][5] = self.cube_state[YELLOW][5]
        self.cube_state[BLUE][2] = self.cube_state[YELLOW][8]

        self.cube_state[YELLOW][2] = tmpG2
        self.cube_state[YELLOW][5] = tmpG5
        self.cube_state[YELLOW][8] = tmpG8

    def l(self):
        self.face_clockwise(L)

        tmpG0 = self.cube_state[GREEN][0]
        tmpG3 = self.cube_state[GREEN][3]
        tmpG6 = self.cube_state[GREEN][6]

        self.cube_state[GREEN][0] = self.cube_state[WHITE][0]
        self.cube_state[GREEN][3] = self.cube_state[WHITE][3]
        self.cube_state[GREEN][6] = self.cube_state[WHITE][6]

        self.cube_state[WHITE][0] = self.cube_state[BLUE][0]
        self.cube_state[WHITE][3] = self.cube_state[BLUE][3]
        self.cube_state[WHITE][6] = self.cube_state[BLUE][6]

        self.cube_state[BLUE][0] = self.cube_state[YELLOW][0]
        self.cube_state[BLUE][3] = self.cube_state[YELLOW][3]
        self.cube_state[BLUE][6] = self.cube_state[YELLOW][6]

        self.cube_state[YELLOW][0] = tmpG0
        self.cube_state[YELLOW][3] = tmpG3
        self.cube_state[YELLOW][6] = tmpG6

    def l_prime(self):
        self.face_counterclockwise(L)

        tmpG0 = self.cube_state[GREEN][0]
        tmpG3 = self.cube_state[GREEN][3]
        tmpG6 = self.cube_state[GREEN][6]

        self.cube_state[GREEN][0] = self.cube_state[YELLOW][0]
        self.cube_state[GREEN][3] = self.cube_state[YELLOW][3]
        self.cube_state[GREEN][6] = self.cube_state[YELLOW][6]

        self.cube_state[YELLOW][0] = self.cube_state[BLUE][0]
        self.cube_state[YELLOW][3] = self.cube_state[BLUE][3]
        self.cube_state[YELLOW][6] = self.cube_state[BLUE][6]

        self.cube_state[BLUE][0] = self.cube_state[WHITE][0]
        self.cube_state[BLUE][3] = self.cube_state[WHITE][3]
        self.cube_state[BLUE][6] = self.cube_state[WHITE][6]

        self.cube_state[WHITE][0] = tmpG0
        self.cube_state[WHITE][3] = tmpG3
        self.cube_state[WHITE][6] = tmpG6
        
    def f(self):
        self.face_clockwise(F)

        tmpG6 = self.cube_state[GREEN][6]
        tmpG7 = self.cube_state[GREEN][7]
        tmpG8 = self.cube_state[GREEN][8]

        self.cube_state[GREEN][6] = self.cube_state[RED][2]
        self.cube_state[GREEN][7] = self.cube_state[RED][5]
        self.cube_state[GREEN][8] = self.cube_state[RED][8]

        self.cube_state[RED][2] = self.cube_state[BLUE][0]
        self.cube_state[RED][5] = self.cube_state[BLUE][1]
        self.cube_state[RED][8] = self.cube_state[BLUE][2]

        self.cube_state[BLUE][0] = self.cube_state[ORANGE][6]
        self.cube_state[BLUE][1] = self.cube_state[ORANGE][3]
        self.cube_state[BLUE][2] = self.cube_state[ORANGE][0]

        self.cube_state[ORANGE][6] = tmpG6
        self.cube_state[ORANGE][3] = tmpG7
        self.cube_state[ORANGE][0] = tmpG8

    def f_prime(self):
        self.face_counterclockwise(F)

        tmpG6 = self.cube_state[GREEN][6]
        tmpG7 = self.cube_state[GREEN][7]
        tmpG8 = self.cube_state[GREEN][8]

        self.cube_state[GREEN][6] = self.cube_state[ORANGE][6]
        self.cube_state[GREEN][7] = self.cube_state[ORANGE][3]
        self.cube_state[GREEN][8] = self.cube_state[ORANGE][0]

        self.cube_state[ORANGE][6] = self.cube_state[BLUE][0]
        self.cube_state[ORANGE][3] = self.cube_state[BLUE][1]
        self.cube_state[ORANGE][0] = self.cube_state[BLUE][2]

        self.cube_state[BLUE][0] = self.cube_state[RED][2]
        self.cube_state[BLUE][1] = self.cube_state[RED][5]
        self.cube_state[BLUE][2] = self.cube_state[RED][8]

        self.cube_state[RED][2] = tmpG6
        self.cube_state[RED][5] = tmpG7
        self.cube_state[RED][8] = tmpG8

    def b(self):
        self.face_clockwise(B)

        tmpB6 = self.cube_state[BLUE][6]
        tmpB7 = self.cube_state[BLUE][7]
        tmpB8 = self.cube_state[BLUE][8]

        self.cube_state[BLUE][6] = self.cube_state[RED][0]
        self.cube_state[BLUE][7] = self.cube_state[RED][3]
        self.cube_state[BLUE][8] = self.cube_state[RED][6]

        self.cube_state[RED][0] = self.cube_state[GREEN][0]
        self.cube_state[RED][3] = self.cube_state[GREEN][1]
        self.cube_state[RED][6] = self.cube_state[GREEN][2]

        self.cube_state[GREEN][0] = self.cube_state[ORANGE][2]
        self.cube_state[GREEN][1] = self.cube_state[ORANGE][5]
        self.cube_state[GREEN][2] = self.cube_state[ORANGE][8]

        self.cube_state[ORANGE][2] = tmpB6
        self.cube_state[ORANGE][5] = tmpB7
        self.cube_state[ORANGE][8] = tmpB8

    def b_prime(self):
        self.face_counterclockwise(B)

        tmpB6 = self.cube_state[BLUE][6]
        tmpB7 = self.cube_state[BLUE][7]
        tmpB8 = self.cube_state[BLUE][8]

        self.cube_state[BLUE][6] = self.cube_state[ORANGE][2]
        self.cube_state[BLUE][7] = self.cube_state[ORANGE][5]
        self.cube_state[BLUE][8] = self.cube_state[ORANGE][8]

        self.cube_state[ORANGE][2] = self.cube_state[GREEN][0]
        self.cube_state[ORANGE][5] = self.cube_state[GREEN][1]
        self.cube_state[ORANGE][8] = self.cube_state[GREEN][2]

        self.cube_state[GREEN][0] = self.cube_state[RED][0]
        self.cube_state[GREEN][1] = self.cube_state[RED][3]
        self.cube_state[GREEN][2] = self.cube_state[RED][6]

        self.cube_state[RED][0] = tmpB6
        self.cube_state[RED][3] = tmpB7
        self.cube_state[RED][6] = tmpB8

    def m(self):
        self.l()
        self.r_prime()

    def m_prime(self):
        self.l_prime()
        self.r()

    def e(self):
        self.u_prime()
        self.d()

    def e_prime(self):
        self.u()
        self.d_prime()

    def s(self):
        self.f()
        self.b_prime()

    def s_prime(self):
        self.f_prime()
        self.b()

    def solve(self):
        self.cube_state = deepcopy(SOLVED_CUBE_LIST)
        self.solved = True

    def scramble(self):
        scramble = []

        for i in range(40):
            scramble.append(random.choice(POSSIBLE_MOVES))

        algo = ' '.join(scramble)
        self.algorithm(algo)

    def algorithm(self, algorithm: str):
        algo_list = algorithm.split()

        for rotation in algo_list:
            match rotation:
                case "U":
                    self.u()
                case "U'":
                    self.u_prime()
                case "U2":
                    self.u()
                    self.u()
                case "D":
                    self.d()
                case "D'":
                    self.d_prime()
                case "D2":
                    self.d()
                    self.d()
                case "L":
                    self.l()
                case "L'":
                    self.l_prime()
                case "L2":
                    self.l()
                    self.l()
                case "F":
                    self.f()
                case "F'":
                    self.f_prime()
                case "F2":
                    self.f()
                    self.f()
                case "R":
                    self.r()
                case "R'":
                    self.r_prime()
                case "R2":
                    self.r()
                    self.r()
                case "B":
                    self.b()
                case "B'":
                    self.b_prime()
                case "B2":
                    self.b()
                    self.b()
                case "M":
                    self.m()
                case "M'":
                    self.m_prime()
                case "M2":
                    self.m()
                    self.m()
                case "E":
                    self.e()
                case "E'":
                    self.e_prime()
                case "E2":
                    self.e()
                    self.e()
                case "S":
                    self.s()
                case "S'":
                    self.s_prime()
                case "S2":
                    self.s()
                    self.s()
                case _:
                    raise ValueError(f"Unknown rotation: {rotation}")
                
            self.solved = self.solved == SOLVED_CUBE_LIST