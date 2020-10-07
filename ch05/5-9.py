names = ['a', 'B', 'c']
names.append('admin')

new_names = [name.lower() for name in names]

new_name = names[:]
new_name.append('d')
new_name.append('b')

for new in new_name:
    if new.lower() in new_names:
        print("is in ")
    else:
        print("you can use")