"""
LR(1) ACTION and GOTO tables
"""

ACTION = {
    0: {"x": ("shift", 2)},
    1: {"$": ("accept", None)},
    2: {"n1": ("reduce", 2)},
    3: {"n1": ("shift", 4)},
    4: {"c1": ("shift", 5)},
    5: {"c2": ("reduce", 3)},
    6: {"c2": ("shift", 7)},
    7: {"g": ("reduce", 4), "v": ("reduce", 4)},
    8: {"g": ("shift", 10), "v": ("reduce", 6)},
    9: {"v": ("shift", 12)},
    10: {"v": ("reduce", 5)},
    11: {"n": ("shift", 14), "c3": ("reduce", 9), "l": ("reduce", 9), "$": ("reduce", 9)},
    12: {"n": ("reduce", 7), "c3": ("reduce", 7), "l": ("reduce", 7), "$": ("reduce", 7)},
    13: {"c3": ("shift", 16), "l": ("reduce", 11), "$": ("reduce", 11)},
    14: {"c3": [("shift", 18), ("reduce", 11)], "l": ("reduce", 11), "$": ("reduce", 11)},
    15: {"l": ("shift", 20), "$": ("reduce", 13)},
    16: {"c4": ("shift", 21)},
    17: {"c3": ("reduce", 8), "l": ("reduce", 8), "$": ("reduce", 8)},
    18: {"c4": ("shift", 22)},
    19: {"$": ("reduce", 1)},
    20: {"$": ("reduce", 12)},
}

GOTO = {
    0: {"S": 1, "X": 3},
    4: {"C1": 6},
    6: {"C2": 8},
    8: {"G": 9},
    9: {"V": 11},
    11: {"N": 13},
    13: {"T": 15},
    14: {"T": 17},
    15: {"L": 19},
}
