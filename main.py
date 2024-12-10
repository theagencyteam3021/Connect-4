from scripts.board import Board

from scripts.utils import coordFormatFromPredictions, formatOnlyColourVals, imageCapture

from scripts.gridBoardTest import GridBoardDisplay

from scripts.TerminalDisplay import TerminalBoard

from alg.connect_4_alg_stolen import pick_best_move

from ultralytics import YOLO

import time

import numpy as np

import pygame

import threading

import cv2 as cv

from PIL import Image

# import inference


# retakes photo until 42 detections are made

def getPredictionsUntilValid(file="webcam_photo.jpg", model=15):

    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("webcam error")

    capture.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc('M','J','P','G'))

    ret, frame = capture.read()

    if ret:
        cv.imwrite("webcam_photo.jpg", frame)

    image = Image.open(file)
    model = YOLO('best.pt')
    results = model('webcam_photo.jpg')
    # model = inference.get_model("connect4-lxv2j/15", "fxXBp7IHZMUOlxGJbueP")
    # results = model.infer(image=image)
    
    # while len(results[0].predictions) != 42:
    while len(results[0].boxes.cls) != 42:
        print(f"Retaking photo {len(results[0].boxes.cls)} spots detected.")
        
        ret, frame = capture.read()

        if ret:
            cv.imwrite("webcam_photo.jpg", frame)

        image = Image.open(file)
        results = model('webcam_photo.jpg')
        # results = model.infer(image=image)

        time.sleep(0.5)
    capture.release()
    return results

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
