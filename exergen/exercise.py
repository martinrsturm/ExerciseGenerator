import exergen


class Exercise:

    def __init__(self, title, text, type, num_sub_exercises, params):
        self.title = title
        self.num_sub_exercises = num_sub_exercises
        self.text = text
        self.type = type
        self.sub_exercises = []
        self.params = params
        self.make_sub_exercises()

    def make_latex(self, is_solution):
        string = self.intro()
        string += self.grid(is_solution)
        return string

    def intro(self):
        string = r'''\section{'''
        string += self.title
        string += r'''} '''
        string += self.text
        return string

    def grid(self, is_solution):
        string = r'''\newline'''
        string += r'''\begin{enumerate}[label=(\alph*),itemsep=3ex] '''
        for sub_ex in self.sub_exercises:
            string += r'''\item '''
            string += sub_ex.print(is_solution)
        string += r'''\end{enumerate}'''
        return string

    def make_sub_exercises(self):
        for i in range(self.num_sub_exercises):
            if self.type == 'fraction':
                self.sub_exercises.append(exergen.FractionSubExercise(self.params[0],
                                                                      self.params[1],
                                                                      self.params[2]))
