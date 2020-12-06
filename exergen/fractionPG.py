import sympy
from random import randint


class FractionProblemGenerator:

    def __init__(self, params):
        self.number_of_fractions = int(params[0])
        self.max_nominator = int(params[1])
        self.max_denominator = int(params[2])
        self.operations = params[3]
        self.expression = 0
        self.nominators = []
        self.denominators = []

    def generate_problem_and_solution(self):
        self.generate_valid_expression()
        problem = self.generate_problem_string()
        solution = self.generate_solution_string()
        return problem, solution

    def get_params(self):
        return str(self.number_of_fractions), str(self.max_nominator), str(self.max_denominator), self.operations

    @staticmethod
    def get_labels():
        return 'number of fractions', 'maximal nominator', 'maximal denominator', 'operations'

    @staticmethod
    def get_type():
        return 'fraction'

    def generate_problem_string(self):
        string = r'''$'''
        for i in range(self.number_of_fractions):
            string += r'''\frac{'''
            string += str(self.nominators[i])
            string += r'''}{'''
            string += str(self.denominators[i])
            string += r'''}'''
            if i < self.number_of_fractions - 1:
                string += r'''+'''
        string += r'''=$'''
        string += r'''\xrfill[-1ex]{0.5pt}[black]'''
        return string

    def generate_solution_string(self):
        string = r'''$'''
        for i in range(self.number_of_fractions):
            string += r'''\frac{'''
            string += str(self.nominators[i])
            string += r'''}{'''
            string += str(self.denominators[i])
            string += r'''}'''
            if i < self.number_of_fractions - 1:
                string += r'''+'''
        string += r'''='''
        string += sympy.latex(self.expression)
        string += r'''$'''
        return string

    def generate_valid_expression(self):
        self.expression = 0
        self.nominators = []
        self.denominators = []
        found_valid_expression = False
        while not found_valid_expression:
            self.generate_random_expression()
            found_valid_expression = self.check_expression()

    def generate_random_expression(self):
        self.expression = 0
        self.nominators = []
        self.denominators = []
        for i in range(self.number_of_fractions):
            self.expression += self.generate_random_fraction()

    def generate_random_fraction(self):
        nom_equals_denom = True
        while nom_equals_denom:
            nominator = randint(1, self.max_nominator)
            denominator = randint(2, self.max_denominator)
            nom_equals_denom = nominator == denominator
            if not nom_equals_denom:
                self.nominators.append(nominator)
                self.denominators.append(denominator)
        return sympy.Rational(self.nominators[-1], self.denominators[-1])

    def check_expression(self):
        nominator_is_valid = (self.expression.as_numer_denom()[0] <= self.max_nominator)
        denominator_is_valid = (self.expression.as_numer_denom()[1] <= self.max_denominator)
        return nominator_is_valid and denominator_is_valid


