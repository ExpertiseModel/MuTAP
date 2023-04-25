def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    ref_output = 0
    while ( ref_output < len ( seq ) ) :
        if ( x > seq [ ref_output ] ) :
            ref_output += 1
        else :
            break
    return ref_output
