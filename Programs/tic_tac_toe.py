

#print what letter each player will get (X or O)
print("Tic-Tac-Toe Game: \nPlayer 1: You are Xs \nPlayer 2: You are Os")
#turns continue as long as no one wins or if the board is not full
keep_playing = True
#keep track of turns beginning at 1
turns = 1
#dictionary of options to place letters beginning completely empty for start of game
options = {'Top Left' : ' ', 'Top Middle' : ' ', 'Top Right' : ' ', 'Center Left': ' ', 'Center Middle' : ' ', 'Center Right' : ' ', 'Bottom Left' : ' ', 'Bottom Middle' : ' ', 'Bottom Right' : ' '}

while keep_playing:
    #on odd turn numbers, player 1 places a letter on the board
    if turns % 2 != 0:
        #list available options
        choice1 = input("Player one, where would you like to place your X.  Your options are: \n{}\n\n".format([x for x in options if options[x] == ' ']))
        #if they do not choose a valid option, let the player try to choose one again
        if choice1 not in list(options.keys()):
            print("\nInvalid Entry. Try Again.\n")
            continue
        else:
            #if the player's choice on the board is not already filled on the board, allow the player to fill it.  else: let the player try again
            if options[choice1] != 'X' and options[choice1] != 'O':
                options[choice1] = 'X'
            else:
                print("\nAn {} is already there. Try again in a different spot\n".format(options[choice1]))
                continue
            #on even turn numbers, player 2 places a letter on the board
    elif turns % 2 == 0:
        #list available options
        choice2 = input("Player two, where would you like to place your O.  Your options are: \n{}\n\n".format([x for x in options if options[x] == ' ']))
        #if a valid option from the list is not chosen, let the player try to choose one again
        if choice2 not in list(options.keys()):
            print("\nInvalid Entry. Try Again.\n")
            continue
        else:
             #if the player's choice on the board is not already filled on the board, allow the player to fill it.  else: let the player try again
            if options[choice2] != 'X' and options[choice2] != 'O':
                options[choice2] = 'O'
            else:
                print("\nAn {} is already there. Try again in a different spot\n".format(options[choice2]))
                continue
            #return game board after each play so the player knows available options for the player's next turn
    print("\n\nGame board after turn number {}\n\n".format(turns))
    #allow adeqaute space between game board spots so the players are able to more clearly see the board as well as available options
    print("{TL}  | {TM} | {TR} \n---|---|--- \n{CL}  | {CM} | {CR} \n---|---|--- \n{BL}  | {BM} | {BR} \n\n"\
          .format(TL = options['Top Left'], TM = options['Top Middle'], TR = options['Top Right'], \
          CL = options['Center Left'], CM = options['Center Middle'], CR = options['Center Right'], \
          BL = options['Bottom Left'], BM = options['Bottom Middle'], BR = options['Bottom Right']))
    #if the player gets three in a row, the player wins the game, keep_playing is assigned to false so the while loop terminates and the game ends
    if ((options['Top Left'] == 'X' and options ['Top Middle'] == 'X' and options ['Top Right'] == 'X') or \
        (options['Center Left'] == 'X' and options ['Center Middle'] == 'X' and options ['Center Right'] == 'X') or \
        (options['Bottom Left'] == 'X' and options ['Bottom Middle'] == 'X' and options ['Bottom Right'] == 'X') or \
        (options['Top Left'] == 'X' and options['Center Middle'] == 'X' and options['Bottom Right'] == 'X') or \
        (options['Top Right'] == 'X' and options['Center Middle'] == 'X' and options['Bottom Left'] == 'X') or \
        (options['Top Left'] == options['Center Left'] == options ['Bottom Left'] == 'X') or \
        (options['Top Middle'] == options['Center Middle'] == options ['Bottom Middle'] == 'X') or \
        (options['Top Right'] == options['Center Right'] == options ['Bottom Right'] == 'X')):
        print("Player 1 is the Winner!!!")
        keep_playing = False
    elif ((options['Top Left'] == 'O' and options ['Top Middle'] == 'O' and options ['Top Right'] == 'O') or \
          (options['Center Left'] == 'O' and options ['Center Middle'] == 'O' and options ['Center Right'] == 'O') or \
          (options['Bottom Left'] == 'O' and options ['Bottom Middle'] == 'O' and options ['Bottom Right'] == 'O') or \
          (options['Top Left'] == 'O' and options['Center Middle'] == 'O' and options['Bottom Right'] == 'O') or \
          (options['Top Right'] == 'O' and options['Center Middle'] == 'O' and options['Bottom Left'] == 'O') or \
          (options['Top Left'] == options['Center Left'] == options ['Bottom Left'] == 'O') or \
          (options['Top Middle'] == options['Center Middle'] == options ['Bottom Middle'] == 'O') or \
          (options['Top Right'] == options['Center Right'] == options ['Bottom Right'] == 'O')):
        print("Player 2 is the Winner!!!")
        keep_playing = False
        #if all game board spaces are filled with an 'X' or an 'O', no player wins the game, keep_playing is assigned to false to terminate the while loop and the game ends
    elif ' ' not in list(options.values()):
        print("No one wins this game.")
        keep_playing = False
        #add turns after each round
    turns += 1
    #Once game is finished, print 'game over'
print("Game Over")