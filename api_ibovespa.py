import pandas as pd # Para evitar escrever pandas e trocar pela escrita apenas de pd para facilitar
from pandas_datareader import data as web # Evita a escrita do data e troca pelo web
import matplotlib.pyplot as plt

#indice
df = web.DataReader(f'^BVSP', data_source='yahoo', start=f'20-10-2021', end='10-26-2021')
# display(df) #usando no jupyter notebook
print(df)
df["Adj Close"].plot(figsize=(15, 10))
plt.show()

#PETR4
df = web.DataReader(f'PETR4.SA', data_source='yahoo', start=f'20-10-2021', end='10-26-2021')
# display(df) #usado no jupyter
print(df)
df["Adj Close"].plot(figsize=(15, 10))
plt.show()