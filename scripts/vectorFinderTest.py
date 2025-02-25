# from utils import imageCapture, coordFormatFromPredictions

import numpy as np
from point import Point
import random

# from ultralytics import YOLO


MARKER_NAME = "Blue"

class tablePieces:
    def __init__(self):
        self.results = []
        # top left marker
        self.pointX = Point(754, 53)
        # bottom left marker
        self.pointOrigin = Point(780, 321)
        # bottom right marker
        self.pointY = Point(363, 288)


    # outputs a list of all points of a certain type
    # formats predictions, searches through list, and outputs new sorted list
    # params: name_of_detection
    # returns: [[x, y, name], ...]
    def findTypePiece(self, color):
        outputList = []
        FormatedList = coordFormatFromPredictions(self.results)
        for point in FormatedList:
            if point[2] == color:
                outputList.append(point)
        return outputList

    # sets properties pointX, pointOrigin, and pointY
    # captures an image, uses computer vision, and sorts out markers to then set properties
    def extractReferencePoints(self):
        imageCapture()
        model = YOLO('best.pt')
        self.results = model('piece_return_photo.jpg')
        referencePoints = self.findTypePiece(MARKER_NAME)

        # have not implemented how to determine which point is which
        self.pointX = referencePoints[0]
        self.pointOrigin = referencePoints[1]
        self.pointY = referencePoints[2]


    # params: name_of_detection
    # returns: [x, y, name]
    def pickPiece(self, color):
        pieceList = self.findTypePiece(color)
        # selects a random point from the list
        selectedPiece = pieceList[random.randint(0, (len(pieceList) - 1))]
        return selectedPiece


    # returns: 
    def solveForConstants(self):

        # piece = Point(self.pickPiece(MARKER_NAME)[0], self.pickPiece(MARKER_NAME)[1])
        piece =  Point(631, 188)

        v = Point((self.pointY.x - self.pointOrigin.x), (self.pointY.y - self.pointOrigin.y))
        u = Point((self.pointX.x - self.pointOrigin.x), (self.pointX.y - self.pointOrigin.y))

        # solveing for constants

        a = np.array([[u.x, v.x], [u.y, v.y]])

        b = np.array([piece.x - self.pointOrigin.x, piece.y - self.pointOrigin.y])

        x = np.linalg.solve(a, b)

        return x

    def convertToRobotPose(self, c1, c2):

        #copied from ipynb
        # Q positions:
        robotOrigin = np.array([.442266846286, -.301612002692, .047130197896, -.507610936746, -3.100185449067, -.000036162732])
        robotX = np.array([.429488966095, -.092791700394, .045215730203, -.381439096286, -3.118239823101, -.000144275467])
        robotY = np.array(.104995015661, -.264398600885, .046163729680, 1.067003049097, 2.943820912978, -.015920545841)
        robotVectorX = robotX - robotOrigin
        robotVectorY = robotY - robotOrigin

        output = (robotOrigin + (robotVectorX * c1) + (robotVectorY * c2))
        #Use the same angles as the origin because they are getting messed up with the linalg
        output = np.hstack((output[0:3], robotOrigin[3:]))

        return output
    
    def getPickUpPieceCommand(self):
        c1 = self.solveForConstants()[0]
        c2 = self.solveForConstants()[1]

        print_pos = [f'{i:.16f}' for i in self.convertToRobotPose(c1, c2)]
        return f'movej(p{print_pos}, a=1, v=0.1)'.replace("'", "")


if __name__ == "__main__":
    TestClassInstance = tablePieces()

    c1 = TestClassInstance.solveForConstants()[0]
    c2 = TestClassInstance.solveForConstants()[1]

    print_pos = [f'{i:.16f}' for i in TestClassInstance.convertToRobotPose(c1, c2)]

    print(f'movej({print_pos}, a=1, v=0.1)'.replace("'", ""))
