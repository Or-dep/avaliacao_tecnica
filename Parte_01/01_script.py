import pandas as pd # importa a biblioteca pandas

tb01 = pd.read_csv('./Parte_01/cadastro.csv', delimiter=";") # faz a leitura do arquivo
tb02 = pd.read_csv('./Parte_01/vendas.csv', delimiter=";")

ind = tb01.copy()
gastos = {}
valores = []
total = {}

for ids in tb01['cod_cadastro']: #percorre a coluna
    gastos[ids] = tb02['valor'].loc[tb02['cod_cadastro']==ids].sum()
        #soma os valores correspondentes ao ids e adiciona no dicionario
    valores.append(tb02['valor'].loc[tb02['cod_cadastro']==ids].sum())
        #soma os valores correspondentes ao ids e adiciona em lista

ind['gasto'] = valores # Adiciona coluna de gastos

for local in ind['reg_procedencia']:
    total[local] = ind['gasto'].loc[ind['reg_procedencia']==local].sum()
    
maior = max(gastos.values())# separando o maior gasto
id_maior = max(gastos, key=gastos.get)# pegando a chave de quem gasta mais

menor = min(gastos.values())# separando o menor gasto
id_menor = min(gastos, key=gastos.get)# pegando a chave de quem gasta menos

rg_vl = max(total.values())# separando o maior valor de gasto regional
regiao = max(total, key=total.get)# pegando a chave do local que mais gasta

produtos = tb02['produto'].value_counts()# conta a quantidade de vezes que repetiram os valores na coluna

# imprimi os resultados
print("-."*17)
print(f'O que mais gatou foi N°:{id_maior}\nNo valor total: {maior}\n',"-"*25,
f'\nO que menos gastou foi N°:{id_menor}\nNo valor total: {menor}')
print("-."*17)
print(f'A região que mais gasta é {regiao}\nNo total: {rg_vl}\n')
print("-."*17)
print(f'O produto mais vendido foi o {produtos.idxmax()}\nNa quatidade {produtos.max()}\n')
print("-."*17)
print('1 - Todos que possuem pelo menos um filho não possuem superior, que pode ser atrelado a causa de estarem em seu início de carreira, ou por conta de não se dedicarem ao seu grau de instrução.\n2 - Aqueles que possuem dois filhos não têm superior, que pode ser atrelado a causa de estarem em seu início de carreira, ou por não focar em desenvolver seu grau de instrução em médio ou superior como objetivo.\n3 - De acordo com os dados, somente 2 dos 3 que possuem 3 filhos têm o grau de instrução superior, e foram os únicos com filhos a investirem mais em seus graus de instrução.\n4 - O único que possui 5 filhos, não detém grau de instrução superior.\n')
print("-."*17)



ind['gasto'] = valores # Adiciona coluna de gastos
ind['compras'] = tb02['cod_cadastro'].value_counts(sort=False).values.tolist()

# ordenamento decrescente por colunas
compram_mais = ind.sort_values(by='compras', ascending=False)
#print(compram_mais)
gastao_mais = ind.sort_values(by='gasto', ascending=False)
#print(gastao_mais)
filhos_mais = ind.sort_values(by='num_filhos', ascending=False)
#print(filhos_mais)
Salario = ind.sort_values(by='salario', ascending=False)
#print(Salario)