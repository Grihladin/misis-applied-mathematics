import pygame
import numpy as np
from math import *

WINDOW_SIZE = 800
angle_x = angle_y = angle_z = 50

rotation_x = np.array([
    [1, 0, 0],
    [0, cos(angle_x), -sin(angle_x)],
    [0, sin(angle_x), cos(angle_x)]
])

rotation_y = np.array([
    [cos(angle_y), 0, sin(angle_y)],
    [0, 1, 0],
    [-sin(angle_y), 0, cos(angle_y)]
])

rotation_z = np.array([
    [cos(angle_z), -sin(angle_z), 0],
    [sin(angle_z), cos(angle_z), 0],
    [0, 0, 1]
])

projection_matrix = np.array ([
    [1,0,0],
    [0,1,0],
    [0,0,0]
])

cube = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [0, 0, 1],
    [0, 1, 0],
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
])

def connect_points(i, j, points):
    pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]) , (points[j][0], points[j][1]))

window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()


#Main Loop
scale = 100

while True:
    clock.tick(60)
    reversedCube = cube.dot(rotation_y)
    point2D = reversedCube.dot(projection_matrix)
 
    points = [0 for _ in range(len(cube))]
    counter = 0
    for pos in range(len(cube)):
        
        x = (point2D[pos][0] * scale) + WINDOW_SIZE/2
        y = (point2D[pos][1] * scale) + WINDOW_SIZE/2
       
        
        points[counter] = (x, y)
        counter +=1 
        
        pygame.draw.circle(window, (255, 0, 0), (x, y), 5)
    
    connect_points(0, 1, points)
    connect_points(0, 3, points)
    connect_points(0, 4, points)
    connect_points(1, 2, points)
    connect_points(1, 5, points)
    connect_points(2, 6, points)
    connect_points(2, 3, points)
    connect_points(3, 7, points)
    connect_points(4, 5, points)
    connect_points(4, 7, points)
    connect_points(6, 5, points)
    connect_points(6, 7, points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
              
    pygame.display.update()
