import ranking
import constants
import first_generation
import reproduction
import utilities
import constants

# criando a primeira geração
generation = first_generation.generation_factory()
print("lista de individuos geralda!")

# calculando a penalidade dos individuos
for individual in generation:
    individual[constants.SCORE] = ranking.score_individual(
        individual[constants.GENES])
    utilities.plot_to_board(
        individual[constants.GENES], individual[constants.SCORE])

generation = ranking.sort_list_by_score(generation)
for i in generation:
    print(i)

x = 0
# y = 20
while(generation[0][constants.SCORE] > 0):
    x = x+1
    # if x == y:
    #     continuar = input('quer rodar mais 20?')
    #     if continuar == "":
    #         break
    #     else:
    #         y += 20

    print(f"====================GERAÇÃO {x}========================")
    # Deletando os piores individuos
    print("\nsó a nata: ")
    ranking.kill_worst_individuals(generation)
    for i in generation:
        utilities.plot_to_board(i[constants.GENES], i[constants.SCORE])

    generation = reproduction.reproduction(generation)

    for individual in generation:
        individual[constants.SCORE] = ranking.score_individual(
            individual[constants.GENES])
        utilities.plot_to_board(
            individual[constants.GENES], individual[constants.SCORE])

    # Ordenando os individuos de acordo com suas penalidades
    generation = ranking.sort_list_by_score(generation)
    for i in generation:
        print(i)


print("Algoritmo genético concluído")
for i in generation:
    print(i)
