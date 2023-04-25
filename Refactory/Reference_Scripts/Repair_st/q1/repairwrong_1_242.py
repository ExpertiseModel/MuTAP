def search ( x , seq ) :
    ref_count = 0
    for i in seq :
        if ( x > i ) :
            ref_count += 1
    return ref_count
