import pygame

pygame.init()

# Defining Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

Screen_Width = 1000
Screen_Height = 600
Card_Width=100
Card_Height=200
gameWindow = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("OBLIQUE OUTPLAY")

FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def TextOnScreen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])




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

    # if len(moves)==0:
    #     moves=["NA", "NA"]
    # if len(moves)==1:
    #     moves.append("NA")
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

def Draw_Game_Board(Gameboard, piece_r, piece_c, Piece_Selected, Player):
    TextOnScreen("Player to Move : " +str(Player), blue, 700, 100)
    TextOnScreen("Piece Selected : " +str(Piece_Selected), blue, 700, 200)
    TextOnScreen("Available Moves : " + str(Possible_Moves(Gameboard, Piece_Selected)), blue, 700, 300)
    pygame.draw.rect(gameWindow, black, [10, 10, Screen_Height-20, Screen_Height-20],5)
    pygame.draw.line(gameWindow, black,[(Screen_Height-10)*0.2, 10],[(Screen_Height-10)*0.2,Screen_Height-15],5 )
    pygame.draw.line(gameWindow, black,[(Screen_Height-10)*0.4, 10],[(Screen_Height-10)*0.4,Screen_Height-15],5 )
    pygame.draw.line(gameWindow, black,[(Screen_Height-10)*0.6, 10],[(Screen_Height-10)*0.6,Screen_Height-15],5 )
    pygame.draw.line(gameWindow, black,[(Screen_Height-10)*0.8, 10],[(Screen_Height-10)*0.8,Screen_Height-15],5 )
    pygame.draw.line(gameWindow, black,[10, (Screen_Height-10)*0.2],[Screen_Height-15 ,(Screen_Height-10)*0.2],5 )
    pygame.draw.line(gameWindow, black,[10, (Screen_Height-10)*0.4],[Screen_Height-15 ,(Screen_Height-10)*0.4],5 )
    pygame.draw.line(gameWindow, black,[10, (Screen_Height-10)*0.6],[Screen_Height-15 ,(Screen_Height-10)*0.6],5 )
    pygame.draw.line(gameWindow, black,[10, (Screen_Height-10)*0.8],[Screen_Height-15 ,(Screen_Height-10)*0.8],5 )
    
    n=len(Gameboard)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if Gameboard[i][j] in ["W1", "W2", "W3", "W4", "W5"]:
                pygame.draw.circle(gameWindow, white, [65 + 118*(j-1), 65 + 118*(i-1)], 40)
            if Gameboard[i][j] in ["B1", "B2", "B3", "B4", "B5"]:
                pygame.draw.circle(gameWindow, black, [65 + 118*(j-1),65 + 118*(i-1)], 40)
    
    if Piece_Selected !="":
        for [i,j] in Possible_Moves(Gameboard, Piece_Selected):
            pygame.draw.circle(gameWindow, red, [65 + 118*(j-1), 65 + 118*(i-1)], 43, 3)
    
    pygame.draw.circle(gameWindow, blue, [65 + 118*(piece_c-1), 65 + 118*(piece_r-1)], 43,3)
    

    pygame.display.update()



# Player 1 = WHITE     Player 2 = BLACK

def OO_Game():
    Game_Over=False
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
        gameWindow.fill((213, 186, 199))
        Draw_Game_Board(Gameboard, piece_r, piece_c, Piece_Selected, Player)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                return 
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
            Game_Over=True
            print("White WINS!!")
        if Player==1 and Black_Wins(Gameboard):
            Game_Over=True
            print("Black WINS!!")    



# Main Code Starts here

OO_Game()