def remove_extras ( lst ) :
    a = ( )
    c = ( )
    n = len ( lst )
    for i in range ( n ) :
        pass
        for j in range ( i , n ) :
            pass
            if ( ( lst [ i ] == lst [ j ] ) and ( i != j ) ) :
                a += ( j , )
            else :
                continue
            pass
        pass
    b = tuple ( set ( a ) )
    for i in b :
        c += ( lst [ i ] , )
    lst . reverse ( )
    for j in range ( len ( c ) ) :
        lst . remove ( c [ j ] )
    lst . reverse ( )
    return lst
