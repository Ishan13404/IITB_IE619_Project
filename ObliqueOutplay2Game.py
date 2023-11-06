import pygame

pygame.init()

# Defining Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (186, 232, 199)

Screen_Width = 1000
Screen_Height = 600
Card_Width=100
Card_Height=200
gameWindow = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("OBLIQUE OUTPLAY")

FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def TextOnScreen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])

def GameValue(Gameboard):
    nimber=0
    for piece in ["W1", "W2", "W3", "W4", "W5"]:
        nimber += len(Possible_Moves(Gameboard, piece))
    for piece in ["B1", "B2", "B3", "B4", "B5"]:
        nimber -= len(Possible_Moves(Gameboard, piece))
    return nimber/2

def get_piece(Gameboard, piece):
    for i in range(1, len(Gameboard)-1):
        for j in range(1, len(Gameboard)-1):
            if Gameboard[i][j]==piece:
                return [i,j]
    return [0,0]
def Possible_Moves(Gameboard, piece):
    moves=[]
    [piece_x, piece_y]=get_piece(Gameboard,piece)
    if piece in ["W1", "W2", "W3", "W4", "W5"]:
        if Gameboard[piece_x+1][piece_y-1]=="__":
            moves.append([piece_x+1,piece_y-1])
        if Gameboard[piece_x+1][piece_y+1]=="__":
            moves.append([piece_x+1,piece_y+1])

    if piece in ["B1", "B2", "B3", "B4", "B5"]:
        if Gameboard[piece_x-1][piece_y-1]=="__":
            moves.append([piece_x-1,piece_y-1])
        if Gameboard[piece_x-1][piece_y+1]=="__":
            moves.append([piece_x-1,piece_y+1])

    return moves

def Move_Piece(Gameboard, piece, arr, Player):
    if arr!="NA":
        [old_x, old_y] = get_piece(Gameboard, piece)
        new_x, new_y = arr[0], arr[1]
        Gameboard[old_x][old_y]="__"
        Gameboard[new_x][new_y]=piece
    else:
        print("Invalid Move! Please Retry!")
    return Gameboard, 3-Player

def Black_Wins(Gameboard):
    for i in ["W1", "W2", "W3", "W4", "W5"]:
        if Possible_Moves(Gameboard,i)!=[]:
            return 0
    return 1

def White_Wins(Gameboard):
    for i in ["B1", "B2", "B3", "B4", "B5"]:
        if Possible_Moves(Gameboard,i)!=[]:
            return 0
    return 1

def Homescreen():
    while(True):
        gameWindow.fill(background)
        TextOnScreen("Welcome to Oblique Outplay", (193,89, 65), Screen_Width*0.3, Screen_Height/2-25)
        TextOnScreen("Press any key to start", (193, 89,65), Screen_Width*0.3, Screen_Height/2+25)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                return

def Display_Rules():
    rule_text = [
        # "Rules of Oblique Outplay:",
        # "",
        "1. Gameplay:",
        "   Players take turns making their moves, starting with the player controlling the white tokens.",
        "",
        "2. Movement Rules:",
        "   Players move their tokens diagonally, one space at a time, towards their opponent's end row.",
        "   Tokens can only move diagonally forward, i.e., towards the opponent's end.",
        "   Tokens cannot move backward, horizontally, or vertically.",
        "",
        "3. Blocking and Obstruction:",
        "   Tokens cannot jump over other tokens, whether they belong to the same player or the opponent.",
        "   If a token's path is blocked by its own or the opponent's token, it cannot move to that square.",
        "   Once a token reaches the opponent's end row, it cannot move further.",
        "",
        "4. Objective:",
        "   The objective of the game is to strategically move your tokens in such a way that",
        "     your opponent is unable to make a valid move on their turn.",
        "",
        "5. Winning Condition:",
        "   A player loses the game if they are unable to move any of their tokens to a valid",
        "     empty square on their turn. In such a situation, the other player wins.",
        "",
        "                                                 Press any key to jump back into the Game! All the Best!"
    ]
    font = pygame.font.SysFont(None, 35)
    while(True):
        gameWindow.fill(background)
        TextOnScreen("Rules of Oblique Outplay:", black, 25,25)
        y = 50
        for line in rule_text:
            font = pygame.font.SysFont(None, 25)
            screen_text = font.render(line, True, black)
            gameWindow.blit(screen_text, [25, y])
            # TextOnScreen(line, black, 50, y)
            y += 25
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                return


