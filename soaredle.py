import pyperclip
from termle import Termle

print("Please ensure possible_words.txt and allowed_words.txt")
print("are in the same folder as this executable.\n")
input("Press ENTER to continue.\n")

L = 5
ANSWERS_FILENAME = "possible_words.txt"
GUESSES_FILENAME = "allowed_words.txt"

termle = Termle(L, ANSWERS_FILENAME, GUESSES_FILENAME)

ANS = input("What's the answer?\n")

while not (len(ANS) == 5 and \
           ANS.isalpha() and \
           ANS.lower() in termle.get_candidates()):
    ANS = input("\nPlease input a valid Wordle answer.\n")

col = termle.theorist.colour(termle.best, ANS)
GUES = [(termle.best, col)]

while not termle.is_solved():
    termle.update(termle.best, col, False)
    col = termle.theorist.colour(termle.best, ANS)
    GUES.append((termle.best, col))

def unicode(c):
    match c:
        case "R":
            return "\U00002B1C"
        case "Y":
            return "\U0001F7E8"
        case "G":
            return "\U0001F7E9"
        case _:
            raise Exception

rows = [f"SOAREdle took {len(GUES)} tries:\n"]
rows.append("||" + "".join(unicode(c) for c in GUES[0][1]) + \
            "||  :  " + GUES[0][0])

for g, col in GUES[1:]:
    rows.append("".join(unicode(c) for c in col) + "  :  ||" + g + "||")

text = "\n".join(rows)
pyperclip.copy(text)

print()
print(text)

input("\nCopied to clipboard. Press ENTER to close.")
