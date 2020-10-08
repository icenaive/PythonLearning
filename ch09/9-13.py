from collections import OrderedDict

dir = OrderedDict()

dir['a'] = 1
dir['b'] = 12
dir['sd'] = 133
# dir = {
#     'a': '1',
#     'b': '2',
#     'c': '25',
#     'd': '3'
# }

dir2 = {}
dir2['d'] = 1
dir2['adf'] = 21
dir2['23'] = 123
for key, values in dir.items():
    print(key + " : " + str(values))
    
for key, values in dir2.items():
    print(key + " : " + str(values))
# for key in dir.keys():
#     print(key)
# for values in dir.values():
#     print(values)