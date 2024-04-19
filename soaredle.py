from copy_header import *

gues = termle.auto_guess(True)

print("\n==========\n")

g, col = gues[0]
rows = [f"SOAREdle took {len(gues)} tries:\n"]
rows.append(f"||{Painter.emojify(col)}||  :  {g}")

for g, col in gues[1:]:
    rows.append(f"{Painter.emojify(col)}  :  ||{g}||")

copy_paste_rows(rows)

input("Press ENTER to close.\n")
