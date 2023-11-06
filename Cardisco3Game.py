import pygame
import random
import os
pygame.init()

def Sort_Remove_Duplicates(arr):
    arr.sort()
    unique_elements = []
    for element in arr:
        if not unique_elements or element != unique_elements[-1]:
            unique_elements.append(element)
    return unique_elements

# Defining Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

Screen_Width = 1200
Screen_Height = 600
Card_Width=100
Card_Height=200
gameWindow = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("CARDISCO 3")

FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


def TextOnScreen(text, colour, x, y, font_size=40):
    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])
def Draw_Game_Board(Gameboard, Available_options, Player_Pointer, Player_to_Move, Last_Picked_Card):
    TextOnScreen("*** CARDISCO 3 ***", (128,204,199), Screen_Width*0.4, Screen_Height*0.1-50)
    TextOnScreen("Player to Move: Player "+ str(Player_to_Move)+"            Last Picked Card: "+str(Last_Picked_Card), black, Screen_Width*0.1, Screen_Height*0.1)
    TextOnScreen("Press e to Exit.", black, Screen_Width*0.1 + 795, Screen_Height*0.1)
    TextOnScreen("Available options are highlighted in        ." + "                              Press r to Restart", black, Screen_Width*0.1, Screen_Height*0.1+50)
    TextOnScreen("RED", red, Screen_Width*0.1+490, Screen_Height*0.1+50)
    TextOnScreen("Currently selected card is highlighted in          ."+"                    Press h for Help.", black, Screen_Width*0.1, Screen_Height*0.1+100)
    TextOnScreen("BLUE", blue, Screen_Width*0.1+550, Screen_Height*0.1+100)
    TextOnScreen("Use the LEFT-RIGHT Arrow keys to navigate. Press SPACEBAR to make a move.", black, Screen_Width*0.1, Screen_Height*0.1+150)    
    TextOnScreen("Press Shift to view/hide Game Position Value", black, Screen_Width*0.4 - 450, Screen_Height*0.9)
    pygame.draw.rect(gameWindow, black, [10, Screen_Height/2, Screen_Width-20, Card_Height])
    pygame.draw.rect(gameWindow, white, [15 , (Screen_Height/2)+5, Screen_Width-30, Card_Height*0.95])
    for i in range(12):
        pygame.draw.line(gameWindow, black,[(Screen_Width-7.5)*(i+1)/13, Screen_Height/2], [(Screen_Width-7.5)*(i+1)/13, Screen_Height/2+ Card_Height*0.99],5 )
    for j in range(len(Gameboard)):
        TextOnScreen(str(Gameboard[j]),black, (Screen_Width-50)*(2*j+1)/26, Screen_Height*10.25/16)
    for k in range(len(Available_options)):
        pygame.draw.line(gameWindow, red,[(Screen_Width-7.5)*(Available_options[k]-1)/13, Screen_Height/2], [((Screen_Width-7.5)*(Available_options[k]-1)/13)+90, Screen_Height/2],5 )
    pygame.draw.line(gameWindow, blue,[(Screen_Width-7.5)*(Player_Pointer)/13, Screen_Height/2 + Card_Height], [((Screen_Width-7.5)*(Player_Pointer)/13)+90, Screen_Height/2 + Card_Height],5 )
    clock.tick(FPS) 
    pygame.display.update()

def Display_Result(Winning_Player):
    while(True):
        gameWindow.fill(white)
        TextOnScreen("Player "+str(Winning_Player)+" Wins!!", green, Screen_Width*0.4, Screen_Height*0.4)
        TextOnScreen("Press e to Exit", green, Screen_Width*0.4, Screen_Height*0.4+50)
        TextOnScreen("Press r to Restart", green, Screen_Width*0.4, Screen_Height*0.4+100)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return False

def Homescreen():
    while(True):
        gameWindow.fill(white)
        TextOnScreen("Welcome to CARDISCO 3", green, Screen_Width*0.4, Screen_Height/2-25)
        TextOnScreen("Press any key to start", green, Screen_Width*0.4, Screen_Height/2+25)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                return

