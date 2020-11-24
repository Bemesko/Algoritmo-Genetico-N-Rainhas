import ranking
import constants
import first_generation
import reproduction
import utilities
import constants

# criando a primeira geração
individuals_list = first_generation.individual_list_factory()
print("lista de individuos geralda!")

# calculando a penalidade dos individuos
for individual in individuals_list:
    individual[constants.SCORE_KEY] = ranking.score_individual(
        individual[constants.GENES_KEY])
    utilities.plot_to_board(
        individual[constants.GENES_KEY], individual[constants.SCORE_KEY])

individuals_list = ranking.sort_list_by_score(individuals_list)
for i in individuals_list:
    print(i)

x = 0
y = 20
while(individuals_list[0][constants.SCORE_KEY] > 0):
    x = x+1
    if x == y:
        continuar = input('quer rodar mais 20?')
        if continuar == "":
            break
        else:
            y += 20

    print(f"====================GERAÇÃO {x}========================")
    # Deletando os piores individuos
    print("\nsó a nata: ")
    ranking.kill_worst_individuals(individuals_list)
    for i in individuals_list:
        utilities.plot_to_board(i[constants.GENES_KEY], i[constants.SCORE_KEY])

    individuals_list = reproduction.reproduction(individuals_list)

    for individual in individuals_list:
        individual[constants.SCORE_KEY] = ranking.score_individual(
            individual[constants.GENES_KEY])
        utilities.plot_to_board(
            individual[constants.GENES_KEY], individual[constants.SCORE_KEY])

    # Ordenando os individuos de acordo com suas penalidades
    individuals_list = ranking.sort_list_by_score(individuals_list)
    for i in individuals_list:
        print(i)


print("Algoritmo genético concluído")
for i in individuals_list:
    print(i)
