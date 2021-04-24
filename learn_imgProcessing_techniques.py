import numpy as np
import cv2
# import random
# import time
import math
#import matplotlib.pyplot as plt


# define  kernel
Gx = np.zeros((3, 3))
Gx[0, 0] = 1
Gx[0, 1] = 0
Gx[0, 2] = -1
Gx[1, 0] = 2
Gx[1, 1] = 0
Gx[1, 2] = -2
Gx[2, 0] = 1
Gx[2, 1] = 0
Gx[2, 2] = -1
Gy = np.zeros((3, 3))
Gy[0, 0] = 1
Gy[0, 1] = 2
Gy[0, 2] = 1
Gy[1, 0] = 0
Gy[1, 1] = 0
Gy[1, 2] = 0
Gy[2, 0] = -1
Gy[2, 1] = -2
Gy[2, 2] = -1


# sobel edge
def norm(img1, img2):
    img_copy = np.zeros(img1.shape)
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            g = math.sqrt(img1[i][j] ** 2 + img2[i][j] ** 2)
            if (g > 200):
                img_copy[i][j] = 255
            else:
                img_copy[i][j] = 0
    return img_copy


# img transform
def conv_transform(img):
    img_copy = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_copy[i][j] = img[img.shape[0] - i - 1][img.shape[1] - j - 1]
    return img_copy


# convolution operation
def conv(img, G):
    kernel = conv_transform(G)
    img_h = img.shape[0]
    img_w = img.shape[1]
    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]
    h = kernel_h // 2
    w = kernel_w // 2

    img_conv = np.zeros(img.shape)
    for i in range(h, img_h - h):
        for j in range(w, img_w - w):
            sum = 0
            for n in range(kernel_h):
                for m in range(kernel_w):
                    sum = sum + kernel[m][n] * img[i - h + m][j - w + n]
            img_conv[i][j] = sum
    return img_conv


if __name__ == "__main__":
    img = cv2.imread('E:/python/img_test_file/1.jpg', 0)
    gx = conv(img, Gx)
    gy = conv(img, Gy)
    g_sobel = norm(gx, gy)
    cv2.imshow("filtered",g_sobel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()