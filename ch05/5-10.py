nums = list(range(1, 10))
for num in nums:
    if num == 1:
        print("%dst" % num)
    elif num == 2:
        print("%dnd" % num)
    elif num == 3:
        print("%drd" % num)
    else:
        print("%dth" % num)