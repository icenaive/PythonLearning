rivers = {
    'nile': 'egypt',
    'a': 'b',
    'c': 'd'
}

names = ['a', 'd']
for name in names:
    if name in rivers.keys():
        print("is in")
    else:
        print("not in ")