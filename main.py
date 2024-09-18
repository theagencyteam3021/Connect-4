from board import Board

def package(results):
  formattedList = []
  for result in results[0].predictions:
    formattedList.append([result.x, result.y, result.class_name])
  return formattedList

fakeArray = [
    [5, 5, ""], [5, 10, " "], [5, 15, " "], [5, 20, " "], [5, 25, " "], [5, 30, " "],
    [10, 5, " "], [10, 10, " "], [10, 15, " "], [10, 20, " "], [10, 25, " "], [10, 30, " "], 
    [15, 5, " "], [15, 10, " "], [15, 15, " "], [15, 20, " "], [15, 25, " "], [15, 30, " "], 
    [20, 5, " "], [20, 10, " "], [20, 15, " "], [20, 20, " "], [20, 25, " "], [20, 30, " "], 
    [25, 5, " "], [25, 10, " "], [25, 15, " "], [25, 20, " "], [25, 25, " "], [25, 30, " "], 
    [30, 5, " "], [30, 10, " "], [30, 15, " "], [30, 20, " "], [30, 25, " "], [30, 30, " "], 
    [35, 5, " "], [35, 10, " "], [35, 15, " "], [35, 20, " "], [35, 25, " "], [35, 30, " "]
]
# array = package(results)

# board2 = Board(array)

# matrix2 = board2.findMatrix()

# print(matrix2)

board = Board(fakeArray)

matrix = board.findMatrix()

print(matrix)
# """
# [[[5, 30, ' '], [10, 30, ' '], [15, 30, ' '], [20, 30, ' '], [25, 30, ' '], [30, 30, ' '], [35, 30, ' ']], 
#  [[5, 25, ' '], [10, 25, ' '], [15, 25, ' '], [20, 25, ' '], [25, 25, ' '], [30, 25, ' '], [35, 25, ' ']], 
#  [[5, 20, ' '], [10, 20, ' '], [15, 20, ' '], [20, 20, ' '], [25, 20, ' '], [30, 20, ' '], [35, 20, ' ']], 
#  [[5, 15, ' '], [10, 15, ' '], [15, 15, ' '], [20, 15, ' '], [25, 15, ' '], [30, 15, ' '], [35, 15, ' ']], 
#  [[5, 10, ' '], [10, 10, ' '], [15, 10, ' '], [20, 10, ' '], [25, 10, ' '], [30, 10, ' '], [35, 10, ' ']], 
#  [[5, 5, ''], [10, 5, ' '], [15, 5, ' '], [20, 5, ' '], [25, 5, ' '], [30, 5, ' '], [35, 5, ' ']]]
# """