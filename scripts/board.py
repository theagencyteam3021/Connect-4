from scripts.line import Line
from scripts.point import Point

imageXWidth = 1920
imageYHeight = 1080

class Board:
    def __init__(self, pointList):
        self.pointList = pointList

    # returns: [topLeft, topRight, bottomLeft, bottomRight]
    def cornerFinder(self):

        #these are set to the farthest pixel from their name
        topLeft = [imageXWidth, imageYHeight, ""]
        topRight = [0, imageYHeight, ""]
        bottomLeft = [imageXWidth, 0, ""]
        bottomRight = [0, 0, ""]

        for point in self.pointList:
            if ((point[0] ** 2 + point[1] ** 2) ** 0.5) < ((topLeft[0] ** 2 + topLeft[1] ** 2) ** 0.5):
                topLeft = point

            if (((imageXWidth - point[0]) ** 2 + point[1] ** 2) ** 0.5) < (((imageXWidth - topRight[0]) ** 2 + topRight[1] ** 2) ** 0.5):
                topRight = point

            if ((point[0] ** 2 + (point[1] - imageYHeight) ** 2) ** 0.5) < ((bottomLeft[0] ** 2 + (imageYHeight - bottomLeft[1]) ** 2) ** 0.5):
                bottomLeft = point

            if (((point[0] - imageXWidth) ** 2 + (point[1] - imageYHeight) ** 2) ** 0.5) < (((bottomRight[0] - imageXWidth) ** 2 + (imageYHeight - bottomRight[1]) ** 2) ** 0.5):
                bottomRight = point

        return [topLeft, topRight, bottomLeft, bottomRight]

    def edgeFinder(self, side: str):

        cornerArray = self.cornerFinder()

        if cornerArray[0][0] == cornerArray[2][0]:
            leftLine = Line.verticalline(cornerArray[0][0])
        if cornerArray[1][0] == cornerArray[3][0]:
            rightLine = Line.verticalline(cornerArray[1][0])
        if cornerArray[0][0] != cornerArray[2][0]:
            leftLine = Line.frompoints(Point(cornerArray[0][0], cornerArray[0][1]), Point(cornerArray[2][0], cornerArray[2][1]))
        if cornerArray[1][0] != cornerArray[3][0]:
            rightLine = Line.frompoints(Point(cornerArray[1][0], cornerArray[1][1]), Point(cornerArray[3][0], cornerArray[3][1]))
        
        if side == 'left':
            return self.sortByY(self.findClosest(leftLine, 6))
        elif side == 'right':
            return self.sortByY(self.findClosest(rightLine, 6))


    def findClosest(self, line, outputNumber):
        smallnums = []
        for i in range(outputNumber):
            smallest = [9999999, 9999999, ""]
            for list in self.pointList:
                point = Point(list[0], list[1])
                dist = line.pointdistfromline(point)
                smallestDist = line.pointdistfromline(Point(smallest[0], smallest[1]))
                if dist < smallestDist and not (list in smallnums):
                    smallest = list
            smallnums.append(smallest)
        return smallnums
    
    def findMatrix(self):
        finishedMatrix = []
        for i in range(6):
            leftEnd = self.edgeFinder('left')[i]
            rightEnd = self.edgeFinder('right')[i]
            line = Line.frompoints(Point(leftEnd[0],leftEnd[1]), Point(rightEnd[0], rightEnd[1]))
            row = self.sortByX(self.findClosest(line, 7))
            row.reverse()
            finishedMatrix.append(row)
        return finishedMatrix
    
    # sorts in desending pixel order(asending height on screen)
    def sortByY(self, points):
        yValues = []
        for point in points:
            yValues.append(point[1])
        yValues.sort()
        sortedList = [None] * len(yValues)
        for val in yValues:
            for point in points:
                if point[1] == val:
                    sortedList[yValues.index(val)] = point
        sortedList.reverse()
        return sortedList
    
    # sorts in desending pixel order(asending height on screen)
    def sortByX(self, points):
        xValues = []
        for point in points:
            xValues.append(point[0])
        xValues.sort()
        sortedList = [None] * len(xValues)
        for val in xValues:
            for point in points:
                if point[0] == val:
                    sortedList[xValues.index(val)] = point
        return sortedList



