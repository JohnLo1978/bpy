# batch-import OBJ files

import bpy
import os

path2dir = "D:\Art Res\Model"
full_list = os.listdir(path2dir)

print(full_list)

obj_list = [item for item in full_list if item[-3:] == 'obj']

print(obj_list)

for item in obj_list:
    path2file = os.path.join(path2dir,item)
    print(path2file)
    bpy.ops.import_scene.obj(filepath=path2file)
