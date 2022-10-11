# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())
    x = light_x-initial_tx
    y = light_y-initial_ty
    if abs(x)==abs(y):
        if x==y and x>0:
            print('SE')
            initial_tx+=1
            initial_ty+=1
        elif x==y and x<0:
            print('NW')
            initial_tx-=1
            initial_ty-=1
        elif x==-y and x>0:
            print('NE')
            initial_tx+=1
            initial_ty-=1
        elif -x==y and x<0:
            print('SW')
            initial_tx-=1
            initial_ty+=1
    else:
        if x<0 and abs(x)>abs(y):
            print('W')
            initial_tx-=1
        elif abs(y)>abs(x) and y>0:
            print('S')
            initial_ty-=1
        elif abs(x)>abs(y) and x>0:
            print('E')
            initial_tx+=1
        elif abs(y)>abs(x) and y<0:
            print('N')
            initial_ty+=1
