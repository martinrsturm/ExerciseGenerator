"""The Exercise class"""


class Exercise:
    """This class implements an exercise with multiple problems"""

    def __init__(self, title, text, problem_generator, number_of_problems):
        self.title = title
        self.number_of_problems = number_of_problems
        self.text = text
        self.problem_generator = problem_generator
        self.problem_strings = []
        self.solution_strings = []
        self.generate_exercise_and_solution_strings()

    def make_latex(self, is_solution):
        """Generate the LaTeX output"""
        string = self.intro()
        string += self.grid(is_solution)
        return string

    def intro(self):
        """Make a new section"""
        string = r'''\section{'''
        string += self.title.replace('\n', ' ').replace('\r', '')
        string += r'''} '''
        string += self.text.replace('\n', ' ').replace('\r', '')
        return string

    def grid(self, is_solution):
        """Makes a grid for the problems"""
        string = r'''\newline'''
        string += r'''\begin{enumerate}[label=(\alph*),itemsep=3ex] '''
        if is_solution:
            for solution_string in self.solution_strings:
                string += r'''\item '''
                string += solution_string
        else:
            for problem_string in self.problem_strings:
                string += r'''\item '''
                string += problem_string
        string += r'''\end{enumerate}'''
        return string

    def generate_exercise_and_solution_strings(self):
        """Generates the strings for the problems"""
        self.problem_strings = []
        self.solution_strings = []
        for _ in range(self.number_of_problems):
            strings = self.problem_generator.generate_problem_and_solution()
            self.problem_strings.append(strings[0])
            self.solution_strings.append(strings[1])
