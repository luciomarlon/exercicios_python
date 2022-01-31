import json, requests

def main():
    try:
        uf = input("Digite um estado: ").upper()
        cidade = input("Digite uma cidade: ").upper()
        rua = input("Digite um endereço: ").upper()

        informa_via_cep = requests.get(f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/')
        via_cep = informa_via_cep.json()

        # devolve_cep = json.dumps(via_cep, sort_keys=True, indent=2, ensure_ascii=False, separators=(":"," => "))
        devolve_cep = json.dumps(via_cep, sort_keys=True, indent=2, ensure_ascii=False, separators=("\t","\t:"))
        print(devolve_cep)

    except:
        print("Valor inválido ou cep inexistente")

if __name__ == "__main__":
    main()
