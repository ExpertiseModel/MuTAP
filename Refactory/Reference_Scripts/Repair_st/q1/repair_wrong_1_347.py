def search ( x , seq ) :
    i = 0
    for ref_p in seq :
        if ( x <= ref_p ) :
            return i
        i += 1
    return len ( seq )
