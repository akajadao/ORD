def leia_reg(file):
    tam_bytes = file.read(2)
    # converte os bytes para inteiro
    tam = int.from_bytes(tam_bytes)
    if tam > 0:
        # armazena no buffer o texto do tamanho dos bytes
        buffer = file.read(tam)
        # transforma numa string
        buffer = buffer.decode()
        return buffer
    else:
        return ''

def main():
    nomeArq = input(f'Digite o nome do arquivo a ser lido em modo binário:\n>>> ')
    try:
        with open(nomeArq, 'rb') as file:
            chave = input('Digite o sobrenome a ser encontrado:\n>>> ')
            find = False
            reg = leia_reg(file)
            i = 1
            while (reg != '') and (find == False):
                sobrenome = reg.split(sep='|')[0]
                if sobrenome == chave:
                    find = True
                else:
                    reg = leia_reg(file)
            if find:
                for item in reg.split(sep='|'):
                    if item:
                        print(f'CAMPO {i}: {item}')
                        i += 1
            else:
                Exception(f'Sobrenome não foi encontrado no arquivo!')

    except:
         FileNotFoundError(f'Arquivo não encontrado ou não existe!')

if __name__ == '__main__':
    main()