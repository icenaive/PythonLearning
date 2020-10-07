names = ['a', 'b', 'c']
names.append('admin')

if names:
    for name in names:
        if name == 'admin':
            print('admin')
        else:
            print("other")
else:
    print("empty")

while names:
    names.pop()
if names:
    print("full")
else:
    print("empty")