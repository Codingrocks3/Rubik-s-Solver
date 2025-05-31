"""Implements a parent class for a Rubik's Cube with subclasses for faces and cubits
with functions to rotate (single rotation or full algorithm), display, and build a cube

Authors:
Kyran McCown
Kai Hogan
Blake Ogilvie
Mason Holly
Henry Fleming"""

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

class Cube:
    def __init__(self, cube_state=SOLVED_CUBE_LIST):
        self.cube_state = cube_state
        self.solved = self.cube_state == SOLVED_CUBE_LIST


    def clockwise(self, face: int):
        # For simplicity's sake, var names are treated as if every turn is U
        
        match face:
            case 0: # GREEN
                tmpF = WHITE
                tmpR = ORANGE
                tmpB = YELLOW
                tmpL = RED
            case 1: # RED
                tmpF = WHITE
                tmpR = GREEN
                tmpB = YELLOW
                tmpL = BLUE
            case 2: # WHITE
                tmpF = GREEN
                tmpR = RED
                tmpB = BLUE
                tmpL = ORANGE
            case 3: # ORANGE
                tmpF = GREEN
                tmpR = WHITE
                tmpB = BLUE
                tmpL = YELLOW
            case 4: # BLUE
                tmpF = WHITE
                tmpR = RED
                tmpB = YELLOW
                tmpL = ORANGE
            case 5: # YELLOW
                tmpF = GREEN
                tmpR = ORANGE
                tmpB = BLUE
                tmpL = RED
            case default:
                tmpF = -1
                tmpR = -1
                tmpB = -1
                tmpL = -1

        if tmpF == -1:
            print("Error! Please provide a valid face")
            exit()


        tmpF0 = self.cube_state[tmpF][0]
        tmpF1 = self.cube_state[tmpF][1]
        tmpF2 = self.cube_state[tmpF][2]

        self.cube_state[tmpF][0] = self.cube_state[tmpR][0]
        self.cube_state[tmpF][1] = self.cube_state[tmpR][1]
        self.cube_state[tmpF][2] = self.cube_state[tmpR][2]

        self.cube_state[tmpR][0] = self.cube_state[tmpB][0]
        self.cube_state[tmpR][1] = self.cube_state[tmpB][1]
        self.cube_state[tmpR][2] = self.cube_state[tmpB][2]
        
        self.cube_state[tmpB][0] = self.cube_state[tmpL][0]
        self.cube_state[tmpB][1] = self.cube_state[tmpL][1]
        self.cube_state[tmpB][2] = self.cube_state[tmpL][2]

        self.cube_state[tmpL][0] = tmpF0
        self.cube_state[tmpL][1] = tmpF1
        self.cube_state[tmpL][2] = tmpF2
        
        self.cube_state[face] = [
            self.cube_state[face][6], self.cube_state[face][3], self.cube_state[face][0],
            self.cube_state[face][7], self.cube_state[face][4], self.cube_state[face][1],
            self.cube_state[face][8], self.cube_state[face][5], self.cube_state[face][2]
        ]

    def counterclockwise(self, face: int):
        # For simplicity's sake, var names are treated as if every turn is U
        
        match face:
            case 0: # GREEN
                tmpF = WHITE
                tmpR = ORANGE
                tmpB = YELLOW
                tmpL = RED
            case 1: # RED
                tmpF = WHITE
                tmpR = GREEN
                tmpB = YELLOW
                tmpL = BLUE
            case 2: # WHITE
                tmpF = GREEN
                tmpR = RED
                tmpB = BLUE
                tmpL = ORANGE
            case 3: # ORANGE
                tmpF = GREEN
                tmpR = WHITE
                tmpB = BLUE
                tmpL = YELLOW
            case 4: # BLUE
                tmpF = WHITE
                tmpR = RED
                tmpB = YELLOW
                tmpL = ORANGE
            case 5: # YELLOW
                tmpF = GREEN
                tmpR = ORANGE
                tmpB = BLUE
                tmpL = RED
            case default:
                tmpF = -1
                tmpR = -1
                tmpB = -1
                tmpL = -1

        if tmpF == -1:
            print("Error! Please provide a valid face")
            exit()


        tmpF0 = self.cube_state[tmpF][0]
        tmpF1 = self.cube_state[tmpF][1]
        tmpF2 = self.cube_state[tmpF][2]

        self.cube_state[tmpF][0] = self.cube_state[tmpL][0]
        self.cube_state[tmpF][1] = self.cube_state[tmpL][1]
        self.cube_state[tmpF][2] = self.cube_state[tmpL][2]

        self.cube_state[tmpL][0] = self.cube_state[tmpB][0]
        self.cube_state[tmpL][1] = self.cube_state[tmpB][1]
        self.cube_state[tmpL][2] = self.cube_state[tmpB][2]
        
        self.cube_state[tmpB][0] = self.cube_state[tmpR][0]
        self.cube_state[tmpB][1] = self.cube_state[tmpR][1]
        self.cube_state[tmpB][2] = self.cube_state[tmpR][2]

        self.cube_state[tmpR][0] = tmpF0
        self.cube_state[tmpR][1] = tmpF1
        self.cube_state[tmpR][2] = tmpF2
        
        self.cube_state[face] = [
            self.cube_state[face][2], self.cube_state[face][5], self.cube_state[face][8],
            self.cube_state[face][1], self.cube_state[face][4], self.cube_state[face][7],
            self.cube_state[face][0], self.cube_state[face][3], self.cube_state[face][6]
        ]