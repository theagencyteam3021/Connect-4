from scripts.board import Board

from scripts.utils import coordFormatFromPredictions, formatOnlyColourVals, imageCapture

from visualization.gridBoardTest import GridBoardDisplay

from PIL import Image

import inference


# from PIL import Image

# retakes photo until 42 detections are made
isFirstTry = False

imageCapture()
image = Image.open("webcam_photo.jpg")
model = inference.get_model("connect4-lxv2j/2", "fxXBp7IHZMUOlxGJbueP")
results = model.infer(image=image)

while len(results[0]) != 42:

    if not isFirstTry:
        print(f"Retaking photo {len(results)} spots detected.")
    else:
        isFirstTry = False

    imageCapture()
    image = Image.open("webcam_photo.jpg")
    results = model.infer(image=image)

array = coordFormatFromPredictions(results)

board = Board(array)

matrix = board.findMatrix()

print(matrix)

colorOnlyMatrix = formatOnlyColourVals(matrix)
                        
disp = GridBoardDisplay(colorOnlyMatrix)
disp.run()




# fakeArray = [
#   [5, 5, ""], [5, 10, " "], [5, 15, " "], [5, 20, " "], [5, 25, " "], [5, 30, " "],
#   [10, 5, " "], [10, 10, " "], [10, 15, " "], [10, 20, " "], [10, 25, " "], [10, 30, " "], 
#   [15, 5, " "], [15, 10, " "], [15, 15, " "], [15, 20, " "], [15, 25, " "], [15, 30, " "], 
#   [20, 5, " "], [20, 10, " "], [20, 15, " "], [20, 20, " "], [20, 25, " "], [20, 30, " "], 
#   [25, 5, " "], [25, 10, " "], [25, 15, " "], [25, 20, " "], [25, 25, " "], [25, 30, " "], 
#   [30, 5, " "], [30, 10, " "], [30, 15, " "], [30, 20, " "], [30, 25, " "], [30, 30, " "], 
#   [35, 5, " "], [35, 10, " "], [35, 15, " "], [35, 20, " "], [35, 25, " "], [35, 30, " "]
# ]

# board = Board(fakeArray)

# matrix = board.findMatrix()

# print(matrix)
# """
# [[[5, 30, ' '], [10, 30, ' '], [15, 30, ' '], [20, 30, ' '], [25, 30, ' '], [30, 30, ' '], [35, 30, ' ']], 
#  [[5, 25, ' '], [10, 25, ' '], [15, 25, ' '], [20, 25, ' '], [25, 25, ' '], [30, 25, ' '], [35, 25, ' ']], 
#  [[5, 20, ' '], [10, 20, ' '], [15, 20, ' '], [20, 20, ' '], [25, 20, ' '], [30, 20, ' '], [35, 20, ' ']], 
#  [[5, 15, ' '], [10, 15, ' '], [15, 15, ' '], [20, 15, ' '], [25, 15, ' '], [30, 15, ' '], [35, 15, ' ']], 
#  [[5, 10, ' '], [10, 10, ' '], [15, 10, ' '], [20, 10, ' '], [25, 10, ' '], [30, 10, ' '], [35, 10, ' ']], 
#  [[5, 5, ''], [10, 5, ' '], [15, 5, ' '], [20, 5, ' '], [25, 5, ' '], [30, 5, ' '], [35, 5, ' ']]]
# """