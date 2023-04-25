def search ( x , seq ) :
    seq = list ( seq )
    if ( seq == [ ] ) :
        return len ( seq )
    else :
        for i in range ( len ( seq ) ) :
            if ( x <= seq [ i ] ) :
                return i
                break
            else :
                continue
        return len ( seq )
