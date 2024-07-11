from sys import argv
import io

# k 
LOWER_VALUE = ''
HIGHER_VALUE = '~'

# global var
numEOF = 0

def inicialize(ArrayNum: int) -> tuple[list[str], list[str], list[io.TextIOWrapper], io.TextIOWrapper, bool]:
    ## 'befores' starts with a array from ArrayNum with LOWER_VALUE
    names = [LOWER_VALUE] * ArrayNum
    befores = [LOWER_VALUE] * ArrayNum
    arrays = [None] * ArrayNum
    test = True
    for i in range(ArrayNum):
        FileName = f'lista{i}.txt'
        arrays[i] = open(f'listas/{FileName}', "r")
    output = open('saidas.txt', "w")
    return befores, names, arrays, output, test

def end(arrays: list[io.TextIOWrapper], output: io.TextIOWrapper, ArrayNum: int) -> None:
    for i in range(ArrayNum):
        arrays[i].close()
    output.close()

def read_name(array: io.TextIOWrapper, before_name: str, test: bool, ArrayNum: int) -> tuple[str,str,bool]:
    global numEOF
    name = array.readline()
    if not name:
        name = HIGHER_VALUE
        numEOF += 1
        if numEOF == ArrayNum:
            test = False
    else:
        if name <= before_name:
            raise Exception(f'Erro na lista{array.name}: {name}')
    before_name = name
    return name, before_name, test

def kwaymerge(ArrayNum: int) -> None:
    befores, names, arrays, output, test = inicialize(ArrayNum)
    names = [LOWER_VALUE]*ArrayNum
    for i in range(ArrayNum):
        names[i], befores[i], test = read_name(arrays[i], befores[i], test, ArrayNum)
    while test:
        lower = 0
        for i in range(ArrayNum):
            if names[i] < names[lower]:
                lower = i
        output.write(names[lower])
        names[lower], befores[lower], test = read_name(arrays[lower], befores[lower],test, ArrayNum)
    
    end(arrays, output, ArrayNum)


def main() -> None:
    if len(argv) < 2:
        raise TypeError('Numero incorreto de argumentos')
    kwaymerge(int(argv[1]))

if __name__ == '__main__':
    main()