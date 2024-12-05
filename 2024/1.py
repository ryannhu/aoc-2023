import collections
list1, list2 = [], []
count = collections.defaultdict(lambda: 0)
with open('1.in', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    for line in lines:
        list1.append(line.split()[0])
        list2.append(line.split()[1])
        count[line.split()[1]] += 1
list1.sort()
list2.sort()

ans = 0

for i, j in zip(list1, list2):
    ans += abs(int(i) - int(j))

print(ans)

ans = 0
for n in list1:
    ans += int(n)    * count[n]
print(ans)
        