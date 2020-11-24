import random
import mutation
import constants


def reproduction(individuals_list):
    """Pega os melhores indivíduos de uma geração e
    combina os números entre eles para criar indivíduos melhores

    # INPUT
    (list) individuals_list: Uma lista de dicionários contendo os genes
    e a pontuação de cada indivíduo.

    # OUTPUT
    (list) mutate_babys: Uma lista de indivíduos após terem sido criados
    e terem sofrido a mutação necessária
    """

    pure_babys = []
    while (len(pure_babys) < constants.INDIVIDUAL_AMOUNT):
        pure_babys.append(make_new_baby(individuals_list))

    # print("Nenéns criados:")
    # for i in pure_babys:
    #     print(i[constants.GENES])

    mutate_babys = mutation.mutate_generation(pure_babys)
    return mutate_babys


def make_new_baby(parents_generation):
    """Retorna um novo bebê feito a partir de pais escolhidos

    # INPUT

    (list) parents_generation: Uma lista contendo todos os indivíduos da geração
    dos paes.

    # OUTPUT
    (dict) new_baby: Um bebê novinho em folha feito a partir de 2 indivíduos da
    parents_generation
    """

    new_baby = {
        constants.GENES: [],
        constants.SCORE: 0
    }

    crossing_over_parents = select_parents(parents_generation)

    new_baby[constants.GENES] = crossing_over(crossing_over_parents)

    return new_baby


def select_parents(individuals_list):
    """Seleciona dois indivíduos aleatórios de uma lista e retorna eles"""

    crossing_over_parents = [0, 0]

    while(crossing_over_parents[0] == crossing_over_parents[1]):
        # TODO fazer essa escolha priorizar os que estão no topo do ranking de um jeito melhor
        #! Quando todo mundo dos índices mais baixos é igual esse while fica rodando pra sempre
        crossing_over_parents[0] = individuals_list[random.randrange(
            0, constants.CROSSING_OVER_MAX_INDEX)]
        crossing_over_parents[1] = individuals_list[random.randrange(
            0, constants.CROSSING_OVER_MAX_INDEX)]
    return crossing_over_parents


def crossing_over(crossing_over_parents):
    """Pega pedaços dos genes de dois indivíduos pais e combina eles
    para ser os genes de um indivíduo bebê.

    # INPUT
    crossing_over_parents: Uma lista com dois indivíduos, cujos genes serão
    misturados, um deles contribuindo para os genes antes do ponto de split e
    o outro dando os genes para depois do ponto de split

    # OUTPUT
    crossing_over_baby: Uma lista de genes para o novo bebê
    """

    baby_genes = []

    for gene in range(constants.CHROMOSSOME_LENGTH):
        if(gene < constants.CROSSING_OVER_SPLIT_INDEX):
            baby_genes.append(
                crossing_over_parents[0][constants.GENES][gene])
        else:
            baby_genes.append(
                crossing_over_parents[1][constants.GENES][gene])

    return baby_genes


if __name__ == "__main__":
    from first_generation import generation_factory
    individuals_list = generation_factory()
    reproduction(individuals_list)
