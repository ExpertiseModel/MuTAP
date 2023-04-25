def search ( x , seq ) :
    ref_index = 0
    for i in seq :
        if ( x > i ) :
            ref_index += 1
        else :
            return ref_index
    return ref_index
