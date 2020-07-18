# Chess Dictionary Validator
# In this chapter, we used the dictionary value
# {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# to represent a chess board. Write a function named
# isValidChessBoard() that takes a dictionary argument
# and returns True or False depending on if the board is valid.

# Some dictionaries to test function.
# A correct dictionary:
newBoard1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# An incorrect dictionary with two 'wking':
newBoard2 = {'1h': 'bking', '6c': 'wking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# An incorrect dictionary with a coordinate typo (1z):
newBoard3 = {'1z': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# An incorrect dictionary with a piece name typo:
newBoard4 = {'1h': 'king', '3e': 'wking'}
# An incorrect argument since it is not a dictionray:
newBoard4 = ['sdf', 'sdf']

def isValidChessBoard(boardTOanalize):
    validLetters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    properCoord = []    
    countChessPieces = {}
    maxChessPieces = {'bking':1, 'wking':1, 'bqueen':1,\
                   'wqueen':1, 'brook':2, 'wrook':2,\
                       'bknight':2, 'wknight':2,\
                           'bbishop':2, 'wbishop':2,\
                           'bpawn':8, 'wpawn':8}
    
    # Eliminate argument if not a dictionary data type.  
    if type(boardTOanalize) != dict :
        print('The argument is not a dictionary.\nThis function works only on dictionary data types.')
        return[False]

    # Find typos in coordinates  
    for coordLetter in validLetters :
        for coordNum in range(1,9):
            properCoord.append(str(coordNum) + coordLetter)
            
    for k in boardTOanalize:
        if k not in properCoord:
            print('There is a coordinate typo')
            return[False]
        
    # Find typos in piece´s names 
    for k in boardTOanalize:
        if boardTOanalize.get(k) not in maxChessPieces:
            print('There is a piece name typo')
            return[False]

    # Find duplicate or excess pieces
    for k in maxChessPieces:
        countChessPieces.setdefault(k,0)

    for k in maxChessPieces:
        for kk in boardTOanalize:
            if boardTOanalize.get(kk) == k :
 
                countChessPieces[k] = countChessPieces[k] + 1
        if maxChessPieces[k] < countChessPieces[k] :
            print('There is an error with duplicate or excess pieces')
            return[False]

    return[True]
