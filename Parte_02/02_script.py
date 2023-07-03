def lista_enc(vl,lista): # 1 - Função
    while True:
        try: # 2 - Conversão
            lt_enc = [int(x) for x in lista]
        except:
            lt_enc = lista
        if len(lista) == vl: # 3 - Verificação
            reversa = []
            for n in range(vl-1, -1, -1): # 4 - Logica da lista encadeada reversa
                reversa.append(lt_enc[n])
            return reversa
        else:
            print(f'o valor numerico atual é de {vl}, está correto?\nA lista encadeada atual é de {lt_enc} contendo {len(lt_enc)} itens no total')
            while True:
                corrigir = int(input(f'Digite 1 para corrigir o valor Numerico: \nOu Digite 2 para corrigir a lista encadeada: '))
                if corrigir == 1:
                    vl = int(input('Digite o valor correto: '))
                    break
                elif corrigir == 2:
                    lista = input('Digite a lista corretamente: ')
                    break
                else:
                    print('Esse valor não é valido!')
    
N_el = int(input('quantidade de itens:'))
lt = input('digite a lista encadeada:').split(','or';')

print(lista_enc(N_el,lt))