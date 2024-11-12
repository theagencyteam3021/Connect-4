import pygame

sampleArray = [[1, 1, 1, 2, 1, 2, 2], [1, 1, 2, 1, 2, 2, 1], [1, 2, 1, 1, 2, 1, 2], [2, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


class GridBoardDisplay():
    def __init__(self, screenSurface, array=sampleArray) -> None:
        pygame.init()
        self.SCREEN_WIDTH = 750
        self.SCREEN_HEIGHT = 650
        self.screen = screenSurface
        # self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.array = reversed(array)
    
    def run(self, stop):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            for row in range(6):
                for col in range(7):
                    if self.array[row][col] == 2:
                        pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(col * 100 + 50, row * 100 + 50, 50, 50))
                    elif self.array[row][col] == 1:
                        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(col * 100 + 50, row * 100 + 50, 50, 50))
                    else:
                        pygame.draw.rect(self.screen, (100, 100, 100), pygame.Rect(col * 100 + 50, row * 100 + 50, 50, 50))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
            if stop():
                break



# this is just output copy pasted from main
# array = [[[687.0, 849.0, 'Red'], [870.5, 850.0, 'Red'], [1052.5, 844.5, 'Red'], [1229.0, 836.0, 'Yellow'], [1393.0, 822.5, 'Red'], [1535.0, 806.5, 'Yellow'], [1661.5, 787.5, 'Yellow']], [[684.5, 684.5, 'Red'], [867.0, 684.0, 'Red'], [1047.5, 681.5, 'Yellow'], [1223.5, 675.5, 'Red'], [1385.0, 668.5, 'Yellow'], [1528.5, 659.0, 'Yellow'], [1655.5, 648.5, 'Red']], [[686.0, 521.0, 'Red'], [863.5, 521.0, 'Yellow'], [1041.0, 519.5, 'Red'], [1214.5, 517.5, 'Red'], [1375.0, 514.5, 'Yellow'], [1517.5, 511.5, 'Red'], [1642.5, 510.0, 'Yellow']], [[691.5, 365.5, 'Yellow'], [862.0, 363.5, 'Red'], [1037.0, 365.0, 'Empty'], [1205.5, 365.5, 'Empty'], [1359.5, 368.5, 'Red'], [1500.0, 372.0, 'Empty'], [1625.0, 376.0, 'Empty']], [[695.5, 219.5, 'Empty'], [861.5, 216.0, 'Empty'], [1030.5, 219.5, 'Empty'], [1192.0, 223.5, 'Empty'], [1343.5, 229.0, 'Empty'], [1482.0, 238.5, 'Empty'], [1602.0, 249.0, 'Empty']], [[703.5, 87.0, 'Empty'], [863.0, 84.0, 'Empty'], [1024.0, 86.5, 'Empty'], [1178.5, 93.0, 'Empty'], [1325.0, 102.0, 'Empty'], [1459.0, 116.0, 'Empty'], [1578.0, 130.0, 'Empty']]]
# array.reverse()

# run = True
# while run:
    
#     screen.fill((0, 0, 0))

#     # for i in range(6):
#     #     for k in range(7):
#     #         if array[i][k][2] == 'Yellow':
#     #             pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(k * 100 + 50, i * 100 + 50, 50, 50))
#     #         elif array[i][k][2] == 'Red':
#     #             pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(k * 100 + 50, i * 100 + 50, 50, 50))
#     #         else:
#     #             pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(k * 100 + 50, i * 100 + 50, 50, 50))
#     for row in range(6):
#         for col in range(7):
#             if arrayColours[row][col] == 2:
#                 pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(col * 100 + 50, row * 100 + 50, 50, 50))
#             elif arrayColours[row][col] == 1:
#                 pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(col * 100 + 50, row * 100 + 50, 50, 50))
#             else:
#                 pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(col * 100 + 50, row * 100 + 50, 50, 50))


#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     pygame.display.update()

# pygame.quit()
