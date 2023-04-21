def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    counter = 0
    for ref_i in seq :
        if ( x < ref_i ) :
            return counter
        elif ( seq [ counter ] >= x ) :
            result = counter
            break
        else :
            counter += 1
    return counter
