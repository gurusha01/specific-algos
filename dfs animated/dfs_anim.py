import pygame as pg
import math
import random
from pygame import mixer
#drawing circle syntax: pg.draw.circle(screen,green,(100,100),20)
#pg.draw.circle(screen,color,coordinates,radius in pixels)

#basic setup code
pg.init()
screen=pg.display.set_mode((500,500))
pg.display.set_caption("dfs_animation")
mixer.music.load("mylove.mp3")
mixer.music.play(-1)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
#nodes
nodex=[100,200,230,450,300]
nodey=[400,300,200,275,250]
no_nodes=5


visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        for i in range(no_nodes):
            x=nodex[i]
            y=nodey[i]
            if str(i) in visited:
                color=red
            else:
                color=green
            pg.draw.circle(screen,color,(x,y),20)
            
            pg.display.update()
        pg.time.delay(1000)
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

running=True
while(running):
    screen.fill((0,0,0))
    for i in range(no_nodes):
        for n in graph [str(i)]:
            point1=(nodex[i],nodey[i])
            point2=(nodex[int(n)],nodey[int(n)])
            pg.draw.line(screen, blue, point1, point2)
    dfs(visited, graph, '0')
    running=False
