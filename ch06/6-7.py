dir1 = {
    'first_name': '1',
    'last_name': '2',
    'age': '25',
    'city': 'bj'
}
dir2 = {
    'first_name': '1',
    'last_name': '2',
    'age': '25',
    'city': 'bj'
}
dir3 = {
    'first_name': '1',
    'last_name': '2',
    'age': '25',
    'city': 'bj'
}
people = [dir1, dir2, dir3]
for peo in people:
    for key, value in peo.items():
        print(key, value)