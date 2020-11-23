# Constantes únicas
INDIVIDUAL_AMOUNT = 10
CHROMOSSOME_LENGTH = 8
SURVIVING_INDIVIDUAL_AMOUNT = 11
MUTATION_LOW_MODIFIER = -8
MUTATION_HIGH_MODIFIER = 8

# Constantes dependentes
REMOVED_INDIVIDUAL_AMOUNT = INDIVIDUAL_AMOUNT - SURVIVING_INDIVIDUAL_AMOUNT
CROSSING_OVER_INDIVIDUAL_AMOUNT = SURVIVING_INDIVIDUAL_AMOUNT
CROSSING_OVER_SPLIT_LENGTH = int(CHROMOSSOME_LENGTH/2)
MUTATED_INDIVIDUALS_AMOUNT = int(INDIVIDUAL_AMOUNT/4)
MUTATED_GENES_AMOUNT = int(CHROMOSSOME_LENGTH/4)

# Constantes que não faz diferença mudar
GENES_KEY = "genes"
SCORE_KEY = "score"


# individuos 10
# mata 50%
# 50% sobra [lista original so com a metade]
# os 50% tem filho(25%) [lista de babys]
# [lista original e manter 10% só]
# [junta os 35%]

# individuos 10
# mata 4
# 6 sobra [lista original so com a metade]
# os 6 tem filho 3 [lista de babys]
# [lista original e manter 3 só]
# [junta os 3 + 7]
