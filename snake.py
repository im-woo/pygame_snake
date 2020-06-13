#Snake Tutorial Python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

width, height, rows, columns, s = 0, 0, 0, 0, 0


class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)  # change our position    

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # Width/Height of each cube
        i = self.pos[0] # Current row
        j = self.pos[1] # Current Column

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        # By multiplying the row and column value of our cube by the width and height of each cube we can determine where to draw it
        
        if eyes: # Draws the eyes
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)   
        

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos, 1, 0, color)  # The head will be the front of the snake
        self.body.append(self.head)  # We will add head (which is a cube object)
        # to our body list

        # These will represent the direction our snake is moving
        self.dirnx = 0 
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                
        for i, c in enumerate(self.body):  # Loop through every cube in our body
            p = c.pos[:]  # This stores the cubes position on the grid
            if p in self.turns:  # If the cubes current position is one where we turned
                turn = self.turns[p]  # Get the direction we should turn
                c.move(turn[0],turn[1])  # Move our cube in that direction
                if i == len(self.body)-1:  # If this is the last cube in our body remove the turn from the dict
                    self.turns.pop(p)
            else:  # If we are not turning the cube
                # If the cube reaches the edge of the screen we will make it appear on the opposite side
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)  # If we haven't reached the edge just move in our current direction

    def reset(self, pos):
        pass

    def addCube(self):
        pass
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  # for the first cube in the list we want to draw eyes
                c.draw(surface, True)  # adding the true as an argument will tell us to draw eyes
            else:
                c.draw(surface)  # otherwise we will just draw a cube


def drawGrid(surface):
    global width, height, rows, columns
    sizeBtwn_w = width // columns
    siwzBtwn_h = height // rows
    
    x = 0 
    y = 0
    for l in range(rows):  # We will draw one vertical and one horizontal line each loop
        x = x + sizeBtwn_w
        y = y + siwzBtwn_h

        pygame.draw.line(surface, (0,0,0), (x,0),(x,height))
        pygame.draw.line(surface, (0,0,0), (0,y),(width, y))
        

def redrawWindow(surface):
    global s
    surface.fill((255,255,255))  # Fills the screen with black
    s.draw(surface)
    drawGrid(surface)  # Will draw our grid lines
    pygame.display.update()  # Updates the screen


def randomSnack(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global width, height, rows, columns, s
    width = 500  # Width of our screen
    height = 500  # Height of our screen
    rows = 20  # Amount of rows
    columns = 20
    pygame.init()

    win = pygame.display.set_mode((width, height))  # Creates our screen object
    s = snake((0,255,0), (10,10))  # Creates a snake object which we will code later
  
    clock = pygame.time.Clock() # creating a clock object
    flag = True
    # STARTING MAIN LOOP
    while flag:
        s.move()
        redrawWindow(win)  # This will refresh our screen
        clock.tick(30)  # Will ensure our game runs at 10 FPS

main()