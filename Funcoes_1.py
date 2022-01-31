def mensagem():
    print("Lúcio Marlon")
mensagem()


def mensagem2(texto):
    print(texto)

mensagem2("Priscila Aparecida Gomes")
mensagem2("Lúcio Marlon Oliveira de Sousa")


def soma(a, b, c):
    print(a + b + c)

# soma(1, 2, 3)
# soma(2, 5 ,6)

def operacao(a, b):
    '''

    :param a:
    :param b:
    :return:
    '''
    return a + b

r = operacao(5, 6)
print(f'O resultado da some é: {r}')

def calculo_energia_potencial(m, h, g = 10):
    energia = g * m *  h
    return energia

energia = calculo_energia_potencial(30, 12, 9.8)
print(f'{energia} Joules')