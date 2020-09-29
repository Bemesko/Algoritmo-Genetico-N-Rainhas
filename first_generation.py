import random
import copy

from constantes import *


# Função que cria individuos da primeira geração
def individual_factory():  # feito
    new_individual = {
        GENES_KEY: [],
        SCORE_KEY: 0
    }

    while len(new_individual[GENES_KEY]) < CROMOSSOME_LENGTH:
        r = random.randint(0, CROMOSSOME_LENGTH-1)
        if r not in new_individual[GENES_KEY]:
            new_individual[GENES_KEY].append(r)
    return new_individual


# Função que junta os individos da primeira geração em uma lista
def individual_list_factory():  # feito

    new_individual_list = []
    for individual in range(INDIVIDUAL_NUMBER):
        generated_individual = individual_factory()
        new_individual_list.append(generated_individual)
        print("Individuo " + str(individual + 1) + " geraldo")
    return new_individual_list
