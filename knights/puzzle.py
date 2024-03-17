from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), # A is either a Knight or a Knave, but not both
    # Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.
    # A says "I am both a knight and a knave."
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), # A is either a Knight or a Knave, but not both
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)), # B is either a Knight or a Knave, but not both
    # Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.
    # A says "We are both knaves."
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), # A is either a Knight or a Knave, but not both
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)), # B is either a Knight or a Knave, but not both
    # Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.
    # A says "We are the same kind."
    #Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    #Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    Implication(AKnight, BKnight),
    Implication(AKnave, BKnight),
    # B says "We are of different kinds."
    #Implication(AKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    #Implication(AKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave)))),
    Implication(BKnight, AKnave),
    Implication(BKnave, AKnave),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), # A is either a Knight or a Knave, but not both
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)), # B is either a Knight or a Knave, but not both
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)), # C is either a Knight or a Knave, but not both
    # Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, Or(AKnight,AKnave)),
    Implication(AKnave, Not(Or(AKnight,AKnave))),
    # B says "A said 'I am a knave'."
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnave)),
    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))

    # a could never say I am a knave, because a knight wouldn't lie (they'll say they're a knight), and a knave would lie (they'll also say they're a knight).
    # therefore b is a knave because A could never have said Aknave
    # and so when b says C is a knave, they are lying. C must be a knight.
    # And with C being a knight telling the truth, we know A is a knight too because C said AKnight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
