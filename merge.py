import io

lower_value = ''
higher_value = '~'

def starting() -> tuple[str, str, io.TextIOWrapper, io.TextIOWrapper, io.TextIOWrapper, bool]:
    global lower_value, higher_value
    before1 = lower_value
    before2 = lower_value
    array1, array2 = open('lista1.txt', 'r'), open('lista2.txt', 'r')
    output = open('saida.txt', 'w')
    return before1, before2, array1, array2, output, True

def end(array1: io.TextIOWrapper, array2: io.TextIOWrapper, output: io.TextIOWrapper) -> None:
    array1.close()
    array2.close()
    output.close()

def read_name(array: io.TextIOWrapper, before_name: str, another_array_name: str, test: bool):
    name = array.readline()
    if not name:
        if another_array_name == higher_value:
            test = False
        else:
            name = higher_value
    else:
        if name <= before_name:
            raise ValueError(f'Erro de sequência na {array.name} -> {name}')
    before_name = name
    return name, before_name, test

def merge() -> None:
    try:
        before1, before2, array1, array2, output, test = starting()
        name1, before1, test = read_name(array1, before1, before2, test)
        name2, before2, test = read_name(array2, before2, before1, test)

        while test:
            if name1 < name2:
                output.write(name1)
                name1, before1, test = read_name(array1, before1, before2, test)
            elif name1 > name2:
                output.write(name2)
                name2, before2, test = read_name(array2, before2, before1, test)
            else:
                output.write(name1)
                name1, before1, test = read_name(array1, before1, before2, test)
                name2, before2, test = read_name(array2, before2, before1, test)
        end(array1, array2, output)
    
    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    merge()