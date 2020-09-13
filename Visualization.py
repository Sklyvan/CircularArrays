from math import ceil
from random import choice

RGB = [[255, 0, i] for i in range(256)] +  [[i, 0, 255] for i in reversed(range(256))] +  [[0, i, 255] for i in range(256)] +  [[0, 255, i] for i in reversed(range(256))] + [[i, 255, 0] for i in range(256)] + [[255, i, 0] for i in reversed(range(256))]
RGB_SIZE = len(RGB)

class VisualizedArray:
    def __init__(self, array, screenSize):
        self.array, maxArray = array, max(array)
        self.normalizedArray = [i/maxArray for i in self.array] # Array with values inside the range (0, 1].
        self.maxRadius = screenSize[1]//2 # The biggest circle is going to have this radius, half of screen y-size.
        self.circleThickness = 4
        self.colourSteps = ceil(RGB_SIZE/len(self.array)) # Depending on the size of the array we acces to the RGB colours with more or less steps.
        self.circleCenter = (screenSize[0]//2, screenSize[1]//2) # The circles are originated on the center of the screen.

    def getCircles(self):
        circlesMatrix = []
        for i in range(len(self.array)):
            circleColour = RGB[self.normalizedArray.index(self.normalizedArray[i]) * self.colourSteps%RGB_SIZE] # Depending on the position of the element, we generete the color.
            circleRadius = round(self.maxRadius * self.normalizedArray[i]) # Getting the current element radius depending on the normalized value of the element.
            circlesMatrix.append([circleColour, self.circleCenter, circleRadius, self.circleThickness])
        return circlesMatrix