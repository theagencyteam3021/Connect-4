from scripts.board import Board

from scripts.point import Point

from scripts.utils import *

from scripts.gridBoardTest import GridBoardDisplay

from scripts.TerminalDisplay import TerminalBoard

from alg.connect_4_alg_stolen import pick_best_move

from scripts.URController import URController

from scripts.vectorFinderTest import tablePieces

from ultralytics import YOLO

import time

import numpy as np

import pygame

import threading

import cv2 as cv

# from PIL import Image

def worker(stop, screen, colorOnlyMatrix):
        disp = GridBoardDisplay(screen, colorOnlyMatrix)
        disp.run(stop)


        
if __name__ == "__main__":

    SCREEN_WIDTH = 750
    SCREEN_HEIGHT = 650

    # should be set to the lables used by the algorithm in results
    REDCOLORNAME = "Red"
    YELLOWCOLORNAME = "yellow"

    controller = URController()

    should_loop = ""

    # set anchor coords

    originXInput = input("input x coordinate pixel value for origin marker: ")
    originYInput = input("input y coordinate pixel value for origin marker: ")

    xXInput = input("input x coordinate pixel value for x marker: ")
    xYInput = input("input y coordinate pixel value for x marker: ")

    yXInput = input("input x coordinate pixel value for y marker: ")
    yYInput = input("input y coordinate pixel value for y marker: ")
    controller.goto_reset()

    while  should_loop != "quit" and should_loop != "q":

        # get image
        # use alg on image to find coords
        imageCapture()
        collectionModel = YOLO('piece_model.pt')

        collectionResults = collectionModel("piece_return_photo.jpg")

        # call vector finder
        collectionPlate = tablePieces(collectionResults, Point(originXInput, originYInput), Point(xXInput, xYInput), Point(yXInput, yYInput))

        # picking piece
        pieceCoords = collectionPlate.pickPiece(REDCOLORNAME)

        # setting attribute piece
        collectionPlate.pieceSetter((pieceCoords[0], pieceCoords[1]))

        pickUpPiecePose = collectionPlate.getPickUpPiecePose()

        controller.pick_up_from_plate(pickUpPiecePose)



        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        
        results = getPredictionsUntilValid()
        stopThreads = False # value changed just to see what happens

        # print(f"DEBUGGING results: \n{results}")
        array = coordFormatFromPredictions(results)

        board = Board(array)

        matrix = board.findMatrix()

        # print(matrix)
        colorOnlyMatrix = formatOnlyColourVals(matrix)

        if not checkFloaters(colorOnlyMatrix):
             print("Floater detected recapturing...")
             continue
        # colorOnlyMatrix = np.array(colorOnlyMatrix)


        threads = []
        stopThreads = False
        t = threading.Thread(target=worker, args =(lambda : stopThreads, screen, colorOnlyMatrix))
        threads.append(t)
        t.start()
        
        pygame.display.update()
        pygame.event.pump()


        displayInCLI = TerminalBoard(colorOnlyMatrix)
        displayInCLI.printBoard()

        robotMove = pick_best_move(np.array(colorOnlyMatrix), 1) + 1

        print(f"Robot's move: column {robotMove}")

        controller.drop_in_column(robotMove)
            
        controller.goto_reset()

        # give opponent a piece
        
        results = getResults()

        # call vector finder
        collectionPlate = tablePieces(results, Point(originXInput, originYInput), Point(xXInput, xYInput), Point(yXInput, yYInput))

        # picking piece
        pieceCoords = collectionPlate.pickPiece(YELLOWCOLORNAME)

        # setting attribute piece
        collectionPlate.pieceSetter((pieceCoords[0], pieceCoords[1]))

        pickUpPiecePose = collectionPlate.getPickUpPiecePose()

        controller.pick_up_from_plate(pickUpPiecePose)

        controller.drop_in_plinko()

        controller.goto_reset()



        input("Enter to open gripper")
        controller.gripper_open()
        should_loop = input("Press enter to contiue or enter (quit or q) to exit: ")


    stopThreads = True

    for t in threads:
        t.join()
    print("Main thread: All threads finished")

    pygame.quit()








# fakeArray = [
#   [5, 5, ""], [5, 10, " "], [5, 15, " "], [5, 20, " "], [5, 25, " "], [5, 30, " "],
#   [10, 5, " "], [10, 10, " "], [10, 15, " "], [10, 20, " "], [10, 25, " "], [10, 30, " "], 
#   [15, 5, " "], [15, 10, " "], [15, 15, " "], [15, 20, " "], [15, 25, " "], [15, 30, " "], 
#   [20, 5, " "], [20, 10, " "], [20, 15, " "], [20, 20, " "], [20, 25, " "], [20, 30, " "], 
#   [25, 5, " "], [25, 10, " "], [25, 15, " "], [25, 20, " "], [25, 25, " "], [25, 30, " "], 
#   [30, 5, " "], [30, 10, " "], [30, 15, " "], [30, 20, " "], [30, 25, " "], [30, 30, " "], 
#   [35, 5, " "], [35, 10, " "], [35, 15, " "], [35, 20, " "], [35, 25, " "], [35, 30, " "]
# ]
