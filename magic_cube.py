import bpy

for i in range(3):
    for j in range(3):
        for k in range(3):
            bpy.ops.mesh.primitive_cube_add(
                size=1,
                location=(i, j, k)
            )
