
# def coordFormatFromPredictions(results):
#     formattedList = []
#     for result in results[0].boxes.cls:
#         formattedList.append([result.x, result.y, result.class_name])
#     return formattedList

def coordFormatFromPredictions(results):
    formattedList = []
    for i in range(len(results[0].boxes.cls)):
        formattedList.append([float(results[0].boxes.xywh[i][0]),float(results[0].boxes.xywh[i][1]), results[0].names[int(results[0].boxes.cls[i])]])
    


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

import cv2 as cv

def imageCapture():
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("webcam error")

    capture.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc('M','J','P','G'))

    ret, frame = capture.read()

    if ret:
        cv.imwrite("webcam_photo.jpg", frame)

    # capture.release()
