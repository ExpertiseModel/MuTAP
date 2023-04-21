def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    ref_counter = 0
    for elem in seq :
        if ( x <= elem ) :
            continue
        elif ( x == elem ) :
            return ( i + 1 )
        else :
            ref_counter += 1
    return ref_counter
