

# def temperatura():
#     celsius = float(input("Digite temperatura em graus Célsius: "))
#     F = (9 * celsius + 160)/5
#     print(F)
# temperatura()
#
# def temperatura(celsius):
#     print((9 * celsius + 160) / 5)
# temperatura(20)
#
# def temperatura(celsius):
#     F = (9 * celsius + 160) / 5
#     return F
#
# F = temperatura(20)
# print(F)

def temperatura():
    celsius = float(input("Digite temperatura em graus Célsius: "))
    return celsius

def temperatura_celsius(celsius):
    temperatura = (9 * celsius + 160) / 5
    return temperatura

def temperatura_celsius2(temperatura):
    print(temperatura)

recebe = temperatura()
recebe2 = temperatura_celsius(recebe)
temperatura_celsius2(recebe2)



