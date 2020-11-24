import random

"""Constantes Independentes"""
INDIVIDUAL_AMOUNT = 10  # Quantidade de indivíduos por geração
CHROMOSSOME_LENGTH = 8  # Quantidade de genes num cromossomo

MUTATION_LOW_MODIFIER = -1  # Valor mínimo para modificar um gene na mutação
MUTATION_HIGH_MODIFIER = 1  # Valor máximo para modificar um gene na mutação

"""Constantes dependentes """
# Quantidade de indivíduos que sobrevivem de uma geração à outra
SURVIVING_INDIVIDUAL_AMOUNT = INDIVIDUAL_AMOUNT - 2

# Quantidade de indivíduos que são removidos ao começar uma nova geração
REMOVED_INDIVIDUAL_AMOUNT = INDIVIDUAL_AMOUNT - SURVIVING_INDIVIDUAL_AMOUNT

# Indivíduos que vão sofrer o crossing over no começo da geração
CROSSING_OVER_INDIVIDUAL_AMOUNT = SURVIVING_INDIVIDUAL_AMOUNT

# Índice do gene no qual vai acontecer o split no crossing over
# (antes desse índice os genes são de um pai e depois dele são os genes do outro)
CROSSING_OVER_SPLIT_INDEX = int(random.randrange(2, CHROMOSSOME_LENGTH-2))

# Quantidade de indivíduos que vão sofrer uma mutação
MUTATED_INDIVIDUALS_AMOUNT = int(INDIVIDUAL_AMOUNT)

# Quantidade de genes que vão ser mutados em cada indivíduo
MUTATED_GENES_AMOUNT = int(CHROMOSSOME_LENGTH/2)

""" Constantes supérfluas """
GENES_KEY = "genes"
SCORE_KEY = "score"
