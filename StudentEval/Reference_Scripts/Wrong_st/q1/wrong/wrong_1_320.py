def search(x, seq):
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
        
       
            
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """

