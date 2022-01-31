import pandas as pd


def main():

    dados = {'Nome': ['Lucio','Samira','Gabriel','Marcelo'], 'Idade':[44, 19, 18, 28], 'Altura':[1.83, 1.60, 1.80, 2.00]}
    bloco_de_dados = pd.DataFrame(data=dados)
    print(bloco_de_dados)
    bloco_de_dados.to_excel('bloco_de_dados.xlsx', index=False)

if __name__ == "__main__":
    main()
