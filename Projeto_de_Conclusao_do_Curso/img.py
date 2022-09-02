import numpy as np
import cv2 as cv

def mod(img):
    imagem = cv.imread(img, 1)
    imagem = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
    imagem = cv.GaussianBlur(imagem, (5, 5), 1)
    return imagem