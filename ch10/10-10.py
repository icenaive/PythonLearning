def count_times(contents, word):
    return contents.lower().count(word.lower())

with open("cats.txt", 'r') as cats:
    lines = cats.readlines()
contents = ""
for line in lines:
    contents += line.strip()

print(count_times(contents, 'nAna'))