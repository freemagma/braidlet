import braidlet as br
import subprocess


def word_problem(b1):
    sb1 = ", ".join(b1)
    output = subprocess.check_output(["sage", "sage/word_problem.sage", f'"{sb1}"'])
    result = output == "True"
    phrase = "is" if result else "is not"
    return f"{b1} {phrase} the identity"


def equal(b1, b2):
    sb1 = ", ".join(b1)
    sb2 = ", ".join(b2)
    output = subprocess.check_output(
        ["sage", "sage/equal.sage", f'"{sb1}"', f'"{sb2}"']
    )
    result = output == "True"
    phrase = "is" if result else "is not"
    return f"{b1} {phrase} equal to {b2}"


def conjugacy_problem(b1, b2):
    sb1 = ", ".join(b1)
    sb2 = ", ".join(b2)
    output = subprocess.check_output(
        ["sage", "sage/conjugate.sage", f'"{sb1}"', f'"{sb2}"']
    )
    if output != "None":
        return f"{b1} and {b2} are conjugates via {output}"
    return f"{b1} and {b2} are not conjugates"


DEFAULT_INIT_QUERY = "Word Problem"
QUERIES = {"Word Problem": 1, "Conjugacy Problem": 2, "Equal": 2}
QUERY_FUNCS = {
    "Word Problem": word_problem,
    "Conjugacy Problem": conjugacy_problem,
    "Equal": equal,
}
