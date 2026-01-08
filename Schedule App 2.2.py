### Schedule Lynx App ###

#------------------------------ IMPORTS ------------------------------#

from ImageLib2 import *
from ListLib import *
import time
import os
import ast



#------------------------------ GLOBAL VARIABLES ------------------------------#    

# Get user input for where to find and save files
DATA_DIRECTORY = input("Enter the directory path for your schedule data files:\n")
if (DATA_DIRECTORY == ""):
    DATA_DIRECTORY = "C:/Users/" + os.getlogin() + "/.__Scheduler App Data__"
OUTPUT_DIRECTORY = input("Enter the output directory path:\n")
if (OUTPUT_DIRECTORY == ""):
    OUTPUT_DIRECTORY = "C:/Users/" + os.getlogin() + "/Desktop"

START_TIME = time.time()

COLORS = [ # These colors were selected from the standard CSS Colors, also called Web Colors. Rearranging the order of these will rearrange the order of the colors on the output image
(220, 20, 60), # Crimson
(255, 69, 0), # Orange Red
(255, 140, 0), # Dark Orange
(255, 215, 0), # Gold
(50, 205, 50), # Lime Green
(30, 144, 255), # Dodger Blue
(0, 0, 205), # Medium Blue
(75, 0, 130), # Indigo
(138, 43, 226), # Blue Violet
(255, 105, 180), # Hot Pink
(160, 82, 45), # Sienna
(169, 169, 169) # Dark Gray
]

TIMES = ["7:00 AM", "7:15 AM", "7:30 AM", "7:45 AM", "8:00 AM", "8:15 AM", "8:30 AM", "8:45 AM", "9:00 AM", "9:15 AM", "9:30 AM", "9:45 AM", "10:00 AM", "10:15 AM", "10:30 AM", "10:45 AM", "11:00 AM", "11:15 AM", "11:30 AM", "11:45 AM", "12:00 PM", "12:15 PM", "12:30 PM", "12:45 PM", "1:00 PM", "1:15 PM", "1:30 PM", "1:45 PM", "2:00 PM", "2:15 PM", "2:30 PM", "2:45 PM", "3:00 PM", "3:15 PM", "3:30 PM", "3:45 PM", "4:00 PM", "4:15 PM", "4:30 PM", "4:45 PM", "5:00 PM", "5:15 PM", "5:30 PM", "5:45 PM", "6:00 PM", "6:15 PM", "6:30 PM", "6:45 PM", "7:00 PM", "7:15 PM", "7:30 PM", "7:45 PM", "8:00 PM", "8:15 PM", "8:30 PM", "8:45 PM", "9:00 PM", "9:15 PM", "9:30 PM", "9:45 PM", "10:00 PM"] # len = 162-4

# Declare global variables having to do with output image spacing, size, and formatting
TIME_COLUMN_WIDTH = 73 # 73 is 75 minus a 2-pixel border
SPACERPIXELS = 30 # Number of pixels to be inserted at the top of the sheet; added directly to the y position from the top of all blocks.
WIDTH = 1850 + 180 + 5 * TIME_COLUMN_WIDTH # was 3600 # then was 1800
HEIGHT = (len(TIMES) + 1) * 15 + SPACERPIXELS # (len(TIMES) + 1) rows * 15 pixels/row
TEXT_FONT_SIZE = 13

grid = [[(255, 255, 255) for _ in range(HEIGHT)] for _ in range(WIDTH)]
names = [] # List of tuples in the form (name, (R, G, B))
DATA_AS_STRINGS = [] # List of data files, converted to strings for parsing into lists by ast




#------------------------------ FUNCTIONS ------------------------------#

def addName(name):
    names.append((name, COLORS[len(names)]))


def addClass(name, startTime, stopTime, daysStr):
    global names


    def defineBlock(startTime, stopTime, columnNo, weekday):
        
        def timeToY(time):
            global SPACERPIXELS, TIME_COLUMN_WIDTH
            hours, minutes = time  
            hours -= 7           
            minutes += 60 * hours  
            y = minutes 
            y = int(y)
            y = y + SPACERPIXELS
            return y

        startY = timeToY(startTime)
        stopY = timeToY(stopTime)

        startX = 400/len(names) * columnNo + TIME_COLUMN_WIDTH * (weekday+1) + 400*weekday
        stopX = startX + 400/len(names)

        return [(startX, startY), (stopX, stopY)]


    def drawBlock(coordinates, rgb):
        global grid
        xi, xf, yi, yf = coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i >= xi and i <= xf):
                    if (j >= yi and j <= yf):
                        grid[i][j] = rgb



    def dayStrToList(string):
        "Take a string of format 'MTWRF' and convert it to a list of mixed numbers equal to their index + 1 (if the day is present in the string) and else = False."
        output = [False, False, False, False, False]
        if ("M" in string):
            output[0] = 1
        if ("T" in string):
            output[1] = 2
        if ("W" in string):
            output[2] = 3
        if ("R" in string):
            output[3] = 4
        if ("F" in string):
            output[4] = 5
        return output
    

    daysList = dayStrToList(daysStr)

    for i in range(0,len(names)):
        for j in range(0,5):
            if (name == names[i][0]):
                if(daysList[j] != False):
                    drawBlock(defineBlock(startTime, stopTime, i, daysList[j]-1), names[i][1])

    

