import os
def main():
    nomeArq = input(f'Digite o nome do arquivo a ser lido:\n>>> ')
    if os.path.exists(nomeArq):
        Arq = open(nomeArq, 'r+b')
        Arq.seek(0)
        TotalReg = int.from_bytes(Arq.read(4))
    else:
        Arq = open(nomeArq, 'w+b')
        # Se o arquivo não existe, inicializa TOTAL_REG como 0
        TotalReg = 0
        # Escreve TOTAL_REG no arquivo
        Arq.write(TotalReg.to_bytes(4))

    while option < 3:
        if option == 1:
            Reg = input("Digite todos os campos do registro: ").encode().ljust(64, b'\0')
            Offset = TotalReg*64+4
            Arq.seek(Offset)
            Arq.write(Reg)
            TotalReg += 1
            Arq.seek(0)
            Arq.write(TotalReg.to_bytes(4))
        
        elif option == 2:
            Offset = RRN

    except:
        FileNotFoundError



if __name__ == '__main__':
    main()