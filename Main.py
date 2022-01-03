import sys
import pygame
from random import shuffle
from pygame.locals import *
from Tools import KEY_PRESSED
from Algorithms import InsertionSort, CocktailShakerSort, BubbleSort
from Visualization import VisualizedArray

def INITIALIZE_SCREEN():
    WIN_SIZE = (1920, 1080)  # Screen resolution depending on the screen size.
    pygame.init()  # Starting PyGame library.
    WIN = pygame.display.set_mode(WIN_SIZE)  # Creating screen in fullscreen mode.
    WIN.set_alpha(None)  # Disabling alpha, since we don't use images so that improves the perfomance.
    pygame.event.set_allowed([QUIT, KEYDOWN])  # Adding the two only allowed keys, for better perfomance.
    pygame.display.set_caption('Array Circular Visualizer')
    pygame.mouse.set_visible(False) # Hidding the mouse.
    FONT = pygame.font.Font('./Font.ttf', 25)
    return WIN, True, WIN_SIZE, FONT

Algorithms = ['Insertion Sort', 'Cocktail Shacker Sort', 'Bubble Sort']
for i in range(len(Algorithms)):
    print(f'{i+1}.{Algorithms[i]}')
inputLoop = True
while inputLoop:
    try:
        UserInput = int(input('Algorithm Number: '))
    except:
        print(f"Algorithm Number isn't valid, it has to be a number between 1-3.\n")
    else:
        if UserInput >= 1 and UserInput <= 3:
            inputLoop = False
        else:
            print(f"Algorithm Number {UserInput} isn't valid, number should be between 1-3.\n")

sizeLoop = True
while sizeLoop:
    try:
        ArraySize = int(input('Array Size: '))
    except:
        print(f"Array Size isn't valid, it has to be a number between 1-1000.\n")
    else:
        if ArraySize >= 1 and ArraySize <= 1000:
            sizeLoop = False
        else:
            print(f"Array Size {ArraySize} isn't valid, number should be between 1-1000.\n")

WIN, MAIN_LOOP, SCREENSIZE, FONT = INITIALIZE_SCREEN()
Array = [i+1 for i in range(ArraySize)]
shuffle(Array)
Iterations = 0
while MAIN_LOOP:
    WIN.fill((0, 0, 0))
    MyArray = VisualizedArray(Array, SCREENSIZE)
    Circles = MyArray.getCircles()
    if KEY_PRESSED() == 'QUIT':
        MAIN_LOOP = False
        pygame.quit()
        sys.exit()
    else:
        for circleInformation in Circles:
            pygame.draw.circle(WIN, circleInformation[0], circleInformation[1], circleInformation[2], circleInformation[3])

    Text = FONT.render(f'Iterations: {Iterations}', True, (255, 255, 255))
    WIN.blit(Text, (10, 10))

    Text = FONT.render(f'Array Size: {len(Array)}', True, (255, 255, 255))
    WIN.blit(Text, (10, 40))

    Text = FONT.render(f'Algorithm: {Algorithms[UserInput-1]}', True, (255, 255, 255))
    WIN.blit(Text, (10, 70))

    Text = FONT.render('Sklyvan', True, (255, 255, 255))
    WIN.blit(Text, (SCREENSIZE[0]-120, 10))

    pygame.display.update()

    if UserInput == 1:
        Array, newIterations = InsertionSort(Array)
    elif UserInput == 2:
        Array, newIterations = BubbleSort(Array)
    elif UserInput == 3:
        Array, newIterations = CocktailShakerSort(Array)
    Iterations += newIterations
