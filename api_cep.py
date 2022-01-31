import json, requests

def main():
    try:
        digitacep = input("Digite o cep: ")
        informa_cep = requests.get(f'https://cep.awesomeapi.com.br/json/{digitacep}')
        informacep = informa_cep.json()
        #print(informacep)
        print("----------------------------------")
        print(informacep['address'])
        print("BAIRRO: ", informacep['district'])
        print("CIDADE: ", informacep['city'])
        print("ESTADO: ", informacep['state'])
        print("Cep: ", informacep['cep'])
        print("DDD: ", informacep['ddd'])
        print("----------------------------------")
        # cep = informacep['cep']
        # print(f'CEP: {cep}')

        # devolve_cep = json.dumps(informacep, sort_keys=True, indent=2, ensure_ascii=False, separators=(":", " => "))
        # print(devolve_cep)

        #imprimir as chaves
        # for chaves in informacep:
        #     print(chaves)

        #imprimir os itens das chaves
        # for itens in informacep.items():
        #     print(itens)

        #imprimir os valores das chaves
        # for valores_da_consulta in informacep.values():
        #     print(valores_da_consulta)


    except:
        print("Valor inválido ou cep inexistente")


if __name__ == "__main__":
    main()