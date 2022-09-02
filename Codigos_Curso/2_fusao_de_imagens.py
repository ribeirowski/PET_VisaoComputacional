"""
---------------------------------------------------------------------------------------------
Construa um programa em Opencv2 que faça o seguinte:

1. Abra duas imagens diferentes: a imagem de uma pessoa (pode ser a sua foto) e
a de um objeto ou de um animal. Essas imagens precisam ter o mesmo tamanho
(resolução em termos de linhas e colunas).

2. Usando a função de blending do Opencv2, gere outra imagem resultante da fusão de imagens,
variando os pesos da imagem da pessoa e a segunda imagem. Faça a constante igual a zero e
defina o peso da segunda imagem como sendo 1 menos o peso da imagem da pessoa.

3. Agora use uma trackbar para capturar o peso da imagem da pessoa e exibir em tempo real
a imagem resultante da fusão. Perceba como uma imagem vai se tornando a outra.

4. Salve o quadro original capturado e os quadros modificados como imagens em extensão PNG.

* Lembre-se de sempre liberar os recursos ao final.
---------------------------------------------------------------------------------------------
"""
# Primeiramente devo importar a biblioteca do opencv-python (cv2):
import cv2


# Criando a função responsável pela alteração do peso da imagem 1 (enio), o que também altera o peso da imagem 2 (otto):
def on_trackbar(valor):
    peso_enio = valor / 10
    peso_otto = (1.0 - peso_enio)

    # Definindo a fusão das imagens através da função cv2.addWeighted (informando as imagens, os pesos e o gama):
    blend = cv2.addWeighted(enio, peso_enio, otto, peso_otto, 0)

    # Exibindo a imagem fundida em tempo real:
    cv2.imshow("Eniotto", blend)

    # Criar arquivo para cada imagem gerada (as imagens Eniotto0.png e Eniotto10.png são as imagens originais):
    cv2.imwrite(f"C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana2/Exercicio2/Eniotto{valor}.png", blend)


# Fazendo a leitura das imagens que estão no meu arquivo:
enio = cv2.imread("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/enio.jpg", 1)
otto = cv2.imread("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/otto.jpg", 1)

# Para criar uma trackbar, primeiro tenho que definir o nome da janela em que ele será criado:
cv2.namedWindow("Eniotto")

# Agora criei uma trackbar que vai de 0 até 100... preenchi todos os parâmetros da função:
cv2.createTrackbar("Alpha", "Eniotto", 0, 10, on_trackbar)

# Inicializar a trackbar no 0 (começo da barra):
on_trackbar(0)

# Esperamos alguma tecla ser pressionada para encerrar o programa e destruir qualquer janela que tenha ficado aberta:
if cv2.waitKey() == 0:
    cv2.destroyAllWindows()
