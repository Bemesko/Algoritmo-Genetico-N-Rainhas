import random

from constants import *


def crossing_over(individuals_list):
    """Função que pega os melhores indivíduos de uma geração e 
    combina os números entre eles para criar indivíduos melhores"""

    # fazer com que o menor cara fique de certeza nos sobreviventes
    new_generation = []
    while (len(new_generation) < 10):
        add_baby_to_generation(new_generation, individuals_list)
    print("Nenéns criados:")
    for i in new_generation:
        print(i[GENES_KEY])

    # Implementar Mutação
    new_generation = mutate_generation(new_generation)
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


def mutate_generation(generation):
    # TODO não tá sendo aleatório
    # criar uma lista com caras aleatórios para fazer a mutação
    individuals_to_mutate = []

    for i in range(MUTATED_INDIVIDUALS_AMOUNT):
        individuals_to_mutate.append(generation[i])

    for individual in individuals_to_mutate:
        mutate_genes(individual)

    print("mutation done!")
    return generation


def mutate_genes(individual):
    """Substitui o valor de genes aleatórios por outros valores aleatórios"""

    genes = individual[GENES_KEY]
    exchanged_genes_index = []

    for _ in range(MUTATED_GENES_AMOUNT):
        """Seleciona uma quantidade MUTATED_GENES_AMOUNT de índices
        dos genes para serem modificados e põe eles na lista
        exchanged_genes_index"""

        random_gene_index = random.randrange(CHROMOSSOME_LENGTH)

        if random_gene_index not in exchanged_genes_index:
            exchanged_genes_index.append(random_gene_index)

    for gene_index in exchanged_genes_index:
        new_gene_value = -1
        while(new_gene_value < 0 or new_gene_value > CHROMOSSOME_LENGTH):
            gene_modifier = random.randrange(
            MUTATION_LOW_MODIFIER, MUTATION_HIGH_MODIFIER)
            new_gene_value = genes[gene_index] + gene_modifier

        genes[gene_index] = new_gene_value


if __name__ == "__main__":
    from first_generation import individual_list_factory
    individuals_list = individual_list_factory()
    crossing_over(individuals_list)
