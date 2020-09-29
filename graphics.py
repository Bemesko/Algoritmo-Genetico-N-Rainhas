from constantes import *

# Função que cria a tabela visual de ascii


def plot_to_board(list, score):

    matrix = []
    for i in range(CROMOSSOME_LENGTH):
        matrix.append([])

    for line in range(CROMOSSOME_LENGTH):
        for column in range(CROMOSSOME_LENGTH):
            if (line == list[column]):
                matrix[line].append("[x]")
            else:
                matrix[line].append("[ ]")

    print("~"*30)

    for line in range(CROMOSSOME_LENGTH):
        for column in range(CROMOSSOME_LENGTH):
            print(f"{matrix[line][column]}", end=" ")
        print(" ")
    print("~"*15)
    print(list)
    print(score)
    print("~"*30)
