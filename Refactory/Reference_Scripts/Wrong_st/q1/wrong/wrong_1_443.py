def search(x, seq):
    if len(seq)==0:
        pass
    for i in range(len(seq)):
        if x<=seq[i]:
            return i
    return i+1 
    
                
        
  
