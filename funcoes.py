import random
import copy

# Criando constantes
INDIVIDUAL_NUMBER = 10
CROMOSSOME_LENGTH = 8
CROMOSSOME_MAGNITUDE = 0, 7
GENES_KEY = "genes"
SCORE_KEY = "score"
REMOVED_INDIVIDUAL_AMOUNT = 3

# Função que cria individuos da primeira geração


def individual_factory():  # feito
    new_individual = {
        "genes": [],
        "score": 0
    }

    for gene in range(CROMOSSOME_LENGTH):
        gene = random.randrange(
            CROMOSSOME_MAGNITUDE[0], CROMOSSOME_MAGNITUDE[1])
        new_individual[GENES_KEY].append(gene)
    return new_individual

# Função que junta os individos da primeira geração em uma lista


def individual_list_factory():  # feito
    new_individual_list = []
    for individual in range(INDIVIDUAL_NUMBER):
        generated_individual = individual_factory()
        new_individual_list.append(generated_individual)
        print("Individuo " + str(individual + 1) + " gerado")
    return new_individual_list


# Função que ordena e calcula a penalidade do individuo
def score_individual(lista):
    clone_a = copy.deepcopy(lista)
    clone_b = copy.deepcopy(lista)
    penalty = 0
    order_list(clone_a, 1)
    penalty = calcular_multa(clone_a, penalty)
    order_list(clone_b, -1)
    penalty = calcular_multa(clone_b, penalty)

    print(f"individuo {0} teve multa = {penalty}")

    return penalty

# Função que faz as diagonais se tornarem linhas horizontais


def order_list(lista, mult_y):
    for y in range(len(lista)):
        lista[y] = lista[y] + y * mult_y
    lista.sort()

# Função que calcula a penalidade


def calcular_multa(lista, penalty):
    for y in range(len(lista)-1):
        if (lista[y] == lista[y+1]):
            penalty += 1
    return penalty

# Função que cria o ranking de individuos


def sort_list_by_score(individuals_list):  # feito
    # Scores maiores indicam indivíduos piores
    return sorted(individuals_list, key=lambda individual: individual[SCORE_KEY])


# Função que mata os piores individuos
def kill_worst_individuals(individuals_list):
    for i in range(REMOVED_INDIVIDUAL_AMOUNT):
        del(individuals_list[-1])


# Função que
def crossing_over():
    print("crossing over!")


# Função que
def check_if_needs_next_generation():
    print("nova geracao checada!")


# Função que cria a tabela visual de ascii
def plot_to_board(list, score):
    matrix = []
    for i in range(8):
        matrix.append(['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'])

    for line in range(8):
        for column in range(8):
            if (line == list[column]):
                matrix[line][column] = "[x]"
            else:
                matrix[line][column] = "[ ]"

    print("~"*30)

    for line in range(8):
        for column in range(8):
            print(f"{matrix[line][column]}", end=" ")
        print(" ")
    print("~"*15)
    print(list)
    print(score)
    print("~"*30)
