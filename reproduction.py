import random

from constants import *

# Função que pega os melhores indivíduos de uma geração e combina os números entre eles para criar indivíduos melhores


def crossing_over(individuals_list):
    # fazer com que o menor cara fique de certeza nos sobreviventes
    new_generation = []
    while (len(new_generation) < 10):
        add_baby_to_generation(new_generation, individuals_list)
    print("Nenéns criados:")
    for i in new_generation:
        print(i)

    # Implementar Mutação
    new_generation = mutate(new_generation)
    return new_generation


def add_baby_to_generation(baby_generation, parents_list):
    # Declarando BEBE e pais vazios
    crossing_over_baby = {
        GENES_KEY: [],
        SCORE_KEY: 0
    }
    crossing_over_parents = [0, 0]

    crossing_over_parents = select_parents(
        crossing_over_parents, parents_list)

    create_new_baby(crossing_over_baby, crossing_over_parents)
    baby_generation.append(crossing_over_baby)

    print("Nosso novo neném: ")
    print(crossing_over_baby[GENES_KEY])


def create_new_baby(crossing_over_baby, crossing_over_parents):
    # Selecionando ponto de split aleatorio
    cromossome_split = random.randrange(1, CHROMOSSOME_LENGTH-2)

    for gene in range(CHROMOSSOME_LENGTH):
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


def mutate(generation):
    # criar uma lista com caras aleatórios para fazer a mutação
    individuals_to_mutate = []
    for i in range(MUTATED_INDIVIDUALS_AMOUNT):
        individuals_to_mutate.append(generation[i])
    # substituir o valor de um gene por outro
    for individual in individuals_to_mutate:
        mutate_genes(individual)
    print("mutation done!")
    return generation


def mutate_genes(individual):
    genes = individual[GENES_KEY]
    exchanged_genes = []
    # criar uma lista com os genes para serem mudados com o tamanho da MUTATED_GENES_AMOUNT
    # TODO


if __name__ == "__main__":
    from first_generation import individual_list_factory
    individuals_list = individual_list_factory()
    crossing_over(individuals_list)
