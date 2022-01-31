import json

carros_json = '{"Marca":"honda", ' \
              '"modelo":"HRV",' \
              '"cor":"prata"}'

carros = json.loads(carros_json)
#print(carros["Marca"])
# for meu_carro in carros:
#     print(meu_carro)

# for meu_carro in carros.values():
#     print(meu_carro)

for chaves, valores in carros.items():
    print(chaves + " - " +  valores)
