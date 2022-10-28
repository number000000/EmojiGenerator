
"""
A function used to make the background of a image transparent
@param: 
filepath - the path to the image name that you want to remove background
bg_color - the rgb value of the background color

Code modified from https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all-white-pixels-transparent
"""
from PIL import Image

def remove_background(filepath, bg_color):
    img = Image.open(filepath)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == bg_color[0] and item[1] == bg_color[1] and item[2] == bg_color[2]:
            newData.append((bg_color[0], bg_color[1], bg_color[2], 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("face_nopg.png", "PNG")
