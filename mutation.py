import random

from constants import *

def mutate_generation(pure_babys):
    babys_to_mutate = []

    # TODO fazer isso aqui pegar babys aleatórios e não só os i primeiros. Pode se insipirar no while de "mutate_genes"
    for i in range(MUTATED_INDIVIDUALS_AMOUNT):
        mutate_genes(pure_babys[i])

    
    print("mutation done!")
    return pure_babys


def mutate_genes(baby):
    """Substitui o valor de genes aleatórios por outros valores aleatórios"""
    exchanged_genes_index = []

    i = 0
    while i < MUTATED_GENES_AMOUNT:
        """Seleciona uma quantidade MUTATED_GENES_AMOUNT de índices
        dos genes para serem modificados e põe eles na lista
        exchanged_genes_index"""
        random_gene_index = random.randrange(CHROMOSSOME_LENGTH)

        if random_gene_index not in exchanged_genes_index:
            exchanged_genes_index.append(random_gene_index)
            i = i+1
        
    for gene_index in exchanged_genes_index:
        new_gene_value = -1
        #while para modificar o gene sem q ele seja menor q e 0 exceda o tamanho padrão de um gene 
        while(new_gene_value < 0 or new_gene_value > CHROMOSSOME_LENGTH-1):
            gene_modifier = random.randrange(
                MUTATION_LOW_MODIFIER, MUTATION_HIGH_MODIFIER)
            new_gene_value = baby[GENES_KEY][gene_index] + gene_modifier

        baby[GENES_KEY][gene_index] = new_gene_value

    return 