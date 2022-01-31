import pandas as pd
import matplotlib.pyplot as plt


def main():

    planilha = pd.read_excel(r"pessoas.xlsx")
    print(planilha)

    # plt.plot(planilha['Idade'])
    # plt.hist(planilha['Idade'], bins = 20) #histograma
    #plt.pie(planilha['Idade'], labels=planilha['Nome'], autopct='%1.2f%%')
    #plt.show()
    #platando as quantidades das idades usando pandas e matplotlib
    planilha.groupby(['Idade']).Idade.count().sort_values()[-7:].plot(kind = "pie",
                                                                        autopct = '%1.2f%%',
                                                                        figsize=(5,5),
                                                                        label = 'Idades por Pessoas');
    plt.show()

if __name__ == "__main__":
    main()
