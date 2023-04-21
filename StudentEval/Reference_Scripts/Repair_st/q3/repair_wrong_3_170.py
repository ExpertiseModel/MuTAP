def remove_extras ( lst ) :
    a = [ ]
    for repeat in lst :
        if ( repeat not in a ) :
            a += [ repeat ]
    return a
