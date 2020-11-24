import copy

from constants import *
from utilities import *


def individual_list_factory():
    """Cria a lista de indivíduos da primeira geração e vai adicionando indivíduos"""

    new_individual_list = []
    for individual in range(INDIVIDUAL_AMOUNT):
        generated_individual = individual_factory()
        new_individual_list.append(generated_individual)
        print("Individuo " + str(individual + 1) + " geraldo")
    return new_individual_list


def individual_factory():  # feito
    """Retorna um indivíduo, que é um dicionário contendo uma lista de genes e uma
    pontuação.
    """

    new_individual = {
        GENES_KEY: [],
        SCORE_KEY: 0
    }

    new_individual[GENES_KEY] = populate_with_unique_values(CHROMOSSOME_LENGTH)
    return new_individual
