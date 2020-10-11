file_name = './ch10/python_learn.txt'

with open('/home/manjaro/WorkSpace/PythonLearning/ch10/python_learn.txt') as file1:
    for line in file1:
        print(line.rstrip())
with open('/home/manjaro/WorkSpace/PythonLearning/ch10/python_learn.txt') as file1:
    lines = file1.readlines()
with open('/home/manjaro/WorkSpace/PythonLearning/ch10/python_learn.txt') as file1:
    contents = file1.read()
    print(contents.rstrip())
with open(file_name) as file1:
    for line in file1:
        print("10-2: ", line.replace('python', 'c').rstrip())

for line in lines:
    print(line.rstrip())