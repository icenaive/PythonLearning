file_name = "guest_book.txt"

name = input("please input your name: ")
while name != '#':
    print("welcome " + name + "\n")
    with open(file_name, 'a') as file1:
        file1.write("%s is comed\n" % name)
    name = input("ypur name: ")