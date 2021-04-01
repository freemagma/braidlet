import braidlet as br


def word_problem(b1):
    result = br.word_problem(b1)
    phrase = "is" if result else "is not"
    return f"{b1} {phrase} the identity"


def conjugacy_problem(b1, b2):
    result = br.word_problem(b1)
    phrase = "are" if result else "are not"
    return f"{b1} and {b2} {phrase} conjugates"


DEFAULT_INIT_QUERY = "Word Problem"
QUERIES = {"Word Problem": 1, "Conjugacy Problem": 2}
QUERY_FUNCS = {"Word Problem": word_problem, "Conjugacy Problem": conjugacy_problem}