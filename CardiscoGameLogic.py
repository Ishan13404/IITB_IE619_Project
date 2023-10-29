def Sort_Remove_Duplicates(arr):
    arr.sort()
    unique_elements = []
    for element in arr:
        if not unique_elements or element != unique_elements[-1]:
            unique_elements.append(element)
    return unique_elements

n = 13
Gameboard = list(range(1, n+1))
if (n % 2 == 1):
    Gameboard[int(n/2)] = "X"
    Last_Picked_Card = int((n+1)/2)
Player_to_Move = 1
Game_Over = False

while (not Game_Over):
    Available_options = []
    if Last_Picked_Card+1 in Gameboard:
        Available_options.append(Last_Picked_Card+1)
    if Last_Picked_Card-1 in Gameboard:
        Available_options.append(Last_Picked_Card-1)
    if Last_Picked_Card*2 in Gameboard:
        Available_options.append(Last_Picked_Card*2)
    if (Last_Picked_Card/2 in Gameboard) and Last_Picked_Card % 2 == 0:
        Available_options.append(int(Last_Picked_Card/2))
    if len(Available_options) == 0:
        Game_Over = True
        break
    print("Player to Move:", Player_to_Move,"  Last Picked Card:", Last_Picked_Card)
    print("Game Board:", Gameboard)
    print("Available Options :", Sort_Remove_Duplicates(Available_options))
    Player_Choice = int(input("Play a move: "))
    print("\n")
    if Player_Choice not in Available_options:
        print("Not a valid move! Play again\n")
    else:
        Player_to_Move = Player_to_Move % 2+1
        Gameboard[Player_Choice-1] = "X"
        Last_Picked_Card = Player_Choice
print("\n\n")
print("Game Over ...... Player", Player_to_Move % 2+1, "WINS !!\n\n")
