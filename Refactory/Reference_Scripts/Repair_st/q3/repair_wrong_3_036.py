def remove_extras ( lst ) :
    ref_output = [ ]
    for entry in lst :
        if ( ref_output . count ( entry ) == 0 ) :
            ( ref_output == ref_output . append ( entry ) )
    return ref_output
