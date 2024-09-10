
fakeArray = [
    [5, 5, ""], [5, 10, " "], [5, 15, " "], [5, 20, " "], [5, 25, " "], [5, 30, " "], [5, 35, " "], 
    [10, 5, " "], [10, 10, " "], [10, 15, " "], [10, 20, " "], [10, 25, " "], [10, 30, " "], [10, 35, " "], 
    [15, 5, " "], [15, 10, " "], [15, 15, " "], [15, 20, " "], [15, 25, " "], [15, 30, " "], [15, 35, " "], 
    [20, 5, " "], [20, 10, " "], [20, 15, " "], [20, 20, " "], [20, 25, " "], [20, 30, " "], [20, 35, " "], 
    [25, 5, " "], [25, 10, " "], [25, 15, " "], [25, 20, " "], [25, 25, " "], [25, 30, " "], [25, 35, " "], 
    [30, 5, " "], [30, 10, " "], [30, 15, " "], [30, 20, " "], [30, 25, " "], [30, 30, " "], [30, 35, " "]
]


#idk what the image res/dimentions are 
imageXWidth = 500
imageYHeight = 500

# params: input is in form 2d array with [xCoord, yCoord, colour]
# returns: [topLeft, topRight, bottomLeft, bottomRight]
def cornerFinder(allPoints):

    #these are set to the farthest pixel from their name
    topLeft = [imageXWidth, imageYHeight, ""]
    topRight = [0, imageYHeight, ""]
    bottomLeft = [imageXWidth, 0, ""]
    bottomRight = [0, 0, ""]

    for point in allPoints:
        if ((point[0] ** 2 + point[1] ** 2) ** 0.5) < ((topLeft[0] ** 2 + topLeft[1] ** 2) ** 0.5):
            topLeft = point

        if (((imageXWidth - point[0]) ** 2 + point[1] ** 2) ** 0.5) < (((imageXWidth - topRight[0]) ** 2 + topRight[1] ** 2) ** 0.5):
            topRight = point

        if ((point[0] ** 2 + (point[1] - imageYHeight) ** 2) ** 0.5) < ((bottomLeft[0] ** 2 + (imageYHeight - bottomLeft[1]) ** 2) ** 0.5):
            bottomLeft = point

        if (((point[0] - imageXWidth) ** 2 + (point[1] - imageYHeight) ** 2) ** 0.5) < (((bottomRight[0] - imageXWidth) ** 2 + (imageYHeight - bottomRight[1]) ** 2) ** 0.5):
            bottomRight = point

    return [topLeft, topRight, bottomLeft, bottomRight]

def edgeFinder(allPoints, cornerArray):
    #find slope m
    #take point p and make perpendicular line using -1/m 
    #find intersection coord q
    #find pixel at intersection q and find distance from p
    #compare distances until top five smallest are found
    #sort by y coord
    #repeat on other side
    #return

    # or make a function called findClosestToLine(array, line, outputNum)
    pass
#testing
print(cornerFinder(fakeArray))
