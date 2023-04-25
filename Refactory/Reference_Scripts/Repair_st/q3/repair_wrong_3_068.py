def remove_extras ( lst ) :
    extra = [ ]
    for i in lst :
        if ( i in extra ) :
            continue
        else :
            extra += [ i ]
    return extra
