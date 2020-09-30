# Criando constantes
INDIVIDUAL_AMOUNT = 10
CROMOSSOME_LENGTH = 8

SURVIVING_INDIVIDUAL_AMOUNT = 11
REMOVED_INDIVIDUAL_AMOUNT = INDIVIDUAL_AMOUNT - SURVIVING_INDIVIDUAL_AMOUNT

CROSSING_OVER_INDIVIDUAL_AMOUNT = SURVIVING_INDIVIDUAL_AMOUNT
CROSSING_OVER_SPLIT_LENGTH = int(CROMOSSOME_LENGTH/2)

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