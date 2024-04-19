from termle import Termle

L = 5
ANSWERS_FILENAME = "words/possible_words.txt"
GUESSES_FILENAME = "words/allowed_words.txt"

termle = Termle(L, ANSWERS_FILENAME, GUESSES_FILENAME)

def reset():
    termle.reset()

def guess(g, col):
    if len(g) != L or len(col) != L:
        raise Exception(f"Length, not {L}.")
    if not g.isalpha():
        raise Exception("Guess must be letters.")
    for c in col:
        if c not in "rygRYG":
            raise Exception("Colouring can only contain R Y G.")
    
    termle.update(g, col, True)

def run():
    reset()
    termle.run_opt()
    reset()

def play():
    reset()
    termle.run()
    reset()

def eval_guess(g):
    return termle.eval(g)

def candis():
    return termle.get_candidates()
