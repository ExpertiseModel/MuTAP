def remove_extras ( lst ) :
    new = [ ]
    x = 0
    for x in lst :
        if ( x not in new ) :
            new += [ x ]
        else :
            continue
    return new
