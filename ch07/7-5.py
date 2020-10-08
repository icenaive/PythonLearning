flag = True
while flag:
    age = input("age: ")
    age = int(age)
    if age > 200:
        flag = False
    else:
        if age < 3:
            print("mianfei")
        elif age < 12:
            print("10")
        elif age >= 12:
            print("15")