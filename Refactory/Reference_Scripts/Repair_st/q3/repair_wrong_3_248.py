def remove_extras ( lst ) :
    newLst = [ ]
    hashtable = [ ]
    for i in range ( len ( lst ) ) :
        if ( lst [ i ] not in newLst ) :
            newLst . append ( lst [ i ] )
    return newLst
