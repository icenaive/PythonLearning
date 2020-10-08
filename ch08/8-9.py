names = ['a', 'b', 'c']
def show(names):
    for name in names:
        print(name)

#传递引用
show(names)
#传递副本
show(names[:])