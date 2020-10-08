def album(name1, name2, num = ''):
    res = {name1 : name2}
    if num:
        res['cnt'] = num
    return res

print(album('a', 'b', '200000'))