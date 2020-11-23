import copy

from constants import *
from utilities import *


def individual_factory():  # feito
    """Função que cria individuos da primeira geração"""

    new_individual = {
        GENES_KEY: [],
        SCORE_KEY: 0
    }

    populate_with_unique_values(new_individual[GENES_KEY], CHROMOSSOME_LENGTH)
    return new_individual


def individual_list_factory():  # feito
    """Função que junta os individos da primeira geração em uma lista"""

    new_individual_list = []
    for individual in range(INDIVIDUAL_AMOUNT):
        generated_individual = individual_factory()
        new_individual_list.append(generated_individual)
        print("Individuo " + str(individual + 1) + " geraldo")
    return new_individual_list