def Display_Rules():

    rules_text = [
        "Rules to play the Game :",
        "1. Gameplay:",
        "   Two players take alternating turns selecting cards.",
        "   Each turn, a player must choose one card based on the card pickup rules.",
        "2. Card Pickup Rules:",
        "   The First Player can pick any card as per their choice, in their first move.",
        "   In subsequent turns, players can only pick cards that meet these conditions :-",
        "     a. The card is adjacent to the last picked card.",
        "     b. The card's number is double the number of the last picked card.",
        "     c. The card's number is half the number of last picked card (except for odd-numbered cards).",
        "3. Objective:",
        "   Players aim to strategically select cards to create a position that prevents their opponent",
        "     from making any legal moves.",
        "4. Winning Condition:",
        "   The player wins when their opponent cannot pick up any more cards.",
        "   In simpler terms, the player who places their opponent in a situation where they can't"
        ,"      make a move emerges victorious.",
        "",
        "Press any key to jump back into the Game! All the Best!"
    ]

    # Font for displaying text
    font = pygame.font.Font(None, 36)

    # Create a list of text surfaces for each line of the rules
    rule_text_surfaces = [font.render(line, True, black) for line in rules_text]

    while(True):
        gameWindow.fill(white)
        for i, text_surface in enumerate(rule_text_surfaces):
            gameWindow.blit(text_surface, (50, 30 + i * 30))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                return

def CardiscoGame():
    n = 13
    Gameboard = list(range(1, n+1))
    # if (n % 2 == 1):
    #     Gameboard[int(n/2)] = "X"
    #     Last_Picked_Card = int((n+1)/2)
    Player_to_Move = 1
    Game_Over = False
    Player_Pointer=0
    Player_Choice=" "
    Last_Picked_Card=" "
    Last_Picked_Cards=[]
    View_Game_Position=False
    while (not Game_Over):

        if Last_Picked_Card!=" ":
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
                Game_Over = Display_Result(3-Player_to_Move)
                if not Game_Over:
                    CardiscoGame()
                break
            Available_options=Sort_Remove_Duplicates(Available_options)
        # print("Player to Move:", Player_to_Move,"  Last Picked Card:", Last_Picked_Card)
        # print("Game Board:", Gameboard)
        # print("Available Options :", Sort_Remove_Duplicates(Available_options))
        # Player_Choice = int(input("Play a move: "))
        # print("\n")
        if Player_Choice==" ": 
            Available_options=Gameboard
            Last_Picked_Card=" "
        gameWindow.fill(white)

        if View_Game_Position:
            TextOnScreen("Game Position :", black, Screen_Width*0.4 +400, Screen_Height*0.9)
            for i in Available_options:
                if i%2==1:
                    TextOnScreen("*", black, Screen_Width*0.4 +400 + 215, Screen_Height*0.9 +1, 90)
                    # Does not works for 2->4->8 type play
                    a=1
                    for m in Available_options:
                        if m%2==0:
                            a+=1
                    if a>1:
                        TextOnScreen(str(a), black, Screen_Width*0.4 +400 + 240, Screen_Height*0.9)
                    break
                if i==Available_options[-1] and i%2==0:
                    TextOnScreen("0", black, Screen_Width*0.4 +400 +215, Screen_Height*0.9)
                    break

        Draw_Game_Board(Gameboard, Available_options, Player_Pointer, Player_to_Move,Last_Picked_Card)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                Game_Over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                CardiscoGame()
                Game_Over=True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                Display_Rules()
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                View_Game_Position = not View_Game_Position
            # Handling Events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and Player_Pointer in list(range(12)):
                    Player_Pointer+=1
                if event.key == pygame.K_LEFT and Player_Pointer in list(range(1,13)):
                    Player_Pointer-=1
                if event.key==pygame.K_SPACE and Player_Pointer+1 in Available_options:
                    Player_Choice=Player_Pointer+1
                    Last_Picked_Card = Player_Choice
                    Last_Picked_Cards.append(Last_Picked_Card)
                    Player_to_Move = 3-Player_to_Move
                    Gameboard[Player_Choice-1] = "X"
                if event.key==pygame.K_TAB and len(Last_Picked_Cards)>0:
                    Available_options.append(Last_Picked_Card)
                    Player_to_Move = 3-Player_to_Move
                    Gameboard[Last_Picked_Card-1] = Last_Picked_Card
                    if len(Last_Picked_Cards)>1:
                        Last_Picked_Cards.pop(-1)
                        Last_Picked_Card=Last_Picked_Cards[-1]
                    else:
                        Last_Picked_Cards=[]
                        Last_Picked_Card=" "
                        Available_options=list(range(1,14))               
    ###################################################
            # gameWindow.fill(white)
            # Draw_Game_Board(Gameboard, Available_options, Player_Pointer, Player_to_Move, Last_Picked_Card)
            # pygame.display.update()
            # clock.tick(FPS)


# Main Code Starts Here
Homescreen()
CardiscoGame()
