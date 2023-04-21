def split_words(txt):
    
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])
def test():
    assert split_words(['zauberer']) == ['zauberer']
    assert split_words('zauberer, magier') == ['zauberer', 'magier']
    assert split_words('jauch, riese, zeug') == ['jauch', 'riese', 'zeug']
    assert split_words('kaffee, wasser, geschirr') == ['kaffee', 'wasser', 'geschirr']
