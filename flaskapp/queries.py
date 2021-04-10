import braidlet as br
from math_braid import Braid


def word_problem(b1):
    bb1, bb2 = create_braid_objects(b1, [])
    result = bb1 == bb2
    phrase = "is" if result else "is not"
    return f"{b1} {phrase} the identity"


def equal(b1, b2):
    bb1, bb2 = create_braid_objects(b1, b2)
    result = bb1 == bb2
    phrase = "is" if result else "is not"
    return f"{b1} {phrase} equal to {b2}"


def conjugacy_problem(b1, b2):
    bb1, bb2 = create_braid_objects(b1, b2)
    result = False
    phrase = "are" if result else "are not"
    return f"{b1} and {b2} {phrase} conjugates"


def create_braid_objects(*braids):
    n = max(max(map(abs, b), default=0) for b in braids) + 1
    return tuple(Braid(b, n) for b in braids)


DEFAULT_INIT_QUERY = "Word Problem"
QUERIES = {"Word Problem": 1, "Conjugacy Problem": 2, "Equal": 2}
QUERY_FUNCS = {
    "Word Problem": word_problem,
    "Conjugacy Problem": conjugacy_problem,
    "Equal": equal,
}