def search ( x , seq ) :
    ref_value = 0
    for i in range ( 0 , len ( seq ) ) :
        if ( x > seq [ i ] ) :
            ref_value += 1
        elif ( x <= seq [ i ] ) :
            break
    return ref_value
