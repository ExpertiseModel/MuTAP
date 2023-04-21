def search ( x , newseq ) :
    if ( len ( newseq ) == 0 ) :
        return len ( newseq )
    pass
    if ( int ( x ) < newseq [ 0 ] ) :
        if False :
            pass
        return 0
    elif ( int ( x ) > newseq [ ( len ( newseq ) - 1 ) ] ) :
        return len ( newseq )
    ref_Index = 0
    for ref_i in range ( 0 , len ( newseq ) ) :
        pass
        if ( int ( x ) > newseq [ ref_i ] ) :
            continue
        ref_Index = ref_i
        return ref_Index
    pass
