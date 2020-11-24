import random
import copy
import constants


def score_individual(individual_chromossome):
    """Função que, dada uma lista de genes, calcula a penalidade a ser
    aplicada.

    ### INPUT
    (list) individual_chromossome: Uma lista guardando os genes a serem
    avaliados

    ### OUTPUT
    (int) penalty: O total de multas que a individual_chromossome recebe.
    Quanto mais alto o valor, pior o desempenho da lista.
    """

    penalty = 0

    clone_a = copy.deepcopy(individual_chromossome)
    clone_b = copy.deepcopy(individual_chromossome)
    clone_reto = copy.deepcopy(individual_chromossome)

    # Calculando reto -
    clone_reto.sort()
    penalty += calculate_penalty(clone_reto)

    # Calculando diagonal \
    order_list(clone_a, 1)
    penalty += calculate_penalty(clone_a)

    # Calculando diagonal /
    order_list(clone_b, -1)
    penalty += calculate_penalty(clone_b)

    # print(f"individuo teve multa = {penalty}")

    return penalty


def order_list(list, y_factor):
    """Função que faz as diagonais se tornarem linhas horizontais

    ### INPUT
    list: a lista para ser posta em ordem, vai conter os genes.
    y_factor: um valor que vai multiplicar todos os valores da
    lista para converter as diagonais em linhas horizontais. Mais
    dúvidas perguntar pro Greg.

    ### OUTPUT
    Não tem porque as modificações já são feitas na lista que é passada.
    """

    for y in range(len(list)):
        list[y] = list[y] + y * y_factor
    list.sort()


def calculate_penalty(list):
    """Função que calcula a multa de uma lista já ordenada"""

    penalty = 0
    for y in range(len(list)-1):
        if (list[y] == list[y+1]):
            penalty += 1
    return penalty


def sort_list_by_score(individuals_list):  # feito
    """Função que organiza uma lista de indivíduos por sua pontuação"""

    # Scores maiores indicam indivíduos piores
    return sorted(individuals_list, key=lambda individual: individual[constants.SCORE])


def kill_worst_individuals(individuals_list):
    """Função que mata os piores individuos numa lista"""

    for _ in range(constants.REMOVED_INDIVIDUAL_AMOUNT):
        del(individuals_list[-1])


if __name__ == "__main__":
    import utilities

    lista_teste = [[2, 5, 4, 3, 7, 6, 0, 7], [7, 3, 0, 1, 6, 4, 5, 2], [
        3, 5, 6, 4, 7, 2, 1, 0], [6, 5, 1, 3, 7, 0, 4, 2], [0, 1, 5, 4, 6, 7, 3, 2]]

    penalidade = score_individual(lista_teste[0])
    utilities.plot_to_board(lista_teste[0], penalidade)
