colecao = {'Opala': 1, 'Caminhão': 10, 'Moto': 0.5, 'Submarino': 1500, 'tanque': 120, 'satélite': 60}
# incluir_nome = input("Digite um nome para a coleção: ")
# incluir_chave = int(input("Digite o número: "))
# colecao[incluir_nome] = incluir_chave

for colecao, massa in colecao.items():
    print(f'Veículo: {colecao}      \t massa dos veiculos: {massa} . Em toneladas')

