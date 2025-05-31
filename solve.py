import os
import random
from cube import Cube
from cube import SOLVED_CUBE_LIST as SOLVED_CUBE_LIST

EmptyFace = ["E"] * 9
faceG = ["E"] * 4 + ["G"] + ["E"] * 4
faceR = ["E"] * 4 + ["R"] + ["E"] * 4
faceW = ["E"] * 4 + ["W"] + ["E"] * 4
faceO = ["E"] * 4 + ["O"] + ["E"] * 4
faceB = ["E"] * 4 + ["B"] + ["E"] * 4
faceY = ["E"] * 4 + ["Y"] + ["E"] * 4

emptyCubeState = [faceG, faceR, faceW, faceO, faceB, faceY]

red = "\x1b[31m"
orange = "\x1b[38;5;208m"
yellow = "\x1b[33m"
green = "\x1b[32m"
blue = "\x1b[34m"
white = "\x1b[37m"
blank = "\x1b[0m"

class Solve:
    cube = Cube(emptyCubeState)
    def printFirstFace(self, face):
        print(f"                [{face[0]}] [{face[1]}] [{face[2]}]")
        print(f"                [{face[3]}] [{face[4]}] [{face[5]}]")
        print(f"                [{face[6]}] [{face[7]}] [{face[8]}] \n")

    def printFacesAndKey(self, face4, face5):
        red_string = red + "Input R for Red" + blank
        orange_string = orange + "Input O for Orange" + blank
        yellow_string = yellow + "Input Y for Yellow" + blank
        green_string = green + "Input G for Green" + blank
        blue_string = blue + "Input B for Blue" + blank
        white_string = white + "Input W for White" + blank

        print(f"                [{face4[0]}] [{face4[1]}] [{face4[2]}]     {red_string}")
        print(f"                [{face4[3]}] [{face4[4]}] [{face4[5]}]     {orange_string}")
        print(f"                [{face4[6]}] [{face4[7]}] [{face4[8]}]     {yellow_string}")
        print(f"                                {green_string}")
        print(f"                [{face5[0]}] [{face5[1]}] [{face5[2]}]     {blue_string}")
        print(f"                [{face5[3]}] [{face5[4]}] [{face5[5]}]     {white_string}")
        print(f"                [{face5[6]}] [{face5[7]}] [{face5[8]}]     Press A for autofill")
    
    def printThreeFaces(self, face1, face2, face3):
        print(f"[{face1[0]}] [{face1[1]}] [{face1[2]}]     [{face2[0]}] [{face2[1]}] [{face2[2]}]    [{face3[0]}] [{face3[1]}] [{face3[2]}]")
        print(f"[{face1[3]}] [{face1[4]}] [{face1[5]}]     [{face2[3]}] [{face2[4]}] [{face2[5]}]    [{face3[3]}] [{face3[4]}] [{face3[5]}]")
        print(f"[{face1[6]}] [{face1[7]}] [{face1[8]}]     [{face2[6]}] [{face2[7]}] [{face2[8]}]    [{face3[6]}] [{face3[7]}] [{face3[8]}] \n")

    def separateCube(self, cubeState):
        faces = []
        for face in cubeState:
            faceArray = []
            for i in range(9):
                square = face[i]
                match square:
                    case "R":
                        squareString = red + square + blank
                    case "O":
                        squareString = orange + square + blank
                    case "Y":
                        squareString = yellow + square + blank
                    case "G":
                        squareString = green + square + blank
                    case "B":
                        squareString = blue + square + blank
                    case "W":
                        squareString = white + square + blank
                    case _:
                        squareString = square
                faceArray.append(squareString)
            faces.append(faceArray)
        return faces

    def printCube(self, cubeState):
        os.system('cls' if os.name == 'nt' else 'clear')
        faces = self.separateCube(cubeState)
        self.printFirstFace(faces[0])
        self.printThreeFaces(faces[1], faces[2], faces[3])
        self.printFacesAndKey(faces[4], faces[5])
    

    # Cube Editing Functions
    def getCubeEditorInput(self, colors_dict, cubeState, faceIndex, squareIndex):
        inputColor = input(f"Enter the color for face {faceIndex} square {squareIndex}: ")
        if inputColor not in colors_dict and inputColor != "A" and inputColor != "S":
            print("Invalid color. Please enter one of the following: R, O, Y, G, B, W")
            return self.getCubeEditorInput(colors_dict, cubeState, faceIndex, squareIndex)

        if inputColor == "A":
            # all faces with their center except the centers
            for idx in range(6):
                center_color = cubeState[idx][4]
                for i in range(9):
                    if i != 4:
                        cubeState[idx][i] = center_color
                colors_dict[center_color] = 8
            return cubeState


        if colors_dict[inputColor] >= 8:
            print("This color has already been used 9 times. Please choose another color.")
            return self.getCubeEditorInput(colors_dict, cubeState, faceIndex, squareIndex)
        
        cubeState[faceIndex][squareIndex] = inputColor
        colors_dict[inputColor] += 1

        return cubeState

    def fillOutCube(self, cubeState):
        colors_dict = {
            "R": 0,
            "O": 0,
            "Y": 0,
            "G": 0,
            "B": 0,
            "W": 0,
        }
        for faceIndex in range(6):
            for squareIndex in range(9):
                if squareIndex == 4:
                    continue
                if all(count == 8 for count in colors_dict.values()):
                    self.printCube(cubeState)
                    return cubeState
                cubeState[faceIndex][squareIndex] = "\x1b[47m \x1b[0m"
                self.printCube(cubeState)
                cubeState = self.getCubeEditorInput(colors_dict, cubeState, faceIndex, squareIndex)
            self.printCube(cubeState)
        return cubeState
        
    # Cube Solving Functions
    def getAlgorithmInput(self, cubeState):
        algorithm = input("Enter the algorithm to solve the cube (e.g., R U R' U'): ")
        self.cube.algorithm(algorithm)
        return self.cube.cube_state
    
    def solveCube(self, cubeState):
        while cubeState != SOLVED_CUBE_LIST:
            self.getAlgorithmInput(cubeState)
            self.printCube(self.cube.cube_state)
            if cubeState == SOLVED_CUBE_LIST:
                print("Cube is solved!")
                return cubeState
            else:
                self.getAlgorithmInput(cubeState)
                self.printCube(self.cube.cube_state)

s1 = Solve()
s1.cube.cube_state = s1.fillOutCube(s1.cube.cube_state)
s1.cube.cube_state = s1.solveCube(s1.cube.cube_state)
