
def velocidade():
    tempo = float(input("Digite Tempo: "))
    velocidade = float(input("Digite velocidade: "))
    distancia = tempo * velocidade
    litros_usados = distancia / 12.0
    print(f'Foi gasto em gasolina: {litros_usados}')
velocidade()

def distancia(tempo, velocidade):
    distancia = float(tempo) * float(velocidade)
    print(f'A distancia é: {distancia}')
distancia(30, 80)

def litros(tempo, velocidade):
    distancia = float(tempo) * float(velocidade)
    litros_usados = distancia / 12.0
    return litros_usados
litros2 = litros(30, 100)
print(f'Os litros gastos foram: {litros2}')

def distancia_litros(tempo = 30, velocidade = 100):
    distancia = float(tempo) * float(velocidade)
    litros_usados = distancia / 12.0
    print(f'Os litros gastos foram: {litros_usados}')
    print(f'A distancia calculada: {distancia}')
distancia_litros()

