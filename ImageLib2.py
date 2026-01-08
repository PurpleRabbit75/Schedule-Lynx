from PIL import Image, ImageDraw, ImageFont
from ListLib import *

def toGrid(image):
    pixels = image.load()
    w, h = image.size
    grid = []
    for i in range(w):
        newList = []
        for j in range(h):
            newList.append(pixels[i, j])
        grid.append(newList)
    return grid


def toImage(grid):
    image = Image.new("RGB", (len(grid), len(grid[0])), "white")
    im = image.load()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            im[i, j] = grid[i][j]
    return image
    

def makeGrid(x, y, color = (255, 255, 255)):
    g = []
    for i in range(x):
        r = []
        for j in range(y):
            r.append(color)
        g.append(r)
    return g
##image = Image.open("C:/Users/abrah/Desktop/test.jpg")
##g = toGrid(image)
##toImage(g).show()





# image.save("new_image.png")
        


def writeText(image, String, coords, fontSize = 12, fontType = "arial.ttf", color = (0, 0, 0)):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontType, fontSize)
    draw.text(coords, String, fill = color, font = font)


##if __name__ == "main":
##    grid = []
##    for i in range(100):
##        l = []
##        for j in range(100):
##            l.append((255, 255, 255))
##        grid.append(l)
##
##    img = toImage(grid)
##    writeText(img, "Hello, World", (20, 20))
##    img.show()


##from PIL import Image, ImageDraw, ImageFont
##
### Open the image
##image = Image.open("your_image.jpg")
##
### Create a drawing object
##draw = ImageDraw.Draw(image)
##
### Choose a font
##font = ImageFont.truetype("arial.ttf", 36)  # Replace with your desired font and size
##
### Text to write
##text = "Hello, World!"
##
### Text color
##text_color = (255, 255, 255)  # White
##
### Position of the text
##x = 10
##y = 10
##
### Draw the text
##draw.text((x, y), text, fill=text_color, font=font)

if (__name__ == "__main__2"):
    def toRGB(minimum, maximum, value):
        "function copied and edited from https://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map"
        minimum, maximum = float(minimum), float(maximum)
        ratio = 2 * (value-minimum) / (maximum - minimum)
        b = int(max(0, 255*(1 - ratio)))
        r = int(max(0, 255*(ratio - 1)))
        g = 255 - b - r
        return (r, g, b)
    cols = []
    for i in range(500):
        cols.append(toRGB(0, 500, i))
    grid = []
    for i in range(500):
        grid.append([cols[i] for j in range(100)])
    img = toImage(grid)
    img.show()

if (__name__ == "__main__"):

    colors = [
        (138, 43, 226),
        #(139, 0, 0),
        (255, 20, 157), #(255, 105, 180), (255, 20, 147)
        (220, 20, 60),
        (255, 69, 0),
        (255, 140, 0),
        #(255, 165, 0),
        (255, 215, 0),
        (75, 185, 50),
        #maybe another green (darkish)
        #(30, 164, 220), #or     (30, 144, 255),      (65, 105, 225)
        (25, 132, 125),
        
        (40, 40, 185), #Dark blue
        (75, 0, 130),
        #(160, 82, 45), #or (139, 69, 19)
        (169, 169, 169),
        (255, 255, 255),
        (266, 266, 266)
        
        ]

    grid = []
    for i in range(1500):
        L = []
        for c in colors:
            for j in range(100):
                L.append(c)
        grid.append(L)

    i = toImage(grid)
    i.show()
        





