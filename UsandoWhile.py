# numero = 0
# while numero <=6:
#     print(numero)
#     numero +=1;
# print("===================")
# numero2 = 5
# while numero > 0:
#     print(numero)
#     numero -=1;

#somando
# soma = 0
# numero = 1
# while numero < 6:
#     soma += numero
#     numero += 1
# print(soma)

#validando
numero = -1
while numero <  1 or numero > 10:
    numero = int(input("Digite um numero entre 1 e 10: "))    
    if numero <= 10:
        print(f'voce digitou um numero correto: {numero}')