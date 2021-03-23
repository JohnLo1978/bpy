bl_info = {
    "name" : "Batch-Import 3D Model",
    "author" : "Pengzhao Luo",
    "version" : (0,0,1),
    "blender" : (2,92,0),
    "location" : "N -> Tools",    # fileformat:select obj/fbx/exc...(Todo)
    "description" : "Batch-import 3D model.",
    "warning": "",
    "doc_url": "https://space.bilibili.com/385719340",
    "tracker_url": "https://space.bilibili.com/385719340",
    "category" : "Object"
}

import bpy
import os


class SimpleOperator(bpy.types.Operator):
    """Print object name in Console"""
    bl_idname = "object.batchadd"
    bl_label = "Batch Import 3D Model"

    def execute(self, context):
        path2dir = bpy.context.scene.dirpath
        full_list = os.listdir(path2dir)

        obj_list = [item for item in full_list if item[-3:] == bpy.context.scene.fileformat]

        for item in obj_list:
            path2file = os.path.join(path2dir,item)
            bpy.ops.import_scene.obj(filepath=path2file)
        
        return {'FINISHED'}

class HelloWorldPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tools"
    bl_options = {"DEFAULT_CLOSED"}


class Batch_Import_Model(HelloWorldPanel, bpy.types.Panel):
    bl_idname = "HELLO_PT_World1"
    bl_label = "Batch Import Model"
    

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello !")
        layout.prop(bpy.context.scene,'dirpath')
        layout.prop(bpy.context.scene,'fileformat')
        layout.operator(SimpleOperator.bl_idname, text="Import Something", icon="CONSOLE")
        


classes = (
    SimpleOperator,
    Batch_Import_Model
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.dirpath = bpy.props.StringProperty(subtype="DIR_PATH")
    bpy.types.Scene.fileformat = bpy.props.StringProperty()
    

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.dirpath
    del bpy.types.Scene.fileformat


if __name__ == "__main__":
    register()