def Display_Result(Gameboard, piece_r, piece_c, Piece_Selected, Player):
    while(True):
        gameWindow.fill(background)
        Draw_Game_Board(Gameboard, piece_r, piece_c, Piece_Selected)
        if Player==1:
            TextOnScreen("White", white, 700, 100)

        else :
            TextOnScreen("Black", black, 700, 100)

        TextOnScreen("         "+" Wins!!", blue, 700, 100)
        TextOnScreen("Press e to Exit", blue, 700, 100+50)
        TextOnScreen("Press r to Restart", blue, 700, 100+100)
        TextOnScreen("Game Evaluation: ", blue, 650, 300)
        if GameValue(Gameboard)>0:
            TextOnScreen(str(GameValue(Gameboard)), white, 900, 300)
        elif GameValue(Gameboard)==0:
            TextOnScreen(str(GameValue(Gameboard)), blue, 900, 300)    
        else :
            TextOnScreen(str(GameValue(Gameboard)), black, 900, 300)
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return False

def Draw_Game_Board(Gameboard, piece_r, piece_c, Piece_Selected):
    TextOnScreen("*** Oblique Outplay ***", (91,69,156), 650, 25)
    pygame.draw.rect(gameWindow, black, [10, 10, Screen_Height-20, Screen_Height-20],5)
    for i in [0.2, 0.4, 0.6, 0.8]:
        pygame.draw.line(gameWindow, black,[(Screen_Height-10)*i, 10],[(Screen_Height-10)*i,Screen_Height-15],5 )
        pygame.draw.line(gameWindow, black,[10, (Screen_Height-10)*i],[Screen_Height-15 ,(Screen_Height-10)*i],5 )

    n=len(Gameboard)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if Gameboard[i][j] in ["W1", "W2", "W3", "W4", "W5"]:
                pygame.draw.circle(gameWindow, white, [65 + 116.5*(j-1), 65 + 116.5*(i-1)], 40)
            if Gameboard[i][j] in ["B1", "B2", "B3", "B4", "B5"]:
                pygame.draw.circle(gameWindow, black, [65 + 116.5*(j-1),65 + 116.5*(i-1)], 40)
    
    if Piece_Selected !="":
        for [i,j] in Possible_Moves(Gameboard, Piece_Selected):
            pygame.draw.circle(gameWindow, red, [65 + 116.5*(j-1), 65 + 116.5*(i-1)], 43, 3)
    
    pygame.draw.circle(gameWindow, blue, [65 + 116.5*(piece_c-1), 65 + 116.5*(piece_r-1)], 43,3)
    pygame.display.update()



# Player 1 = WHITE     Player 2 = BLACK

