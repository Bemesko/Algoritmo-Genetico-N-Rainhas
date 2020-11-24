import random

from mutation import *
from constants import *


def reproduction(individuals_list):
    """Função que pega os melhores indivíduos de uma geração e 
    combina os números entre eles para criar indivíduos melhores"""


    pure_babys = []
    while (len(pure_babys) < INDIVIDUAL_AMOUNT):
        add_baby_to_generation(pure_babys, individuals_list)

    print("Nenéns criados:")
    for i in pure_babys:
        print(i[GENES_KEY])

    mutate_babys = mutate_generation(pure_babys)
    return mutate_babys


def add_baby_to_generation(baby_generation, parents_list):
    """Cria um bebê vazio, escolhe os pais dentro de uma lista de indivíduos
    e adiciona o bebê na lista baby_generation"""

    crossing_over_baby = {
        GENES_KEY: [],
        SCORE_KEY: 0
    }
    crossing_over_parents = [0, 0]

    crossing_over_parents = select_parents(
        crossing_over_parents, parents_list)

    crossing_over(crossing_over_baby, crossing_over_parents)
    
    baby_generation.append(crossing_over_baby)


def select_parents(crossing_over_parents, individuals_list):
    """Seleciona dois indivíduos aleatórios de uma lista e retorna eles"""

    while(crossing_over_parents[0] == crossing_over_parents[1]):
        # TODO fazer essa escolha priorizar os que estão no topo do ranking
        crossing_over_parents = [individuals_list[random.randrange(0, SURVIVING_INDIVIDUAL_AMOUNT-1)],
                                 individuals_list[random.randrange(0, SURVIVING_INDIVIDUAL_AMOUNT-1)]]
    return crossing_over_parents


def crossing_over(crossing_over_baby, crossing_over_parents):
    # Selecionando ponto de split aleatorio
    cromossome_split = CROSSING_OVER_SPLIT_LENGTH

    for gene in range(CHROMOSSOME_LENGTH):
        if(gene < cromossome_split):
            crossing_over_baby[GENES_KEY].append(
                crossing_over_parents[0][GENES_KEY][gene])
        else:
            crossing_over_baby[GENES_KEY].append(
                crossing_over_parents[1][GENES_KEY][gene])





if __name__ == "__main__":
    from first_generation import individual_list_factory
    individuals_list = individual_list_factory()
    reproduction(individuals_list)
