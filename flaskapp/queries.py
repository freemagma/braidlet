from sage.all_cmdline import *


def word_problem(b1):
    sb1, sb2 = create_braid_objects(b1, [])
    result = sb1 == sb2
    phrase = "is" if result else "is not"
    return f"{b1} {phrase} the identity"


def equal(b1, b2):
    sb1, sb2 = create_braid_objects(b1, b2)
    result = sb1 == sb2
    phrase = "is" if result else "is not"
    return f"{b1} {phrase} equal to {b2}"


def conjugacy_problem(b1, b2):
    sb1, sb2 = create_braid_objects(b1, b2)
    if sb1.is_conjugated(sb2):
        conj = sb1.conjugating_braid(sb2)
        return f"{b1} and {b2} are conjugates via {conj}"
    else:
        return f"{b1} and {b2} are not conjugates"


def create_braid_objects(*braids):
    n = 1 + max(max(map(abs, b), default=1) for b in braids)
    B = BraidGroup(n, [f's{x}' for x in range(1, n)])
    return tuple(map(B, braids))


DEFAULT_INIT_QUERY = "Word Problem"
QUERIES = {"Word Problem": 1, "Conjugacy Problem": 2, "Equal": 2}
QUERY_FUNCS = {
    "Word Problem": word_problem,
    "Conjugacy Problem": conjugacy_problem,
    "Equal": equal,
}
