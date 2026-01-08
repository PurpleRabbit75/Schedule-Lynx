# Basic UI Schedule Overlap


from ImageLib2 import *
from ListLib import *
import time

start = time.time()
numPeople = int(input("Please enter the number of people for whom you would like to make this schedule:\n>>>"))

grid = []

for i in range(1800): # was 3600
    l = []
    for j in range(915): # was 1800
        l.append((255, 255, 255))
    grid.append(l)

    



def timeToY(time):
    hours, minutes = time  
    hours -= 7.5           
    minutes += 60 * hours  
    y = minutes 
    #y = y % 1
    y = int(y)
    #print(y)
    return y



def defineBlock(startTime, stopTime, columnNo, weekday):
    startY = timeToY(startTime)
    stopY = timeToY(stopTime)

    startX = int(350/numPeople) * columnNo + 100 + 350*weekday
    #print("startX =", startX, "columnNo =", columnNo, "weekday =", weekday)
    stopX = startX + int(50/numPeople)

    return [(startX, startY), (stopX, stopY)]


def drawBlock(coordinates, rgb):
    global grid
    xi = coordinates[0][0]
    xf = coordinates[1][0]
    yi = coordinates[0][1]
    yf = coordinates[1][1]
    # print(xi, xf, yi, yf)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i >= xi and i <= xf):
                if (j >= yi and j <= yf):
                    #print("grid edited")
                    grid[i][j] = rgb

def dayStrToList(string):
    "Take a string of format 'MTWRF' and convert it to a list of mixed numbers equal to their index (if the day is present in the string) and else = False."
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



def addClass(name, startTime, stopTime, daysStr):
    names = [("A", (138, 43, 226)),
        ("B", (255, 20, 157) ),
        ("C", (220, 20, 60)),
        ("D", (255, 69, 0)),
        ("E", (255, 140, 0)),
        ("F", (255, 215, 0)),
        ("G", (75, 185, 50)),
        ("H", (25, 132, 125)),
        ("I", (40, 40, 185)),
        ("J", (75, 0, 130)),
        ("K", (169, 169, 169))
        ]

    daysList = dayStrToList(daysStr)
    #print("daysList =", daysList)

    for i in range(0,7):
        for j in range(0,5):
            #print("daysList[j] pre ifs =", daysList[j])
            if (name == names[i][0]):
                if(daysList[j] != False):
                    #print("daysList[j] post ifs =", daysList[j])
                    drawBlock(defineBlock(startTime, stopTime, i, daysList[j]-1), names[i][1])


# The days of the week are "MTWRF"


peopleList = []
for i in range(numPeople):
    peopleList.append([])

for i in range(len(peopleList)):
    person = peopleList[i]
    print('Please enter the schedule items in the following format:\nstartTimeHours,startTimeMinutes,stopTimeHours,stopTimeMinutes,"DAYS OF THE WEEK"\n. [Days of the week may be any combination of "MTWRF"]. \nWhen you are finished, type DONE and hit enter.')
    text = ''
    text = text + '\n'.join(iter(input, 'DONE'))
    List = text.split('\n')
    for line in List:
        pieces = line.split(",")
        person.append('addClass("' + chr(i + 65) + '", (' + pieces[0] + "," + pieces[1] + "), (" + pieces[2] + ", " + pieces[3] + '),' + pieces[4] + ")") 

##    addClass("Dixie", (11,15), (13, 45), "TR") # Psychology



for person in peopleList:
    for command in person:
        eval(command)



def drawDayLines():
    for i in range(5):
        colNo = 100 + 350*i
        for j in range(len(grid)-4):
            for k in range(len(grid[0])):
                if (j == colNo):
                    grid[j][k] = (0, 0, 0)
                    grid[j+1][k] = (0, 0, 0)
                    grid[j+2][k] = (0, 0, 0)
                    grid[j+3][k] = (0, 0, 0)
                    grid[j+4][k] = (0, 0, 0)

drawDayLines()


##q = 0.03
##k = 0
##for i in range(58):
##    i = i * (29.96551724137931 - q) + 15 + k
##    i = int(i)
##    if (i % 7 == 0):
##        k -= 0.7
##    for j in range(3630):
##        try:
##            grid[j][i] = (0, 0, 0)
##        except IndexError:
##            print(j, i)

times = [
    "7:30 AM",
    "7:45 AM",
    "8:00 AM",
    "8:15 AM",
    "8:30 AM",
    "8:45 AM",
    "9:00 AM",
    "9:15 AM",
    "9:30 AM",
    "9:45 AM",
    "10:00 AM",
    "10:15 AM",
    "10:30 AM",
    "10:45 AM",
    "11:00 AM",
    "11:15 AM",
    "11:30 AM",
    "11:45 AM",
    "12:00 PM",
    "12:15 PM",
    "12:30 PM",
    "12:45 PM",
    "1:00 PM",
    "1:15 PM",
    "1:30 PM",
    "1:45 PM",
    "2:00 PM",
    "2:15 PM",
    "2:30 PM",
    "2:45 PM",
    "3:00 PM",
    "3:15 PM",
    "3:30 PM",
    "3:45 PM",
    "4:00 PM",
    "4:15 PM",
    "4:30 PM",
    "4:45 PM",
    "5:00 PM",
    "5:15 PM",
    "5:30 PM",
    "5:45 PM",
    "6:00 PM",
    "6:15 PM",
    "6:30 PM",
    "6:45 PM",
    "7:00 PM",
    "7:15 PM",
    "7:30 PM",
    "7:45 PM",
    "8:00 PM",
    "8:15 PM",
    "8:30 PM",
    "8:45 PM",
    "9:00 PM",
    "9:15 PM",
    "9:30 PM",
    "9:45 PM",
    "10:00 PM",
    "10:15 PM",
    "10:30 PM",
    ] # len = 159

hasTriggered = False
for i in range(len(times)):
    i *= 15
    for j in range(3600):
        try:
            grid[j][i] = (0, 0, 0)
        except IndexError:
            if (hasTriggered == False):
                print("IndexError at",j, i)
                hasTriggered = True
        



print("Writing grid into image")
img = toImage(grid)


for i in range(len(times)):
##    print(10, i*15)
    writeText(img, times[i], (10, i * 15))



img.show()

print("Saving...")
img.save("C:/Users/abrah/Desktop/schedule.jpg")

print("Elapsed time:", time.time()-start, "s")
print("PROGRAM HAS TERMINATED")

