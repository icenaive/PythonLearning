def build(name, xing, **qita):
    res = {}
    res['name'] = name
    res['xing'] = xing
    for key, value in qita.items():
        res[key] = value
    return res

print(build('a', 'v', num1 = '12', num2 = '34'))