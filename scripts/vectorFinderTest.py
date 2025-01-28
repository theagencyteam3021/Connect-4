from utils import imageCapture, coordFormatFromPredictions

import numpy as np
from point import Point
import random

from ultralytics import YOLO

MARKER_NAME = "Blue"

class tablePieces:
    def __init__(self):
        self.results = []
        # top left marker
        self.point1 = None
        # bottom left marker
        self.point2 = None
        # bottom right marker
        self.point3 = None

    @classmethod
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

    @classmethod
    # sets properties point1, point2, and point3
    # captures an image, uses computer vision, and sorts out markers to then set properties
    def extractReferencePoints(self):
        imageCapture()
        model = YOLO('best.pt')
        self.results = model('piece_return_photo.jpg')
        referencePoints = self.findTypePiece(MARKER_NAME)

        # have not implemented how to determine which point is which
        self.point1 = referencePoints[0]
        self.point2 = referencePoints[1]
        self.point3 = referencePoints[2]

    @classmethod
    # params: name_of_detection
    # returns: [x, y, name]
    def pickPiece(self, color):
        pieceList = self.findTypePiece(color)
        # selects a random point from the list
        selectedPiece = pieceList[random.randint(0, (len(pieceList) - 1))]
        return selectedPiece

    @classmethod
    # returns: 
    def solveForConstants(self):

        piece = Point(self.pickPiece[0], self.pickPiece[1])

        v = Point((self.point2.x - self.point3.x), (self.point2.y - self.point2.y))
        u = Point((self.point1.x - self.point3.x), (self.point1.y - self.point2.y))

        # solveing for constants

        a = np.array([[(self.point2.x - self.point3.x), (self.point1.x - self.point3.x)], [(self.point2.y- self.point3.y), (self.point1.x - self.point3.x)]])

        b = np.array([piece.x - self.point3.x, piece.y - self.point3.y])

        x = np.linalg.solve(a, b)

        return x

    c1 = solveForConstants()[0]
    c2 = solveForConstants()[1]

