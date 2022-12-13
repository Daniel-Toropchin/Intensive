from PIL import Image
import os, sys

path = "Food/Bread_made_from_wheat_flour/Bad"
dirs = os.listdir(path)
newFolder = "New Food/Bread_made_from_wheat_flour/Bad"

for item in dirs:
    #i = 1
    img = Image.open(os.path.join(path, item))
    img.resize((300, 300))
    img = img.convert("L")
    img.save(os.path.join(newFolder, item))
    #i+=1