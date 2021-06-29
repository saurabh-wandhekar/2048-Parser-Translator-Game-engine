# 2048-Parser-Translator-Game-engine

Parser-translator for a game programming language using sly in python.

The game elements, its lexicon, and grammatical demands of its programming language are given here.  

It is a 2048-game "family": Here, variations on the original 2048 game are to be also provided for.  The variations are:  

1.  Allowing  subtraction,  multiplication  and  division  in  addition  to  the  plain  doubling operation at tile mergers.  Thus,  each move,  when it is making two same-value tiles merge, may obliterate them together (making them 0 by subtraction), or reduce them to 1 by divition, or square them by multiplication.  In this variation, the goal also will be flexible, any number not necessarily a power of 2 will be achievable.   

2.  Allowing variables in place of tile values to make puzzles:  enabling questions like how many operations it would take at the least, to double the maximum tile value in this position? Thus, the elementary operations of the 2048 game are to be provided, and little tweaks tothem to allow all four arithmetic operations and variables are to be added.   

**The Operations:**
   
**16 Moves**: Add/Subtract/Multiply/Divide Left/Right/Up/Down.: Natural, ex-cept the extensions due to the airthmetic operations added, and the variables assigned.   

**Assignment:** Setting a tile value.

```
Assign valueto x,y.
```

**Naming:** Naming  a  tile.   Each  subsequentmove will move the name also to the destination of this tile according to merging and stopping results.  This may result in a tile getting several names.

```
Var varnameis x,y.
```

**Query:** This value can be used in an assignment.

```
Value in x,y.
```

**Semantics**  

This is a game programming language, so ultimately the semantics should result in the gamestates evolving and in their rendering on the screen.  But, we want only a translation part to be implemented – it is about compilation only – therefore we settle for a text or array structure to be modified as a result of operations. Moreover, we are not giving a full program structure yet. Thus, the developed program should begin an interactive shell. The beginning promptis the start state, in which a random 2 or 4 tile is there, others are blank. Subsequently, each line of input from the user should be interpreted into an action on the current state, and a new state should be produced and rendered as a response.  Internally,keeping track of this current state must be done.  Internally, variable name assignments to tiles also needs to be tracked.  Whatever is needed to give a logically consistent interaction must be maintained in the internal data structures. Thus,the task is to make an interpreter for the language of interaction that allows the user give operation commands listed above.

**Execution**

The project is run and compiled in python3.6.  

There are 3 files:   
lexer.py  - It implements the lexer   
parser.py - It implements the parser class, functions used for the game and the main function.   
makefile - It is used to run the program    

To run the program in the terminal :    

```
make
```

To exit the game type    

```
EXIT.
```

