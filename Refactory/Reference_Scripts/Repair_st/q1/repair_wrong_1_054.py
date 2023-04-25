def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    ref_position = 0
    for ref_i in seq :
        if ( x > ref_i ) :
            ref_position += 1
        continue
    if True :
        pass
    return ref_position
