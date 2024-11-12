

sampleArray = [[1, 1, 1, 2, 1, 2, 2], [1, 1, 2, 1, 2, 2, 1], [1, 2, 1, 1, 2, 1, 2], [2, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]



class TerminalBoard():
    def __init__(self, array="none") -> None:
        if array == "none":
            print("No array provided; sample array is being used.")
            self.array = sampleArray
        else:
            self.array = array
            self.array = list(reversed(array))
    
    def printBoard(self):
        for row in range(6):
            for col in range(7):
                if self.array[row][col] == 2:
                    print("\033[33m●\033[0m", end=" ") 
                elif self.array[row][col] == 1:
                    print("\033[31m●\033[0m", end=" ") 
                else:
                    print("\033[38;5;244m●\033[0m", end=" ")
            print()
board = TerminalBoard()
board.printBoard()
