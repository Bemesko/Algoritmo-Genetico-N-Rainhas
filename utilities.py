import random
from constants import *


def plot_to_board(list, score):
    """Função que cria a tabela visual de ascii:

    ### Exemplo de tabela quando CHROMOSSOME_LENGTH = 8

    ```
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Indivíduo: [0, 3, 0, 0, 0, 0, 0, 4]
    Penalidade: 7
    [x] [ ] [x] [x] [x] [x] [x] [ ]
    [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
    [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
    [ ] [x] [ ] [ ] [ ] [ ] [ ] [ ]
    [ ] [ ] [ ] [ ] [ ] [ ] [ ] [x]
    [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
    [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
    [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ```
    """

    matrix = []
    for i in range(CHROMOSSOME_LENGTH):
        matrix.append([])

    for line in range(CHROMOSSOME_LENGTH):
        for column in range(CHROMOSSOME_LENGTH):
            if (line == list[column]):
                matrix[line].append("[x]")
            else:
                matrix[line].append("[ ]")

    print("~"*30)
    print(f'Indivíduo: {list}')
    print(f'Penalidade: {score}')
    for line in range(CHROMOSSOME_LENGTH):
        for column in range(CHROMOSSOME_LENGTH):
            print(f"{matrix[line][column]}", end=" ")
        print(" ")

    print("~"*30)


def populate_with_unique_values(new_list, max_length):
    """Pega uma lista vazia e vai acrescentando valores sem repeti-los.
    """
    while len(new_list) < max_length:
        new_element = random.randint(0, max_length-1)
        if new_element not in new_list:
            new_list.append(new_element)
