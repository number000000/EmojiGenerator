"""
Written by Meihui Liu
An Emoji Generator adapted from a VIS 142 Image Generator Demo For A01 & A02 (by TA: Mingyong Cheng)
"""

# Import Modules
import pygame
from pygame.locals import *
import background_remove as rm
import random
import os.path

# Initializing pygame
pygame.init()

# Setting up the screen
screen_wide = (int)(input("The width of the canvas(in pixels): "))
screen_high = (int)(input("The height of the canvas(in pixels): "))
rm_bg = (int)(input("Do you want to make the background color transparent?(y=1/n=0): "))
screen = pygame.display.set_mode((screen_wide, screen_high), pygame.SRCALPHA)
pygame.display.set_caption('Emoji Generator')
screen = pygame.display.get_surface()
if rm_bg:
    used_color = [9, 255, 0]
else: 
    used_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
screen.fill((used_color[0], used_color[1], used_color[2]))

# make sure that the face won't exceed the size of the canvas
radius = screen_wide / 4
if radius * 2 > screen_high:
    radius = screen_high / 4
center_x = screen_wide / 2
center_y = screen_high / 2

IMAGE_SIZE = (radius, radius)

# A function for generate the color of the face randomly
def draw():
    #choose the face color
    color = (0, 0, 0)
    color_list = list(color)
    for n in range(3):
        cur_color = random.randint(0,255)
        while cur_color in used_color: # make sure the color of the face is not the same as the color of the background
            cur_color = random.randint(0,255)
        color_list[n] = cur_color
    color = tuple(color_list)

    # making sure that the circle would not be exceed the edge of the page  
    pygame.draw.circle(screen, color, (center_x, center_y), radius)

# call the function to draw
draw()


# load face components
eye1 = pygame.image.load(os.path.join('data', 'eye1.png'))
eye2 = pygame.image.load(os.path.join('data', 'eye2.png'))
eye3 = pygame.image.load(os.path.join('data', 'eye3.png'))
eye4 = pygame.image.load(os.path.join('data', 'eye4.png'))
eye5 = pygame.image.load(os.path.join('data', 'eye5.png'))
eye6 = pygame.image.load(os.path.join('data', 'eye6.png'))
eye7 = pygame.image.load(os.path.join('data', 'eye7.png'))
eye8 = pygame.image.load(os.path.join('data', 'eye8.png'))
eye9 = pygame.image.load(os.path.join('data', 'eye9.png'))
eyes = [eye1, eye2, eye3, eye4, eye5, eye6, eye7, eye8]

mouth1 = pygame.image.load(os.path.join('data', 'mouth1.png'))
mouth2 = pygame.image.load(os.path.join('data', 'mouth2.png'))
mouth3 = pygame.image.load(os.path.join('data', 'mouth3.png'))
mouth4 = pygame.image.load(os.path.join('data', 'mouth4.png'))
mouth5 = pygame.image.load(os.path.join('data', 'mouth5.png'))
mouth6 = pygame.image.load(os.path.join('data', 'mouth6.png'))
mouth7 = pygame.image.load(os.path.join('data', 'mouth7.png'))
mouths = [mouth1, mouth2, mouth3, mouth4, mouth5, mouth6, mouth7]


def draw_left_eye():
    left_eye = random.choice(eyes)
    # Scale the image to your needed size
    left_eye = pygame.transform.scale(left_eye, IMAGE_SIZE)
    # Position the eye
    img_width = left_eye.get_width()
    img_height = left_eye.get_height()
    x = center_x - (radius / 2) - (img_width / 2)
    y = center_y - (radius / 3) - (img_height / 2)
    screen.blit(left_eye, (x, y))

def draw_right_eye():
    right_eye = random.choice(eyes)
    # Scale the image to your needed size
    right_eye = pygame.transform.scale(right_eye, IMAGE_SIZE)
    # Position the eye
    img_width = right_eye.get_width()
    img_height = right_eye.get_height()
    x = center_x + (radius / 2) - (img_width / 2)
    y = center_y - (radius / 3) - (img_height / 2)
    screen.blit(right_eye, (x, y))

def draw_mouth():
    mouth = random.choice(mouths)
    # Scale the image to your needed size
    mouth = pygame.transform.scale(mouth, IMAGE_SIZE)
    # Position the mouth
    img_width = mouth.get_width()
    img_height = mouth.get_height()
    x = center_x - (img_width / 2)
    y = center_y + (radius / 2) - (img_height / 2)
    screen.blit(mouth, (x, y))

# A wrapper function that call sub-functions to draw eyes and mouth(or no mouth)
def face_draw():
    if random.randint(0,1):
        draw_mouth()
    draw_left_eye()
    draw_right_eye()

face_draw()

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
        if rm_bg:
            rm.remove_background(fileName, used_color)
        pygame.display.set_caption(fileName)
        running = True
        # Keep Displaying the window until close it manually
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit_program()
    n += 1