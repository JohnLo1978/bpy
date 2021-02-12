import bpy  
import os

path2dir = os.getcwd()
print("writing to  " + path2dir + "\n\n")

path2file = os.path.join(path2dir, 'mesh_data.txt')
with open(path2file, 'w') as f:
      
    # verts  
    f.write("verts=[\n")   
      
    for i in bpy.context.active_object.data.vertices:   
        coords = i.co.x, i.co.y, i.co.z  
        f.write(str(coords)+",\n")  
      
    f.write("]\n\n\n\n")  
      
    
    # edges
    f.write("edges=[\n")  
      
    for i in bpy.context.active_object.data.edges:  
        verts_on_edge = i.vertices[:]  
        f.write(str(verts_on_edge)+",\n")  
      
    f.write("]\n\n\n\n")  
    
    
    # faces  
    f.write("faces=[\n")
      
    for i in bpy.context.active_object.data.polygons:  
        verts_on_face = i.vertices[:]   
        f.write(str(verts_on_face)+",\n")  
      
    f.write("]\n\n\n\n")

with open(path2file, 'r') as f:
    print(f.read())
    
os.startfile(path2file)
