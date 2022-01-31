import json

carros_dicionario = {"Marca":"honda", "modelo":"HRV","cor":"prata"}

#dicionário -> objeto JSON

carros_lista = ["Honda", "BMW", "FORD", "GENERAL MOTORS", "FIAT"]
#lista -> array JSON

carros_tupla = ("Renault", "Citroen", "Hyundai", "Subaru")
#tupla ->array JSON

carros_jd = json.dumps(carros_dicionario)
print(carros_jd)
# convertendo para dicionário
print("-------------------------------------------------------------")

carros_jl = json.dumps(carros_lista)
print(carros_jl)

print("-------------------------------------------------------------")
carros_jt = json.dumps(carros_tupla)
print(carros_jt)
#
#
# for carros, cars in carros_dicionario.items():
#         print(f'{carros} e {cars}')


