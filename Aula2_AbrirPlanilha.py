import pandas as pd


def main():

    # abrirplanilha = pd.read_excel(r"bloco_de_dados.xlsx")
    abrirplanilha2 = pd.read_excel('bloco_de_dados.xlsx', sheet_name='Planilha2')


    print(abrirplanilha2)

if __name__ == "__main__":
    main()
