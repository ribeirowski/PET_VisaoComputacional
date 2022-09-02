import numpy as np
import cv2 as cv

def suave(img):
    imagem = cv.GaussianBlur(img, (5, 5), 0)
    return imagem