from scripts.board import Board

from scripts.utils import coordFormatFromPredictions, formatOnlyColourVals, imageCapture

from scripts.gridBoardTest import GridBoardDisplay

from scripts.TerminalDisplay import TerminalBoard

from scripts.utils import getPredictionsUntilValid

from alg.connect_4_alg_stolen import pick_best_move

from ultralytics import YOLO

import time

import numpy as np

import pygame

import threading

import cv2 as cv

# from PIL import Image

def worker(stop):
        disp = GridBoardDisplay(screen, colorOnlyMatrix)
        disp.run(stop)


        
if __name__ == "__main__":

    SCREEN_WIDTH = 750
    SCREEN_HEIGHT = 650


    should_loop = ""

    while  should_loop != "quit" and should_loop != "q":

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        results = getPredictionsUntilValid()
        stopThreads = True

        # print(f"DEBUGGING results: \n{results}")
        array = coordFormatFromPredictions(results)

        board = Board(array)

        matrix = board.findMatrix()

        # print(matrix)
        colorOnlyMatrix = formatOnlyColourVals(matrix)

        # colorOnlyMatrix = np.array(colorOnlyMatrix)


        threads = []
        stopThreads = False
        t = threading.Thread(target=worker, args =(lambda : stopThreads, ))
        threads.append(t)
        t.start()

        displayInCLI = TerminalBoard(colorOnlyMatrix)
        displayInCLI.printBoard()

        print(f"Robot's move: column {pick_best_move(np.array(colorOnlyMatrix), 1) + 1}")


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
