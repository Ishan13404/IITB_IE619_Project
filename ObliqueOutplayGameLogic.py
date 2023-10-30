n=5
Gameboard=[
    ["XX", "XX", "XX", "XX", "XX", "XX", "XX"],
    ["XX", "W1", "W2", "W3", "W4", "W5", "XX"],
    ["XX", "__", "__", "__", "__", "__", "XX"],
    ["XX", "__", "__", "__", "__", "__", "XX"],
    ["XX", "__", "__", "__", "__", "__", "XX"],
    ["XX", "B1", "B2", "B3", "B4", "B5", "XX"],
    ["XX", "XX", "XX", "XX", "XX", "XX", "XX"]
    ]


def Show_Gameboard(Gameboard):
    print()
    print("    Gameboard")
    for i in range(1, len(Gameboard)-1):
        for j in range(1, len(Gameboard)-1):
            print(" "+Gameboard[i][j]+"", end="")
        print()
    print()
def get_piece(piece):
    for i in range(1, len(Gameboard)-1):
        for j in range(1, len(Gameboard)-1):
            if Gameboard[i][j]==piece:
                return [i,j]
    return 0

def Possible_Moves(Gameboard, piece):
    moves=[]
    piece_x, piece_y=get_piece(piece)
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

    if len(moves)==0:
        moves=["NA", "NA"]
    if len(moves)==1:
        moves.append("NA")
    return moves

def Move_Piece(Gameboard, piece, arr, Player):
    if arr!="NA":
        Player = (Player+1)%2
        [old_x, old_y] = get_piece(piece)
        new_x, new_y = arr[0], arr[1]
        Gameboard[old_x][old_y]="__"
        Gameboard[new_x][new_y]=piece
    else:
        print("Invalid Move! Please Retry!")
    return Gameboard, Player

def Black_Wins(Gameboard):
    for i in ["W1", "W2", "W3", "W4", "W5"]:
        if Possible_Moves(Gameboard, i)[0]!="NA" or Possible_Moves(Gameboard, i)[1]!="NA":
            return 0
    return 1

def White_Wins(Gameboard):
    for i in ["B1", "B2", "B3", "B4", "B5"]:
        if Possible_Moves(Gameboard, i)[0]!="NA" or Possible_Moves(Gameboard, i)[1]!="NA":
            return 0
    return 1

# Player 0 = WHITE     Player 1 = BLACK
Game_Over=False
Player=0
while(not Game_Over):
    Show_Gameboard(Gameboard)
    if Player==0:
        print("White to Move !")
        piece=input("Choose a Piece (W1 - W5): ")
        if piece not in ["W1", "W2", "W3", "W4", "W5"]:
            print("Invalid Piece! Please Retry!")
            continue
    if Player==1:
        print("Black to Move !")
        piece=input("Choose a Piece (B1 - B5): ")
        if piece not in ["B1", "B2", "B3", "B4", "B5"]:
            print("Invalid Piece! Please Retry!")
            continue
    print("Possible moves:")
    print("1 -", Possible_Moves(Gameboard, piece)[0])
    print("2 -", Possible_Moves(Gameboard, piece)[1])
    Move = input("Enter your move (1/2): ")
    if int(Move) in [1,2]:
        Gameboard, Player=Move_Piece(Gameboard, piece, Possible_Moves(Gameboard, piece)[int(Move)-1], Player)
    elif int(Move) not in [1,2]:
        print("Invalid Move! Please Retry!")
        continue
    if Player==1 and White_Wins(Gameboard):
        print("       Final")
        Show_Gameboard(Gameboard)
        print()
        print("*** White Wins ***")
        print()
        Game_Over=True
    if Player==0 and Black_Wins(Gameboard):
        print("       Final")
        Show_Gameboard(Gameboard)
        print()
        print("*** Black Wins ***")
        print()
        Game_Over=True