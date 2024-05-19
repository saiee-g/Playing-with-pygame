# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:26:38 2024
reference: https://www.youtube.com/watch?v=675teI6-_-g
@author: snowfox
"""

import pygame
import pyaudio
import math

#initialize the pygame window
screenWidth = 700
screenHeight = 700
pygame.init()
pygame.display.set_caption("Sound Visualizer")
screen = pygame.display.set_mode((screenWidth,screenHeight))
clock = pygame.time.Clock()


#Audio Initialization
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 4100

audio = pyaudio.PyAudio()
openStream = audio.open(format=FORMAT, rate=RATE, channels=CHANNELS, input=True, frames_per_buffer=CHUNK)


def getMicInputLevel():
   data = openStream.read(CHUNK) #reads audio
   #calculate root mean squared for shape of audio wave
   rms=0
   for i in range(0, len(data), 2):
       sample = int.from_bytes(data[i:i+2], byteorder='little', signed=True)
       rms += sample * sample
   rms = math.sqrt(rms/(CHUNK/2))
   return rms
    
def sineWave(amplitude):
    screen.fill((0,0,0)) #bgcolor of screen
    points=[]  #holds all the points of sine wave
    if amplitude>10:  #set min amp
        for x in range(screenWidth):
            y = screenHeight/2+ int(amplitude* math.sin(x*0.02))
            points.append((x,y))
    else : #flat line if no audio
        points.append((0, screenHeight/2))
        points.append((screenWidth, screenHeight/2))
    
    if amplitude<=10:
        pygame.draw.lines(screen,(255,255,255), False, points, 2)
    elif 10<amplitude<40:
        pygame.draw.lines(screen,(60,255,255), False, points, 2)
    elif 40<=amplitude<70:
        pygame.draw.lines(screen,(255,165,0), False, points, 2)
    else:
        pygame.draw.lines(screen,(255,0,0), False, points, 2)
    
    pygame.display.flip()

isRunning = True
amplitude = 100

while isRunning:
    for event in pygame.event.get():
        #if keystroke on cross button pressed, quits
        if event.type == pygame.QUIT:
            isRunning = False
    
    #to dampen the very high amp level
    ampAdjust = getMicInputLevel()/50
    amplitude = max(10, ampAdjust)
    
    sineWave(amplitude)
    #loop is repeated only 60 times per second        
    clock.tick(60)

pygame.quit()
    
    

