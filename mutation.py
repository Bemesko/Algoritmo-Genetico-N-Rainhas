import random
import constants


def mutate_generation(pure_babys):
    """
    Aplica as mutações necessárias para uma nova geração de bebês

    ### INPUT
    ([dicts]) pure_babys: uma lista de dicionários que representam
    indivíduos que acabaram de ser gerados, portanto só possuem um 
    valor para seus genes.

    ### OUTPUT
    ([dicts]) pure_babys: a mesma lista de indivíduos que foi recebida, porém
    com as alterações das mutações feitas (talvez retornar isso não
    seja necessário)
    """

    babys_to_mutate = []
    i = 0

    while i < constants.MUTATED_INDIVIDUALS_AMOUNT:

        random_baby_index = random.randrange(constants.INDIVIDUAL_AMOUNT)

        if random_baby_index not in babys_to_mutate:
            babys_to_mutate.append(random_baby_index)
            i = i+1

    for i in babys_to_mutate:
        mutate_genes(pure_babys[i])

    # print("mutation done!")
    return pure_babys


def mutate_genes(baby):
    """Substitui o valor de genes aleatórios de um indivíduo por outros
    valores aleatórios

    ### INPUT
    baby: um indivíduo recém criado, 
    consistindo de um dicionário, cujo elemento GENES_KEY é equivalente 
    aos genes decididos no crossing over e o SCORE_KEY é 0, pois ainda 
    não foi avaliado pela primeira vez

    ### OUTPUT
    Sem output, apenas faz a mutação dentro do baby
    """

    exchanged_genes_index = []

    i = 0
    while i < constants.MUTATED_GENES_AMOUNT:
        """Seleciona uma quantidade MUTATED_GENES_AMOUNT de índices
        dos genes para serem modificados e põe eles na lista
        exchanged_genes_index
        """

        random_gene_index = random.randrange(constants.CHROMOSSOME_LENGTH)

        if random_gene_index not in exchanged_genes_index:
            exchanged_genes_index.append(random_gene_index)
            i = i+1

    for gene_index in exchanged_genes_index:
        new_gene_value = -1
        # while para modificar o gene sem q ele seja menor q e 0 exceda o tamanho padrão de um gene
        while(new_gene_value < 0 or new_gene_value > constants.CHROMOSSOME_LENGTH-1):
            gene_modifier = random.randrange(
                constants.MUTATION_LOW_MODIFIER, constants.MUTATION_HIGH_MODIFIER)
            new_gene_value = baby[constants.GENES][gene_index] + \
                gene_modifier

        baby[constants.GENES][gene_index] = new_gene_value
