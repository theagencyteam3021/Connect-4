# shows the board with the coords provided by object detection
from scripts.board import Board
from scripts.line import Line
from scripts.point import Point
import pygame


class BoardDisplay:
    def __init__(self):
        pygame.init()
        # pygame setup
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.running = True

        # fakeArray = [[5, 5, ""], [5, 10, " "], [5, 15, " "], [5, 20, " "], [5, 25, " "], [5, 30, " "],[10, 5, " "], [10, 10, " "], [10, 15, " "], [10, 20, " "], [10, 25, " "], [10, 30, " "], [15, 5, " "], [15, 10, " "], [15, 15, " "], [15, 20, " "], [15, 25, " "], [15, 30, " "], [20, 5, " "], [20, 10, " "], [20, 15, " "], [20, 20, " "], [20, 25, " "], [20, 30, " "], [25, 5, " "], [25, 10, " "], [25, 15, " "], [25, 20, " "], [25, 25, " "], [25, 30, " "], [30, 5, " "], [30, 10, " "], [30, 15, " "], [30, 20, " "], [30, 25, " "], [30, 30, " "], [35, 5, " "], [35, 10, " "], [35, 15, " "], [35, 20, " "], [35, 25, " "], [35, 30, " "]]
        # self.board = Board(fakeArray)
        # self.array = self.board.findMatrix()
        # self.corners = self.board.cornerFinder()

        # this is just output copy pasted from main
        self.array = [[687.0, 849.0, 'Red'], [870.5, 850.0, 'Red'], [1052.5, 844.5, 'Red'], [1229.0, 836.0, 'Yellow'], [1393.0, 822.5, 'Red'], [1535.0, 806.5, 'Yellow'], [1661.5, 787.5, 'Yellow'], [684.5, 684.5, 'Red'], [867.0, 684.0, 'Red'], [1047.5, 681.5, 'Yellow'], [1223.5, 675.5, 'Red'], [1385.0, 668.5, 'Yellow'], [1528.5, 659.0, 'Yellow'], [1655.5, 648.5, 'Red'], [686.0, 521.0, 'Red'], [863.5, 521.0, 'Yellow'], [1041.0, 519.5, 'Red'], [1214.5, 517.5, 'Red'], [1375.0, 514.5, 'Yellow'], [1517.5, 511.5, 'Red'], [1642.5, 510.0, 'Yellow'], [691.5, 365.5, 'Yellow'], [862.0, 363.5, 'Red'], [1037.0, 365.0, 'Empty'], [1205.5, 365.5, 'Empty'], [1359.5, 368.5, 'Red'], [1500.0, 372.0, 'Empty'], [1625.0, 376.0, 'Empty'], [695.5, 219.5, 'Empty'], [861.5, 216.0, 'Empty'], [1030.5, 219.5, 'Empty'], [1192.0, 223.5, 'Empty'], [1343.5, 229.0, 'Empty'], [1482.0, 238.5, 'Empty'], [1602.0, 249.0, 'Empty'], [703.5, 87.0, 'Empty'], [863.0, 84.0, 'Empty'], [1024.0, 86.5, 'Empty'], [1178.5, 93.0, 'Empty'], [1325.0, 102.0, 'Empty'], [1459.0, 116.0, 'Empty'], [1578.0, 130.0, 'Empty']]
        self.board = Board(self.array)
        self.corners = self.board.cornerFinder()
        self.matrixedBoard = self.board.findMatrix()

        self.radius = 5

        

    def findEdgeLines(self):
        if self.corners[0][0] == self.corners[2][0]:
            leftLine = Line.verticalline(self.corners[0][0])
        if self.corners[1][0] == self.corners[3][0]:
            rightLine = Line.verticalline(self.corners[1][0])
        if self.corners[0][0] != self.corners[2][0]:
            leftLine = Line.frompoints(Point(self.corners[0][0], self.corners[0][1]), Point(self.corners[2][0], self.corners[2][1]))
        if self.corners[1][0] != self.corners[3][0]:
            rightLine = Line.frompoints(Point(self.corners[1][0], self.corners[1][1]), Point(self.corners[3][0], self.corners[3][1]))

        return [leftLine, rightLine]
        

    def drawPointdistfromline(self, line, coordList):
        for coord in coordList:
            point = Point(coord[0], coord[1])

            if line.slope == "infinity":
                pygame.draw.line(self.screen, (255,0,255), (line.x, point.y), (point.x, point.y), 5)
            elif line.slope == 0:
                pygame.draw.line(self.screen, (255,0,255), (point.x, line.y), (point.x, point.y), 5)
            else:
                perpline = line.perplineatpoint(point)
                intersection = line.intersection(perpline)
                pygame.draw.line(self.screen, (255,0,255), (point.x, point.y), (intersection.x, intersection.y), 5)
    
    def run(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")
        
            # RENDER YOUR GAME HERE

            # for row in self.array:
                # for peice in row:
            for peice in self.array:
                if peice[2] == 'Red':
                    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(peice[0], peice[1], 25, 25))
                    pygame.draw.circle(self.screen, (255, 0, 0), (peice[0], peice[1]), 25)
                elif peice[2] == 'Yellow':
                    # pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(peice[0], peice[1], 25, 25))
                    pygame.draw.circle(self.screen, (255, 255, 0), (peice[0], peice[1]), 25)
                else:
                    # pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(peice[0], peice[1], 25, 25))
                    pygame.draw.circle(self.screen, (100, 100, 100), (peice[0], peice[1]), 25)

            # draw corner lines
            pygame.draw.line(self.screen, (0,0,255), (0,0), (self.corners[0][0], self.corners[0][1]), 2)
            pygame.draw.line(self.screen, (0,0,255), (self.screen.get_width(),0), (self.corners[1][0], self.corners[1][1]), 2)
            pygame.draw.line(self.screen, (0,0,255), (0, self.screen.get_height()), (self.corners[2][0], self.corners[2][1]), 2)
            pygame.draw.line(self.screen, (0,0,255), (self.screen.get_width(),self.screen.get_height()), (self.corners[3][0], self.corners[3][1]), 2)
           
            # draw edge lines
            pygame.draw.line(self.screen, (0,255,255), (self.corners[0][0], self.corners[0][1]), (self.corners[2][0], self.corners[2][1]), 2)
            pygame.draw.line(self.screen, (0,255,255), (self.corners[1][0], self.corners[1][1]), (self.corners[3][0], self.corners[3][1]), 2)

            # draw closest to edge lines
            edgeLines = self.findEdgeLines()
            leftCoordList = self.board.sortByY(self.board.findClosest(edgeLines[0], 6))
            rightCoordList = self.board.sortByY(self.board.findClosest(edgeLines[1], 6))

            self.drawPointdistfromline(edgeLines[0], leftCoordList)
            self.drawPointdistfromline(edgeLines[1], rightCoordList)

            # draw horizontal lines
            for i in range(6):
                pygame.draw.line(self.screen, (255,255,255), (self.matrixedBoard[i][0][0], self.matrixedBoard[i][0][1]), (self.matrixedBoard[i][6][0], self.matrixedBoard[i][6][1]), 2)
                
                horizontalCoordList = self.board.sortByX(self.board.findClosest(Line.frompoints(Point(self.matrixedBoard[i][0][0], self.matrixedBoard[i][0][1]), Point(self.matrixedBoard[i][6][0], self.matrixedBoard[i][6][1])), 7))
                self.drawPointdistfromline(Line.frompoints(Point(self.matrixedBoard[i][0][0], self.matrixedBoard[i][0][1]), Point(self.matrixedBoard[i][6][0], self.matrixedBoard[i][6][1])), horizontalCoordList)

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()