bl_info = {
    "name" : "Origin to Buttom",
    "author" : "Pengzhao Luo",
    "version" : (0,0,1),
    "blender" : (2,92,0),
    "location" : "F3 -> origin2buttom",    # Object > Set Origin(Todo)
    "description" : "Set Object(Only Mesh Included) Origin to Buttom.",
    "warning": "",
    "doc_url": "https://space.bilibili.com/385719340",
    "tracker_url": "https://space.bilibili.com/385719340",
    "category" : "Object"
}


import bpy


def main(context):
    obj = context.object
    bpy.ops.object.transform_apply(
        location=True, 
        rotation=True, 
        scale=True)
    bpy.ops.object.origin_set(
        type='ORIGIN_CENTER_OF_VOLUME',
        center='MEDIAN')

    obj.location=(0,0,0)

    min = 0
    for v in obj.data.vertices:
        if(v.co.z < min):
            min = v.co.z
    context.scene.cursor.location.z = min
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    obj.location=(0,0,0)
    context.scene.cursor.location = (0,0,0)


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.custom_origin_set"
    bl_label = "origin2buttom"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()

