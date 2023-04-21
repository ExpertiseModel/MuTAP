def remove_extras ( lst ) :
    ref_sumx = [ ]
    for i in lst :
        if ( i not in ref_sumx ) :
            ref_sumx . append ( i )
    return ref_sumx
