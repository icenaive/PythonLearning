res = {}
active = True
while active:
    name = input("name: ")
    place = input("place: ")
    res[name] = place
    jixu = input("no? ")
    if jixu == 'no':
        active = False
print(res)
    