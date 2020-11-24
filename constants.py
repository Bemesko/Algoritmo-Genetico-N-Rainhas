import random

"""Constantes Independentes"""
INDIVIDUAL_AMOUNT = 500  # Quantidade de indivíduos por geração
CHROMOSSOME_LENGTH = 8  # Quantidade de genes num cromossomo

# Valor mínimo para modificar um gene na mutação
MUTATION_LOW_MODIFIER = -CHROMOSSOME_LENGTH
# Valor máximo para modificar um gene na mutação
MUTATION_HIGH_MODIFIER = CHROMOSSOME_LENGTH

"""Constantes dependentes """
# Quantidade de indivíduos que sobrevivem de uma geração à outra
SURVIVING_INDIVIDUAL_AMOUNT = INDIVIDUAL_AMOUNT - 2

# Quantidade de indivíduos que são removidos ao começar uma nova geração
REMOVED_INDIVIDUAL_AMOUNT = INDIVIDUAL_AMOUNT - SURVIVING_INDIVIDUAL_AMOUNT

# Indivíduos que vão sofrer o crossing over no começo da geração
CROSSING_OVER_INDIVIDUAL_AMOUNT = SURVIVING_INDIVIDUAL_AMOUNT

# Controla o índice máximo para escolher um pai em uma lista de indivíduos para fazer crossing over
# Na lista, quanto menor o índice, melhor a pontuação, então queremos pais com pontuações boas
#! Se esse valor for baixo demais e der hegemonia o sistema fica rodando pra sempre
CROSSING_OVER_MAX_INDEX = int(SURVIVING_INDIVIDUAL_AMOUNT-1)

# Índice do gene no qual vai acontecer o split no crossing over
# (antes desse índice os genes são de um pai e depois dele são os genes do outro)
CROSSING_OVER_SPLIT_INDEX = int(random.randrange(2, CHROMOSSOME_LENGTH-2))

# Quantidade de indivíduos que vão sofrer uma mutação
MUTATED_INDIVIDUALS_AMOUNT = int(INDIVIDUAL_AMOUNT/100)

# Quantidade de genes que vão ser mutados em cada indivíduo
MUTATED_GENES_AMOUNT = 1

""" Constantes supérfluas """
GENES = "genes"
SCORE = "score"
