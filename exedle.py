from logic.terminle import Termle

print("Please ensure 'possible_words.txt' and 'allowed_words.txt' are")
print("  both in the '/words' folder, relative to this executable.\n")
input("Press ENTER to continue.\n")

L = 5
ANSWERS_FILENAME = "words/possible_words.txt"
GUESSES_FILENAME = "words/allowed_words.txt"

termle = Termle(L, ANSWERS_FILENAME, GUESSES_FILENAME)

print("G for Green, Y for Yellow, R for Grey.\n")

termle.play()

input("Press ENTER to close.")
