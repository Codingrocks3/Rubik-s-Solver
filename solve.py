"""Implements the algorithm to solve a cube as well as a terminal-based
cube solving application

Authors:
Kyran McCown
Kai Hogan
Blake Ogilvie
Mason Holly
Henry Fleming"""

EmptyFace = [["R", "O", "Y"],["G", "B", "W"],["R", "R", "R"]]
faceG = EmptyFace
faceR = EmptyFace
faceW = EmptyFace
faceO = EmptyFace
faceB = EmptyFace
faceY = EmptyFace
cubeState = [faceG, faceR, faceW, faceO, faceB, faceY]

red = "\x1b[31m"
orange = "\x1b[38;5;208m"
yellow = "\x1b[33m"
green = "\x1b[32m"
blue = "\x1b[34m"
white = "\x1b[37m"
blank = "\x1b[0m"

class Solve:
    def printOneFace(self, face):
        print(f"                [{face[0][0]}] [{face[0][1]}] [{face[0][2]}]")
        print(f"                [{face[1][0]}] [{face[1][1]}] [{face[1][2]}]")
        print(f"                [{face[2][0]}] [{face[2][1]}] [{face[2][2]}] \n")
    
    def printThreeFaces(self, face1:list[list[str]],face2:list[list[str]],face3:list[list[str]]):
        print(f"[{face1[0][0]}] [{face1[0][1]}] [{face1[0][2]}]     [{face2[0][0]}] [{face2[0][1]}] [{face2[0][2]}]    [{face3[0][0]}] [{face3[0][1]}] [{face3[0][2]}]")
        print(f"[{face1[1][0]}] [{face1[1][1]}] [{face1[1][2]}]     [{face2[1][0]}] [{face2[1][1]}] [{face2[1][2]}]    [{face3[1][0]}] [{face3[1][1]}] [{face3[1][2]}]")
        print(f"[{face1[2][0]}] [{face1[2][1]}] [{face1[2][2]}]     [{face2[2][0]}] [{face2[2][1]}] [{face2[2][2]}]    [{face3[2][0]}] [{face3[2][1]}] [{face3[2][2]}] \n")

    def separateCube(self, cubeState):
        faces = []
        for face in cubeState:
            faceArray = []
            for row in face:
                rowArray = []
                for square in row:
                    squareString = ""
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
                    rowArray.append(squareString)
                faceArray.append(rowArray)
            faces.append(faceArray)
        return faces

    def printCube(self, cubeState):
        faces = self.separateCube(cubeState)
        self.printOneFace(faces[0])
        self.printThreeFaces(faces[1], faces[2], faces[3])
        self.printOneFace(faces[4])
        self.printOneFace(faces[5])
        

s1 = Solve()
s1.printCube(cubeState)
#print(red + "r")