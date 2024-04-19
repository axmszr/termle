from logic import terminle

print("Please ensure possible_words.txt and allowed_words.txt")
print("are in the same folder as this executable.\n")
input("Press ENTER to continue.\n")

L = 5
ANSWERS_FILENAME = "possible_words.txt"
GUESSES_FILENAME = "allowed_words.txt"

termle = Termle(L, ANSWERS_FILENAME, GUESSES_FILENAME)

print("G for Green, Y for Yellow, R for Grey.\n")

termle.run()

input("Press ENTER to close.")
