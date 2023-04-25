def remove_extras ( lst ) :
    removed = [ ]
    for e in lst :
        if ( e not in removed ) :
            removed . append ( e )
    return removed
