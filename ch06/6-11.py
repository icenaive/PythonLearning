citiey = {
    'a': {'nation' : '1'}
}

for key, values in citiey.items():
    print(key)
    for values_key, values_value in values.items():
        print(values_key,values_value )