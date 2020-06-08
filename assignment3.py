# This function accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments. 
# It searches the rows and columns of the 2d list to find a match for the word. 
# If a match is found, this functions capitalizes the matched characters in 2-dimensional list and returns the list. 
# If no match is found, this function simply returns the original 2-dimensional list with no modification.

def find_word_horizontal(crosswords,word):
    lines=[]
    for num in range(len(crosswords)):
        line=''.join(crosswords[num])
        lines.append(line)
    for num in range(len(lines)):
        if word in lines[num]:
            position = lines[num].find(word)
            if position != -1:
                return([num,position])
    return(None)

def find_word_vertical(crosswords, word):
    lines=[]
    for col in range(len(crosswords[0])):
        line=''
        for row in range(len(crosswords)):
            line = line + crosswords[row][col]
        lines.append(line)
    for col in range(len(lines)):
        if word in lines[col]:
            specific_row = lines[col].find(word)
            if specific_row != -1:
                return([specific_row,col])
    return(None)

def capitalize_word_in_crossword(crosswords,word):
    wordlength = len(word)
    horizontal = find_word_horizontal(crosswords,word)
    vertical = find_word_vertical(crosswords,word)
    if horizontal != None:
        row = horizontal[0]
        col = horizontal[1]
        for n in range(wordlength):
            crosswords[row][col+n]=crosswords[row][col+n].upper()
        return(crosswords)
    if vertical != None:
        row = vertical[0]
        col = vertical[1]
        for n in range(0,wordlength):
            crosswords[row+n][col]=crosswords[row+n][col].upper()
        return(crosswords)
    return(crosswords)
