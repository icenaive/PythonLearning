dir = {
    'a': '1',
    'b': '2',
    'c': '25',
    'd': '3'
}
for key, values in dir.items():
    print(key + " : " + values)
for key in dir.keys():
    print(key)
for values in dir.values():
    print(values)