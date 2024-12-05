
example = """Time:      7  15   30
Distance:  9  40  200"""

input = """Time:        50     74     86     85
Distance:   242   1017   1691   1252"""

aInput ="""Time:        50748685
Distance:   242101716911252""" 

input = aInput.split("\n")
# part a) solution
time = input[0].split(" ")
time = [i for i in time if i != ""]
distance = input[1].split(" ")
distance = [i for i in distance if i != ""]
n = len(time)
ans = 1
for i in range(1, n):
    curTime = int(time[i])
    curDistance = int(distance[i])
    sum = 0
    for speed in range(curTime):
        moved = speed * (curTime - speed)
        if i == 2: print(moved, curDistance)
        if moved > curDistance:
            sum += 1
    ans *= sum
print(time)
print(distance)
print(ans)


