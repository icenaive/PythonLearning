places = {
    'a': ['1', '2'],
    'b': ['3', '4']
}
for key, values in places.items():
    print(key)
    for value in values:
        print(value)
    print()