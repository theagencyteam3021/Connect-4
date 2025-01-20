
# # def coordFormatFromPredictions(results):
# #     formattedList = []
# #     for result in results[0].boxes.cls:
# #         formattedList.append([result.x, result.y, result.class_name])
# #     return formattedList

# def coordFormatFromPredictions(results):
#     formattedList = []
#     for i in range(len(results[0].boxes.cls)):
#         formattedList.append([float(results[0].boxes.xywh[i][0]),float(results[0].boxes.xywh[i][1]), results[0].names[int(results[0].boxes.cls[i])]])
#     return formattedList
    


# def formatOnlyColourVals(coordsArray):
#     formatedList = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
#     for i in range(6):
#         for k in range(7):
#             if coordsArray[i][k][2] == 'Empty':
#                 formatedList[i][k] = 0
#             elif coordsArray[i][k][2] == 'Red':
#                 formatedList[i][k] = 1
#             else:
#                 formatedList[i][k] = 2
#     return formatedList

# import cv2 as cv

# def imageCapture():
#     capture = cv.VideoCapture(0)

#     if not capture.isOpened():
#         print("webcam error")

#     capture.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc('M','J','P','G'))

#     ret, frame = capture.read()

#     if ret:
#         cv.imwrite("webcam_photo.jpg", frame)

#     # capture.release()

# from ultralytics import YOLO

# import time

# # capture and repreat until 42 detections are made
# # once detectons are made returns the results of the object detection

# def getPredictionsUntilValid(file="webcam_photo.jpg", model=15):

#     capture = cv.VideoCapture(0)

#     if not capture.isOpened():
#         print("webcam error")

#     capture.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc('M','J','P','G'))

#     ret, frame = capture.read()

#     if ret:
#         cv.imwrite("webcam_photo.jpg", frame)

#     model = YOLO('best.pt')
#     results = model('webcam_photo.jpg')
#     # model = inference.get_model("connect4-lxv2j/15", "fxXBp7IHZMUOlxGJbueP")
#     # results = model.infer(image=image)
    
#     # while len(results[0].predictions) != 42:
#     while len(results[0].boxes.cls) != 42:
#         print(f"Retaking photo {len(results[0].boxes.cls)} spots detected.")
        
#         ret, frame = capture.read()

#         if ret:
#             cv.imwrite("webcam_photo.jpg", frame)

#         results = model('webcam_photo.jpg')
#         # results = model.infer(image=image)

#         time.sleep(0.5)
#     capture.release()
#     return results

sampleArray = [[1, 1, 1, 2, 1, 2, 2], [1, 1, 2, 1, 2, 2, 1], [1, 2, 1, 1, 2, 1, 2], [2, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


def checkFloaters(colorMatrix):
    # colorMatrix.reverse()
    for i in range(6):
        for k in range(1, 5):
            if (colorMatrix[k][i] != 0) and (colorMatrix[k-1][i] == 0):
                return False
    return True
print(checkFloaters(sampleArray))