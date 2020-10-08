def show(names):
    for name in names:
        print(name)

def make(names):
    for index in range(len(names)):
        names[index] = "this greate " + names[index].title()

names = ['a', 'b', 'c']

#传递副本
make(names[:])
print(names)
#传递引用
make(names)
print(names)
