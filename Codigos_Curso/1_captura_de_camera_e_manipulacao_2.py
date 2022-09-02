"""
---------------------------------------------------------------------------------------------
Construa um programa em OpenCV que faça o seguinte:

1. Capture um quadro do vídeo de uma webcam;

2. Exiba em janelas diferentes versões do quadro:
a) em níveis de cinza;
b) em vermelho;
c) em verde;
d) em azul;

3. Salve o quadro original capturado e os quadros modificados como imagens em extensão PNG.

* Lembre-se de sempre liberar os recursos ao final.
---------------------------------------------------------------------------------------------
"""

# Primeiro de tudo devo importar as bibliotecas necessárias: numpy (np) e opencv-phyton (cv2):
import numpy as np
import cv2

# Inicializando a captura de vídeo a partir da webcam padrão (0) do meu notebook:
webCam = cv2.VideoCapture(0)

# Verificando se a abertura da webcam funcionou corretamente:
if webCam.isOpened():
    print("Conected!")

    # Ciclo While que vai rodar infinitamente enquanto o valor for True e vai parar apenas quando uma tecla de apoio for pressionada:
    while True:

    # O parâmetro .read gera duas informações, um valor booleano (T/F) e uma lista, então criei duas variáveis para receber o valor de leitura da webcam:
    # ret => valor booleano que representa o retorno do webCam.read(), se der certo retorna True;
    # frame => lista de pixels da webcam, ou seja, representação matricial da imagem que a webcam está lendo;
        ret, frame = webCam.read()

    # Exibindo a imagem original que a webcam está reproduzindo:
        cv2.imshow('Original', frame)

    # Convertendo e exibindo a imagem da webcam para a escala de cinza:
        cv2.imshow('Gray', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

    # Divisão dos canais de cores BGR na imagem mostrada pela webcam, eles se dividem em 3 novos arrays para cada cor separada:
        (blue, green, red) = cv2.split(frame)

    # Exibindo a imagem que a webcam está reproduzindo isolando o canal de cor azul:
        cv2.imshow('Blue', blue)

    # Exibindo a imagem que a webcam está reproduzindo isolando o canal de cor verde:
        cv2.imshow('Green', green)

    # Exibindo a imagem que a webcam está reproduzindo isolando o canal de cor vermelha:
        cv2.imshow('Red', red)

    # Se a tecla 27 (ESC) for pressionada, um 'break' é acionado e o programa saí do ciclo:
        if cv2.waitKey(1) == 27:
            break

    # Criar arquivo com a imagem original:
    cv2.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana2/Exercicio1/2_webCam_Original.png", frame)

    # Criar arquivo com a imagem em escala de cinza:
    cv2.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana2/Exercicio1/2_webCam_Gray.png", cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

    # Criar arquivo da imagem apenas com o canal de cor azul:
    cv2.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana2/Exercicio1/2_webCam_Blue.png", blue)

    # Criar arquivo da imagem apenas com o canal de cor verde:
    cv2.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana2/Exercicio1/2_webCam_Green.png", green)

    # Criar arquivo da imagem apenas com o canal de cor vermelha:
    cv2.imwrite("C:/Users/enior/Desktop/Github/EC_UFPE/PET_Visao_Computacional/imagens/Semana2/Exercicio1/2_webCam_Red.png", red)

# Encerrando a conexão com a webcam:
webCam.release()

# Garantia de que as janelas abertas pelo programa serão fechadas:
cv2.destroyAllWindows()