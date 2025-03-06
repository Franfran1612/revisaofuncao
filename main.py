from utils.math_utils import *
#esse é pra vc digitar em baixo quando vc botar pra roda
ano_atual = int(input('Digite seu ano atual: '))
ano_nasc = int(input('Digite seu ano de nascimento: '))
print(ano_atual - ano_nasc)


def kelin(celsius):
    """
    calcula o kelin conforme a temperatura em celsius
    :param celsius: a temperatura em celsius
    :return:transforma temperatura em celsius em Kelin
    """
    kelin = celsius + 273.15
    return kelin

def fahrente(celsius):
    """
    calcula o fahrente conforme a temperatura em celsius
    :param celsius: a temperatura em celsius
    :return: transforma temperatura em celsius em Fahrente
    """
    fahrente = celsius * 1.8 + 32
    return fahrente

def menu_calculadora():
    print("calculadora")
    print("1 - soma\n2 - subtração\n3- multiplicação\n4 - divisão\n5 - todas as contas")


def soma(numero1, numero2):
    return numero1 + numero2
def subtracao(numero1, numero2):
    return numero1 - numero2
def multiplicacao(numero1, numero2):
    return numero1 * numero2
def divisao(numero1, numero2):
    return numero1 / numero2


def escolhas(escolha,numero1, numero2):
    if escolha == 1:
        print("soma", soma(numero1, numero2))
    elif escolha == 2:
        print("subtração", subtracao(numero1, numero2))
    elif escolha == 3:
        print("multiplicação", multiplicacao(numero1, numero2))
    elif escolha == 4:
        print("divisao", divisao(numero1, numero2))
    else:
        print("escolha invalida")


def imc(altura1, peso1):
    return peso1 / (altura1 * altura1)

celsius = int(input("Digite o valor da celsius: "))
print("O valor em Kelvin é", kelin(celsius=celsius))
print("O valor em fahrent é", fahrente(celsius=celsius))


numero1 = int(input("Digite o primeito numero: "))
numero2 = int(input("Digite o segundo numero: "))
menu_calculadora()
escolha = int(input("digite sua escolha: "))
escolhas(escolha=escolha,numero1=numero1, numero2=numero2)


peso1 = float(input("Digite o primeito peso: "))
altura1 = float(input("Digite sua altura: "))

print("Seu IMC é", imc(peso1=peso1, altura1=altura1))
