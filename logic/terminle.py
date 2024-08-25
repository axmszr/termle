from .cs3236 import Theorist
from .law_school import Painter
from random import choice

def check_file(L, filename):
    with open(filename) as file:
        full_str = file.read()
        words = tuple(w.upper() for w in full_str.split('\n'))

    for word in words:
        if len(word) != L:
            raise Exception(f"Word '{word}' in {filename} does not match length {L}.")

    return words


class Termle:
    # soare is the best first guess, assuming the full G and A
    SOARE = "TARSE"

    def __init__(self, L, answers_filename, guesses_filename):
        self.A = check_file(L, answers_filename)
        self.G = check_file(L, guesses_filename)
        self.L = L
        self.theorist = Theorist(L, self.A)
        self.best = Termle.SOARE

    # (Theorist) Getters
    def is_solved(self):
        return self.theorist.has_one_candidate()

    def get_candidates(self):
        return self.theorist.C

    def eval(self, g):
        return self.theorist.get_entropy(g)
    
    # Interaction
    def reset(self):
        self.theorist = Theorist(self.L, self.A)
        self.best = Termle.SOARE

    def update(self, g, col, visual):
        new_theorist = self.theorist.update(g, col)
        try:
            if visual:
                self.best = new_theorist.show_best_guess(self.G).upper()
            else:
                self.best = new_theorist.get_best_guess(self.G).upper()
            self.theorist = new_theorist
            return True
        except:
            print("No remaining candidates. Try again?")
            return False

    def ask_word(self, type):
        invalid = True
        while invalid:
            word = input(type + ":\n")
            
            if len(word) != self.L:
                print(f"\n{type} length must be {self.L}. Please try again.\n")
            elif not word.isalpha():
                print(f"\n{type} must only contain alphabets. Please try again.\n")
            else:
                invalid = False
        return word.upper()

    def ask_guess(self):
        return self.ask_word("Guess")

    def ask_answer(self):
        while (a := self.ask_word("Answer")) not in self.A:
            print("\nNot an accepted answer. Please try again.\n")
        return a
    
    def ask_colour(self):
        invalid = True
        while invalid:
            col = self.ask_word("Colouring")

            for c in col:
                if c not in "GYR":
                    print("\nPlease try again. Use: 'G' = green, 'Y' = yellow, 'R' = grey.\n")
                    break
            else:
                invalid = False
        return col

    def play_with(self, guesser, visual):
        self.reset()
        gues = []
        
        while not self.is_solved():
            g = guesser()
            print(f"\nPlease use {g}.")
            col = self.ask_colour()
            
            print()
            if self.update(g, col, visual):
                gues.append((g, col))
            print()
        
        if col != "GGGGG":
            gues.append((self.get_candidates()[0], "GGGGG"))
        
        self.reset()
        return gues

    def play(self, visual):
        return self.play_with(self.ask_guess, visual)

    def play_opt(self):
        return self.play_with(lambda : self.best, True)

    def auto_guess(self, visual):
        self.reset()
        a = self.ask_answer()
        gues = []
        
        while not self.is_solved():
            col = Painter.colour(self.best, a)
            gues.append((self.best, col))
            
            if visual:
                print(f"\nTrying {self.best}, got colouring {col}.\n")
            
            self.update(self.best, col, visual)

        if col != "GGGGG":
            gues.append((a, "GGGGG"))
        
        self.reset()
        return gues


class TermleGame(Termle):
    def __init__(self, L, answers_filename, guesses_filename, *answer):
        super().__init__(L, answers_filename, guesses_filename)
        if answer:
            if answer[0] not in self.A:
                raise ValueError(f"{answer} is not an accepted answer.")
            self.answer = answer[0]
        else:
            self.answer = choice(self.A)
    
    def play_with(self, guesser, visual):
        self.reset()
        gues = []
        QWERTY = "QWERTYUIOP" +\
                 "ASDFGHJKL" +\
                 "ZXCVBNM"
        remain = {q : q for q in QWERTY}
        
        while len(gues) < 6:
            g = guesser()
            col = Painter.colour(g, self.answer)
            gues.append((g, col))
            print()
            
            if col == "GGGGG":
                break

            if visual:
                self.update(g, col, visual)
                print()

            print("Current state:")
            for g, col in gues:
                print(f"    {g}\n    {col}\n")
            
            for i in range(self.L):
                if col[i] == 'R':
                    remain[g[i]] = '_'
            rem = tuple(remain.values())
            rem = (rem[:10], rem[10:19], rem[19:])
            rem = tuple(' '.join(row) for row in rem)
            
            print("Remaining letters:")
            print(f"  |{rem[0]}|\n  | {rem[1]} |\n  |  {rem[2]}    |\n")
            
        self.reset()
        return gues

    def auto_guess(self, visual):
        self.reset()
        a = self.answer
        gues = []
        
        while not self.is_solved():
            col = Painter.colour(self.best, a)
            gues.append((self.best, col))
            
            if visual:
                print(f"\nTrying {self.best}, got colouring {col}.\n")
            
            self.update(self.best, col, visual)

        if col != "GGGGG":
            gues.append((a, "GGGGG"))
        
        self.reset()
        return gues
