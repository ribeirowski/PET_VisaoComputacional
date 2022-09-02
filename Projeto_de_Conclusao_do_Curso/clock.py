import numpy as np
import cv2 as cv
import time

def horario():
    agora = time.ctime()
    return agora

# Função para pegar a data de hoje
def data(dados):
    ano = dados[0]
    mes = dados[1]
    dia = dados[2]
    data = str(dia) + "-" + str(mes) + "-" + str(ano)
    return data

# Função para pegar as horas atuais
def hora(dados):
    horas = dados[3]
    min = dados[4]
    seg = dados[5]
    horario = str(horas) + "-" + str(min) + "-" + str(seg)
    return horario
