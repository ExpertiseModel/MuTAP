def search ( x , seq ) :
    ref_output = 0
    for ref_j in seq :
        if ( x > ref_j ) :
            ref_output += 1
    return ref_output
