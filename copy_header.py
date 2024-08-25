import pyperclip
from logic.terminle import Termle, TermleGame
from logic.law_school import Painter

print("\n    Please ensure 'possible_words.txt' and 'allowed_words.txt' are")
print("    both in the '/words' folder, relative to this executable.\n")
input("Press ENTER to continue.\n")

L = 5
ANSWERS_FILENAME = "words/possible_words.txt"
GUESSES_FILENAME = "words/allowed_words.txt"

print("==========\n")

def copy_paste_rows(rows):
    text = "\n".join(rows)
    pyperclip.copy(text)
    print(text)
    print("\nCopied to clipboard.")
