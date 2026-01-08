from ImageLib2 import *
from ListLib import *
import time

start = time.time()

#image = Image.open("C:/Users/abrah/Desktop/Times.png")
grid = []

for i in range(1850+250): # was 3600 # then was 1800
    l = []
    for j in range(915): # was 1800
        l.append((255, 255, 255))
    grid.append(l)

    


##timesGrid = toGrid(Image.open("C:/Users/abrah/Desktop/Times.png")) # size = (130, 1738)
##for i in range(len(timesGrid)):
##    for j in range (len(timesGrid[0])):
##        grid[i][j] = timesGrid[i][j]


# Hours = 14.5
# minutes = 870
# Pixels = 1738
# pixels/minute = 1.9977011494252874
# pixels/hour = 119.86206896551724
# pixels/15 mins = 29.96551724137931



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

    startX = 50 * columnNo + 100 + 400*weekday
    #print("startX =", startX, "columnNo =", columnNo, "weekday =", weekday)
    stopX = startX + 50 

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



names = [("Abby",   (220, 20, 60)), # was (186, 85, 211)
             ("Abe", (255, 69, 0)),
             ("Ava",    (255, 140, 0)),
             ("Dixie",  (255, 215, 0)),
             ("Ella", (50, 205, 50)),
             ("Ellie",  (30, 144, 255)), # Was (255, 255, 0)
             ("Flora",  (0, 0, 205)),
             ("Hosea",  (75, 0, 130))
             ]



def addClass(name, startTime, stopTime, daysStr):
    global names
    daysList = dayStrToList(daysStr)
    #print("daysList =", daysList)

    for i in range(0,len(names)):
        for j in range(0,5):
            #print("daysList[j] pre ifs =", daysList[j])
            if (name == names[i][0]):
                if(daysList[j] != False):
                    #print("daysList[j] post ifs =", daysList[j])
                    drawBlock(defineBlock(startTime, stopTime, i, daysList[j]-1), names[i][1])

    

# The days of the week are "MTWRF"



print("LOADING HOSEA")
addClass("Hosea", (9,20), (10, 30), "MWF") # PHIL 243
addClass("Hosea", (11,35), (12, 45), "MWF") # PPE 201 ##################### Question: 11:45 or 11:35?
addClass("Hosea", (12,55), (14, 5), "MWF") # ENGW 103
addClass("Hosea", (14, 15), (15, 25), "MWF") # COMP 245
addClass("Hosea", (18, 30), (21, 0), "MW") # ARTS 221
addClass("Hosea", (16, 15), (18, 0), "T") # MUEP 214
addClass("Hosea", (16, 30), (18, 0), "R") # MUEP 214
addClass("Hosea", (8, 30), (10, 20), "R") # AQTS 152
addClass("Hosea", (13, 15), (15, 5), "R") # COMP 245L
addClass("Hosea", (12, 0), (14, 0), "T") # Library
addClass("Hosea", (12, 0), (13, 0), "T") # Library
addClass("Hosea", (16, 0), (18, 0), "F") # Library
print("elapsed time =", time.time() - start, "s")



print("LOADING Abe")
addClass("Abe", (9, 20), (10, 30), "MWF") # PHYS 232    # currently at ypx = 120
addClass("Abe", (13, 15), (16, 5), "R") # PHYS 232L
addClass("Abe", (12, 55), (14, 5), "MWF") # MATH 237
#addClass("Abe", (11, 35), (12, 45), "MWF") # ARCH 213
addClass("Abe", (14, 15), (15, 25), "MWF") # ENGR 132
# addClass("Abe", (8, 30), (10, 20), "TR") # BITH 211
addClass("Abe", (18, 30), (21, 0), "MW") # ARTS 221 class only actually goes until 9
addClass("Abe", (16, 15), (18, 0), "T") # MUEP 214 # srarts at 415 on T
addClass("Abe", (16, 30), (18, 0), "R") # MUEP 214 # srarts at 415 on T
addClass("Abe", (8,30), (10, 20), "TR") # Creative Writing
print("elapsed time =", time.time() - start, "s")



