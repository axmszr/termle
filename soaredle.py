import pyperclip
from logic.terminle import Termle
from logic.law_school import Painter

print("Please ensure 'possible_words.txt' and 'allowed_words.txt' are")
print("  both in the '/words' folder, relative to this executable.\n")
input("Press ENTER to continue.\n")

L = 5
ANSWERS_FILENAME = "words/possible_words.txt"
GUESSES_FILENAME = "words/allowed_words.txt"

termle = Termle(L, ANSWERS_FILENAME, GUESSES_FILENAME)

gues = termle.auto_guess(True)

print("\n=====\n")

g, col = gues[0]
rows = [f"SOAREdle took {len(gues)} tries:\n"]
rows.append(f"||{Painter.emojify(col)}||  :  {g}")

for g, col in gues[1:]:
    rows.append(f"{Painter.emojify(col)}  :  ||{g}||")

text = "\n".join(rows)
pyperclip.copy(text)

print(text)

input("\nCopied to clipboard. Press ENTER to close.")
