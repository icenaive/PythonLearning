names = ['a', 'b', 'c']
print("yao qing %s chi fan" % names[0])
print("yao qing %s chi fan" % names[1])
print("yao qing %s chi fan" % names[2])
print(names[1] + "bu lai")
names[1] = 'd'
print("yao qing %s chi fan" % names[0])
print("yao qing %s chi fan" % names[1])
print("yao qing %s chi fan" % names[2])
print("i find a big zuo zi")
names.insert(0, 'e')
names.insert(int(len(names) / 2), 'f')
names.append('g')
print("yao qing %s chi fan" % names[0])
print("yao qing %s chi fan" % names[1])
print("yao qing %s chi fan" % names[2])
print("yao qing %s chi fan" % names[3])
print("yao qing %s chi fan" % names[4])
print("yao qing %s chi fan" % names[5])
print("i change zhu yi")
while(len(names) != 2):
    name = names.pop()
    print("i am sorry %s" % name)
print("yao qing %s chi fan" % names[0])
print("yao qing %s chi fan" % names[1])
del names[0]
del names[0]
print(names)