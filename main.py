import random
from ranking import *
from constantes import *
from first_generation import *
from reproducao import *
from graphics import *


# criando a primeira geração
individuals_list = individual_list_factory()
print("lista de individuos gerada!")

# calculando a penalidade dos individuos
for individual in individuals_list:
    individual[SCORE_KEY] = score_individual(individual[GENES_KEY])
    plot_to_board(individual[GENES_KEY], individual[SCORE_KEY])

# Ordenando os individos de acordo com suas penalidades
individuals_list = sort_list_by_score(individuals_list)
for i in individuals_list:
    print(i)

# Deletando os piores individuos
print("\nsó a nata: ")
kill_worst_individuals(individuals_list)
for i in individuals_list:
    plot_to_board(i[GENES_KEY], i[SCORE_KEY])

crossing_over()  # quando for continuar, fazer isso aqui
check_if_needs_next_generation()