import json
import requests


def main():
    cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL")
    cotacoes_moedas = cotacoes.json()
    # print(cotacoes)
    libra = cotacoes_moedas['GBPBRL']
    dolar = cotacoes_moedas['USDBRL']
    euro = cotacoes_moedas['EURBRL']
    print("MUDANDO O PARAMETRO")
    print("LIBRA: ", libra['bid'])
    print("DÓLAR: ", dolar['bid'])
    print("EURO: ", euro['bid'])
    # bid é o chave para o valor atual do dólar
    # print("POR ACESSO A CHAVE DO JSON()")
    # print(libra['name'], libra['bid'])
    # print(dolar['name'], dolar['bid'])
    # print(euro['name'], euro['bid'])
    print("--------------------------------")
    # bid é a chave para o valor atual do dólar
    # libra_ = cotacoes_moedas['GBPBRL']['bid']
    # dolar_ = cotacoes_moedas['USDBRL']['bid']
    # euro_ = cotacoes_moedas['EURBRL']['bid']
    # print("UTILIZANDO f strings")
    # print(f'Euro: {euro_}')
    # print(f'Dólar Americano {dolar_}')
    # print(f'Libra Esterlina {libra_}')
    print("--------------------------------")


if __name__ == "__main__":
    main()

