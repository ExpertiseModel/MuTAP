def search ( x , seq ) :
    if ( len ( seq ) == 0 ) :
        return len ( seq )
    else :
        for num in range ( 0 , len ( seq ) ) :
            ref_no = len ( seq )
            if ( x > seq [ num ] ) :
                continue
            elif ( x <= seq [ num ] ) :
                return num
        return ref_no
