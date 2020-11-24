import random

from mutation import *
from constants import *


def reproduction(individuals_list):
    """Pega os melhores indivíduos de uma geração e 
    combina os números entre eles para criar indivíduos melhores

    ### INPUT
    (list) individuals_list: Uma lista de dicionários contendo os genes
    e a pontuação de cada indivíduo.

    ### OUTPUT
    (list) mutate_babys: Uma lista de indivíduos após terem sido criados 
    e terem sofrido a mutação necessária
    """

    pure_babys = []
    while (len(pure_babys) < INDIVIDUAL_AMOUNT):
        add_baby_to_generation(pure_babys, individuals_list)

    print("Nenéns criados:")
    for i in pure_babys:
        print(i[GENES_KEY])

    mutate_babys = mutate_generation(pure_babys)
    return mutate_babys


def add_baby_to_generation(baby_generation, parents_generation):
    """Cria um bebê vazio, escolhe os pais dentro de uma lista de indivíduos
    e adiciona o bebê na lista baby_generation

    ### INPUT
    (list) baby_generation: A lista de indivíduos na qual o bebê será
    adicionado

    (list) parents_generation: Uma lista contendo todos os indivíduos da geração
    dos paes.

    ### OUTPUT
    Nenhum, mas modifica a lista baby_generation de modo que ao final da função
    ela possua mais um indivíduo
    """

    crossing_over_baby = {
        GENES_KEY: [],
        SCORE_KEY: 0
    }
    # TODO isso podia estar dentro da select parents
    crossing_over_parents = [0, 0]

    crossing_over_parents = select_parents(
        crossing_over_parents, parents_generation)

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
    """Pega pedaços dos genes de dois indivíduos pais e combina eles
    para ser os genes de um indivíduo bebê.

    ### INPUT
    crossing_over_baby: Uma lista vazia na qual os genes serão acrescentados
    crossing_over_parents: Uma lista com dois indivíduos, cujos genes serão
    misturados, um deles contribuindo para os genes antes do ponto de split e
    o outro dando os genes para depois do ponto de split
    """

    for gene in range(CHROMOSSOME_LENGTH):
        if(gene < CROSSING_OVER_SPLIT_INDEX):
            crossing_over_baby[GENES_KEY].append(
                crossing_over_parents[0][GENES_KEY][gene])
        else:
            crossing_over_baby[GENES_KEY].append(
                crossing_over_parents[1][GENES_KEY][gene])


if __name__ == "__main__":
    from first_generation import individual_list_factory
    individuals_list = individual_list_factory()
    reproduction(individuals_list)
