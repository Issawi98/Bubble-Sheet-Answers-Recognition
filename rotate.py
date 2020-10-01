import cv2
import numpy as np
import math


def invRotation(image):
    # scale image
    image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)

    # convert into grey scale img
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect edges, used default Sobel-kernel
    img_edges = cv2.Canny(image, 100, 100, apertureSize=3)
    # Run Hough on edge detected image
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

    angle = 0

    # get the rotation angle of the line
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        # angles.append(angle) # no need for it as i am taking one angle only.
    # print(angle)
    # rotate the image and return result
    # median_angle = np.median(angle) # no need for it as i am taking one angle only.
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

    # this code was used but it doesn't rotate the photo perfectly to the ideal position
    # ---------------------------------------------------------------
    # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
    # lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
    #
    # angles = []
    #
    # for x1, y1, x2, y2 in lines[0]:
    #     cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
    #     angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    #     angles.append(angle)
    #
    # median_angle = np.median(angles)
    # img_rotated = ndimage.rotate(image, median_angle)
    #
    # print("Angle is {}".format(median_angle))
    # return img_rotated
