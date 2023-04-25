def remove_extras ( lst ) :
    i = [ ]
    for j in range ( len ( lst ) ) :
        if ( lst [ j ] in i ) :
            continue
        else :
            i . append ( lst [ j ] )
    return i
