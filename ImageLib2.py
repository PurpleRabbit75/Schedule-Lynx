import sys
import subprocess
import importlib

def install_and_import(package_name, import_name):
    try:
        # Check if the module can be imported
        importlib.import_module(import_name)
        print(f"'{import_name}' is already installed.")
    except ImportError:
        print(f"'{import_name}' not found. Installing '{package_name}'...")
        try:
            # Use subprocess to run the pip install command
            # sys.executable ensures we use the pip associated with the CURRENT Python interpreter
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            
            # Ensure the module is available in the current session
            importlib.invalidate_caches()
            importlib.import_module(import_name)
            print(f"Successfully installed '{package_name}'.")
        except Exception as e:
            print(f"Failed to install '{package_name}'. Error: {e}")
            sys.exit(1)

install_and_import("Pillow", "PIL")

# --- Your main script code goes here ---
from PIL import Image
print("PIL is ready to use!")

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

