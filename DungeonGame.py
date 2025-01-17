#! /usr/bin/python3

import os
import random


# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [ (0,0), (1,0), (2,0), (3,0), (4,0),
          (0,1), (1,1), (2,1), (3,1), (4,1),
          (0,2), (1,2), (2,2), (3,2), (4,2),
          (0,3), (1,3), (2,3), (3,3), (4,3),
          (0,4), (1,4), (2,4), (3,4), (4,4)]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def draw_grid(old_player, player, monster):
    print(' _' * 5)
    tile = '|{}'
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
                
            if cell == player:
                if cell == monster:
                    output = tile.format('X')
                else:
                    output = tile.format('o')
                
            elif cell in old_player:
                output = tile.format('*')
                
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
    
            if cell == player:
                if cell == monster:
                    output = tile.format('X|')
                else:
                    output = tile.format('o|')
                 
            elif cell in old_player:
                output = tile.format('*|')
            
            else:
                output = tile.format('_|')
        print(output, end=line_end)

        


def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        x -= 1
    if move == 'RIGHT':
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1
    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x , y = player
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')
    return moves

def game_loop():
    monster, door, player = get_locations()
    old_player = []
    
    while True:
        valid_moves = get_moves(player)
        old_player.append(player)

        print("You're currently in room {}".format(player))
        print("You can move {}".format(', '.join(valid_moves)))
        print("Enter QUIT to quit!")
        draw_grid(old_player, player, monster)
        
        if player == monster:
            print('Oh no, you ran into the monster, you lose!')
            break
        elif player == door:
            print('You found the exit! You win!')
            break

        move = input('> ')
        move = move.upper()

        if move == 'QUIT':
            break
        if move not in coordinates:
            print('\n ** Type better, fool! **\n')
            input('press return if you\'re ready ')
            continue
        if move in valid_moves:
            player = move_player(player, move)
        else:
            print('\n ** Walls are hard! Don\'t run into them! **\n')
            input('press return if you\'re ready ')
            continue


clear_screen()
print('Welcome to the dungeon!')
input('Press return to start!')
coordinates = ['LEFT', 'RIGHT', 'UP', 'DOWN']

again = 'y'
while again == 'y':
    game_loop()
    again = input('Play again? ')
    

