""" --------------------------------------------------------------------------------------------------------
Escolha uma imagem colorida do rosto de uma pessoa famosa e aplique os seguintes filtros passa baixas 5x5: 

a) filtro da média; 
b) filtro gaussiano; 
c) filtro da mediana. 

Aplique a cada banda da imagem (vermelho, verde e azul) e plote o resultado à direita da imagem original. 

O que você pôde observar?
----------------------------------------------------------------------------------------------------------"""

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

theRock = cv.cvtColor(cv.imread("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/therock.jpg", 1), cv.COLOR_BGR2RGB)

(blue, green, red) = cv.split(theRock)

# Average Filter (BGR)
theRock_averageBlur_blue = cv.blur(blue, (5, 5))
theRock_averageBlur_green = cv.blur(green, (5, 5))
theRock_averageBlur_red = cv.blur(red, (5, 5))

# Gaussian Filter (BGR)
theRock_gaussianBlur_blue = cv.GaussianBlur(blue, (5, 5), 0)
theRock_gaussianBlur_green = cv.GaussianBlur(green, (5, 5), 0)
theRock_gaussianBlur_red = cv.GaussianBlur(red, (5, 5), 0)

# Median Filter (BGR)
theRock_medianBlur_blue = cv.medianBlur(blue, 5)
theRock_medianBlur_green = cv.medianBlur(green, 5)
theRock_medianBlur_red = cv.medianBlur(red, 5)

plt.subplot(451), plt.imshow(theRock), plt.title('Original', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(452), plt.imshow(cv.cvtColor(blue, cv.COLOR_BGR2RGB)), plt.title('Canal Azul', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(453), plt.imshow(cv.cvtColor(theRock_averageBlur_blue, cv.COLOR_BGR2RGB)), plt.title('Filtro da Média - BLUE', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(454), plt.imshow(cv.cvtColor(theRock_gaussianBlur_blue, cv.COLOR_BGR2RGB)), plt.title('Filtro Gaussiano - BLUE', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(455), plt.imshow(cv.cvtColor(theRock_medianBlur_blue, cv.COLOR_BGR2RGB)), plt.title('Filtro da Mediana - BLUE', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])

plt.subplot(456), plt.imshow(theRock), plt.title('Original', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(457), plt.imshow(cv.cvtColor(green, cv.COLOR_BGR2RGB)), plt.title('Canal Verde', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(458), plt.imshow(cv.cvtColor(theRock_averageBlur_green, cv.COLOR_BGR2RGB)), plt.title('Filtro da Média - GREEN', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(459), plt.imshow(cv.cvtColor(theRock_gaussianBlur_green, cv.COLOR_BGR2RGB)), plt.title('Filtro Gaussiano - GREEN', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,10), plt.imshow(cv.cvtColor(theRock_medianBlur_green, cv.COLOR_BGR2RGB)), plt.title('Filtro da Mediana - GREEN', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])

plt.subplot(4,5,11), plt.imshow(theRock), plt.title('Original', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,12), plt.imshow(cv.cvtColor(red, cv.COLOR_BGR2RGB)), plt.title('Canal Vermelho', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,13), plt.imshow(cv.cvtColor(theRock_averageBlur_red, cv.COLOR_BGR2RGB)), plt.title('Filtro da Média - RED', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,14), plt.imshow(cv.cvtColor(theRock_gaussianBlur_red, cv.COLOR_BGR2RGB)), plt.title('Filtro Gaussiano - RED', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,15), plt.imshow(cv.cvtColor(theRock_medianBlur_red, cv.COLOR_BGR2RGB)), plt.title('Filtro da Mediana - RED', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])

plt.suptitle("Filtros de Passa Baixa", fontsize=20)

final = plt.gcf()

final.set_size_inches(13, 7)

plt.savefig("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana3/Exercício1/Filtros_Passa_Baixa.png", dpi=199)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()