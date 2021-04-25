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


def lcm(b1, b2):
    sb1, sb2 = create_braid_objects(b1, b2)
    lcm = sb1.lcm(sb2)
    return f"lcm({b1},{b2}) = {lcm}"


def gcd(b1, b2):
    sb1, sb2 = create_braid_objects(b1, b2)
    gcd = sb1.gcd(sb2)
    return f"gcd({b1},{b2}) = {gcd}"


######
######  Polynomials
######


# NOTE: the size of the braid group is important here
def alexander_poly(b1):
    sb1 = create_braid_objects(b1)
    poly = sb1.alexander_polynomial()
    return f"The Alexander polynomial of the closure of {b1} is {poly}"


def jones_poly(b1):
    sb1 = create_braid_objects(b1)
    poly = sb1.jones_polynomial()
    return f"The Jones polynomial of the closure of {b1} is {poly}"


######
######  Representations
######

def Burau_unreduced(b1):
     sb1, sb2 = create_braid_objects(b1, [])
     matrix = sb1.burau_matrix()
     return f"The unreduced Burau representation of {sb1} is \n" + str(matrix)

def burau_unreduced(b1):
    sb1, sb2 = create_braid_objects(b1, [])
    matrix = sb1.burau_matrix()
    return f"The unreduced Burau representation of {b1} is \n{matrix}"


def burau_reduced(b1):
    sb1, sb2 = create_braid_objects(b1, [])
    matrix = sb1.burau_matrix(reduced=True)
    return f"The reduced Burau representation of {b1} is \n{matrix}"


def LKB(b1):
    sb1, sb2 = create_braid_objects(b1, [])
    matrix = sb1.LKB_matrix()
    return f"The Lawrence-Krammer-Bigelow representation of {b1} is \n{matrix}"


# note: this is a *right* action of Bn on Fn
def aut_Fn_representation(b1):
    sb1, sb2 = create_braid_objects(b1, [])
    num_strands = sb1.strands()
    F = FreeGroup(num_strands)
    gens = list(F.generators())
    images = [gen * sb1 for gen in gens]
    return f"The action of {b1} on F_{num_strands} is given by {gens} -> {images}"


# what is the "drain size"...?

# def TL(b1):
#     sb1, sb2 = create_braid_objects(b1, [])
#     matrix = sb1.TL_matrix()
#     return f"The Temperley–Lieb–Jones representation of {sb1} is \n{matrix}"


######
######  Generic Braid info
######


def NT_type(b1):
    sb1 = create_braid_objects(b1)
    nt_type = sb1.thurston_type()
    return f"{b1} is {nt_type}"


def induced_permutation(b1):
    sb1 = create_braid_objects(b1)
    permutation = sb1.permutation()
    one_to_n = [i for i in range(1, sb1.strands() + 1)]
    return f"The permutation induced by {b1} is {one_to_n} -> {permutation}"


def gens_centralizer(b1):
    sb1 = create_braid_objects(b1)
    gens = sb1.centralizer()
    return "The centralizer generators are:\n" + ",\n".join(map(str, gens))


def num_components(b1):
    sb1 = create_braid_objects(b1)
    components = sb1.components_in_closure()
    return f"{b1} has {components} components in it's link closure"


######
######  Helper Functions
######


def create_braid_objects(*braids):
    n = 1 + max(max(map(abs, b), default=1) for b in braids)
    B = BraidGroup(n, [f"s{x}" for x in range(1, n)])
    return tuple(map(B, braids))


DEFAULT_INIT_QUERY = "Word Problem"
QUERIES = {
    "Aut(F_n) Representation": 1,
    # "Temperley–Lieb–Jones Representation": 1,
    "Lawrence-Krammer-Bigelow Representation": 1,
    "Components in Closure": 1,
    "Generators of the Centralizer": 1,
    "Induced Permutation": 1,
    "Nielsen-Thurston type": 1,
    "Burau (unreduced)": 1,
    "Burau (reduced)": 1,
    "Alexander Polynomial": 1,
    "Jones Polynomial": 1,
    "LCM": 2,
    "GCD": 2,
    "Word Problem": 1,
    "Conjugacy Problem": 2,
    "Equal": 2,
}


QUERY_FUNCS = {
    "Aut(F_n) Representation": aut_Fn_representation,
    # "Temperley–Lieb–Jones Representation": TL,
    "Lawrence-Krammer-Bigelow Representation": LKB,
    "Components in Closure": num_components,
    "Generators of the Centralizer": gens_centralizer,
    "Induced permutation": induced_permutation,
    "Nielsen-Thurston type": NT_type,
    "Burau (unreduced)": burau_unreduced,
    "Burau (reduced)": burau_reduced,
    "Jones polynomial": jones_poly,
    "Alexander polynomial": alexander_poly,
    "GCD": gcd,
    "LCM": lcm,
    "Word Problem": word_problem,
    "Conjugacy Problem": conjugacy_problem,
    "Equal": equal,
}
