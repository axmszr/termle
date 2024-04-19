import math
#from painter_OOP import Painter
from painter import Painter

class Theorist:
    def __init__(self, L, C):
        for c in C:
            if len(c) != L:
                raise Exception(f"Candidate {c} does not match length {L}.")

        self.painter = Painter(L)
        self.C = C

    # (Painter) Getters
    def get_L(self):
        return self.painter.get_L()

    def has_no_candidates(self):
        return len(self.C) == 0

    def has_one_candidate(self):
        return len(self.C) == 1

    def colour(self, g, a):
        return self.painter.colour(g, a)
    
    # Entropy Calc
    def get_counts(self, g):
        counts = {}
        for a in self.C:
            col = self.colour(g, a)
            if col not in counts:
                counts[col] = 0
            counts[col] += 1
        return counts

    def get_entropy(self, g):
        e = 0
        counts = self.get_counts(g).values()
        for c in counts:
            p_inv = len(self.C) / c
            e += math.log(p_inv, 2) / p_inv
        return e

    def get_best_guess(self, G):
        if self.has_no_candidates():
            raise Exception("No candidates left.")
        if self.has_one_candidate():
            return self.C[0]

        best_g = None
        best_e = 0
        
        for g in G:
            e = self.get_entropy(g)
            if e > best_e:
                best_e = e
                best_g = g

        return best_g

    def show_best_guess(self, G):
        if self.has_no_candidates():
            raise Exception("No candidates left.")
        if self.has_one_candidate():
            print("Only one candidate left! " + self.C[0].upper())
            return self.C[0]

        print(f"{len(self.C)} remaining candidates. Calculating best guess...")
        best_g = None
        best_e = 0

        #can be changed accordingly
        TIERS = 4
        perc = {int(len(G) * i / TIERS) : int(i * 100 / TIERS)
                for i in range(1, TIERS)}

        for i in range(len(G)):
            if i in perc:
                print(f"~{perc[i]}% done.")
            
            g = G[i]
            e = self.get_entropy(g)
            if e > best_e:
                print(f"{g} ({e}) is better than {best_g}.")
                best_e = e
                best_g = g

        print("Best guess: " + best_g.upper())
        return best_g

    # Updating
    def filter_candidates(self, g, col):
        return tuple(filter(lambda a: self.painter.is_match(g, a, col.upper()), self.C))

    def update(self, g, col):
        new_C = self.filter_candidates(g, col)
        return Theorist(self.get_L(), new_C)