# The days of the week are "MTWRF"


def writeFile(data):
    name = data[0]
    for i in range(1, len(data)):
        addClass(name, data[i][0], data[i][1], data[i][2])


def importData():
    global DATA_AS_STRINGS
    print("Loading file info...")
    print("Elapsed time:", time.time()- START_TIME, "s")

    for filename in os.listdir(DATA_DIRECTORY):
        filename = os.path.join(DATA_DIRECTORY, filename)
        print(filename)
        if (filename != DATA_DIRECTORY + "\\Scheduler App Archives"):
            with open(filename, "r") as inputDocument:
                file = inputDocument.read()
                file = file.replace("\n", "").replace(" ", "").replace("\t", "")
                DATA_AS_STRINGS.append(file)

    print("Writing data to image...")
    print("Elapsed time:", time.time()- START_TIME, "s")
    for i in DATA_AS_STRINGS:
        i = ast.literal_eval(i)
        addName(i[0])





def linesAndText():

    

    def drawDayLines():
        global TIME_COLUMN_WIDTH
        for i in range(5):
            colNo = TIME_COLUMN_WIDTH*i + 400*i
            for j in range(len(grid)-4):
                for k in range(len(grid[0])):
                    if (j == colNo):
                        grid[j][k] = (0, 0, 0)
                        grid[j+1][k] = (0, 0, 0)
                        grid[j+2][k] = (0, 0, 0)
                        grid[j+3][k] = (0, 0, 0)
                        grid[j+4][k] = (0, 0, 0)
            colNo = TIME_COLUMN_WIDTH*(i+1) + 400*i
            for j in range(len(grid)-4):
                for k in range(len(grid[0])):
                    if (j == colNo):
                        grid[j][k] = (0, 0, 0)
                        grid[j+1][k] = (0, 0, 0)
                        grid[j+2][k] = (0, 0, 0)
                        grid[j+3][k] = (0, 0, 0)
                        grid[j+4][k] = (0, 0, 0)




    def drawHorizontalLines():
        global SPACERPIXELS
        for i in range(len(TIMES) + int(SPACERPIXELS/15)):
            i *= 15
            if (i % 2 == 0):
                for j in range(WIDTH):
                    grid[j][i] = (0, 0, 0)
        


    def writeNameText(names, img):
        global TIME_COLUMN_WIDTH
        for day in range(5):
            for i in range(len(names)):
                writeText(img, names[i][0], (TIME_COLUMN_WIDTH*(day+1) + 10 + 400/len(names)*i + 400*day, 1+15), fontSize = TEXT_FONT_SIZE)    
    


    def writeWeekdayText(img):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for i in range(len(days)):
            writeText(img, days[i], ((400 + TIME_COLUMN_WIDTH + 10 )/2 + 400*i + TIME_COLUMN_WIDTH*i, 1), fontSize = TEXT_FONT_SIZE)
    

    def writeTimeText(img, xPos):
        global WIDTH, TIMES, SPACERPIXELS
        for i in range(len(TIMES)):
            if (i % 2 == 0):
                writeText(img, TIMES[i], (xPos + 10, i * 15 + SPACERPIXELS + 7.5), fontSize = TEXT_FONT_SIZE)
    print("Writing grid into image")
    print("Elapsed time:", time.time()- START_TIME, "s")
    drawDayLines()
    drawHorizontalLines()
    print("Completing the formatting...")
    print("Elapsed time:", time.time()- START_TIME, "s")
    img = toImage(grid)
    for i in range(5):
        writeTimeText(img, (400 + TIME_COLUMN_WIDTH) * i)
    writeNameText(names, img)
    writeWeekdayText(img)
    return img



def main():
    global DATA_AS_STRINGS

    importData()
    for i in DATA_AS_STRINGS:
        writeFile(eval(i))
    img = linesAndText()
    img.show()
    print("Saving...")
    img.save(OUTPUT_DIRECTORY + "/scheduleTest.jpg")

    print("Elapsed time:", time.time()- START_TIME, "s")
    print("PROGRAM HAS TERMINATED")


main()