from scripts.board import Board

from scripts.utils import *

from scripts.gridBoardTest import GridBoardDisplay

from scripts.TerminalDisplay import TerminalBoard

from alg.connect_4_alg_stolen import pick_best_move

from scripts.URController import URController

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
    controller = URController()

    should_loop = ""

    while  should_loop != "quit" and should_loop != "q":

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        controller.goto_reset()
        results = getPredictionsUntilValid()
        stopThreads = True

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
        t = threading.Thread(target=worker, args =(lambda : stopThreads, colorOnlyMatrix))
        threads.append(t)
        t.start()


        displayInCLI = TerminalBoard(colorOnlyMatrix)
        displayInCLI.printBoard()

        robotMove = pick_best_move(np.array(colorOnlyMatrix), 1) + 1

        print(f"Robot's move: column {robotMove}")

        controller.drop_in_column(robotMove)
            
        controller.goto_reset()
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
