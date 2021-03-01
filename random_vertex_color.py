import bpy
import random

obj = bpy.data.objects["Cube"]
mesh = obj.data

if not mesh.vertex_colors:
    mesh.vertex_colors.new()

color_layer = mesh.vertex_colors["Col"] 

# 8 polygonss  24 loop_indices
i = 0
for polygon in mesh.polygons:
    for loop_index in polygon.loop_indices:
        r, g, b = [random.random() for i in range(3)]
        color_layer.data[i].color = (r, g, b, 1.0)
        i += 1

bpy.ops.object.mode_set(mode='VERTEX_PAINT')
