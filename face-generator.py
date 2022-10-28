"""
Written by Meihui Liu
An Emoji Generator adapted from a VIS 142 Image Generator Demo For A01 & A02 (by TA: Mingyong Cheng)
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
screen_wide = 1000
screen_high = 720
screen = pygame.display.set_mode((screen_wide, screen_high), pygame.SRCALPHA)
pygame.display.set_caption('My Image Generator')
screen = pygame.display.get_surface()
screen.fill((233, 223, 202))

radius = screen_wide / 4
if radius * 2 > screen_high:
    radius = screen_high / 4
center_x = screen_wide / 2
center_y = screen_high / 2

# A function for generate the color of the face randomly
def draw():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #circle(surface, color, center, radius)
    #making sure that the circle would not be exceed the edge of the page
        
    pygame.draw.circle(screen, color, (center_x, center_y), radius)

# call the function to draw
draw()


# load face components
cat_1 = pygame.image.load(os.path.join('data', 'cat_1.png'))
cat_2 = pygame.image.load(os.path.join('data', 'cat_2.png'))
cat_3 = pygame.image.load(os.path.join('data', 'cat_3.png'))
cat_4 = pygame.image.load(os.path.join('data', 'cat_4.png'))
cat_5 = pygame.image.load(os.path.join('data', 'cat_5.png'))
cat_6 = pygame.image.load(os.path.join('data', 'cat_6.png'))
cat_images = [cat_1, cat_2, cat_3, cat_4, cat_5, cat_6]


def draw_left_eye():
    left_eye = random.choice(cat_images)
    img_width = left_eye.get_width()
    img_height = left_eye.get_height()
    x = center_x - (radius / 2) - (img_width / 2)
    y = center_y - (radius / 3) - (img_height / 2)
    screen.blit(left_eye, (x, y))

# call the function to draw the left eye
draw_left_eye()


def draw_right_eye():
    right_eye = random.choice(cat_images)
    img_width = right_eye.get_width()
    img_height = right_eye.get_height()
    x = center_x + (radius / 2) - (img_width / 2)
    y = center_y - (radius / 3) - (img_height / 2)
    screen.blit(right_eye, (x, y))

# call the function to draw the right eye
draw_right_eye()

def draw_mouth():
    mouth = random.choice(cat_images)
    img_width = mouth.get_width()
    img_height = mouth.get_height()
    x = center_x - (img_width / 2)
    y = center_y + (radius / 2) - (img_height / 2)
    screen.blit(mouth, (x, y))

# call the function to draw the right eye
draw_mouth()


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
    fileName = "face{}.png"
    fileName = fileName.format(n)

    if not os.path.exists(fileName):
        fileName = "face{}.png"
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