import bpy
from .layouts import SASTViewportPanel
from ..properties import SASTSceneProperties
from ..operators.sast_scene_operators import SASTSceneOperators

class SASTSceneInterface(SASTViewportPanel):
    '''Scene Properties UI Handler.'''
    bl_idname = 'VIEW_PT_SASTSceneInterface'
    bl_label = 'Scene Settings & Import Tools'
    bl_description='Scene specific settings and IO processing.'

    def draw(self, context: bpy.types.Context):
        layout: bpy.types.UILayout = self.layout

        from ..pynet import PyNetManager
        if (PyNetManager.is_installed() is True):
            scene_properties: SASTSceneProperties = SASTSceneProperties.get_properties()

            if (scene_properties is not None):
                scene_properties.draw_ui(layout, context)
                layout.separator(factor=1, type='LINE')
                grid: bpy.types.UILayout = layout.grid_flow(columns=2, even_columns=True)
                match (scene_properties.mode):
                    case 'AUTO':
                        grid.enabled = len(scene_properties.load_directory) > 0
                        SASTSceneOperators.draw_ui_auto(grid, context)
                    case 'MANUAL':
                        grid.enabled = True
                        SASTSceneOperators.draw_ui_manual(grid, context)
        else:
            PyNetManager.draw_ui(layout, context)
            