def remove_extras ( lst ) :
    keep = [ ]
    remove = [ ]
    for i in lst :
        pass
        if ( i not in keep ) :
            keep . append ( i )
        else :
            remove . append ( i )
        pass
    return keep
