import cv2



def scaleImg(img):
    imgOriginal = img
    dimensions = imgOriginal.shape

    height = imgOriginal.shape[0]
    width = imgOriginal.shape[1]
    # print('Image Height       : ', height)
    # print('Image Width        : ', width)

    if width == 1654 and height == 2338:
        return imgOriginal
    else:
        dim = (1654, 2338)
        imgOriginal = cv2.resize(imgOriginal, dim, interpolation = cv2.INTER_AREA)
        dimensions = imgOriginal.shape
        height = imgOriginal.shape[0]
        width = imgOriginal.shape[1]
        # print('Image Height       : ', height)
        # print('Image Width        : ', width)
        return imgOriginal

cv2.waitKey()