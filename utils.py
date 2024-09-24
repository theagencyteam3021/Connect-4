
def coordFormatFromPredictions(results):
    formattedList = []
    for result in results[0].predictions:
        formattedList.append([result.x, result.y, result.class_name])
    return formattedList

def formatOnlyColourVals(coordsArray):
    formatedList = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    for i in range(6):
        for k in range(7):
            if coordsArray[i][k][2] == 'Empty':
                formatedList[i][k] = 0
            elif coordsArray[i][k][2] == 'Red':
                formatedList[i][k] = 1
            else:
                formatedList[i][k] = 2
    return formatedList
