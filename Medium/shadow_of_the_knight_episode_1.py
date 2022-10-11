# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
left = 0
right = w - 1
top = h - 1
bot = 0
sauth = y0
sautx = x0
while True:
    bomb_dir = input()

    if bomb_dir == 'U':
        top = sauth
        top -= 1
        sauth = int(round((top + bot) / 2))

    elif bomb_dir == 'UR':
        left = sautx + 1
        top = sauth - 1
        sauth = int(round((bot + top) / 2))
        sautx = int(round((left + right) / 2))

    elif bomb_dir == 'UL':
        top = sauth - 1
        right = sautx - 1
        sauth = int(round((bot + top) / 2))
        sautx = int(round((left + right) / 2))

    elif bomb_dir == 'D':
        bot = sauth
        bot += 1
        sauth = int(round((top + bot) / 2))

    elif bomb_dir == 'DR':
        bot = sauth + 1
        left = sautx + 1
        sauth = int(round((bot + top) / 2))
        sautx = int(round((left + right) / 2))

    elif bomb_dir == 'DL':
        bot = sauth + 1
        right = sautx - 1
        sauth = int(round((bot + top) / 2))
        sautx = int(round((left + right) / 2))

    elif bomb_dir == 'L':
        right = sautx - 1
        sautx = int(round((left + right) / 2))

    elif bomb_dir == 'R':
        left = sautx + 1
        sautx = int(round((left + right) / 2))

    print(sautx, sauth)