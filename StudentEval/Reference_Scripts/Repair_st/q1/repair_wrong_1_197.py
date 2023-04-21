def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    count = 0
    ref_found = False
    while ( count < len ( seq ) ) :
        if ( not ( ( count < len ( seq ) ) and ( not ref_found ) ) ) :
            break
        elif ( x <= seq [ count ] ) :
            ref_found = True
        else :
            count += 1
    return count
