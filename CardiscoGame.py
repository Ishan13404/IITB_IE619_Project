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
pygame.display.set_caption("CARDISCO")

FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


def TextOnScreen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])

def Draw_Game_Board(Gameboard, Available_options, Player_Pointer, Player_to_Move):
    TextOnScreen("*** CARDISCO ***", (128,204,199), Screen_Width*0.4, Screen_Height*0.1-50)
    TextOnScreen("Player to Move: Player "+ str(Player_to_Move)+"                                                           Press e to exit.", black, Screen_Width*0.1, Screen_Height*0.1)
    TextOnScreen("Available options are highlighted in        ." + "                              Press r to restart", black, Screen_Width*0.1, Screen_Height*0.1+50)
    TextOnScreen("RED", red, Screen_Width*0.1+490, Screen_Height*0.1+50)
    TextOnScreen("Currently selected card is highlighted in          .", black, Screen_Width*0.1, Screen_Height*0.1+100)
    TextOnScreen("BLUE", blue, Screen_Width*0.1+550, Screen_Height*0.1+100)
    TextOnScreen("Use the LEFT-RIGHT Arrow keys to navigate. Press ENTER to make a move.", black, Screen_Width*0.1, Screen_Height*0.1+150)    
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
        TextOnScreen("Press e to exit", green, Screen_Width*0.4, Screen_Height*0.4+50)
        TextOnScreen("Press r to restart", green, Screen_Width*0.4, Screen_Height*0.4+100)
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
        TextOnScreen("Welcome to CARDISCO", green, Screen_Width*0.4, Screen_Height/2-25)
        TextOnScreen("Press any key to start", green, Screen_Width*0.4, Screen_Height/2+25)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                return


def CardiscoGame():
    n = 13
    Gameboard = list(range(1, n+1))
    if (n % 2 == 1):
        Gameboard[int(n/2)] = "X"
        Last_Picked_Card = int((n+1)/2)
    Player_to_Move = 1
    Game_Over = False
    Player_Pointer=0
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
            Game_Over = Display_Result(3-Player_to_Move)
            if not Game_Over:
                CardiscoGame()
            break
        # print("Player to Move:", Player_to_Move,"  Last Picked Card:", Last_Picked_Card)
        # print("Game Board:", Gameboard)
        # print("Available Options :", Sort_Remove_Duplicates(Available_options))
        Available_options=Sort_Remove_Duplicates(Available_options)
        # Player_Choice = int(input("Play a move: "))
        # print("\n")
        Player_Choice=7
        gameWindow.fill(white)
        Draw_Game_Board(Gameboard, Available_options, Player_Pointer, Player_to_Move)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                Game_Over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                CardiscoGame()
                Game_Over=True
            # Handling Events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and Player_Pointer in list(range(12)):
                    Player_Pointer+=1
                if event.key == pygame.K_LEFT and Player_Pointer in list(range(1,13)):
                    Player_Pointer-=1
                if event.key==pygame.K_RETURN and Player_Pointer+1 in Available_options:
                    Player_Choice=Player_Pointer+1
                    Last_Picked_Card = Player_Choice
                    Player_to_Move = 3-Player_to_Move
                    Gameboard[Player_Choice-1] = "X"
    ###################################################
            gameWindow.fill(white)
            Draw_Game_Board(Gameboard, Available_options, Player_Pointer, Player_to_Move)
            pygame.display.update()
            clock.tick(FPS)


# Main Code Starts Here
Homescreen()
CardiscoGame()