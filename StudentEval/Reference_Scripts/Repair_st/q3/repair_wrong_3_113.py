def remove_extras ( lst ) :
    compare = [ ]
    for element in lst :
        if ( element not in compare ) :
            compare . append ( element )
    return compare
