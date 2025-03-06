def calcula_idade(ano_atual, ano_nascimento):
   """
    calcula idade de conforme o ano  e o ano de nacismento.
    :param ano_atual: O ano atual.
    :param ano_nascimento: O ano de nascimento.
    :return: A idade de conforme o ano de nascimento.
  """
   idade = ano_atual - ano_nascimento
   return idade
 #return  ano_atual - ano_nascimento    OU

###################################################################

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
#################################################################################################
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

