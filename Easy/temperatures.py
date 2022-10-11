t = []
n = int(input())
temp = 5527
if n == 0:
    print("0")  # the number of temperatures to analyse
else:
    for i in input().split():
        t.append(int(i))
    for j in range(len(t)):
        if abs(t[j]) <= abs(temp):
            if abs(t[j]) == temp:
                temp = -t[j]
            else:
                temp = t[j]

    print(temp)
