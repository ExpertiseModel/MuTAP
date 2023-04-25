def search ( x , seq ) :
    ref_a = 0
    for ( i , v ) in enumerate ( seq ) :
        if ( ( x > v ) and ( i != ( len ( seq ) - 1 ) ) ) :
            continue
        elif ( x <= v ) :
            ref_a = i
            break
        else :
            ref_a = len ( seq )
    return ref_a
