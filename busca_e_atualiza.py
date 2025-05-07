import os

def main() -> None:
    nome_arq: str = input('Digite o nome do arquivo\n>>> ')
    try:
        if not os.path.exists(nome_arq):
            arq = open(nome_arq, 'w+b')
            total_reg = 0
            arq.write(total_reg.to_bytes(4))
        else:
            arq = open(nome_arq, 'r+b')
            arq.seek(0)
            total_reg = int.from_bytes(arq.read(4))
        
        choose: int = int(input('O que deseja?\n1 - Inserir\n2 - Buscar\n3 - Sair\n>>> '))
        while choose < 3 and choose > 0:
            if choose == 1:
                reg = input('Digite os campos do seu registros\n>>> ').encode().ljust(64,b'\0')
                offset = total_reg * 64 + 4
                arq.seek(offset)
                arq.write(reg)
                total_reg += 1
                arq.write(total_reg.to_bytes(4))
            
            if choose == 2:
                rrn: int = int(input('Digite qual registro deseja buscar\n>>> '))
                if rrn >= total_reg:
                    Exception('Valor do RRN maior que o número de registros!')
                else:
                    offset = rrn * 64 +4
                    arq.seek(offset)
                    reg = (arq.read(64)).decode('utf-8').split(sep='|')
                    i = 1
                    for item in reg:
                        if i <= 6:
                            print(f'CAMPO{i}: {item}')
                            i += 1
                    turn = input('Deseja alterar o registro?\ny/N?\n>>> ')
                    if turn == 'y':
                        arq.seek(offset)
                        new_reg = input('Digite os campos do seu registro:\n>>> ').encode().ljust(64,b'\0')
                        arq.write(new_reg)
            if choose == 3:
                break
            
            arq.seek(0)
            total_reg = int.from_bytes(arq.read(4))
            choose: int = int(input('O que deseja?\n1 - Inserir\n2 - Buscar\n3 - Sair\n>>> '))

    except:
        FileNotFoundError
    
    finally:
        arq.close()
        return None

if __name__ == '__main__':
    main()
