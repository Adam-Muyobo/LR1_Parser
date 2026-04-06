"""
Grammar definitions and productions
"""

PRODUCTIONS = {
    1: ("S", 9, "X n1 C1 C2 G V N T L"),
    2: ("X", 1, "x"),
    3: ("C1", 1, "c1"),
    4: ("C2", 1, "c2"),
    5: ("G", 1, "g"),
    6: ("G", 0, "ε"),
    7: ("V", 1, "v"),
    8: ("N", 2, "n T"),
    9: ("N", 0, "ε"),
    10: ("T", 5, "c3 c4 G V N"),
    11: ("T", 0, "ε"),
    12: ("L", 1, "l"),
    13: ("L", 0, "ε"),
}

TERMINALS = {
    "v": {"gatang","bonang","itseng","thusang","bofang","utlwang","utlweng","boneng","amogelang"},
    "n": {"motho","mosimane","moruti","molaodi","mothusi","ngwana","mopalamente","morui","mothudi"},
    "l": {"phakela","bosigo","motshegare","mantseboa","thata"},
    "c1": {"ba"},
    "c2": {"ba"},
    "g": {"sa","tla"},
    "c3": {"yo"},
    "c4": {"o"},
    "x": {"ya","tsa"},
    "n1": {"bana","batho","baruti"},
}
