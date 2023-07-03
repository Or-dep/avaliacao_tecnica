import pandas as pd
from unidecode import unidecode

tab = pd.read_csv('./Parte_03/base.csv', delimiter=",")
formatado = []
tabela = tab.copy()
campos = ['nome','e-mail']
com = ".com"
br = ".com.br"
def formatar(name):
    nome = unidecode(name.strip().lower().replace("'", ""))
    #unicode() substitui todos os caracteres especiais
    #.split() remover espaços em branco no começo e no fim
    #.lower() transforma todos os caracteres em maiúsculos
    #.replace("'", "")
    return nome

for campo in campos:
    for nm in tab[campo]: # Formatando colunas 
        formatado.append(formatar(nm))
    tabela[campo] = formatado
    formatado = []

for validar in tabela['e-mail']: # Analisando e-mails
    if "@" in validar:
        if validar[-len(com):] == com or validar[-len(br):] == br:
            formatado.append(True)
        else:
            formatado.append(False)
    elif "@" not in validar:
        formatado.append(False)

tabela['valido'] = formatado # Criando nova coluna

tabela.to_csv('./Parte_03/03_Base.csv')
# cria novo arquivo formatado Com nome 03_Base_Formatada.csv

#print(tabela)