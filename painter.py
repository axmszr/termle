
class Painter:
    GRN = "G"
    YLW = "Y"
    GRY = "R"

    def __init__(self, L):
        self.L = L
        self.R = tuple(range(L))
    
    def get_L(self):
        return self.L

    def check_word(self, word):
        if len(word) != self.L:
            raise Exception(f"Incorrect length of '{word}' (expected {L}).")
        if not word.isalpha():
            raise Exception(f"Invalid input: {word}.")

        return word.lower()

    def colour(self, g, a):
        new_g = self.check_word(g)
        new_a = self.check_word(a)

        match = tuple(new_g[i] == new_a[i] for i in self.R)
        remain = [new_a[i] for i in self.R if not match[i]]

        out = []
        for i in self.R:
            if match[i]:
                out.append(Painter.GRN)
            elif new_g[i] in remain:
                out.append(Painter.YLW)
                remain.remove(new_g[i])
            else:
                out.append(Painter.GRY)

        return ''.join(out)

    def is_match(self, g, a, col):
        return self.colour(g, a) == col
