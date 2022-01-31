import json
import requests

#cotação de moedas a cada 30 segundos
def main():


    #################################################################################################
    cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL")
    cotacoes_moedas = cotacoes.json()
    # print(cotacoes_moedas)
    libra = cotacoes_moedas['GBPBRL']
    dolar = cotacoes_moedas['USDBRL']
    euro = cotacoes_moedas['EURBRL']
    print("MUDANDO O PARAMETRO")
    print("LIBRA: ", libra['bid'])
    print("DÓLAR: ", dolar['bid'])
    print("EURO: ", euro['bid'])
    #################################################################################################
if __name__ == "__main__":
    main()

