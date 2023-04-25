def remove_extras ( mylist ) :
    ref_newlist = [ ]
    for i in mylist :
        if ( i not in ref_newlist ) :
            ref_newlist . append ( i )
    return ref_newlist
