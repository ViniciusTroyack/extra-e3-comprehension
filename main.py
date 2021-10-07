def list_comprehension_exercise_1():
    return [x for x in range(0,11)]


def list_comprehension_exercise_2():
    return [x for x in range(0, 22) if x % 2 == 0 or x % 3 == 0]


def list_comprehension_exercise_3():
    return [x for x in range(-5, 32) if x % 2 != 0 and x % 5 != 0]


def list_comprehension_exercise_4():
    return [x ** 2 for x in range(0,11)]


def list_comprehension_exercise_5(sentence):
    return [x for x in sentence if x.isupper()]


def list_comprehension_exercise_6(sentence):
    new_sentence = sentence.split(' ')
    return [x for x in new_sentence if len(x) > 3 and x.startswith('r')]


list_comprehension_exercise_3()
