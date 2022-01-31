import json
import requests
import pandas as pd

def main():

    moeda = input("Digite a moeda: ")
    cotacoes = requests.get(f'http://economia.awesomeapi.com.br/json/last/{moeda}')
    cotacoes_moedas = cotacoes.json()
    print(cotacoes.json())

    # cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    # cotacoes_moedas = cotacoes.json()
    # print(cotacoes_moedas)

    # libra = cotacoes_moedas['GBPBRL']
    # dolar = cotacoes_moedas['USDBRL']
    # euro = cotacoes_moedas['EURBRL']
    # print("MUDANDO O PARAMETRO")
    # print("LIBRA: ", libra['bid'])
    # print("DÓLAR: ", dolar['bid'])
    # print("EURO: ", euro['bid'])

    gravar_cotacao = pd.DataFrame(data=cotacoes_moedas)
    # print(bloco_de_dados)
    gravar_cotacao.to_excel('cotacoes_moedas.xlsx', sheet_name='Cotação Dolar', na_rep='#N/A', header=True, index=True)

    ler_cotacao = pd.read_excel(r'cotacoes_moedas.xlsx')
    print(ler_cotacao['USDBRL'][1])
    print(ler_cotacao['USDBRL'][3])
    print(ler_cotacao['USDBRL'][5])
    print(ler_cotacao['USDBRL'][6])
    print(ler_cotacao['USDBRL'][7])
    print(ler_cotacao['USDBRL'][8])
    print(ler_cotacao['USDBRL'][10])


    # libra = cotacoes_moedas['GBPBRL']
    # dolar = cotacoes_moedas['USDBRL']
    # euro = cotacoes_moedas['EURBRL']
    # print("MUDANDO O PARAMETRO")
    # print("LIBRA: ", libra['bid'])
    # print("DÓLAR: ", dolar['bid'])
    # print("EURO: ", euro['bid'])
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

