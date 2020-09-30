import random
from constants import *

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
    print(f'Indivíduo: {list}')
    print(f'Penalidade: {score}')
    for line in range(CROMOSSOME_LENGTH):
        for column in range(CROMOSSOME_LENGTH):
            print(f"{matrix[line][column]}", end=" ")
        print(" ")

    print("~"*30)


def populate_with_unique_values(new_list, max_length, min_length=0):
    while len(new_list) < max_length:
        new_element = random.randint(0, max_length-1)
        if new_element not in new_list:
            new_list.append(new_element)
