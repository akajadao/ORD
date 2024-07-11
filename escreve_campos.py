## Aluno: Jader Alves dos Santos
## RA: 120286


def main():
    nomeArq = input('Digite o nome do arquivo: ') ## abre o arquivo
    try: ## recebe try e o with para abrir o arquivo
        with open(nomeArq, 'w') as file: ## abre o arquivo com função de escrita
            sobrenome = input('Digite o sobrenome: ') ## recebe o sobrenome
            while sobrenome: ## enquanto o sobrenome não for uma string vazia

                nome = input('Digite seu nome: ')
                endereco = input('Digite seu endereço: ')
                cidade = input('Digite a sua cidade: ')
                estado = input('Digite o seu estado: ')
                cep = input('Digite o seu CEP: ')

                ##organização:
                sobrenome = sobrenome.capitalize() ## Uppercase na primeira letra...
                nome = nome.capitalize()
                endereco = endereco.title()
                cidade = cidade.title()
                estado = estado.upper()
                ## fim organização

                file.write(f'{sobrenome}|{nome}|{endereco}|{cidade}|{estado}|{cep}') ## concatena as informações
                
                sobrenome = input('Digite o sobrenome: ')
    except:
        print(f'Erro!')

# a exemplo da prof, utilizei um iniciador
if __name__ == '__main__':
    main()