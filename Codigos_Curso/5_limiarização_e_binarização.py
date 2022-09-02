""" ---------------------------------------------------------------------------------------------------------------
Utilizando de preferência a mesma imagem dos exercícios de filtros passa altas e passa baixas, converta a imagem 
em níveis de cinza e exiba o resultado. Em seguida, gere versões binárias usando limiarização (thresholding): 

a) limiar de 30; 
b) limiar de 150; 
c) limiar de 200; 
d) limiar adaptativo da média; 
e) limiar adaptativo gaussiano. 

Para facilitar a visualização, plote a imagem em níveis de cinza e as imagens binárias como uma matriz com duas 
linhas e três colunas, identificando adequadamente as legendas. 

O que você pode observar?
-----------------------------------------------------------------------------------------------------------------"""

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

theRock = cv.imread("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/therock.jpg", 0)

limiar1 = 30
limiar2 = 150
limiar3 = 200

ret, limiar_30 = cv.threshold(theRock, limiar1, 255, cv.THRESH_BINARY)
ret, limiar_150 = cv.threshold(theRock, limiar2, 255, cv.THRESH_BINARY)
ret, limiar_200 = cv.threshold(theRock, limiar3, 255, cv.THRESH_BINARY)
limiarAdaptativo_Media = cv.adaptiveThreshold(theRock, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
limiarAdaptativo_Gaussiano = cv.adaptiveThreshold(theRock, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

plt.subplot(231), plt.imshow(cv.cvtColor(theRock, cv.COLOR_BGR2RGB)), plt.title('Original', fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(cv.cvtColor(limiarAdaptativo_Media, cv.COLOR_BGR2RGB)), plt.title('Limiar A. da Média', fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(cv.cvtColor(limiarAdaptativo_Gaussiano, cv.COLOR_BGR2RGB)), plt.title('Limiar A. Gaussiano', fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(cv.cvtColor(limiar_30, cv.COLOR_BGR2RGB)), plt.title('Limiar 30', fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(cv.cvtColor(limiar_150, cv.COLOR_BGR2RGB)), plt.title('Limiar 150', fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(cv.cvtColor(limiar_200, cv.COLOR_BGR2RGB)), plt.title('Limiar 200', fontsize=10)
plt.xticks([]), plt.yticks([])

plt.suptitle("Limiarização e Binarização", fontsize=20)

plt.savefig("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana3/Exercício3/Limiarização_e_Binarização.png", dpi=200)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()