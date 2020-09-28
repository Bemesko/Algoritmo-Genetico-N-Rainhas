import random
from funcoes import *

individuals_list = individual_list_factory()
print("lista de individuos gerada!")

for individual in individuals_list:
    individual[SCORE_KEY] = score_individual(individual[GENES_KEY])
    plot_to_board(individual[GENES_KEY], individual[SCORE_KEY])

individuals_list = sort_list_by_score(individuals_list)
print("Lista organizada!\n" + str(individuals_list))

kill_worst_individuals(individuals_list)
print("Piores caras removidos!\n" + str(individuals_list))

crossing_over()  # quando for continuar, fazer isso aqui
check_if_needs_next_generation()
