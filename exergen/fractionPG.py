"""Generating problems related to fractions"""
from random import randint, choice
import sympy


class FractionProblemGenerator:
    """This class implements a problem generator for fractions"""

    def __init__(self, params):
        self.number_of_fractions = int(params[0])
        self.max_nominator = int(params[1])
        self.max_denominator = int(params[2])
        self.operation_set = params[3]
        self.expression = 0
        self.fractions = []
        self.operations = []

    def generate_problem_and_solution(self):
        """Generating the latex output for the problem and the solution"""
        self.generate_valid_expression()
        problem = self.generate_problem_string()
        solution = self.generate_solution_string()
        return problem, solution

    def get_params(self):
        """Returns the parameters given to the constructor"""
        return (str(self.number_of_fractions), str(self.max_nominator),
                str(self.max_denominator), self.operation_set)

    @staticmethod
    def get_labels():
        """The labels for the GUI"""
        return 'Number of fractions', 'Maximal nominator', 'Maximal denominator', 'Operations'

    @staticmethod
    def get_type():
        """Type of the problems"""
        return 'fraction'

    def generate_problem_string(self):
        """Generating the LaTeX string for a problem"""
        string = r'''$'''
        for i in range(self.number_of_fractions):
            string += sympy.latex(self.fractions[i])
            if i < self.number_of_fractions - 1:
                string += self.operation_string(self.operations[i])
        string += r'''=$'''
        string += r'''\xrfill[-1ex]{0.5pt}[black]'''
        return string

    def generate_solution_string(self):
        """Generating the LaTeX string for a solution"""
        string = r'''$'''
        for i in range(self.number_of_fractions):
            string += sympy.latex(self.fractions[i])
            if i < self.number_of_fractions - 1:
                string += self.operation_string(self.operations[i])
        string += r'''='''
        string += sympy.latex(self.expression)
        string += r'''$'''
        return string

    def generate_valid_expression(self):
        """Generate the fractions for a problem"""
        found_valid_expression = False
        while not found_valid_expression:
            self.generate_random_expression()
            found_valid_expression = self.check_expression()

    def generate_random_expression(self):
        """Generates a random fraction expression"""
        self.expression = 0
        self.fractions = []
        self.operations = []
        expression_string = ''
        for i in range(self.number_of_fractions):
            expression_string += self.print_fraction(
                self.generate_random_fraction())
            if i < self.number_of_fractions - 1:
                self.operations.append(choice(self.operation_set))
                expression_string += self.operations[-1]
        self.expression = eval(expression_string)

    def generate_random_fraction(self):
        """Generate a random fraction"""
        rest_equlas_zero = True
        while rest_equlas_zero:
            nominator = randint(1, self.max_nominator)
            denominator = randint(2, self.max_denominator)
            rest_equlas_zero = (nominator % denominator) == 0
            if not rest_equlas_zero:
                self.fractions.append(sympy.Rational(nominator, denominator))
        return self.fractions[-1]

    @staticmethod
    def print_fraction(fraction):
        """Prints a sympy rational"""
        fraction_string = 'sympy.Rational('
        fraction_string += str(fraction.as_numer_denom()[0])
        fraction_string += ','
        fraction_string += str(fraction.as_numer_denom()[1])
        fraction_string += ')'
        return fraction_string

    def check_expression(self):
        """Check if the randomly generated expression is useful"""
        no_duplicates = len(self.fractions) == len(set(self.fractions))
        nominator_is_valid = (abs(self.expression.as_numer_denom()[0])
                              <= self.max_nominator)
        denominator_is_valid = (abs(self.expression.as_numer_denom()[1])
                                <= self.max_denominator)
        return no_duplicates and nominator_is_valid and denominator_is_valid

    @staticmethod
    def operation_string(op_string):
        """Returns the LaTeX string for the chosen mathematical operation"""
        return_string = op_string
        if op_string == '*':
            return_string = r'''\cdot'''
        elif op_string == '/':
            return_string = r''':'''
        return return_string
