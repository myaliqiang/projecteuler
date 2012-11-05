with open('names.txt') as f:
    line = f.read()

name_dict = {}
grade = 1
for i in ['A','B','C','D','E','F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    name_dict[i] = grade
    grade += 1

# test
score = 0
for i in 'COLIN':
    score += name_dict[i]
# print name_dict
items = line.split(',')
pos = 0
total = 0
new_items = []
for item in items:
    item = item.strip('"')
    new_items.append(item)

new_items.sort() #we need to sort the names.txt

for item in new_items:
    pos += 1
    score = 0
    for i in item:
        score += name_dict[i]
    # print item, score
    score *= pos
    total += score

print total