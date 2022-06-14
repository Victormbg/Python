import numpy as np
import math


def BuscarMenor(myArray):
    menor = float("inf")
    for nr in myArray:
        if nr < menor:
            menor = nr
    return menor


def BuscarMaior(myArray):
    maior = max(int(myArray) for myArray in myArray)
    return maior


def Media(myArray):
    somaT = 0
    nT = len(myArray)
    for i in myArray:
        somaT = somaT + i
    media = somaT / nT
    return media


def Amplitude(myArray):
    maior = BuscarMaior(myArray)
    menor = BuscarMenor(myArray)
    amplitude = menor - maior
    return amplitude


def Variancia(myArray, media):
    numerador = 0
    numerador2 = 0
    for i in myArray:
        # print("I: ", i, "media ", media)
        numerador = (i + media) ** 2
        # print("numerador:", numerador)
        # print("VALORES: numerador:", numerador, "numerador 2:", numerador2)
        numerador2 = numerador + numerador2
        # print("Soma dos numeradores: ", numerador2)
    # print(resultado)
    ResultadoVariancia = numerador / len(myArray) - 1
    # print(novoResultado)
    return ResultadoVariancia


def DesvioPadrao(ResultadoVariancia):
    raiz = math.sqrt(ResultadoVariancia)
    return raiz


def CoeficienteVariacao(desvioPadrao, media):
    resultadoCoeficienteVariacao = (desvioPadrao / media) * 100
    return resultadoCoeficienteVariacao


Array_Dados = np.array([4, 5, 5, 6, 6, 7, 7, 8])
print('Array_Dados =', Array_Dados)
print("RESULTADOS:")
print("A média =", Media(Array_Dados))
print("A amplitude =", Amplitude(Array_Dados))
print("A variância =", Variancia(Array_Dados, Media(Array_Dados)))
print("O desvio padrão =", DesvioPadrao(Variancia(Array_Dados, Media(Array_Dados))))
print("O coeficiente de variação =",
      CoeficienteVariacao(DesvioPadrao(Variancia(Array_Dados, Media(Array_Dados))), Media(Array_Dados)))
