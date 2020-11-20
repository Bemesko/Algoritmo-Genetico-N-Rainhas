from ranking import *
from constants import *
from first_generation import *
from reproduction import *


# criando a primeira geração
individuals_list = individual_list_factory()
print("lista de individuos gerada!")

# calculando a penalidade dos individuos
for individual in individuals_list:
    individual[SCORE_KEY] = score_individual(individual[GENES_KEY])
    plot_to_board(individual[GENES_KEY], individual[SCORE_KEY])

individuals_list = sort_list_by_score(individuals_list)
for i in individuals_list:
    print(i)

while(individuals_list[0][SCORE_KEY] > 0):

    # Deletando os piores individuos
    print("\nsó a nata: ")
    kill_worst_individuals(individuals_list)
    for i in individuals_list:
        plot_to_board(i[GENES_KEY], i[SCORE_KEY])

    individuals_list = crossing_over(individuals_list)

    for individual in individuals_list:
        individual[SCORE_KEY] = score_individual(individual[GENES_KEY])
        plot_to_board(individual[GENES_KEY], individual[SCORE_KEY])

    # Ordenando os individos de acordo com suas penalidades
    individuals_list = sort_list_by_score(individuals_list)
    for i in individuals_list:
        print(i)

print("Algoritmo genético concluído")
for i in individuals_list:
    print(i)
