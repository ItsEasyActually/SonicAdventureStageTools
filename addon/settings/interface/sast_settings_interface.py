import bpy

from ...utilities.interface.sast_viewport_panel_base import SASTViewportPanelBase
from ..properties.sast_settings_properties import SASTSettingsProperties

class SASTSettingsInterface(SASTViewportPanelBase):
    '''Addon Settings Handler'''
    bl_idname = 'VIEW_PT_SASTSettingsInterface'
    bl_label = 'Addon Settings'
    bl_description='Change preferences and settings for the SAST Addon.'
    bl_options={'DEFAULT_CLOSED'}

    def draw(self, context: bpy.types.Context):
        layout: bpy.types.UILayout = self.layout
        settings: SASTSettingsProperties = SASTSettingsProperties.get_settings()
        settings.draw_ui(layout)