print("LOADING ELLIE")
addClass("Ellie", (9, 20), (10, 30), "MWF") # PHYS 232
addClass("Ellie", (13, 15), (16, 5), "R") # PHYS 232L
addClass("Ellie", (12,55), (14, 5), "MWF") # EDUC 135/136
addClass("Ellie", (14, 15), (15, 20), "MWF") # Intermediate spanish
addClass("Ellie", (8, 30), (10, 20), "T") # Physics for the Future
addClass("Ellie", (11, 15), (13, 5), "TR") # BITH 213
print("elapsed time =", time.time() - start, "s")



print("LOADING ABBY")
addClass("Abby", (11,35), (12,45), "MWF") # CHIN 102
addClass("Abby", (8, 30), (10, 20), "TR") # BITH 211
addClass("Abby", (11,15), (13, 5), "TR") # ENGL 215
addClass("Abby", (18,30), (22, 0), "T") # HIST 103
addClass("Abby", (16, 15), (18,0), "M") # Women's Chorale
addClass("Abby", (16, 30), (18,0), "W") # Women's Chorale
print("elapsed time =", time.time() - start, "s")



print("LOADING AVA")
addClass("Ava", (8, 0), (9, 10), "MWF") # GREK 346   9:20 Class, top left of block is (330, 430) 
addClass("Ava", (8, 30), (10, 20), "TR") # BITH 211
addClass("Ava", (11,15), (13, 5), "TR") # ENGL 215
addClass("Ava", (13,15), (15, 5), "TR") # HIST 102
addClass("Ava", (12,55), (14, 5), "MWF") # Music History 135/136
addClass("Ava", (16, 0), (18, 0), "F") # Library
print("elapsed time =", time.time() - start, "s")
# also MUCS 101



print("LOADING FLORA")
addClass("Flora", (9, 20), (10, 30), "MWF") # Intro to music: historical
addClass("Flora", (11,35), (12,45), "MWF") # Intro to modern east asia
addClass("Flora", (12,55), (14, 5), "MWF") # EDUC 135/136
# addClass("Flora", (11, 15), (13, 5), "TR") # American politics and government
addClass("Flora", (18,30), (22, 0), "T") # Origins of contemporary europe
addClass("Flora", (8, 30), (10, 20), "TR") # BITH 211
print("elapsed time =", time.time() - start, "s")



print("LOADING DIXIE")
addClass("Dixie", (11,35), (12, 45), "MWF") # Spanish
addClass("Dixie", (12,55), (14, 5), "MWF") # NT Lit. & Interpretation
addClass("Dixie", (8,30), (10, 20), "TR") # Creative Writing
addClass("Dixie", (11,15), (13, 45), "TR") # Psychology
print("elapsed time =", time.time() - start, "s")



print("LOADING ELLA")
#addClass("Ella", (7, 30), (22, 30), "MTWRF")
addClass("Ella", (9, 20), (10, 30), "MWF") # Psych stats
addClass("Ella", (11, 35), (12, 45), "MWF") # Human development and ministry
addClass("Ella", (14, 15), (15, 25), "MWF") # Art Survey
addClass("Ella", (8, 30), (10, 20), "TR") # OT
addClass("Ella", (16, 15), (17, 30), "TR") # Theatre Workout
addClass("Ella", (13, 15), (15, 5), "T") # Spiritual Practices
print("elapsed time =", time.time() - start, "s")







def drawDayLines():
    for i in range(5):
        colNo = 100 + 400*i
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

for day in range(5):
    for i in range(len(names)):
        writeText(img, names[i][0], (100 + 10 + 50*i + len(names)*50*day, 3))    


img.show()

print("Saving...")
img.save("C:/Users/abrah/Desktop/schedule.jpg")

print("Elapsed time:", time.time()-start, "s")
print("PROGRAM HAS TERMINATED")


# the day is divided into 16.5 hours and 1738 pixels
# 16.5 hours * 60 minutes = 1738 pixels
# 1.755555555555 pixels/minute
# Abby Abe Ava Dixie Ella Ellie Flora Hosea
