#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 16:10:35 2018

@author: liuchuang

改变角度
"""

from LightPipes import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

wavelength=1040*nm #wavelength of HeNe laser
size=10*mm # size of the grid
N=800 # number (NxN) of grid pixels
R=3*mm # laser beam radius
z1=8*cm # length of arm 1
z2=8*cm # length of arm 2
z3=1*cm # distance laser to beamsplitter
z4=5*cm # distance beamsplitter to screen
Rbs=0.3 # 分光镜反射  37  55 影响不大
ty=0.0*mrad # tilt of mirror 1
f=50*cm # focal length of positive lens

"""
###读取 迈克尔逊干涉图片
img=mpimg.imread('Michelson.png')
plt.imshow(img); plt.axis('off')
plt.show()
"""

for i in range(10):
    tx=(i-1)/10*mrad
#Generate a weak converging laser beam using a weak positive lens:
    F=Begin(size,wavelength,N)
    F=GaussHermite(0,0,1,R,F)
    F=Lens(f,0,0,F)

#Propagate to the beamsplitter:
    F=Forvard(z3,F)

#Split the beam and propagate to mirror #2:
    F2=IntAttenuator(1-Rbs,F)
    F2=Forvard(z2,F2)

#Introduce tilt and propagate back to the beamsplitter:
    F2=Tilt(tx,ty,F2)
    F2=Forvard(z2,F2)
    F2=IntAttenuator(Rbs,F2)

#Split off the second beam and propagate to- and back from the mirror #1:
    F10=IntAttenuator(Rbs,F)
    F1=Forvard(z1*2,F10)
    F1=IntAttenuator(1-Rbs,F1)

#Recombine the two beams and propagate to the screen:
    F=BeamMix(F1,F2)
    F=Forvard(z4,F)
    I=Intensity(1,F)
    
    plt.subplot(2,5,i+1)
    
    plt.imshow(I,cmap='jet'); plt.axis('off');
plt.show()
    