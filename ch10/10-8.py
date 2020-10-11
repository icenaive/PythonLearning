file1 = "cats.txt"
file2 = "dogss.txt"

try:
    with open(file1, 'r') as cats, open(file2, 'r') as dogs:
        cat_lines = cats.readlines()
        dog_lines = dogs.readlines()
except FileNotFoundError:
    # print("file is not found")
    pass
else:
    for line in cat_lines:
        print(line.strip())
    for line in dog_lines:
        print(line.strip())
