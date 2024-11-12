from scripts.board import Board

from scripts.utils import coordFormatFromPredictions, formatOnlyColourVals, imageCapture

from scripts.gridBoardTest import GridBoardDisplay

from alg.connect_4_alg_stolen import pick_best_move

import numpy as np

import threading

from PIL import Image

import inference


# retakes photo until 42 detections are made

def getPredictionsUntilValid(file="webcam_photo.jpg", model=15):

    imageCapture()
    image = Image.open(file)
    model = inference.get_model("connect4-lxv2j/15", "fxXBp7IHZMUOlxGJbueP")
    results = model.infer(image=image)
    
    while len(results[0].predictions) != 42:
        print(f"Retaking photo {len(results[0].predictions)} spots detected.")
        imageCapture()
        image = Image.open(file)
        results = model.infer(image=image)
    return results

def worker():
        disp = GridBoardDisplay(colorOnlyMatrix)
        disp.run()

        
if __name__ == "__main__":

    results = getPredictionsUntilValid()

    array = coordFormatFromPredictions(results)

    board = Board(array)

    matrix = board.findMatrix()

    # print(matrix)
    colorOnlyMatrix = formatOnlyColourVals(matrix)


    threads = []
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

    print(pick_best_move(colorOnlyMatrix, 1))

    for t in threads:
        t.join()

    print("Main thread: All threads finished")





# sampleArray = [[1, 1, 1, 2, 1, 2, 2], [1, 1, 2, 1, 2, 2, 1], [1, 2, 1, 1, 2, 1, 2], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
# print(pick_best_move(sampleArray, 1))

# fakeArray = [
#   [5, 5, ""], [5, 10, " "], [5, 15, " "], [5, 20, " "], [5, 25, " "], [5, 30, " "],
#   [10, 5, " "], [10, 10, " "], [10, 15, " "], [10, 20, " "], [10, 25, " "], [10, 30, " "], 
#   [15, 5, " "], [15, 10, " "], [15, 15, " "], [15, 20, " "], [15, 25, " "], [15, 30, " "], 
#   [20, 5, " "], [20, 10, " "], [20, 15, " "], [20, 20, " "], [20, 25, " "], [20, 30, " "], 
#   [25, 5, " "], [25, 10, " "], [25, 15, " "], [25, 20, " "], [25, 25, " "], [25, 30, " "], 
#   [30, 5, " "], [30, 10, " "], [30, 15, " "], [30, 20, " "], [30, 25, " "], [30, 30, " "], 
#   [35, 5, " "], [35, 10, " "], [35, 15, " "], [35, 20, " "], [35, 25, " "], [35, 30, " "]
# ]
