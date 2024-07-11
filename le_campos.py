## Aluno: Jader Alves dos Santos
## RA: 120286

#função usada para ler as informações do arquivo de texto
def ler_campos(file):
    campo = ''
    f = file.read(1) ## lê a primeira informação para inicializar
    while (f != '') and (f != '|'):
        campo += f
        f = file.read(1)
    return campo ## retorna as informações

def main():
    nomeArq = input('Digite o nome do arquivo: ')
    try:
        with open(nomeArq, 'r') as file:
            campo = ler_campos(file) ## usa a função
            while campo:
                print(campo)
                campo = ler_campos(file)
    except FileNotFoundError:
        print(f'Não foi possível abrir o arquivo {nomeArq} pois ele não existe!')

# a exemplo da prof, utilizei um iniciador
if __name__ == '__main__':
    main()