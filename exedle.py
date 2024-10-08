from copy_header import *

termle = Termle(L, ANSWERS_FILENAME, GUESSES_FILENAME)

print("G for Green, Y for Yellow, R for Grey.")
print(f"The best starting word is {Termle.SOARE}.\n")

gues = termle.play(True)

print("==========\n")

rows = [f"You took {len(gues)} tries:\n"]
for g, col in gues:
    rows.append(f"{Painter.emojify(col)}  :  {g}")

copy_paste_rows(rows)

input("Press ENTER to close.\n")
