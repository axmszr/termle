# Shorthand
Symbol | Usage
:---: | ---
a / A | answer/all answers
C | candidate answers
col | colouring
g / G | guess/all guesses
'G' | green
L | word length
'R' | red (i.e. grey)
'Y' | yellow


# Logic Files

**cs3236.py**
- holds Theorist class
- handles entropy calculation

**law_school.py**
- holds Painter class
- handles Wordle colouring logic

**painter_OOP.py** (UNUSED)
- holds Colour, Colouring, Painter classes
- OOP version of law_school.py (possibly useful when considering other langs)

**terminle.py**
- holds Termle class
- holds TermleGame class
- main access point for files below


# Main Files
**auto_terminle.py**
- TODO
- automation for daily Wordle
- no prints, maybe should make a growing .csv?
- meant for GH Actions but idk how to do that yet

**copy_header.py**
- useful header file for the .exe files

**exedle.py**
- simple Wordle solver
- copies to clipboard
- can be made into an .exe (see Releases)
- accepts colour and guess inputs from user

**play_exedle.py**
- Wordle game, with a hidden & random answer
- copies to clipboard
- can be made into an .exe (see Releases)
- accepts guess inputs from user

**soaredle.py**
- solves Wordle 'optimally'
- copies to clipboard
- can be made into an .exe (see Releases)
- accepts single answer input from user
