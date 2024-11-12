from scripts.board import Board

from scripts.utils import *

from scripts.gridBoardTest import GridBoardDisplay

from scripts.boardDisplay import *

from alg.connect_4_alg_stolen import pick_best_move

boardImage = BoardDisplay()
boardImage.run()

sampleArray = [[0, 1, 1, 2, 1, 2, 2], [0, 1, 2, 1, 2, 2, 1], [1, 2, 1, 1, 2, 1, 2], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
print(pick_best_move(sampleArray, 1))