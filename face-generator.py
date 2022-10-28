"""
VIS 142 Image Generator Demo For A01 & A02 | TA: Mingyong Cheng
Install pygame, run this line in Terminal: python3 -m pip install -U pygame --user
Check this page if you meet any issues with installation: https://www.pygame.org/wiki/GettingStarted
Check pygame documentation for more information: https://www.pygame.org/docs/
"""

# Import Modules
import pygame
from pygame.locals import *
import gradient_pygame as gp
import random
import os.path

# Initializing pygame
pygame.init()

# Setting up the screen in 640 pixels wide, and 360 pixels high
screen_wide = 1280
screen_high = 720
screen = pygame.display.set_mode((screen_wide, screen_high), pygame.SRCALPHA)
pygame.display.set_caption('My Image Generator')
screen = pygame.display.get_surface()
screen.fill((233, 223, 202))


# A function for generate the color of the face randomly
def draw():
    for n in range(3000):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        #circle(surface, color, center, radius)
        #making sure that the circle would not be exceed the edge of the page
        radius = screen_wide / 4
        if (radius * 2) > screen_high:
            radius = screen_high / 4
        
        pygame.draw.circle(screen, color, (screen_wide / 2, screen_high / 2), min(screen_wide, screen_high) / 4)


# call the function to draw
draw()

"""
# 2️⃣Let's play with gradient! As we are still using draw function, we cannot draw transparently
def draw_gradient():
    for n in range(0, 3000):
        x = random.randint(1, 1280)
        y = random.randint(1, 720)
        w = random.randint(1, 320)
        h = random.randint(1, 180)
        rect_1 = Rect(x, y, w, h)
        color_1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        vertical = bool(random.getrandbits(1))
        forward = bool(random.getrandbits(1))

        # See gradient_pygame.py; A block of code shared on the pygame wiki for quick simple gradient generation
        gp.fill_gradient(screen, color_1, color_2, rect_1, vertical, forward)


# Call the function to draw the rects with gradient color
# draw_gradient()
"""

# 3️⃣load images in a lists and randomly draw on the screen
cat_1 = pygame.image.load(os.path.join('VIS142-Week3-Demo\data', 'cat_1.png'))
cat_2 = pygame.image.load(os.path.join('VIS142-Week3-Demo\data', 'cat_2.png'))
cat_3 = pygame.image.load(os.path.join('VIS142-Week3-Demo\data', 'cat_3.png'))
cat_4 = pygame.image.load(os.path.join('VIS142-Week3-Demo\data', 'cat_4.png'))
cat_5 = pygame.image.load(os.path.join('VIS142-Week3-Demo\data', 'cat_5.png'))
cat_6 = pygame.image.load(os.path.join('VIS142-Week3-Demo\data', 'cat_6.png'))
cat_images = [cat_1, cat_2, cat_3, cat_4, cat_5, cat_6]


def draw_image():
    for n in range(0, 100):
        x = random.randint(1, 1280)
        y = random.randint(1, 720)
        screen.blit(random.choice(cat_images), (x, y))


# call the function to draw the loaded images
draw_image()


# Define a function for exiting program
def exit_program():
    pygame.display.quit()
    pygame.quit()
    exit()


# Update the display
pygame.display.update()

n = 1

# infinite run
while True:
    fileName = "drawn{}.png"
    fileName = fileName.format(n)

    if not os.path.exists(fileName):
        fileName = "drawn{}.png"
        fileName = fileName.format(n)
        pygame.image.save(screen, fileName)
        print("export image:", fileName)
        pygame.display.set_caption(fileName)
        running = True
        # Keep Displaying the window until close it manually
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit_program()
    n += 1