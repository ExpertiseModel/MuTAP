def search ( x , seq ) :
    ref_lst = list ( seq )
    if ( ref_lst == [ ] ) :
        ref_lst . append ( x )
    else :
        pass
        for i in range ( len ( ref_lst ) ) :
            pass
            if ( x < ref_lst [ i ] ) :
                ref_lst . insert ( i , x )
            else :
                ref_lst . insert ( len ( ref_lst ) , x )
        pass
    if True :
        for i in range ( len ( ref_lst ) ) :
            pass
            if ( ref_lst [ i ] == x ) :
                return i
            pass
    pass
