from random import randint
import math
import numpy


class FractionSubExercise:

    param_list = ['Title', 'Text', 'Subexercise type', 'Number of subexercises', 'Maximal nominator', 'Maximal denominator', 'Operation']

    def __init__(self, max_nom, max_denom, operation):
        self.max_nom = max_nom
        self.max_denom = max_denom
        self.operation = operation
        self.nom1 = 0
        self.nom2 = 0
        self.denom1 = 0
        self.denom2 = 0
        self.nom_sol = 0
        self.denom_sol = 0
        self.sign_sol = 0
        self.make_fractions()

    def make_fractions(self):
        found_valid_exercise = False
        while not found_valid_exercise:
            self.generate_random_exercise()
            found_valid_exercise = self.check_exercise()

    def generate_random_exercise(self):
        [self.nom1, self.denom1] = self.generate_random_fraction()
        [self.nom2, self.denom2] = self.generate_random_fraction()
        self.solve()

    def generate_random_fraction(self):
        nom = randint(1, self.max_nom)
        denom = randint(2, self.max_denom)
        gcd = math.gcd(nom, denom)
        gcd = gcd
        nom = int(nom / gcd)
        denom = int(denom / gcd)
        return [nom, denom]

    def check_exercise(self):
        fraction1_ok = self.check_fraction(self.nom1, self.denom1)
        fraction2_ok = self.check_fraction(self.nom2, self.denom2)
        solution_ok = self.check_fraction(self.nom_sol, self.denom_sol)
        return fraction1_ok and fraction2_ok and solution_ok

    def check_fraction(self, nom, denom):
        is_nom_ok = nom <= self.max_nom
        is_denom_ok = 1 < denom <= self.max_denom
        return is_nom_ok and is_denom_ok

    def check_solution(self):
        is_nom_ok = self.nom_sol <= self.max_nom
        is_denom_ok = self.denom_sol <= self.max_denom
        return is_nom_ok and is_denom_ok

    def print(self, is_solution):
        string = self.print_lhs()
        if is_solution:
            string += self.print_solution()
        else:
            string += self.print_rhs()
        return string

    def print_rhs(self):
        return r'''\;$ \uline{\hfill \phantom{g}}'''

    def print_lhs(self):
        string = r'''$'''
        string += self.print_fraction(self.nom1, self.denom1)
        string += self.print_operation()
        string += self.print_fraction(self.nom2, self.denom2)
        string += r'''='''
        return string

    def print_fraction(self, nom, denom):
        string = r'''\frac{'''
        string += str(nom)
        string += r'''}{'''
        string += str(denom)
        string += r'''}'''
        return string

    def print_solution(self):
        string = r''''''
        if self.sign_sol == -1:
            string += r'''-'''
        string += self.print_fraction(self.nom_sol, self.denom_sol)
        string += r'''$'''
        return string

    def solve(self):
        if self.operation == 'plus':
            self.add()
        elif self.operation == 'minus':
            self.subtract()
        elif self.operation == 'mal':
            self.multiply()
        elif self.operation == 'geteilt':
            self.divide()

    def add(self):
        nom = self.nom1 * self.denom2 + self.nom2 * self.denom1
        denom = self.denom1 * self.denom2
        self.cancel_down_solution(nom, denom)

    def subtract(self):
        nom = abs(self.nom1 * self.denom2 - self.nom2 * self.denom1)
        denom = self.denom1 * self.denom2
        self.sign_sol = numpy.sign(self.nom1 * self.denom2 - self.nom2 * self.denom1)
        self.cancel_down_solution(nom, denom)

    def multiply(self):
        nom = self.nom1 * self.nom2
        denom = self.denom1 * self.denom2
        self.cancel_down_solution(nom, denom)

    def divide(self):
        nom = self.nom1 * self.denom2
        denom = self.denom1 * self.nom2
        self.cancel_down_solution(nom, denom)

    def cancel_down_solution(self, nom, denom):
        gcd = math.gcd(nom, denom)
        self.nom_sol = int(nom/gcd)
        self.denom_sol = int(denom/gcd)

    def print_operation(self):
        if self.operation == 'plus':
            return r''' + '''
        elif self.operation == 'minus':
            return r''' - '''
        elif self.operation == 'mal':
            return r''' \cdot '''
        elif self.operation == 'geteilt':
            return r''' : '''
