def build(name, xing, **qita):
    res = {}
    res['name'] = name
    res['xing'] = xing
    for key, value in qita.items():
        res[key] = value
    return res

car = build('s', 'o', color = 'bulu', two = True)
print(car)