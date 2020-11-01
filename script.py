import exergen
from tkinter import *

fractionExpr = exergen.FractionProblemGenerator(['3', '9', '9', '0'])
print(fractionExpr.generate_problem_and_solution())

root = Tk()
app = exergen.MainWindow(root)
root.mainloop()
