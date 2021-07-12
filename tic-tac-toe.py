active = True
board  = {"topl": " ", "topm": " ", "topr": " ", 
    "midl": " ", "mid" : " ", "midr": " ", "botl": " ", "botm": " ", "botr": " "}
def draw_board(board):
    print(f"{board['topl']}|{board['topm']}|{board['topr']}")
    print("-----")
    print(f"{board['midl']}|{board['mid']}|{board['midr']}")
    print("-----")
    print(f"{board['botl']}|{board['botm']}|{board['botr']}")
def check_winner(board):
    winner = None
    game_over = False  
    #check for horizontal winning possibilities  for x
    if board['topl'] == 'x'  and board ['topm'] == "x" and board['topr']  == "x" :
        winner = x
        print("The winner is x")
        game_over = True      
    elif board['midl'] == 'x'  and board ['mid'] == "x" and board['midr']  == "x" :
        winner = x
        print("The winner is x")
        game_over = True  
    elif board['botl'] == 'x'  and board ['botm'] == "x" and board['botr']  == "x" : 
        winner = x      
        print("The winner is x")
        game_over = True
    #Check Vertical winning possibilities for x
    elif board['botl'] == 'x'  and board ['midl'] == "x" and board['botl']  == "x" :       
        winner = x
        print("The winner is x")
        game_over = True
    elif board['topm'] == 'x'  and board ['mid'] == "x" and board['botm']  == "x" :    
        winner = x  
        print("The winner is x")
        winner = x
        game_over = True
    elif board['topr'] == 'x'  and board ['midr'] == "x" and board['botr']  == "x" :       
        winner = x
        print("The winner is x")
        game_over = True
    # Check diagonal winning possibilities for x
    elif board['topl'] == 'x' and board['mid'] == 'x' and board['botr'] == 'x':
        winner = x
        winner = x
        print("The winner is x")
        game_over = True
    elif board['botl'] == 'x' and board['mid'] == 'x' and board['topr'] == 'x':
        winner = x
        print("The winner is x")
        game_over = True
        game_over = True
    #Check horizontal  winning possibilities for o
    elif board['topl'] == 'o'  and board ['topm'] == "o" and board['topr']  == "o" :
        winner = o
        print("The winner is o")
        game_over = True 
    elif board['midl'] == 'o'  and board ['mid'] == "o" and board['midr']  == "o" :
        winner = o
        print("The winner is o")
        game_over = True  
    #Check Vertical winning possibilities for o
    elif board['botl'] == 'o'  and board ['midl'] == "o" and board['botl']  == "o" :   
        winner = o    
        print("The winner is o")
        game_over = True
    elif board['topm'] == 'o'  and board ['mid'] == "o" and board['botm']  == "o" :  
        winner = o     
        print("The winner is o")
        game_over = True
    elif board['topr'] == 'o'  and board ['midr'] == "o" and board['botr']  == "o" :     
        winner = o  
        print("The winner is o")
        game_over = True
    # Check diagonal winning possibilities for o
    elif board['botl'] == 'o'  and board ['botm'] == "o" and board['botr']  == "o" : 
        winner = o
        print("The winner is o")
        game_over = True
    elif board['topl'] == 'o' and board['mid'] == 'o' and board['botr'] == 'o':
        winner = o
        winner = o
        print("The winner is o")
        game_over = True
    elif board['botl'] == 'o' and board['mid'] == 'o' and board['topr'] == 'o':
        winner = o
        print("The winner is o")
        game_over = True      
    elif winner == None and " " not in board.values():

        print("Tie")
        game_over = True
    
    else:
        pass 
    return game_over

def check_vacancy(board, move):
    global game_over, active
    allowed = True
    if move == "q":
        active == False
        game_over = True
    else:
        try:
            if board[move] == " ":
                allowed = True
            elif board[move] != " ":
                allowed = False
        except KeyError:
           pass
    
    return allowed
def x_control(board):
    x_move = input('x,what is your move?: ') 
    if x_move == 'q':
        print("x has exited the game")
        active = False
        game_over = True   
    elif check_vacancy(board, x_move) == True:
        board[x_move] = "x"
        draw_board(board)
    else:
        print("Spot Already taken")
        x_control(board)
def o_control(board):
    global active, game_over
    o_move = input('o,what is your move?: ')
    if o_move == 'q':
        print("o has exited the game")
        active = False
        game_over = True
  
    elif check_vacancy(board, o_move) == True:
        board[o_move] = "o"
        draw_board(board)
    else:
        print("Spot Already taken")
        o_control(board)
print("Welcome to the tic-tac-toe game, if your opponent quits, you should quit too!")
while active:
  
    x_control(board)
    if check_winner(board) == True:
        break
   
    o_control(board)
    if check_winner(board) == True:
        break
 
    
   
  
    

   
    

     
        
         
     
    
     
     
  

     
    
   
    
