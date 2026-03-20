import bpy

class SASTViewportPanelBase(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SA Stage Tools'