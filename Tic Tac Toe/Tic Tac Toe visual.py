import sys
import pygame
import Tic_Tac_Toe_logic as ttt



pygame.init()
clock = pygame.time.Clock()

clicked = False
action = False

field = ['blank', 'blank', 'blank',\
         'blank', 'blank', 'blank',\
         'blank', 'blank', 'blank']

### GAME WINDOW
# scale = 1
screen_height = 700 #600 * scale 
screen_width = 700 #* scale
screen = pygame.display.set_mode((screen_width, screen_height))


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')


#imgaes
grid_img = pygame.image.load('grid.png').convert_alpha()
grid = pygame.transform.scale(grid_img, (700, 700))

cross_img = pygame.image.load('cross.png').convert_alpha()
circle_img = pygame.image.load('circle.png').convert_alpha()

### GAME LOOP ###
run = True
while run:
    
    pos = pygame.mouse.get_pos()
    
    screen.fill((202, 228, 241))
    screen.blit(grid, (0,0))
    

												
    if field[0] != 'blank':
        if field[0] == 'cross':
            screen.blit(cross_img, (35,35))
        else:
            screen.blit(circle_img, (35, 35))
												
    if field[1] != 'blank':
        if field[1] == 'cross':
            screen.blit(cross_img, (268, 35))
        else:
            screen.blit(circle_img, (265, 35))
												
    if field[2] != 'blank':
        if field[2] == 'cross':
            screen.blit(cross_img, (495, 35))
        else:
            screen.blit(circle_img, (495, 35))
												
    if field[3] != 'blank':
        if field[3] == 'cross':
            screen.blit(cross_img, (35, 266))
        else:
            screen.blit(circle_img, (35, 266))
												
    if field[4] != 'blank':
        if field[4] == 'cross':
            screen.blit(cross_img, (268, 266))
        else:
            screen.blit(circle_img, (265, 266))
												
    if field[5] != 'blank':
        if field[5] == 'cross':
            screen.blit(cross_img, (495, 266))
        else:
            screen.blit(circle_img, (495, 266))
												
    if field[6] != 'blank':
        if field[6] == 'cross':
            screen.blit(cross_img, (35, 497))
        else:
            screen.blit(circle_img, (35, 497))
												
    if field[7] != 'blank':
        if field[7] == 'cross':
            screen.blit(cross_img, (268, 497))
        else:
            screen.blit(circle_img, (265, 497))
												
    if field[8] != 'blank':
        if field[8] == 'cross':
            screen.blit(cross_img, (495, 497))
        else:
            screen.blit(circle_img, (495, 497))
												

    
    
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
            clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False
        if clicked == True:
																				
            if pos[0] >= 0 and pos[1] >= 0 and pos[0] <= 235 and pos[1] <= 230 and field[0] == 'blank':
                if ttt.turn == 'player1':
                    field[0] = 'cross'
                    ttt.player1_spaces.append([1,1])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[0] = 'circle'
                    ttt.player2_spaces.append([1,1])
                    ttt.turn = 'player1'
												
            if pos[0] >= 250 and pos[1] >= 0 and pos[0] <= 450 and pos[1] <= 230 and field[1] == 'blank':
                if ttt.turn == 'player1':
                    field[1] = 'cross'
                    ttt.player1_spaces.append([2,1])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[1] = 'circle'
                    ttt.player2_spaces.append([2,1])
                    ttt.turn = 'player1'
												
            if pos[0] >= 470 and pos[1] >= 0 and pos[0] <= 700 and pos[1] <= 230 and field[2] == 'blank':
                if ttt.turn == 'player1':
                    field[2] = 'cross'
                    ttt.player1_spaces.append([3,1])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[2] = 'circle'
                    ttt.player2_spaces.append([3,1])
                    ttt.turn = 'player1'
																				
            if pos[0] >= 0 and pos[1] >= 255 and pos[0] <= 235 and pos[1] <= 455 and field[3] == 'blank':
                if ttt.turn == 'player1':
                    field[3] = 'cross'
                    ttt.player1_spaces.append([1,2])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[3] = 'circle'
                    ttt.player2_spaces.append([1,2])
                    ttt.turn = 'player1'
												
            if pos[0] >= 250 and pos[1] >= 255 and pos[0] <= 450 and pos[1] <= 455 and field[4] == 'blank':
                if ttt.turn == 'player1':
                    field[4] = 'cross'
                    ttt.player1_spaces.append([2,2])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[4] = 'circle'
                    ttt.player2_spaces.append([2,2])
                    ttt.turn = 'player1'
												
            if pos[0] >= 470 and pos[1] >= 255 and pos[0] <= 700 and pos[1] <= 455 and field[5] == 'blank':
                if ttt.turn == 'player1':
                    field[5] = 'cross'
                    ttt.player1_spaces.append([3,2])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[5] = 'circle'
                    ttt.player2_spaces.append([3,2])
                    ttt.turn = 'player1'
																				
            if pos[0] >= 0 and pos[1] >= 457 and pos[0] <= 235 and pos[1] <= 700 and field[6] == 'blank':
                if ttt.turn == 'player1':
                    field[6] = 'cross'
                    ttt.player1_spaces.append([1,3])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[6] = 'circle'
                    ttt.player2_spaces.append([1,3])
                    ttt.turn = 'player1'
												
            if pos[0] >= 250 and pos[1] >= 457 and pos[0] <= 450 and pos[1] <= 700 and field[7] == 'blank':
                if ttt.turn == 'player1':
                    field[7] = 'cross'
                    ttt.player1_spaces.append([2,3])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[7] = 'circle'
                    ttt.player2_spaces.append([2,3])
                    ttt.turn = 'player1'
												
            if pos[0] >= 470 and pos[1] >= 457 and pos[0] <= 700 and pos[1] <= 700 and field[8] == 'blank':
                if ttt.turn == 'player1':
                    field[8] = 'cross'
                    ttt.player1_spaces.append([3,3])
                    ttt.turn = 'player2'
                elif ttt.turn == 'player2':
                    field[8] = 'circle'
                    ttt.player2_spaces.append([3,3])
                    ttt.turn = 'player1'
            print(ttt.player1_spaces, '\n', ttt.player2_spaces, '\n')

    if ttt.check_combos():
        sys.exit()
																				


    if event.type == pygame.QUIT:
        run = False

    
    clock.tick(120)            
    pygame.display.update()
    
sys.exit()