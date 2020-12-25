from tkinter import *
from tkinter.ttk import *
import exergen


class MainWindow:

    def __init__(self, master):
        self.exercises = []
        self.exercises.append(exergen.make_default_exercise())
        self.index_active_exercise = 0

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

        Separator(self.frame, orient=HORIZONTAL).grid(
            row=2, columnspan=5, sticky="ew", pady=10)

        self.list_box = Listbox(
            self.frame, selectmode='browse', exportselection=0)
        self.list_box.grid(column=2, row=3, columnspan=2,
                           rowspan=8, padx=10, pady=10)
        self.list_box.bind('<<ListboxSelect>>', self.update_exercise_entries)

        self.make_pdf_button = Button(
            self.frame, text="Make PDF", command=self.make_pdf)
        self.make_pdf_button.grid(column=2, row=0)

        self.add_exercise_button = Button(
            self.frame, text="Add exercise", command=self.add_exercise)
        self.add_exercise_button.grid(column=2, row=1)

        self.select_initial_exercise()

    def select_initial_exercise(self):
        """Selecting the initial entry in the listbox"""
        self.list_box.insert(
            END, self.exercises[self.index_active_exercise].title)
        self.list_box.select_set(0)
        self.list_box.event_generate("<<ListboxSelect>>")
        self.initialize_exercise_entries()

    def update_exercise(self, event=None):
        """Updating the exercise after changes in the GUI entries"""
        title = self.exercise_entries[0].get(1.0, END)
        text = self.exercise_entries[1].get(1.0, END)
        problem_type = self.exercise_entries[2].get()
        number_of_sub_exercises = int(self.exercise_entries[3].get())
        params = []
        for entry in self.exercise_entries[4:]:
            params.append(entry.get())
        problem_generator = exergen.make_problem_generator(
            problem_type, params)
        exercise = exergen.Exercise(
            title, text, problem_generator, number_of_sub_exercises)
        index = self.list_box.curselection()[0]
        self.exercises[self.index_active_exercise] = exercise
        return

    def update_exercise_entries(self, event=None):
        """Update the GUI entries after selecting a different exercise"""
        if not self.list_box.curselection():
            return
        self.update_exercise()
        index = self.list_box.curselection()[0]
        self.index_active_exercise = index
        exercise = self.exercises[index]
        self.exercise_entries[0].delete(1.0, END)
        self.exercise_entries[0].insert(END, exercise.title)
        self.exercise_entries[1].delete(1.0, END)
        self.exercise_entries[1].insert(END, exercise.text)
        self.exercise_entries[2].delete(0, END)
        self.exercise_entries[2].insert(
            0, exercise.problem_generator.get_type())
        self.exercise_entries[3].delete(0, END)
        self.exercise_entries[3].insert(0, exercise.number_of_problems)
        params = exercise.problem_generator.get_params()
        index = 4
        for param in params:
            self.exercise_entries[index].delete(0, END)
            self.exercise_entries[index].insert(0, param)
            index = index + 1

    def initialize_exercise_entries(self, event=None):
        """initializing the GUI entries with values from the current exercise"""
        if not self.list_box.curselection():
            return
        index = self.list_box.curselection()[0]
        self.index_active_exercise = index
        exercise = self.exercises[index]
        self.exercise_entries[0].delete(1.0, END)
        self.exercise_entries[0].insert(END, exercise.title)
        self.exercise_entries[1].delete(1.0, END)
        self.exercise_entries[1].insert(END, exercise.text)
        self.exercise_entries[2].delete(0, END)
        self.exercise_entries[2].insert(
            0, exercise.problem_generator.get_type())
        self.exercise_entries[3].delete(0, END)
        self.exercise_entries[3].insert(0, exercise.number_of_problems)
        params = exercise.problem_generator.get_params()
        index = 4
        for param in params:
            self.exercise_entries[index].delete(0, END)
            self.exercise_entries[index].insert(0, param)
            index = index + 1

    def add_exercise(self):
        """Adds a new exercise"""
        exercise = exergen.make_default_exercise()
        self.exercises.append(exercise)
        self.list_box.insert(END, exercise.title)

    def make_document_labels(self):
        """Makes the labels for the document related GUI part"""
        label_title = Label(self.frame, text='Title')
        label_title.grid(column=0, row=0, sticky=W)
        self.document_labels.append(label_title)
        label_file_name = Label(self.frame, text='File name')
        label_file_name.grid(column=0, row=1, sticky=W)
        self.document_labels.append(label_file_name)

    def make_document_entries(self):
        """Makes the entries for the exercise related GUI part"""
        entry_title = Entry(self.frame, width=40)
        entry_title.grid(column=1, row=0)
        entry_title.insert(0, "Exercise sheet")
        self.document_entries.append(entry_title)
        entry_file_name = Entry(self.frame, width=40)
        entry_file_name.grid(column=1, row=1)
        entry_file_name.insert(0, "document")
        self.document_entries.append(entry_file_name)

    def make_exercise_labels(self):
        """Makes the labels for the exercise related GUI part"""
        for iterator in range(3, 7 + len(self.exercises[self.index_active_exercise].problem_generator.get_labels())):
            if iterator == 3:
                label_string = 'Title'
            elif iterator == 4:
                label_string = 'Text'
            elif iterator == 5:
                label_string = 'Type'
            elif iterator == 6:
                label_string = 'Number of problems'
            else:
                labels = self.exercises[self.index_active_exercise].problem_generator.get_labels(
                )
                index = iterator - 7
                label_string = labels[index]
            label = Label(self.frame, text=label_string)
            label.grid(column=0, row=iterator, sticky=W)
            self.document_labels.append(label)

    def make_exercise_entries(self):
        """Makes the entries for the exercise related GUI part"""
        for iterator in range(3, 7 + len(self.exercises[self.index_active_exercise].problem_generator.get_labels())):
            if iterator == 3:
                entry = Text(self.frame, height=2, width=40)
            elif iterator == 4:
                entry = Text(self.frame, height=5, width=40)
            elif iterator == 5:
                entry = Combobox(self.frame, values=['fraction'])
            elif iterator == 6:
                entry = Entry(self.frame, width=40)
            else:
                entry = Entry(self.frame, width=40)
            entry.bind("<FocusOut>", self.update_exercise)
            entry.grid(column=1, row=iterator)
            self.exercise_entries.append(entry)

    def make_pdf(self):
        """Triggers the generation of the PDF output"""
        title = self.document_entries[0].get()
        file_name = self.document_entries[1].get()
        doc = exergen.Document('scrartcl', 12, file_name, title)
        for exercise in self.exercises:
            doc.add_exercise(exercise)
        doc.make_pdf()
