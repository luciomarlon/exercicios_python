import json
import requests
import time
import pandas as pd


#cotação de moedas a cada 30 segundos
def main():
    try:
        moeda = input("Digite a moeda: ")

        cotacoes = requests.get(f'http://economia.awesomeapi.com.br/json/last/{moeda}')
        cotacoes_moedas = cotacoes.json()
        # print(cotacoes_moedas)

        if moeda == "usd-brl" or moeda == "USD-BRL":
            dolar = cotacoes_moedas['USDBRL']
            # tempo = time.gmtime()
            # print("DÓLAR: ", dolar['bid'],
            #       "\nHorario", dolar['create_date'],
            #       "\nAGORA: ", time.strftime("%Y-%m-%d %H:%M:%S", tempo))
            tempo = time.gmtime()
            print(dolar['name'],": ", dolar['bid'],
                  "\nHorario", dolar['create_date'],
                  "\nAlta: ", dolar['high'],
                  "\nBaixa: ", dolar['low'],
                  "\nVariação: ", dolar['pctChange'])

        elif moeda == "eur-brl" or moeda == "EUR-BRL":
            euro = cotacoes_moedas['EURBRL']
            print(euro['name'],": ", euro['bid'],
                  "\nHorario", euro['create_date'],
                  "\nAlta: ", euro['high'],
                  "\nBaixa: ", euro['low'],
                  "\nVariação: ", euro['pctChange'])

        elif moeda == "gbp-brl" or moeda == "GBP-BRL":
            libra = cotacoes_moedas['GBPBRL']
            print(libra['name'],": ",libra['bid'],
                  "\nHorario", libra['create_date'],
                  "\nAlta: ", libra['high'],
                  "\nBaixa: ", libra['low'],
                  "\nVariação: ", libra['pctChange'])

        elif moeda == "cad-brl" or moeda == "CAD-BRL":
            dolar_canadense = cotacoes_moedas['CADBRL']
            print(dolar_canadense['name'],": ", dolar_canadense['bid'],
                  "\nHorario", dolar_canadense['create_date'],
                  "\nAlta: ", dolar_canadense['high'],
                  "\nBaixa: ", dolar_canadense['low'],
                  "\nVariação: ", dolar_canadense['pctChange'])

        elif moeda == "btc-brl" or moeda == "BTC-BRL":
            bitcoin = cotacoes_moedas['BTCBRL']
            print(bitcoin['name'],": ", bitcoin['bid'],
                  "\nHorario:", bitcoin['create_date'],
                  "\nAlta:", bitcoin['high'],
                  "\nBaixa:", bitcoin['low'],
                  "\nVariação:", bitcoin['pctChange'])


    except:
        print("Valor invalido ou ocorreu um erro")

if __name__ == "__main__":
    main()

