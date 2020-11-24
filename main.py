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
    # utilities.plot_to_board(
    #     individual[constants.GENES], individual[constants.SCORE])

generation = ranking.sort_list_by_score(generation)
# for i in generation:
#     print(i)

x = 0
# y = 20
while(generation[1][constants.SCORE] > 0 and x < 500):
    x = x+1
    # if x == y:
    #     continuar = input('quer rodar mais 20?')
    #     if continuar == "":
    #         break
    #     else:
    #         y += 20

    print(x, end=" ")
    # Deletando os piores individuos
    # print("\nsó a nata: ")
    ranking.kill_worst_individuals(generation)
    # for i in generation:
    #     utilities.plot_to_board(i[constants.GENES], i[constants.SCORE])

    generation = reproduction.reproduction(generation)

    # TODO deixar esses fors só pra dentro das funções
    for individual in generation:
        individual[constants.SCORE] = ranking.score_individual(
            individual[constants.GENES])
        # utilities.plot_to_board(
        #     individual[constants.GENES], individual[constants.SCORE])

    # Ordenando os individuos de acordo com suas penalidades
    generation = ranking.sort_list_by_score(generation)
    # for i in generation:
    #     print(i)
    utilities.print_random_element(generation)

    # TODO adicionar uma condição pra fazer com que ele pare depois
    # de um número de gerações consecutivas com um cara bom


print("Algoritmo genético concluído")
for i in range(10):
    print(generation[i])
