import random

from constants import *

# Função que pega os melhores indivíduos de uma geração e combina os números entre eles para criar indivíduos melhores


def crossing_over(individuals_list):
    # criar lista aleatória de indivíduos com os quais acontecerá crossing over
    crossing_over_individuals = []
    # fazer com que o menor cara fique de certeza nos sobreviventes
    while len(crossing_over_individuals) < CROSSING_OVER_INDIVIDUAL_AMOUNT:
        new_individual = individuals_list[random.randrange(
            0, SURVIVING_INDIVIDUAL_AMOUNT)]
        if new_individual not in crossing_over_individuals:
            crossing_over_individuals.append(
                new_individual)
    print(crossing_over_individuals)
    # pegar quantidade aleatória do cromossomo de cada um e criar indivíduo com eles
    for i in range(int(CROSSING_OVER_INDIVIDUAL_AMOUNT/2)):
        crossing_over_parents = [
            crossing_over_individuals[i*2], crossing_over_individuals[i*2+1]]
        crossing_over_baby = {
            GENES_KEY: [],
            SCORE_KEY: 0
        }
        for gene in range(CROMOSSOME_LENGTH):
            if(gene < CROSSING_OVER_SPLIT_LENGTH):
                crossing_over_baby[GENES_KEY].append(
                    crossing_over_parents[0][GENES_KEY][gene])
            else:
                crossing_over_baby[GENES_KEY].append(
                    crossing_over_parents[1][GENES_KEY][gene])
        print("mamai e papai")
        print(crossing_over_parents[0][GENES_KEY])
        print(crossing_over_parents[1][GENES_KEY])
        print("Nosso novo neném: ")
        print(crossing_over_baby[GENES_KEY])
        # adicionar novos indivíduos na lista de indivíduos
        # individuals_list.append(crossing_over_individuals)

        # Função que


def check_if_needs_next_generation(individuals_list):
    print("nova geracao checada!")


if __name__ == "__main__":
    from first_generation import *
    individuals_list = individual_list_factory()
    crossing_over(individuals_list)
