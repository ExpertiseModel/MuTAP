def search ( x , seq ) :
    n = len ( seq )
    if seq :
        for i in range ( n ) :
            next_element = seq [ i ]
            if ( x <= next_element ) :
                return i
        return n
    else :
        return 0
