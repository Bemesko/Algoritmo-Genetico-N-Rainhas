import utilities
import constants


def generation_factory():
    """Cria a lista de indivíduos da primeira geração e vai adicionando indivíduos"""

    new_individual_list = []
    for individual in range(constants.INDIVIDUAL_AMOUNT):
        generated_individual = individual_factory()
        new_individual_list.append(generated_individual)
        print("Individuo " + str(individual + 1) + " geraldo")
    return new_individual_list


def individual_factory():  # feito
    """Retorna um indivíduo, que é um dicionário contendo uma lista de genes e uma
    pontuação.
    """

    new_individual = {
        constants.GENES: [],
        constants.SCORE: 0
    }

    new_individual[constants.GENES] = utilities.populate_with_unique_values(
        constants.CHROMOSSOME_LENGTH)
    return new_individual
