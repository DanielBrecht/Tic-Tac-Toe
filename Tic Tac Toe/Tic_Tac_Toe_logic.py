""" THE LOGIC OF
        TIC TAC TOE"""


###### VARIABLES etc. ######
turn = "player1"

player1_spaces = [] #e.g.[[3,1], [1,1], [2,1]]
player2_spaces = []
player_spaces = [player1_spaces] #if turn == 'player2': player_spaces = [player2_spaces]

sort_list1 = []
sort_list2 = []

correct_spaces = 0 #finding a complete line
game_finished = False
							


######### SORT #########
def sort_spaces():
    global turn, player1_spaces, player2_spaces, player_spaces,\
           sort_list1, sort_list2
    
    for e in range(1,4):
                    
        if turn == 'player1':
            for i in player1_spaces:
                if e == i[0]:
                    sort_list1.append(i)
        else:
            for i in player2_spaces:
                if e == i[0]:
                    sort_list1.append(i)
        
        for l in sort_list2:
            if l in sort_list1:
                sort_list1.remove(l)
            
        for u in range(1,4):
            for d in sort_list1:
                if u == d[1]:
                    sort_list2.append(d)
                   
    sort_list1 = []


    player_spaces[0] = sort_list2
    sort_list2 = []                     	
											                                            
            
# print(player2_spaces, 'player_spaces')
# print(sort_list1, 'sort_list1')
# print(sort_list2, 'sort_list2')

            


####### COMBINATIONS ######
															
horizontal_1 = [[1,1], [2,1], [3,1]]                    	
horizontal_2 = [[1,2], [2,2], [3,2]]                    	
horizontal_3 = [[1,3], [2,3], [3,3]]                    	
horizontals = [horizontal_1, horizontal_2, horizontal_3]	
															
vertical_1 = [[1,1], [1,2], [1,3]]              	
vertical_2 = [[2,1], [2,2], [2,3]]              	
vertical_3 = [[3,1], [3,2], [3,3]]              	
verticals = [vertical_1, vertical_2, vertical_3]	
													
diagonal_1 = [[1,1], [2,2], [3,3]]  	
diagonal_2 = [[3,1], [2,2], [1,3]]  	
diagonals = [diagonal_1, diagonal_2]	
															
combinations = [horizontal_1, horizontal_2, horizontal_3,\
                vertical_1, vertical_2, vertical_3,\
                diagonal_1, diagonal_2]
															


#### CHECK COMBINATIONS ####
def check_combos():
    global correct_spaces, combinations, player_spaces, game_finished
    
    sort_spaces()
    for h in combinations:
        correct_spaces = 0
        for g in h:
    #         print(g)
            for i in player_spaces[0]:
                if g == i:
                    correct_spaces += 1
                if correct_spaces == 3:
                    game_finished = True
                    return game_finished


#     if game_finished:
#         print('YES SIR')
#     else:
#         print('NOOOO')
#     #     Gameloop
# 							