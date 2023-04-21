def search ( x , seq ) :
    ref_a = 0
    for ( i , elem ) in enumerate ( seq ) :
        if ( ( x > elem ) and ( i < ( len ( seq ) - 1 ) ) ) :
            continue
        elif ( x <= elem ) :
            return i
        else :
            return len ( seq )
    return ref_a
