import pandas as pd
import numpy as np

#abrir arquivo com o nome planilha especificada através do parâmetro sheet_name = 'Nome da planilha'
dados = pd.read_excel('bloco_de_dados.xlsx', sheet_name='Planilha2')

#usecols: permite visualização apenas as colunas especificas

# dados = pd.read_excel('bloco_de_dados.xlsx', sheet_name='Planilha2', usecols=['Nome','altura'])

# dados2 = pd.read_excel('bloco_de_dados.xlsx', sheet_name='Sheet1')

# dados2 = pd.read_excel('bloco_de_dados.xlsx', sheet_name='Sheet1', usecols=['Nome','Idade'])

print(dados)
# print(dados2)

#gravando no arquivo, use index = False para elimina colunas com indices
dados.to_excel('arquivo.xlsx', sheet_name='Planilha1', na_rep='#N/A', header=True, index=False)
# dados2.to_excel('arquivo.xlsx', sheet_name='Planilha2', header=True, index=False)

