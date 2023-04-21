def search ( x , seq ) :
    if seq :
        for i in range ( len ( seq ) ) :
            if ( x <= seq [ i ] ) :
                return i
            else :
                pass
        return len ( seq )
    return 0
