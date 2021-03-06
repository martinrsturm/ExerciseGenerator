"""This is the catalog for all the exercise types"""
import exergen


def make_problem_generator(problem_type, params):
    """Returns a problem generator of the specified type"""
    problem_generator = None
    if problem_type == 'fraction':
        problem_generator = exergen.FractionProblemGenerator(params)
    return problem_generator


def make_default_exercise():
    """Returns a default problem generator"""
    title = 'Title'
    text = 'Text'
    exercise_type = 'fraction'
    number_of_sub_exercises = 6
    params = [2, 9, 15, '+']
    problem_generator = exergen.make_problem_generator(exercise_type, params)
    exercise = exergen.Exercise(
        title, text, problem_generator, number_of_sub_exercises)
    return exercise
