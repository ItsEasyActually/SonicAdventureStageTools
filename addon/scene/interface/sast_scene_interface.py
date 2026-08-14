import bpy
from ...utilities.interface.sast_viewport_panel_base import SASTViewportPanelBase
from ...scene.properties.sast_scene_properties import SASTSceneProperties
from .sast_objlist_interface import SASTObjListInterface

class SASTSceneInterface(SASTViewportPanelBase):
    '''Scene Properties UI Handler.'''
    bl_idname = 'VIEW_PT_SASTSceneInterface'
    bl_label = 'Scene Settings & Properties'
    bl_description='Scene related settings including the Scene Object List'

    def draw(self, context: bpy.types.Context):
        layout: bpy.types.UILayout = self.layout

        from ...pynet import PyNetManager
        if (PyNetManager.is_installed() is True):
            scene_properties: SASTSceneProperties = SASTSceneProperties.get_properties()

            if (scene_properties is not None):
                scene_properties.draw_ui(layout, context)
                layout.separator(factor=1, type='LINE')
                olist_header: bpy.types.UILayout
                olist_layout: bpy.types.UILayout
                olist_header, olist_layout = layout.panel(idname='pt_olist', default_closed=True)
                olist_header.label(text='Scene Object List')
                if (olist_layout != None):
                    SASTObjListInterface.draw(olist_layout, context)
        else:
            PyNetManager.draw_ui(layout, context)