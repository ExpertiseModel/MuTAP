def search ( x , seq ) :
    pos = 0
    for i in range ( len ( seq ) ) :
        ref_elem = seq [ i ]
        if ( x <= ref_elem ) :
            pos = i
            break
        else :
            pos += 1
    return pos
