import random
import copy

from constantes import *


# Função que ordena e calcula a penalidade do individuo
def score_individual(individual_chromossome):
    clone_a = copy.deepcopy(individual_chromossome)
    clone_b = copy.deepcopy(individual_chromossome)
    penalty = 0
    order_list(clone_a, 1)
    penalty = calculate_penalty(clone_a, penalty)
    order_list(clone_b, -1)
    penalty = calculate_penalty(clone_b, penalty)

    print(f"individuo teve multa = {penalty}")

    return penalty


# Função que faz as diagonais se tornarem linhas horizontais
def order_list(list, y_factor):
    for y in range(len(list)):
        list[y] = list[y] + y * y_factor
    list.sort()

# Função que calcula a penalidade


def calculate_penalty(list, penalty):
    for y in range(len(list)-1):
        if (list[y] == list[y+1]):
            penalty += 1
    return penalty


# Função que cria o ranking de individuos
def sort_list_by_score(individuals_list):  # feito
    # Scores maiores indicam indivíduos piores
    return sorted(individuals_list, key=lambda individual: individual[SCORE_KEY])


# Função que mata os piores individuos
def kill_worst_individuals(individuals_list):
    for i in range(REMOVED_INDIVIDUAL_AMOUNT):
        del(individuals_list[-1])


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


if __name__ == "__main__":

    matrix = []
    tamanho = []

    for i in range(8):
        tamanho.append([])

    for i in range(8):
        matrix.append(tamanho)

    matrix = []
    for i in range(8):
        matrix.append(['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'])
    print(matrix)
    print(type(matrix))
