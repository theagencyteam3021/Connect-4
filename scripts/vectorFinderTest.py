# from utils import imageCapture, coordFormatFromPredictions

import numpy as np
from scripts.point import Point
from scripts.utils import coordFormatFromPredictions, imageCapture
import random

# from ultralytics import YOLO

# obsolete code from a possible detection based marker system
MARKER_NAME = "Blue"

class tablePieces:
    def __init__(self, piece=Point(529, 66)):
        self.results = []
        # top left marker
        self.pointX = Point(754, 65)
        # bottom left marker
        self.pointOrigin = Point(780, 321)
        # bottom right marker
        self.pointY = Point(362, 284)

        self.piece = piece


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

    # obsolete code from a possible detection based marker system
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
        piece =  Point(814, 776)

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
        robotOrigin = np.array([-3.885793749486105, -0.678901807670929, 0.5224292914019983, 4.866715195565977, -1.5703538099872034, 1.151811957359314])
        robotX = np.array([-3.507979694996969, -1.0948572617820282, 1.2464740912066858, 4.558636828059814, -1.5702813307391565, 1.4487932920455933])
        robotY = np.array([-4.708534542714254, -1.9790808163084925, 2.1679933706866663, 4.508105917567871, -1.5636118094073694, 0.6998665928840637])

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
        return f'movej(p{print_pos}, a=1.3962634015954636, v=1.0471975511965976)'.replace("'", "")


if __name__ == "__main__":
    TestClassInstance = tablePieces()

c1 = TestClassInstance.solveForConstants()[0]
c2 = TestClassInstance.solveForConstants()[1]

print_pos = [f'{i:.16f}' for i in TestClassInstance.convertToRobotPose(c1, c2)]

print(f'movej({print_pos}, a=1, v=0.1)'.replace("'", ""))
