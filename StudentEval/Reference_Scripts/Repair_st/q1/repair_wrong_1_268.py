def search ( x , new_seq ) :
    ref_a = 0
    for ( ref_i , ref_j ) in enumerate ( new_seq ) :
        if ( ( x > ref_j ) and ( ref_i < ( len ( new_seq ) - 1 ) ) ) :
            continue
        if ( x <= ref_j ) :
            ref_a = ref_i
            break
        else :
            ref_a = len ( new_seq )
    return ref_a
