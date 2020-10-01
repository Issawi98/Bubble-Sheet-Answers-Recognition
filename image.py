import cv2
import numpy as np

def getLabels(img):
    # threshold, and inverse the photo
    th, ciclesImg = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
    ciclesImg = 255 - ciclesImg

    # obtaining answers' circles alone without any noise
    SE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    ciclesImg = cv2.morphologyEx(ciclesImg, cv2.MORPH_OPEN, SE)
    # cv2.imshow("detected1", ciclesImg)

    # connected components to obtain centroid coordinates
    result = cv2.connectedComponentsWithStats(ciclesImg, 4, cv2.CV_32S)
    number = result[0]
    centroids = result[3]

    # counter = 1
    # for i in centroids[1:]:  # in the normal case the first centroid represents the background.
    #     temp = tuple([int(i[0]), int(i[1])])  # get the x, y coordinates
    #     cv2.putText(ciclesImg, str(counter), temp, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100,100,100), 2)
    #     # print(str(counter) + str(temp))
    #     counter += 1
    return centroids, number - 1, ciclesImg


