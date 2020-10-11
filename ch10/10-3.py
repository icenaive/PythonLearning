names = input("input your name: ")
with open("guest.txt", 'a') as file1:
    file1.write("names = %s\n" % names)