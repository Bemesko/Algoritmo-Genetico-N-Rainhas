import random

from constants import *

# Função que pega os melhores indivíduos de uma geração e combina os números entre eles para criar indivíduos melhores


def crossing_over(individuals_list):
    # matar indivíduos

    # criar lista aleatória de indivíduos com os quais acontecerá crossing over
    crossing_over_individuals = []
    while len(crossing_over_individuals) < CROSSING_OVER_INDIVIDUAL_AMOUNT:
        new_individual = individuals_list[random.randrange(
            0, INDIVIDUAL_AMOUNT)]
        if new_individual not in crossing_over_individuals:
            crossing_over_individuals.append(
                new_individual)
    print(crossing_over_individuals)
    # pegar quantidade aleatória do cromossomo de cada um e criar indivíduo com eles
    # adicionar novos indivíduos na lista de indivíduos
    # individuals_list.append(crossing_over_individuals)

# Função que


def check_if_needs_next_generation(individuals_list):
    print("nova geracao checada!")


if __name__ == "__main__":
    from first_generation import *
    individuals_list = individual_list_factory()
    crossing_over(individuals_list)
