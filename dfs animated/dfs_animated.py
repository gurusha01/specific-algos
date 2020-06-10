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
graph = {'0': set(['1']),
         '1': set(['0', '2', '11']),
         '2': set(['1','3','4']),
         '3': set(['2']),
         '4': set(['2', '5','14']),
         '5': set(['4', '7','9']),
         '6': set(['7']),
         '7': set(['6','8','5']),
         '8': set(['7']),
         '9': set(['5', '16']),
         '10': set(['14']),
         '11': set(['1', '13', '12']),
         '12': set(['11']),
         '13': set(['11']),
         '14': set(['10', '4']),
         '15': set(['16']),
         '16': set([ '9', '15'])
         
         }
#nodes
nodex=[25,100,150,200,200,250,150,200,250,300,400,75,100,50,350,300,350]
nodey=[50,50,100,150,100,150,150,200,250,250,400,100,200,200,200,400,300]
no_nodes=17

    
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
    running=False