def OO_Game():
    Game_Over=False
    View_Game_Value=False
    Gameboard=[
    ["XX", "XX", "XX", "XX", "XX", "XX", "XX"],
    ["XX", "W1", "W2", "W3", "W4", "W5", "XX"],
    ["XX", "__", "__", "__", "__", "__", "XX"],
    ["XX", "__", "__", "__", "__", "__", "XX"],
    ["XX", "__", "__", "__", "__", "__", "XX"],
    ["XX", "B1", "B2", "B3", "B4", "B5", "XX"],
    ["XX", "XX", "XX", "XX", "XX", "XX", "XX"]
    ]
    Player=1 
    piece_r, piece_c=1,1
    Piece_Selected=""
    while(not Game_Over):
        gameWindow.fill(background)
        TextOnScreen("Player to Move :", blue, 650, 100)
        if Player==1:
            TextOnScreen("White", white, 875, 100)
        else :
            TextOnScreen("Black", black, 875, 100)

        if not View_Game_Value:
            TextOnScreen("Use the         Pointer to select", black, 600, 350)
            TextOnScreen("Blue", blue, 705, 350)
            TextOnScreen("a piece. Use Arrow keys to ", black, 600, 400)
            TextOnScreen("navigate, press SPACEBAR to ", black, 600, 450)
            TextOnScreen("select. Available options", black, 600, 500)
            TextOnScreen("will be marked in       .", black, 600, 550)
            TextOnScreen("Red", red, 835, 550)
        if View_Game_Value:
            TextOnScreen("Game Evaluation: ", blue, 650, 400)
            if GameValue(Gameboard)>0:
                TextOnScreen(str(GameValue(Gameboard)), white, 900, 400)
            elif GameValue(Gameboard)==0:
                TextOnScreen(str(GameValue(Gameboard)), blue, 900, 400)    
            else :
                TextOnScreen(str(GameValue(Gameboard)), black, 900, 400)
            
            # Left_Options, Right_Options = [], []
            # for i in ["W1", "W2", "W3", "W4", "W5"]:    
            #     Temp_Gameboard=Gameboard.copy()
            #     for [x1,y1] in Possible_Moves(Temp_Gameboard,i):
            #         Player=1
            #         Temp2_Gameboard, Player = Move_Piece(Temp_Gameboard, i, [x1,y1], Player)
            #         Left_Options.append(GameValue(Temp2_Gameboard)*2)
            #         print("Gameboard :")
            #         print(Temp2_Gameboard)
            # Left_Options=unique(Left_Options)
            # for j in ["B1", "B2", "B3", "B4", "B5"]:
            #     Temp_Gameboard=Gameboard.copy()
            #     for [x1,y1] in Possible_Moves(Temp_Gameboard,j):
            #         Player=2
            #         Temp2_Gameboard, Player = Move_Piece(Temp_Gameboard, j, [x1,y1], Player)
            #         Right_Options.append(GameValue(Temp2_Gameboard)*2)
            #         print("Gameboard :")
            #         print(Temp2_Gameboard)
            # Right_Options=unique(Right_Options)
            # TextOnScreen("Left Options: " + str(Left_Options), black, 600, 400)
            # TextOnScreen("Right Options: "+ str(Right_Options), black, 600, 450)
            TextOnScreen("White has    Moves", blue, 650, 450)
            TextOnScreen("Black has    Moves", blue, 650, 500)
            n_white_moves, n_black_moves=0,0
            for piece in ["W1", "W2", "W3", "W4", "W5"]:
                n_white_moves += len(Possible_Moves(Gameboard, piece))
            for piece in ["B1", "B2", "B3", "B4", "B5"]:
                n_black_moves += len(Possible_Moves(Gameboard, piece))
            TextOnScreen(str(n_white_moves), white, 790, 450)
            TextOnScreen(str(n_black_moves), black, 790, 500)

        TextOnScreen("Press e to Exit", black, 650, 150)
        TextOnScreen("Press r to Restart", black, 650, 200)
        TextOnScreen("Press h for Help", black, 650, 250)
        TextOnScreen("Press TAB for Game Analysis", black, 600, 300)
        Draw_Game_Board(Gameboard, piece_r, piece_c, Piece_Selected)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                Game_Over=True 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                OO_Game()
                Game_Over=True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                Display_Rules()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                View_Game_Value= not View_Game_Value
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and piece_r in list(range(2,6)):
                piece_r-=1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and piece_r in list(range(1,5)):
                piece_r+=1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and piece_c in list(range(2,6)):
                piece_c-=1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and piece_c in list(range(1,5)):
                piece_c+=1
            if Player == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if [piece_r, piece_c] == get_piece(Gameboard, "W1") :
                    Piece_Selected="W1"
                if [piece_r, piece_c] == get_piece(Gameboard, "W2") :
                    Piece_Selected="W2"
                if [piece_r, piece_c] == get_piece(Gameboard, "W3") :
                    Piece_Selected="W3"
                if [piece_r, piece_c] == get_piece(Gameboard, "W4") :
                    Piece_Selected="W4"
                if [piece_r, piece_c] == get_piece(Gameboard, "W5") :
                    Piece_Selected="W5"
            if Player == 2 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if [piece_r, piece_c] == get_piece(Gameboard, "B1") :
                    Piece_Selected="B1"
                if [piece_r, piece_c] == get_piece(Gameboard, "B2") :
                    Piece_Selected="B2"
                if [piece_r, piece_c] == get_piece(Gameboard, "B3") :
                    Piece_Selected="B3"
                if [piece_r, piece_c] == get_piece(Gameboard, "B4") :
                    Piece_Selected="B4"
                if [piece_r, piece_c] == get_piece(Gameboard, "B5") :
                    Piece_Selected="B5"
            if Piece_Selected in ["W1", "W2", "W3", "W4", "W5"] and Player==1:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and [piece_r, piece_c] in Possible_Moves(Gameboard,Piece_Selected):
                    Gameboard , Player = Move_Piece(Gameboard, Piece_Selected, [piece_r, piece_c], Player)
                    Piece_Selected=""
            if Piece_Selected in ["B1", "B2", "B3", "B4", "B5"] and Player==2:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and [piece_r, piece_c] in Possible_Moves(Gameboard,Piece_Selected):
                    Gameboard,Player=Move_Piece(Gameboard, Piece_Selected, [piece_r, piece_c], Player)
                    Piece_Selected=""
        if Player==2 and White_Wins(Gameboard):
            Game_Over=Display_Result(Gameboard, -1, -1, "", 1)
            
            if not Game_Over:
                OO_Game()
                Game_Over=True
        if Player==1 and Black_Wins(Gameboard):
            Game_Over=Display_Result(Gameboard, -1, -1, "", 2)
            if not Game_Over:
                OO_Game()
                Game_Over=True

# Main Code Starts here
Homescreen()
OO_Game()