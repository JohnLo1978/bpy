import bpy
import numpy as np
import math as m

tempX = tempY = 0
for i in np.arange(0,22*m.pi,m.pi/1000):
    x = i * m.cos(i)
    y = i * m.sin(i)
    bpy.ops.mesh.duplicate_move(TRANSFORM_OT_translate={"value":(x-tempX,y-tempY,43*m.pi/0.618/22000)})
    tempX = x
    tempY = y
