"""Indice Linear, prática 4. Professora Valéria.
O arquivo está em inglês, mas os comentários estão em português para ajudá-los!"""

from dataclasses import dataclass

SIZEOF_TOTALREG = 4
SIZEOF_TAMREG = 2

@dataclass
class ElemIndex:
    ID: int
    OFFSET: int

def read_reg(file):
    """ função usada para ler o registo de 2 bytes
    do arquivo 'trabalhos.dat' e realizar o decode"""
    TAM_BYTES = file.read(2)
    TAM = int.from_bytes(TAM_BYTES)
    if TAM > 0:
        buffer = file.read(TAM)
        buffer = buffer.decode('utf-8')
        return buffer
    return ''

def binarysearch(x:int, v:list) -> int:
    """função de busca binária para a lista INDICE com ElemIndex: ID"""
    i = 0
    f = len(v)-1
    while i<=f:
        m = (i + f)//2
        if v[m].ID == x:
            return m
        if v[m].ID < x:
            i = m+1
        else:
            f = m - 1
    return -1

def mergesort(array, start=0, dead=None):
    """Função de Sort: MergeSort, adaptada para comparar os elementos
    ElemIndex(ID)"""
    if dead is None:
        dead = len(array)
    if (dead - start > 1):
        mid = (dead + start)//2
        mergesort(array, start, mid)
        mergesort(array, mid, dead)
        merge(array, start, mid, dead)

def merge(array, start, mid, dead):
    """Dividir para conquistar"""
    left = array[start:mid]
    right = array[mid:dead]
    top_left, top_right = 0, 0
    for k in range(start, dead):
        if top_left >= len(left):
            array[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            array[k] = left[top_left]
            top_left += 1
            ## comparação usando os elementos "ID" ##
        elif left[top_left].ID < right[top_right].ID:
            array[k] = left[top_left]
            top_left += 1
        else:
            array[k] = right[top_right]
            top_right += 1

def main():
    """Função principal, utilizada para resolver o assunto"""
    try:
        ## vamos abrir o arquivo ##
        with open('trabalhos.dat', 'rb') as file:
            global SIZEOF_TAMREG, SIZEOF_TOTALREG
            ## leitura do cabeçalho ##
            header = file.read(SIZEOF_TOTALREG)
            ## captura pro TOTALREG ##
            TOTALREG = int.from_bytes(header)
            ## lista INDICE vazia ##
            INDEX = []
            ## OFFSET assume o valor do tamanho total de registros (os primeiros 4 bytes de cabeçalho) ##
            OFFSET = SIZEOF_TOTALREG
            ## apontamos a leitura pro primeiro indice de valor 4 bytes##
            file.seek(OFFSET)
            ## para capturar os registros, vamos de 'for' com limite no número total de registros'
            for i in range(TOTALREG):
                ## enquanto for verdade, a leitura vai ocorrer da seguinte forma: ##
                while True:
                    ## o buffer faz a leitura do registro#
                    buffer = read_reg(file)
                    #se ele for diferente de vazio
                    if buffer != '':
                        #separamos o buffer entre as barras '|'##
                        item = buffer.split(sep='|')
                        ## aqui impedimos que a lista tenha itens vazios, caso contrário o último item sempre retornaria ''#
                        item = [x for x in item if x!= '']
                        ##então se o item existir##
                        if item:
                            ##REG assume item##
                            REG = item
                            ##o IDENTIFICADOR do REGISTRO sempre se encontrará no primeiro campo, o "0"##
                            REGID = int(REG[0])
                            ##diferente do que você pensa, o tamanho do registro não é o tamanho do item na lista REG, é o tamanho do buffer ##
                            ## e isso se deve ao fato de que em "REG" nós excluímos as barras, isso impede a leitura do OFFSET de forma correta ##
                            TAMREG = (len(buffer))
                            ## criamos uma variável auxiliar para que a lista de indices na verdade seja preenchida somente com elementos da dataclass ELEMINDICE ##
                            aux = ElemIndex(ID = REGID, OFFSET=OFFSET) ## o ID vai assumir REGID e o OFFSET sempre vai estar em ordem##
                            INDEX.append(aux)
                            ## então atualizamos o OFFSET com o tamanho do registro e também com o indicador de tamanho dele ##
                            ## isso não vai impedir que a função de leitura funcione, pois a variável OFFSET não está inclusa na função, somente auxiliará na busca binária ##
                            OFFSET += TAMREG + SIZEOF_TAMREG
                        ## QUANDO TERMINAR A LEITURA DO REGISTRO ELE PARA E ENTRA NO LOOP DENOVO ##
                        break
            ## implementei uma função própria de mergesort comparando o ID, você pode verificar melhor na função como fiz isso#
            mergesort(INDEX)
            SEARCH_ID = int(input('Digite o ID:\n>>>: '))
            ## inicia a busca binária comparando os IDs, verifique na função a forma que fiz##
            index = binarysearch(SEARCH_ID, INDEX)

            ## se o indice existir, então##
            if index != -1:
                ## o leitor vai para o OFFSET do indice##
                file.seek(INDEX[index].OFFSET)
                ## aqui faremos a leitura do registro##
                buffer = read_reg(file)
                ## separamos os campos do registro##
                REG = buffer.split(sep='|')
                ## e por fim, fazemos um log/debug##
                print(f'ID: {REG[0]}\nNome: {REG[1]}\nTítulo: {REG[2]}\nCurso: {REG[3]}\nTipo: {REG[4]}')
            else:
                raise IndexError(f'Invalid index')

            ## fechamos o arquivo ##
            file.close()

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()