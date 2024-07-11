## Aluno: Jader Alves dos Santos
## RA: 120286


def main():
    nomeArq = input('Digite o nome do arquivo: ') ## abre o arquivo
    try: ## recebe try e o with para abrir o arquivo
        with open(nomeArq, 'wb') as file: ## abre o arquivo com função de escrita
            sobrenome = input('Digite o sobrenome: ') ## recebe o sobrenome
            registro = ''
            while sobrenome: ## enquanto o sobrenome não for uma string vazia

                nome = input('Digite seu nome: ')
                endereco = input('Digite seu endereço: ')
                cidade = input('Digite a sua cidade: ')
                estado = input('Digite o seu estado: ')
                cep = input('Digite o seu CEP: ')

                ## organização das letras
                sobrenome = sobrenome.capitalize() 
                nome = nome.capitalize()
                endereco = endereco.title()
                cidade = cidade.title()
                estado = estado.upper()
                ## fim organização
                
                registro = sobrenome+'|'+nome+'|'+endereco+'|'+cidade+'|'+estado+'|'+cep
                registro = registro.encode() ## codifica para binário
                tam = len(registro)
                tam = tam.to_bytes(2) ## armazena em bytes o tamanho da string
                file.write(tam)
                file.write(registro)

                sobrenome = input('Digite o sobrenome: ') ## recebe o sobrenome

    except:
        print(f'Erro ao abrir o arquivo {nomeArq} em modo de escrita, verifique por favor se ele existe ou se o nome está correto!')

# a exemplo da prof, utilizei um iniciador
if __name__ == '__main__':
    main()