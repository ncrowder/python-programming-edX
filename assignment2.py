# This program is a very simple spelling corrector.  
# The first argument is a sentence (string) and the second argument is a list of words (correct_spells).
# If a word in the sentence can match a word in the correct_spells list by replacing, inserting, or deleting a single character, then that word should be replaced by the correct word in the correct_spelled list.
# Otherwise the word is not modified and simply printed to the output string.

def fixword(s1, s2):
    position = 0
    s1len = len(s1)
    s2len = len(s2)
    if s1 == s2:
        return(s1)
    if abs(s1len-s2len) > 1:
        return(s1)
    elif s1len == s2len:
        for char in s1:
            if char != s2[position]:
                ns1 = s1[:position]+s2[position]+s1[position+1:]
                if ns1 == s2:
                    return(ns1)
                else:
                    return(s1)
            position = position+1
    elif s1len == s2len-1:
        for char in s1:
            if char != s2[position]:
                ns1 = s1[:position]+s2[position]+s1[position:]
                if ns1 == s2:
                    return(ns1)
                else:
                    return(s1)
            position = position+1
            if position == s1len:
                return(s2)
    elif s1len-1 == s2len:
        for char in s1:
            if char != s2[position]:
                ns1 = s1[:position]+s1[position+1:]
                if ns1 == s2:
                    return(ns1)
                else:
                    return(s1)
            position = position+1
            if position == s2len:
                return(s2)
            
#print(fixword('fixe', 'fixorr'))

def spelling_corrector(s1,s2):
    s1 = s1.lower()
    s1list = s1.split()
    outputlist = []
    space = ' '
    for index in range(len(s1list)):
        if len(s1list[index]) == 1 or len(s1list[index]) == 2:
            outputlist.insert(index, s1list[index])
            #print('Word', index, 'not checked.')
        elif s1list[index] in s2:
            outputlist.insert(index, s1list[index])
            #print('Word', index, 'in list.')
        else:
            for word in s2:
                change = 1
                replacement = fixword(s1list[index],word)
                #outputlist.insert(index, replacement)
                if replacement != s1list[index]:
                    outputlist.insert(index, replacement)
                    #print('Word', s1list[index], 'replaced', 'by', replacement)
                    change = 0
                    break
            if change:    
                outputlist.insert(index, s1list[index])
                    
    return(space.join(outputlist))
