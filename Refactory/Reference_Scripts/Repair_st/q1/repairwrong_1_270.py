def search ( x , new_seq ) :
    counter = 0
    new_seq = list ( new_seq )
    if ( new_seq == [ ] ) :
        return 0
    for element in new_seq :
        if ( x <= element ) :
            return counter
        if ( x > new_seq [ ( len ( new_seq ) - 1 ) ] ) :
            return len ( new_seq )
        else :
            counter += 1
            continue
