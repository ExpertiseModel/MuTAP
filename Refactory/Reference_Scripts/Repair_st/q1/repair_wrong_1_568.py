def search ( x , seq ) :
    position = 0
    for ref_i in seq :
        if ( x <= ref_i ) :
            break
        position += 1
    return position
