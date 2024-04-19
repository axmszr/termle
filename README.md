# shorthand:
    L - word length
    R - range(L), but tuple

    g - guess
    a - answer
    G - all guesses
    A - all answers
    C - candidate answers

    'R' - red (i.e. grey)
    'Y' - yellow
    'G' - green

# Logic Files

**cs3236.py**
- holds Theorist class
- handles entropy calculation

**law_school.py**
- holds Painter class
- handles Wordle colouring logic

**law_school_OOP.py**
- UNUSED
- holds Colour, Colouring, Painter classes
- OOP version of law_school.py (possibly useful when considering other langs)

**terminle.py**
- holds Termle class
- main access point for files below


# Main Files
**auto_terminle.py**
- TODO
- automation for daily Wordle
- no prints, maybe should make a growing .csv?
- meant for GH Actions but idk how to do that yet

**exedle.py**
- simple Wordle solver
- can be made into an .exe
- accepts colour and guess inputs from user

**soaredle.py**
- solves Wordle 'optimally', and copies to clipboard
- can be made into an .exe
- accepts single answer input from user
