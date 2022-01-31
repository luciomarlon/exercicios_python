import json
import requests
import datetime
import time


# moeda = input("Digite a moeda: ")
# cotacoes = requests.get(f'http://economia.awesomeapi.com.br/json/last/{moeda}')
#
#
# with open("cotacao_moedav3.json", "w") as moedas:
#     periodo_cotacao = cotacoes.json()
#     arquivo_salvo = json.dump(periodo_cotacao,moedas)


 # ALGORITMO A CONVERTER O DICIONÁRIO {} PARA LISTA []
# with open("cotacao_moedav3.json", 'r') as abrir:
#     for moedas in abrir:
#         carregar_info = json.loads(moedas)
#         for info_moedas in carregar_info:
#             moeda_carregada = info_moedas['USDBRL']
#             print("Moeda convertida:\t", moeda_carregada['name'])
#             print("Fechamento:      \t", moeda_carregada['bid'])
#             print("Alta:            \t", moeda_carregada['high'])
#             print("Baixa:           \t", moeda_carregada['low'])
#             print("Taxa variação:   \t", moeda_carregada['varBid'])
#             # tempo = moeda_carregada['timestamp']
#             tempo_convertido = time.gmtime()
#             print("Data da consulta: \t", time.strftime("%Y-%m-%d %H:%M:%S", tempo_convertido))

print("=============================================")
print("=============================================")
#ALGORITMO B, OS DICIONÁRIO NÃO POSSUI UMA CHAVE PRINCIPAL
with open("cotacao_moedav2.json", 'r') as abrir:
    for linhas in abrir:
        carrega_moeda = json.loads(linhas)
        for moeda in carrega_moeda:
            print("Moeda convertida:\t", moeda['name'])
            print("Código da moeda: \t", moeda['code'])
            print("Valor atual:     \t", moeda['bid'])
            print("Valor alta:      \t", moeda['high'])
            print("Valor baixa:     \t", moeda['low'])
            print("Taxa variação:   \t", moeda['varBid'])
            #tempo = moeda['timestamp']
            tempo_convertido = time.gmtime()
            print("Data da consulta: \t", time.strftime("%Y-%m-%d %H:%M:%S", tempo_convertido))