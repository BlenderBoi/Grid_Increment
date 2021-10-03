import bpy


ENUM_Grid_Increment_Operation = [("ADD","Add","Add"),("MINUS","Minus","Minus")]

class GRID_OT_Grid_Increment(bpy.types.Operator):
    """Increase the amount of grid by x amount"""
    bl_idname = "grid_overlay.grid_increment"
    bl_label = "Grid Increment"

    OPERATION: bpy.props.EnumProperty(items=ENUM_Grid_Increment_Operation)

    def execute(self, context):
        
        overlay = context.space_data.overlay
        scn = context.scene
        
        if self.OPERATION == "ADD":
            overlay.grid_scale += scn.grid_increment_rate
        if self.OPERATION == "MINUS":
            overlay.grid_scale -= scn.grid_increment_rate
         
        
        return {'FINISHED'}
    

def grid_increment_button(self, context):
    
    space_data = context.space_data.overlay
    
    layout = self.layout
    row = layout.row(align=True)
    row.operator("grid_overlay.grid_increment", icon="ADD", text="").OPERATION = "ADD"
    row.prop(space_data, "grid_scale", text="Grid Scale", icon="GRID")
    row.operator("grid_overlay.grid_increment", icon="REMOVE", text="").OPERATION = "MINUS"
    row = layout.row(align=True)
    row.prop(context.scene, "grid_increment_rate", text="Rate")
    
    
    

def register():
    
    
    bpy.types.Scene.grid_increment_rate = bpy.props.FloatProperty(default=0.5)
    
    bpy.utils.register_class(GRID_OT_Grid_Increment)
    
    bpy.types.VIEW3D_HT_header.prepend(grid_increment_button)

def unregister():
    
    del bpy.types.Scene.grid_increment_rate
    
    bpy.utils.unregister_class(GRID_OT_Grid_Increment)
    
    bpy.types.VIEW3D_HT_header.remove(grid_increment_button)


if __name__ == "__main__":
    register()

