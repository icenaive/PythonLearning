sandwich_orders = ['a', 'b', 'c', 'd']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("i make your %s sandwich" % sandwich)
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)

while 'a' in finished_sandwiches:
    finished_sandwiches.remove('a')
print(finished_sandwiches)
