import pandas as pd


def main():

    abrirplanilha = pd.read_excel(r"bloco_de_dados.xlsx")

    dados_filtrados = abrirplanilha['Idade'] > 20
    print("DADOS DA PLANILHA")
    print(abrirplanilha)

    print("Dados filtrados")
    print(abrirplanilha[dados_filtrados])

if __name__ == "__main__":
    main()
