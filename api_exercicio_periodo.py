import json
import requests
import datetime
import time

#busca a cotação diária do dólar
print("FECHAMENTO DOS ULTIMOS DIAS")
periodo = input("Digite o período: ")

cotacao = requests.get(f"https://economia.awesomeapi.com.br/json/daily/GBP-BRL/{periodo}")

# print(devolver_dias)

#fatia os valores dentro da linha
# devolver_dias = json.loads(cotacao.content); # content
# for dolar in devolver_dias:
#     converter = dolar['bid']
#     tempo = dolar['timestamp']
#     tempo_convertido = time.gmtime()
#     print("Dólar: ", converter, " ==== " ,"Data da consulta: ", time.strftime("%Y-%m-%d %H:%M:%S", tempo_convertido))

with open("cotacao_moedav3.json", "w") as dolar:
    periodo_cotacao = cotacao.json()
    json.dump(periodo_cotacao, dolar)
    # devolver_dias = json.dumps(periodo_cotacao, sort_keys=True, indent=4, ensure_ascii=False)
    # json.dump(devolver_dias, dolar)

# with open("cotacao_moeda.json", "r") as ler_dolar:
#     carrega_moeda = json.load(ler_dolar)
#     print(carrega_moeda)

# with open("cotacao_moedav2.json", "w") as dolar:
#     periodo_cotacao = cotacao.json()
#     json.dump(periodo_cotacao, dolar)

# with open("cotacao_moedav3.json", "r") as ler_dolar:
#     carrega_moeda = json.loads(ler_dolar)
#     # print(carrega_moeda)
#     for dolar in carrega_moeda:
#         print(dolar['bid'])


