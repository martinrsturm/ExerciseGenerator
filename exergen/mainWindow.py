from tkinter import *
from tkinter.ttk import *
import exergen


class MainWindow:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        self.document_labels = []
        self.make_document_labels()

        self.document_entries = []
        self.make_document_entries()

        self.exercise_labels = []
        self.make_exercise_labels()

        self.string_vars = []
        self.exercise_entries = []
        self.make_exercise_entries()

        Separator(self.frame, orient=HORIZONTAL).grid(row=2, columnspan=5, sticky="ew", pady=10)

        self.list_box = Listbox(self.frame, selectmode='browse', exportselection=0)
        self.list_box.grid(column=2, row=3, columnspan=2, rowspan=8, padx=10, pady=10)
        self.list_box.bind('<<ListboxSelect>>', self.update_exercise_entries)

        self.make_pdf_button = Button(self.frame, text="Make PDF", command=self.make_pdf)
        self.make_pdf_button.grid(column=2, row=0)

        self.add_exercise_button = Button(self.frame, text="Add exercise", command=self.add_exercise)
        self.add_exercise_button.grid(column=2, row=1)

        self.exercises = []

    def update_exercise(self, event):
        try:
            title = self.exercise_entries[0].get()
            text = self.exercise_entries[1].get()
            exercise_type = self.exercise_entries[2].get()
            number_of_sub_exercises = int(self.exercise_entries[3].get())
            params = []
            for entry in self.exercise_entries[4:]:
                try:
                    params.append(int(entry.get()))
                except:
                    params.append(entry.get())
            exercise = exergen.Exercise(title, text, exercise_type, number_of_sub_exercises, params)
            index = self.list_box.curselection()[0]
            self.exercises[index] = exercise
        except:
            return

    def update_exercise_entries(self, event):
        if not self.list_box.curselection():
            return
        index = self.list_box.curselection()[0]
        exercise = self.exercises[index]
        self.exercise_entries[0].delete(0, END)
        self.exercise_entries[0].insert(0, exercise.title)
        self.exercise_entries[1].delete(0, END)
        self.exercise_entries[1].insert(0, exercise.text)
        self.exercise_entries[2].delete(0, END)
        self.exercise_entries[2].insert(0, exercise.type)
        self.exercise_entries[3].delete(0, END)
        self.exercise_entries[3].insert(0, exercise.num_sub_exercises)
        self.exercise_entries[4].delete(0, END)
        self.exercise_entries[4].insert(0, exercise.params[0])
        self.exercise_entries[5].delete(0, END)
        self.exercise_entries[5].insert(0, exercise.params[1])
        self.exercise_entries[6].delete(0, END)
        self.exercise_entries[6].insert(0, exercise.params[2])

    def add_exercise(self):
        title = r'''Addition von Brüchen'''
        text = 'Berechne die folgenden Terme und kürze soweit wie möglich.'
        exercise_type = 'fraction'
        number_of_sub_exercises = 6
        params = [9, 15, 'plus']
        exercise = exergen.Exercise(title, text, exercise_type, number_of_sub_exercises, params)
        self.exercises.append(exercise)
        self.list_box.insert(END, title)

    def make_document_labels(self):
        label_title = Label(self.frame, text='Title')
        label_title.grid(column=0, row=0, sticky=W)
        self.document_labels.append(label_title)
        label_file_name = Label(self.frame, text='File name')
        label_file_name.grid(column=0, row=1, sticky=W)
        self.document_labels.append(label_file_name)

    def make_document_entries(self):
        entry_title = Entry(self.frame)
        entry_title.grid(column=1, row=0)
        entry_title.insert(0, "Aufgabenblatt zur Bruchrechnung")
        self.document_entries.append(entry_title)
        entry_file_name = Entry(self.frame)
        entry_file_name.grid(column=1, row=1)
        entry_file_name.insert(0, "document")
        self.document_entries.append(entry_file_name)

    def make_exercise_labels(self):
        iterator = 3
        for param_string in exergen.FractionSubExercise.param_list:
            label = Label(self.frame, text=param_string)
            label.grid(column=0, row=iterator, sticky=W)
            self.document_labels.append(label)
            iterator = iterator + 1

    def make_exercise_entries(self):
        iterator = 3
        for param_string in exergen.FractionSubExercise.param_list:
            if iterator == 5:
                entry = Combobox(self.frame, values=['fraction'])
            elif iterator == 9:
                entry = Combobox(self.frame, values=['plus', 'minus', 'mal', 'geteilt'])
            else:
                entry = Entry(self.frame)
            entry.bind("<FocusOut>", self.update_exercise)
            entry.grid(column=1, row=iterator)
            self.exercise_entries.append(entry)
            iterator = iterator + 1

    def make_pdf(self):
        title = self.document_entries[0].get()
        file_name = self.document_entries[1].get()
        doc = exergen.Document('scrartcl', 12, file_name, title)
        for exercise in self.exercises:
            doc.add_exercise(exercise)
        doc.make_pdf()


