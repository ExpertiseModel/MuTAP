def search ( x , seq ) :
    ref_n = len ( seq )
    if seq :
        for i in range ( ref_n ) :
            ref_next_element = seq [ i ]
            if ( x <= ref_next_element ) :
                return i
            else :
                pass
        return ref_n
    else :
        return len ( seq )
