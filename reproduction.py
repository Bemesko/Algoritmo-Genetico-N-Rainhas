import random

from constants import *

# Função que pega os melhores indivíduos de uma geração e combina os números entre eles para criar indivíduos melhores


def crossing_over(individuals_list):
    # fazer com que o menor cara fique de certeza nos sobreviventes
    new_generation = []
    while (len(new_generation) < 10):

        # Declarando BEBE
        crossing_over_baby = {
            GENES_KEY: [],
            SCORE_KEY: 0
        }
        crossing_over_parents = [0, 0]
        crossing_over_parents = select_parents(
            crossing_over_parents, individuals_list)

        make_new_baby(crossing_over_baby, crossing_over_parents)
        new_generation.append(crossing_over_baby)

        print("Nosso novo neném: ")
        print(crossing_over_baby[GENES_KEY])
    for i in new_generation:
        print(i)

    # Implementar Mutação

    # adicionar novos indivíduos na lista de indivíduos
    return new_generation


def make_new_baby(crossing_over_baby, crossing_over_parents):
    # Selecionando ponto de split aleatorio
    cromossome_split = random.randrange(1, CROMOSSOME_LENGTH-2)

    # Fazendo crossing over em si
    for gene in range(CROMOSSOME_LENGTH):
        if(gene < cromossome_split):
            crossing_over_baby[GENES_KEY].append(
                crossing_over_parents[0][GENES_KEY][gene])
        else:
            crossing_over_baby[GENES_KEY].append(
                crossing_over_parents[1][GENES_KEY][gene])


def select_parents(crossing_over_parents, individuals_list):
    while(crossing_over_parents[0] == crossing_over_parents[1]):
        crossing_over_parents = [individuals_list[random.randrange(0, SURVIVING_INDIVIDUAL_AMOUNT-1)],
                                 individuals_list[random.randrange(0, SURVIVING_INDIVIDUAL_AMOUNT-1)]]
    return crossing_over_parents


if __name__ == "__main__":
    from first_generation import *
    individuals_list = individual_list_factory()
    crossing_over(individuals_list)
