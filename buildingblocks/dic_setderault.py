"""
d = {}
# To add a key->value pair, do the following:
d.setdefault(key, []).append(value)

# To retrieve a list of the values for a key
list_of_values = d[key]

# To remove a key->value pair is still easy, if
# you don't mind leaving empty lists behind when
# the last value for a given key is removed:
d[key].remove(value)

# Despite the empty lists, it's still possible to 
# test for the existance of values easily:
if d.has_key(key) and d[key]:
    pass # d has some values for key
"""
# Note: Each value can exist multiple times!
e = {}
print e
e.setdefault('Cars', []).append('Toyota')
print e
e.setdefault('Motorcycles', []).append('Yamaha')
print e
e.setdefault('Airplanes', []).append('Boeing')
print e
e.setdefault('Cars', []).append('Honda')
print e
e.setdefault('Cars', []).append('BMW')
print e
e.setdefault('Cars', []).append('Toyota')
print e

# NOTE: now e['Cars'] == ['Toyota', 'Honda', 'BMW', 'Toyota']
e['Cars'].remove('Toyota')
print e
# NOTE: it's still true that ('Toyota' in e['Cars'])
