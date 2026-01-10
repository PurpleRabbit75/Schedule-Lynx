from PIL import Image, ImageDraw, ImageFont

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
    for _ in range(x):
        r = []
        for _ in range(y):
            r.append(color)
        g.append(r)
    return g
        


def writeText(image, String, coords, fontSize = 12, fontType = "arial.ttf", color = (0, 0, 0)):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontType, fontSize)
    draw.text(coords, String, fill = color, font = font)

