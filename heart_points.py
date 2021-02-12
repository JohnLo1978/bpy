import bpy
import math as m
import numpy as np

tempX = tempY = 0

for t in np.arange(0,2*m.pi,m.pi/50):
    x=16*(m.sin(t))**3
    y=13*m.cos(t)-5*m.cos(2*t)-2*m.cos(3*t)-m.cos(4*t)
    bpy.ops.mesh.duplicate_move(
        TRANSFORM_OT_translate={"value":(x-tempX,y-tempY,0)}
    )
    tempX = x
    tempY = y
