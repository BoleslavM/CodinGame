n = int(input())
v = []

for i in input().split():
    v.append(int(i))

curren_max = v[0]
current_min = v[0]
result = 0

for i in v:

    if i > curren_max:
        curren_max = i
        current_min = i

    elif i < current_min:
        current_min = i

    temp = current_min - curren_max

    if temp < result:
        result = temp

print(result)
