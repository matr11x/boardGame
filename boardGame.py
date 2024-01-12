import pygame
import random
import time

pygame.font.init() 

#height and width of the checkerboard
width = 7 
height = 8

#size of the boxes in the checkerboard
squareSize = 100

#colours
white = (255, 255, 255)
black = (  0,   0,   0)
red = (255,0,0)
blue = (0, 0, 255)
grey = (125,125, 125)

colour = white

#draws 8x7 checkerboard
def checkerBoard(window):
   
    currentColour = white

    for i in range(0, height):
              # top-left corner Y coordinate
        for j in range(0, width):
            #alternates between black and white to create the checkerboard
            if currentColour == white:
                currentColour = black
            else:
                currentColour = white
            
            pygame.draw.rect(window, currentColour, (j * squareSize, i * squareSize, squareSize, squareSize))   

#function to draw the numbers on the tiles
#the first board game feature
def numbers(numberFont):
    #every second line when numbers are going from right to left
    number = 56
    for i in range(0, height, 2):
        
            # top-left corner Y coordinate
        for j in range(0, width):
            
            
            numberCreate = numberFont.render( str(number), True, grey ) #creates the number
            number -= 1
            # Space it off the corner a bit
            offset = 7 #offsets the number from the corner
            window.blit( numberCreate, ( j*squareSize + offset, i*squareSize + offset ) )  # draws the number
        number -= 7

#every second line when nubmers are going from left to right
    number = 43
    for i in range(1, height,2):
        
            # top-left corner Y coordinate
        for j in range(0, width):
            
            
            numberCreate = numberFont.render( str(number), True, grey ) #creates the number
            number += 1
            # Space it off the corner a bit
            offset = 7 #offsets the number from the corner
            window.blit( numberCreate, ( j*squareSize + offset, i*squareSize + offset ) )  #draws the number
        number -= 21


running = True

#two 2-sided dice
def number():
    #
	dice1 = random.randint(1,2)
	dice2 = random.randint(1,2)
	diceroll = dice1+dice2 #sum of the two dice
	return(diceroll) 

#initial positions of player 1 (rx,rx) and player 2 (bx,by)
rx = 50
ry = 750

bx = 50
by = 750

#player 1
def rplayer(rx,ry): 
        player1 = pygame.draw.circle(window, (red), [rx,ry], 30) #draws player 1 and location of circle is stored
        pygame.display.update()

#player 2
def bplayer(bx,by):
        player2 = pygame.draw.circle(window, (blue), [bx,by], 30) #draws player 2 and location of circle is stored
        pygame.display.update()

#switching the direction from left to right for both players 
switchR = 1
switchB = 1

#counterXR and couterXB are the values of the boxes in the rows shown below and represent the x coordinates of the players or circles
#[14|13|12|11|10|9|8]
#[1|2|3|4|5|6|7]
#these are the main ways the players are going to move, from left to right first in the bottom row, then right to left in the top row

#initially counterXR and B are at 1 becuase they start in the bottom left corner
counterXR = 1 
counterXB = 1

#counterYR and counterYB is the values the boxes in the coloumns and represent the y coordinates of the players or circles
#[8]
#[7]
#[6]
#[5]
#[3]
#[2]
#[1]

#initially counterYR and B are at 1 becuase the players start in the bottom left corner
counterYR = 1
counterYB = 1

window = pygame.display.set_mode((width*squareSize, height*squareSize)) #window is the size of the checkboard

font = pygame.font.SysFont( None, 22, bold =pygame.font.Font.bold) #font of the numbers

#draws the checkerboard and the players in the starting position before the game starts
checkerBoard(window)
rplayer(rx,ry)
bplayer(bx,by)

delay = 1 #initially delays the game to show the players in the starting position

turn = "player1" #player 1's turn is first

#main game loop
while running:

    checkerBoard(window) #draws the checkboard on the window
    numbers(font) #draws the numbers on the board

    if turn == "player1" and delay == 2: #if its player 1's turn the 

        diceroll = number() #assigns player 1's diceroll

        print(f"Player 1 rolled a {diceroll}")

        counterXR += diceroll #the value of the diceroll is added to counterXR
        
        #if the value of counterXR is greater than seven, meaning row 2, 4, 6, or 8, and the player was moving from left to right
        if  counterXR > 7 and switchR == 1:
            counterYR +=1 #player is moved up one square
            switchR = 2 #player is now moving right to left

        #if value of counterXR is greater than 14, meaning row 1, 3, 5, or 7, and the player was moving right to left
        if counterXR > 14:
            counterYR += 1 #moves circle up one square
            counterXR -= 14 #resets counterXR since player is moving left to right again
            switchR = 1 #player is now moving left to right
        
        #if the counterXR is in the range 1-7, or rows 1,3,5, or 7
        for i in range(1, 8):
            if counterXR == i: 
                rx = (100*i)-50 #x coordinate of the player depending on what they roll

        #if the counterXR is in the range 8-14, or rows 2,4,6, or 8
        for i in range(8, 15):
            if counterXR == i: 
                rx = 650 - ((i-8)*100) #x coordinate of the player depending on what they roll

        #moving the player up a square
        for i in range(2,9):
            if counterYR == i:
                ry = 650 - ((i-2)*100) #y coordinate of the player depending on what they roll

        #second board game feature which is exact "requirements"
        #if the player moves past tile 56, which is the last tile, the game ends and this player wins
        if (counterXR > 13 and counterYR > 7) or counterYR==9:
            print("Player 1 Wins!")
            break
            
        turn = "player2"

    #player 2's turn 
    #same operatoins as player 1 are used
    elif turn == "player2":
        
        diceroll = number() #assigns player 2's diceroll


        print(f"Player 2 rolled a {diceroll}")

        counterXB += diceroll #the value of the diceroll is added to counterXB

         #if the value of counterXB is greater than seven, meaning row 2, 4, 6, or 8, and the player was moving from left to right
        if  counterXB > 7 and switchB == 1:
            counterYB +=1 #player is moved up one square
            switchB = 2 #player is now moving right to left

        #if value of counterXB is greater than 14, meaning row 1, 3, 5, or 7, and the player was moving right to left
        if counterXB > 14:
            counterYB += 1 #moves circle up one square
            counterXB -= 14 #resets counterXB since player is moving left to right again
            switchB = 1 #player is now moving left to right
        
        #if the counterXB is in the range 1-7, or rows 1,3,5, or 7
        for i in range(1, 8):
            if counterXB == i:
                bx = (100*i)-50 #x coordinate of the player depending on what they roll

        #if the counterXB is in the range 8-14, or rows 2,4,6, or 8
        for i in range(8, 15):
            if counterXB == i:
                bx = 650 - ((i-8)*100) #x coordinate of the player depending on what they roll

        #moving the player up a square if they finish a row
        for i in range(2,9):
            if counterYB == i:
                by = 650 - ((i-2)*100) #y coordinate of the player depending on what they roll

        #if the player moves past tile 56, which is the last tile, the game ends and this player wins
        if (counterXB > 13 and counterYB > 7) or counterYB == 9:
            print("Player 2 Wins!")
            break

        turn = "player1" #switches the turn back to player 1
    
    delay = 2 #delay value changed so game can execute

    rplayer(rx, ry) #calls the player 1 function passing the coordinates of the red circle
    bplayer(bx, by) #calls the player 2 function passing the coordinates of the blue circle

    time.sleep(2) #delays execution for 2 seconds so you can see the dicerolls and players moving

    #closes pygame window when x is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
