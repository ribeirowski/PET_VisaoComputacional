from playsound import playsound
from matplotlib import pyplot as plt
import numpy as np, cv2 as cv, time, img, clock

area = 5000
perimetro = 500
areaParametro = 5000
perimetroParametro = 150

i = 1
flag = 0

# Começar a captura da imagem da webcam:
webCam = cv.VideoCapture(0)

# Informações do retângulo vermelho:
startPoint = (260, 195)
endPoint = (380, 285)
colorRed = (0, 0, 255)

if webCam.isOpened():
    print("Conected!")
    
    print(clock.horario())

    while True:
        ret, video = webCam.read()

        videoRet = cv.rectangle(video, startPoint, endPoint, colorRed, 1)

        cutVideo = video[196 : 285, 261 : 380]

        if flag == 0:
            cv.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/referencia/imgReferencia.png", cutVideo)
            imgReferenciaSuave = img.mod("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/referencia/imgReferencia.png")
            cv.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/referencia/imgReferencia_GrayBlured.png", imgReferenciaSuave)
            flag+=1
        
        cv.imshow("Enio", videoRet)

        time.sleep(0.25)
        cv.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/corte.png", cutVideo)
        corte = img.mod("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/corte.png")

        imgDiferenca = cv.subtract(corte, imgReferenciaSuave)
        ret2, imgDiferencaLimiar = cv.threshold(imgDiferenca, 100, 255, cv.THRESH_BINARY)
        area = np.sum(imgDiferencaLimiar == 255)
        print("Area: ", area)

        imgDiferencaLaplacian = cv.Laplacian(imgDiferenca, cv.CV_64F)
        imgDiferencaLaplacian = np.absolute(imgDiferencaLaplacian)
        imgDiferencaLaplacian = np.uint8(imgDiferencaLaplacian)
        ret2, imgDiferencaLaplacian = cv.threshold(imgDiferencaLaplacian, 9, 255, cv.THRESH_BINARY)
        perimetro = np.sum(imgDiferencaLaplacian == 255)
        print("Perimetro: ", perimetro)

        cv.imshow("Diferença Limiar", imgDiferencaLimiar)
        cv.imshow("Diferença Laplaciano", imgDiferencaLaplacian)

        if area < areaParametro and perimetro < perimetroParametro and flag>1:
            dataHora = time.ctime()
            playsound("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/audios/alarme_1s.mp3")
            #print(f"Alerta! Invasão às {dataHora}")
            cv.imwrite(f"C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/invasao/invasao{i}_{clock.data(time.localtime())}_{clock.hora(time.localtime())}.png", cutVideo)
            i+=1

        flag+=1

        if cv.waitKey(1) == 27:
            print(clock.horario())
            break
    
"""     scale_percent = 1000 # percent of original size
    width = int("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/corte.png".shape[1] * scale_percent / 100)
    height = int("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/corte.png".shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv.resize("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/corte.png", dim, interpolation = cv.INTER_AREA)
    
    cv.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/resized.png", resized) """

webCam.release()

cv.destroyAllWindows()