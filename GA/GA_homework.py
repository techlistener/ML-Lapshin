import numpy as np
from random import randrange


class GenTuple:
    range_to_result = 0
    accuracy = 0.0
    values = []

    @staticmethod
    def create(current_gen):
        probability_distribution = [current_gen[x].accuracy for x in range(len(current_gen))]
        parent1, parent2 = np.random.choice(current_gen, 2, p=probability_distribution)
        if parent1 == parent2:
            parent2 = np.random.choice(current_gen, 1, p=probability_distribution)[0]
        rnd = randrange(len(equation_parameters))
        dominantParent = randrange(2)
        if dominantParent == 0:
            new_gen = parent1.values
            new_gen[rnd] = parent2.values[rnd]
        else:
            new_gen = parent2.values
            new_gen[rnd] = parent1.values[rnd]
        mutation_probability = randrange(101)
        mutation_chance = 10
        if mutation_probability < mutation_chance:
            rand2 = randrange(len(equation_parameters))
            new_gen[rand2] = randrange(31)
        res = GenTuple()
        res.values = new_gen
        return res

    @staticmethod
    def map(values, accuracy=0.0):
        res = GenTuple()
        res.accuracy = accuracy
        res.values = values
        return res

    def __repr__(self):
        return "Range to result: " + str(self.range_to_result) + ", Accuracy: " \
               + str(self.accuracy) + ", Generation: " + str(self.values)


def recalculate_accuracy(gen, sum):
    for s in range(len(gen)):
        gen[s].accuracy = (1.0 / gen[s].range_to_result) / sum


def init_generation(gen, param_count, res, size):
    for _ in range(size):
        gen.append(GenTuple.map([randrange(res) for _ in range(param_count)]))


def step(gen, sum, size, eq_parameters):
    for i in range(size):
        value = 0
        for j in range(len(eq_parameters)):
            value += gen[i].values[j] * eq_parameters[j]
        absValue = abs(value - result)
        if absValue == 0:
            print("Solution: " + str(gen[i].values))
            return True, sum
        gen[i].range_to_result = absValue
        sum += 1.0 / absValue
    return False, sum


result = 30
generation = []
gen_size = 15
equation_parameters = [1, 2, 3, 4]
iterations = 50000
inverse_coefficients_sum = 0.0
iterator = 0

init_generation(generation, len(equation_parameters), result, gen_size)

solved, inverse_coefficients_sum = step(generation, inverse_coefficients_sum, gen_size, equation_parameters)

recalculate_accuracy(generation, inverse_coefficients_sum)

while not solved and iterator < iterations:
    inverse_coefficients_sum = 0.0
    generation = [GenTuple.create(generation) for i in range(gen_size)]

    solved, inverse_coefficients_sum = step(generation, inverse_coefficients_sum, gen_size, equation_parameters)
    if solved:
        break

    recalculate_accuracy(generation, inverse_coefficients_sum)

    iterator += 1

print("Iterations: " + str(iterator))
if not solved:
    print("Iterations overflow")