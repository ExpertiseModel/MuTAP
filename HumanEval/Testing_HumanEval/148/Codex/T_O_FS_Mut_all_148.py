def bf(planet1, planet2):
    
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        return (planet_names[planet2_index + 1 : planet1_index])



def test():
    assert bf(planet1 = "Earth", planet2 = "Saturn") == ("Mars", "Jupiter")
    assert bf(planet1 = "Earth", planet2 = "Earth") == ()
    assert bf(planet1 = "Earth", planet2 = "Venus") == ()
    assert bf(planet1 = "Mars", planet2 = "Neptune") == ('Jupiter', 'Saturn', 'Uranus')
    assert bf(planet1 = "Earth", planet2 = "Saturn") == ("Mars", "Jupiter")
    assert bf(planet1 = "Earth", planet2 = "Earth") == ()
    assert bf(planet1 = "Earth", planet2 = "Venus") == ()
    assert bf(planet1 = "Mars", planet2 = "Neptune") == ('Jupiter', 'Saturn', 'Uranus')
    assert bf(planet1 = "Saturn", planet2 = "Mars") == ()
    assert bf(planet1 = "Saturn", planet2 = "Earth") == ("Jupiter", "Saturn", "Uranus")
    assert bf(planet1 = "Earth", planet2 = "Earth") == ()
    assert bf(planet1 = "Earth", planet2 = "Venus") == ()
    assert bf(planet1 = "Mars", planet2 = "Neptune") == ('Jupiter', 'Saturn', 'Uranus')

