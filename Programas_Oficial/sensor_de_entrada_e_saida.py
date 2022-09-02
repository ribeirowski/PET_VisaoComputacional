from matplotlib import pyplot as plt
import numpy as np, cv2 as cv, img

i = 1
flag = 0

# Começar a captura da imagem da webcam:
webCam = cv.VideoCapture(0)

# Informações do retângulo vermelho:
startPoint1 = (630, 10)
endPoint1 = (635, 470)
startPoint2 = (5, 10)
endPoint2 = (10, 470)
colorRed = (0, 0, 0)

if webCam.isOpened():
    print("Conected!")

    while True: 
        ret, video = webCam.read()

        videoRet1 = cv.rectangle(video, startPoint1, endPoint1, colorRed, 0)
        videoRet2 = cv.rectangle(video, startPoint2, endPoint2, colorRed, 0)

        cutVideo1 = video[11 : 470, 631 : 635]
        cutVideo2 = video[11 : 470, 6 : 10]

        if flag == 0:
            cv.imwrite("imgReferencia1.png", cutVideo1)
            imgReferenciaSuave1 = img.mod("imgReferencia1.png")
            cv.imwrite("imgReferencia_GrayBlured1.png", imgReferenciaSuave1)
            cv.imwrite("imgReferencia2.png", cutVideo2)
            imgReferenciaSuave2 = img.mod("imgReferencia2.png")
            cv.imwrite("imgReferencia_GrayBlured2.png", imgReferenciaSuave2)
            flag+=1
        
        cv.imshow("Enio", video)

        cv.imwrite("corte1.png", cutVideo1)
        corte1 = img.mod("corte1.png")

        cv.imwrite("corte2.png", cutVideo2)
        corte2 = img.mod("corte2.png")

        imgDiferenca1 = cv.subtract(corte1, imgReferenciaSuave1)
        ret2, imgDiferencaLimiar1 = cv.threshold(imgDiferenca1, 100, 255, cv.THRESH_BINARY)
        area1 = np.sum(imgDiferencaLimiar1 == 255)
        print("Area1: ", area1)

        imgDiferenca2 = cv.subtract(corte2, imgReferenciaSuave2)
        ret3, imgDiferencaLimiar2 = cv.threshold(imgDiferenca2, 100, 255, cv.THRESH_BINARY)
        area2 = np.sum(imgDiferencaLimiar2 == 255)
        print("Area2: ", area2)

        imgDiferencaLaplacian1 = cv.Laplacian(imgDiferenca1, cv.CV_64F)
        imgDiferencaLaplacian1 = np.absolute(imgDiferencaLaplacian1)
        imgDiferencaLaplacian1 = np.uint8(imgDiferencaLaplacian1)
        ret2, imgDiferencaLaplacian1 = cv.threshold(imgDiferencaLaplacian1, 9, 255, cv.THRESH_BINARY)
        perimetro1 = np.sum(imgDiferencaLaplacian1 == 255)
        print("Perimetro1: ", perimetro1)

        imgDiferencaLaplacian2 = cv.Laplacian(imgDiferenca2, cv.CV_64F)
        imgDiferencaLaplacian2 = np.absolute(imgDiferencaLaplacian2)
        imgDiferencaLaplacian2 = np.uint8(imgDiferencaLaplacian2)
        ret3, imgDiferencaLaplacian2 = cv.threshold(imgDiferencaLaplacian2, 9, 255, cv.THRESH_BINARY)
        perimetro2 = np.sum(imgDiferencaLaplacian2 == 255)
        print("Perimetro2: ", perimetro2)

        cv.imshow("Diferença Limia1", imgDiferencaLimiar1)
        cv.imshow("Diferença Laplaciano1", imgDiferencaLaplacian1)

        cv.imshow("Diferença Limiar2", imgDiferencaLimiar2)
        cv.imshow("Diferença Laplaciano2", imgDiferencaLaplacian2)

        if area1 < 100 and perimetro1 < 200 and flag>1:
            print("Alerta! Invasão")
            cv.imwrite("kkeaeman1.png", cutVideo1)

        if area2 < 100 and perimetro2 < 200 and flag>1:
            print("Alerta! Invasão")
            cv.imwrite("kkeaeman2.png", cutVideo2)

        if cv.waitKey(1) == 27:
            break

webCam.release()

cv.destroyAllWindows()