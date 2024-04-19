from cs3236 import Theorist

def check_file(L, filename):
    with open(filename) as file:
        full_str = file.read()
        words = tuple(full_str.split('\n'))

    for word in words:
        if len(word) != L:
            raise Exception(f"Word '{a}' in {filename} does not match length {L}.")

    return words


class Termle:
    # soare is the best first guess, assuming the full G and A
    SOARE = "SOARE"

    def __init__(self, L, answers_filename, guesses_filename):
        self.A = check_file(L, answers_filename)
        self.G = check_file(L, guesses_filename)
        self.theorist = Theorist(L, self.A)
        self.best = Termle.SOARE

    def get_L(self):
        return self.theorist.get_L()

    def is_solved(self):
        return self.theorist.has_one_candidate()

    def reset(self):
        self.theorist = Theorist(self.get_L(), self.A)
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

    def get_candidates(self):
        return self.theorist.C

    def eval(self, g):
        return self.theorist.get_entropy(g)

    def ask_word(self):
        word = input("Your guess:\n")

        if len(word) != self.get_L():
            print(f"\nPlease try again. Length must be {self.get_L()}.\n")
            return self.ask_word()

        if not word.isalpha():
            print("\nPlease try again. Word must only contain alphabets.\n")
            return self.ask_word()

        return word

    def ask_colour(self):
        col = input("What's the colouring?\n")

        valid = False
        if len(col) != self.get_L():
            print(f"\nPlease try again. Length must be {self.get_L()}.\n")
            return self.ask_colour()

        for c in col:
            if c not in "rygRYG":
                print("\nPlease try again. Use: 'R' = grey, 'Y' = yellow, 'G' = green.\n")
                return self.ask_colour()

        return col

    def run(self):
        self.reset()
        while not self.is_solved():
            g = self.ask_word()
            print(f"\nOk! Please use {g.upper()}.")

            col = self.ask_colour()
            print()
            self.update(g, col, True)
            print()
        self.reset()

    def run_opt(self):
        self.reset()
        while not self.is_solved():
            print(f"Please use {self.best}.")

            col = self.ask_colour()
            print()
            self.update(self.best, col, True)
            print()
        self.reset()

