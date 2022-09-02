""" --------------------------------------------------------------------------------------------------------
Escolha uma imagem colorida do rosto de uma pessoa famosa, de preferência a mesma do exercício de filtros 
passa baixas,e aplique os seguintes filtros passa altas 5x5: 

a) Laplaciano; 
b) Sobel X; 
c) Sobel Y. 

Aplique a cada banda da imagem (vermelho, verde e azul) e plote o resultado à direita da imagem original. 

O que você pode observar?
----------------------------------------------------------------------------------------------------------"""

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

theRock = cv.cvtColor(cv.imread("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/therock.jpg", 1), cv.COLOR_BGR2RGB)

(blue, green, red) = cv.split(theRock)

# Laplacian Filter (BGR)
theRock_Laplacian_blue = cv.Laplacian(blue, cv.CV_64F)
theRock_Laplacian_blue = np.absolute(theRock_Laplacian_blue)
theRock_Laplacian_blue = np.uint8(theRock_Laplacian_blue)
theRock_Laplacian_green = cv.Laplacian(green, cv.CV_64F)
theRock_Laplacian_green = np.absolute(theRock_Laplacian_green)
theRock_Laplacian_green = np.uint8(theRock_Laplacian_green)
theRock_Laplacian_red = cv.Laplacian(red, cv.CV_64F)
theRock_Laplacian_red = np.absolute(theRock_Laplacian_red)
theRock_Laplacian_red = np.uint8(theRock_Laplacian_red)

# Sobel X Filter (BGR)
theRock_SobelX_blue = cv.Sobel(blue, cv.CV_64F, 1, 0, ksize=5)
theRock_SobelX_blue = np.absolute(theRock_SobelX_blue)
theRock_SobelX_blue = np.uint8(theRock_SobelX_blue)
theRock_SobelX_green = cv.Sobel(green, cv.CV_64F, 1, 0, ksize=5)
theRock_SobelX_green = np.absolute(theRock_SobelX_green)
theRock_SobelX_green = np.uint8(theRock_SobelX_green)
theRock_SobelX_red = cv.Sobel(red, cv.CV_64F, 1, 0, ksize=5)
theRock_SobelX_red = np.absolute(theRock_SobelX_red)
theRock_SobelX_red = np.uint8(theRock_SobelX_red)

# Sobel Y Filter (BGR)
theRock_SobelY_blue = cv.Sobel(blue, cv.CV_64F, 0, 1, ksize=5)
theRock_SobelY_blue = np.absolute(theRock_SobelY_blue)
theRock_SobelY_blue = np.uint8(theRock_SobelY_blue)
theRock_SobelY_green = cv.Sobel(green, cv.CV_64F, 0, 1, ksize=5)
theRock_SobelY_green = np.absolute(theRock_SobelY_green)
theRock_SobelY_green = np.uint8(theRock_SobelY_green)
theRock_SobelY_red = cv.Sobel(red, cv.CV_64F, 0, 1, ksize=5)
theRock_SobelY_red = np.absolute(theRock_SobelY_red)
theRock_SobelY_red = np.uint8(theRock_SobelY_red)

plt.subplot(451), plt.imshow(theRock), plt.title('Original', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(452), plt.imshow(cv.cvtColor(blue, cv.COLOR_BGR2RGB)), plt.title('Canal Azul', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(453), plt.imshow(cv.cvtColor(theRock_Laplacian_blue, cv.COLOR_BGR2RGB)), plt.title('Filto Laplaciano - BLUE', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(454), plt.imshow(cv.cvtColor(theRock_SobelX_blue, cv.COLOR_BGR2RGB)), plt.title('Filtro Sobel X - BLUE', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(455), plt.imshow(cv.cvtColor(theRock_SobelY_blue, cv.COLOR_BGR2RGB)), plt.title('Filtro Sobel Y - BLUE', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])

plt.subplot(456), plt.imshow(theRock), plt.title('Original', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(457), plt.imshow(cv.cvtColor(green, cv.COLOR_BGR2RGB)), plt.title('Canal Verde', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(458), plt.imshow(cv.cvtColor(theRock_Laplacian_green, cv.COLOR_BGR2RGB)), plt.title('Filto Laplaciano - GREEN', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(459), plt.imshow(cv.cvtColor(theRock_SobelX_green, cv.COLOR_BGR2RGB)), plt.title('Filtro Sobel X - GREEN', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,10), plt.imshow(cv.cvtColor(theRock_SobelY_green, cv.COLOR_BGR2RGB)), plt.title('Filtro Sobel Y - GREEN', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])

plt.subplot(4,5,11), plt.imshow(theRock), plt.title('Original', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,12), plt.imshow(cv.cvtColor(red, cv.COLOR_BGR2RGB)), plt.title('Canal Vermelho', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,13), plt.imshow(cv.cvtColor(theRock_Laplacian_red, cv.COLOR_BGR2RGB)), plt.title('Filto Laplaciano - RED', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,14), plt.imshow(cv.cvtColor(theRock_SobelX_red, cv.COLOR_BGR2RGB)), plt.title('Filtro Sobel X - RED', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])
plt.subplot(4,5,15), plt.imshow(cv.cvtColor(theRock_SobelY_red, cv.COLOR_BGR2RGB)), plt.title('Filtro Sobel Y - RED', y=-0.21, fontsize=10)
plt.xticks([]), plt.yticks([])

plt.suptitle("Filtros de Passa Alta", fontsize=20)

final = plt.gcf()

final.set_size_inches(13, 7)

plt.savefig("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana3/Exercício2/Filtros_Passa_Alta.png", dpi=199)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()