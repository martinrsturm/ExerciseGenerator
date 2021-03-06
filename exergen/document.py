"""The Document class"""
import os


class Document:
    """This class implements the skeleton of a LaTeX document"""

    def __init__(self, document_class, font_size, file_name, title, date=r'''\today'''):
        self.document_class = document_class
        self.font_size = font_size
        self.file_name = file_name
        self.file_name_solution = file_name + "_solution"
        self.title = title
        self.date = date
        self.exercises = []

    def make_pdf(self):
        """Generates the PDF output"""
        # make the exercise sheet
        file = open(self.file_name + ".tex", "w")
        file.write(self.make_latex(False))
        file.close()
        os.system("pdflatex " + self.file_name + ".tex")
        # make the solution sheet
        file = open(self.file_name_solution + ".tex", "w")
        file.write(self.make_latex(True))
        file.close()
        os.system("pdflatex " + self.file_name_solution + ".tex")
        # get rid of the garbage
        self.clean_up()

    def make_latex(self, is_solution):
        """Generates the .tex file"""
        string = self.header()
        string += self.begin_document()
        for ex in self.exercises:
            string += ex.make_latex(is_solution)
        string += self.end_document()
        return string

    def header(self):
        """Writes the LaTeX header"""
        string = r'''\documentclass['''
        string += str(self.font_size)
        string += r'''pt]{'''
        string += self.document_class
        string += r'''} '''
        string += r'''\usepackage{amsmath} '''
        string += r'''\usepackage{enumitem} '''
        string += r'''\usepackage{german} '''
        string += r'''\usepackage{xhfill} '''
        string += r'''\usepackage{titling} '''
        string += r'''\setlength{\droptitle}{-8cm} '''
        string += r'''\pagestyle{empty}'''
        return string

    def begin_document(self):
        """Begin of the document"""
        string = r'''\begin{document} '''
        string += r'''\hfill '''
        string += self.date
        string += r'''\begin{center} \huge\bfseries '''
        string += self.title
        string += r''' \end{center} '''
        return string

    @staticmethod
    def end_document():
        """End of the document"""
        string = r'''\end{document} '''
        return string

    def clean_up(self):
        """Clean up the .tex and log files"""
        os.remove(self.file_name + ".log")
        os.remove(self.file_name + ".aux")
        os.remove(self.file_name + ".tex")
        os.remove(self.file_name_solution + ".log")
        os.remove(self.file_name_solution + ".aux")
        os.remove(self.file_name_solution + ".tex")

    def add_exercise(self, exercise):
        """Adds an exercise"""
        self.exercises.append(exercise)
