
# unused OOP version of law_school.py
# notably slower, but hopefully clearer

class Colour:

    def __init__(self, long, short, *nicks):
        self.long = long
        self.short = short
        self.lower_names = (long.lower(), short.lower()) + tuple(name.lower() for name in nicks)

    def __str__(self):
        return f"{self.long}, aka: {', '.join(self.lower_names[1:])}"

    def __eq__(self, other):
        if isinstance(other, str):
            return other.lower() in self.lower_names

        if isinstance(other, Colour):
            return self.long == other.long

        return False


class Colouring:
    GRN = Colour("Green", "G")
    YLW = Colour("Yellow", "Y")
    GRY = Colour("Grey", "R", "Gray")

    def __init__(self, colours):
        cols = []
        for colour in colours:
            match colour:
                case Colouring.GRY:
                    cols.append(Colouring.GRY)
                case Colouring.YLW:
                    cols.append(Colouring.YLW)
                case Colouring.GRN:
                    cols.append(Colouring.GRN)
                case _:
                    raise Exception("Invalid colour code: " + colour)

        self.cols = tuple(cols)

    def __eq__(self, other):
        if not isinstance(other, Colouring):
            return False
        return self.cols == other.cols

    def __str__(self):
        return ''.join(map(lambda c: c.short, self.cols))
    
    def __hash__(self):
        return hash(str(self))


class Painter:
    GRN = "G"
    YLW = "Y"
    GRY = "R"

    def __init__(self, L):
        self.L = L
        self.R = tuple(range(L))

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

        return Colouring(out)

    def is_match(self, g, a, col):
        return self.colour(g, a) == Colouring(col)

    def filter_candidates(self, C, g, col):
        return tuple(filter(lambda a: is_match(g, a, col), C))

    def __str__(self):
        return f"Wordle colour-er with length {self.L}"
