#!/usr/bin/env python
# coding: utf-8

# In[1]:

#NAME: A. SAI NITISH REDDY
#ROLL NO:50
#SAP ID:500075162
#BATCH: CSC AI AND ML -2


box = [' ' for x in range(10)]

def input_choiseter(choiseter, pos):
    box[pos] = choiseter

def Empty_box(pos):
    return box[pos] == ' '

def display_box(box):
    print('   |   |')
    print(' ' + box[1] + ' | ' + box[2] + ' | ' + box[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + box[4] + ' | ' + box[5] + ' | ' + box[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + box[7] + ' | ' + box[8] + ' | ' + box[9])
    print('   |   |')
    
def winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def user_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if Empty_box(move):
                    run = False
                    input_choiseter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def AI_move():
    moves_possible = [x for x, choiseter in enumerate(box) if choiseter == ' ' and x != 0]
    move = 0

    for choise in ['O', 'X']:
        for i in moves_possible:
            boxCopy = box[:]
            boxCopy[i] = choise
            if winner(boxCopy, choise):
                move = i
                return move

    open_corner = []
    for i in moves_possible:
        if i in [1,3,7,9]:
            open_corner.append(i)
            
    if len(open_corner) > 0:
        move = random_choise(open_corner)
        return move

    if 5 in moves_possible:
        move = 5
        return move

    open_edge = []
    for i in moves_possible:
        if i in [2,4,6,8]:
            open_edge.append(i)
            
    if len(open_edge) > 0:
        move = random_choise(open_edge)
        
    return move

def random_choise(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def box_full(box):
    if box.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('AI Tic Tac Toe!')
    display_box(box)

    while not(box_full(box)):
        if not(winner(box, 'O')):
            user_move()
            display_box(box)
        else:
            print('AI WON!!')
            break

        if not(winner(box, 'X')):
            move = AI_move()
            if move == 0:
                print('Game Is Tie!')
            else:
                input_choiseter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                display_box(box)
        else:
            print('user won!!')
            break

    if box_full(box):
        print('Game Is Tie!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        box = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break

