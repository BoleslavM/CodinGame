# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

liste = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
# game loop
while True:
    for i in range(8):
        mountain_h = int(input())
        liste[i] = mountain_h

    print(liste.index(max(liste)))
    liste[liste.index(max(liste))] = -1