def main():
    nomeArq = input(f'Digite o nome do arquivo binário a ser lido:\n>>> ')
    i = 1
    try:
        with open(nomeArq, 'rb') as file:
            cab = file.read(4)
            total_reg = int.from_bytes(cab)

            rrn = int(input('Digite o número do registro a ser lido:>>> '))
            if rrn >= total_reg:
                Exception(f'O número do registro a ser buscado é maior do que os registros existentes!')
            
            offset = rrn*64+4
            file.seek(offset)
            regbytes = file.read(64)


            # decode #
            reg = regbytes.decode('utf-8')
            reg = reg.split(sep='|')
            
            for item in reg:
                if i <= 6:
                    print(f'CAMPO {i}: {item}')
                    i += 1


    except:
        FileNotFoundError

if __name__ == '__main__':
    main()