import bpy
from bpy.props import (
    BoolProperty
)
from ..logger.sast_logger import SASTLogger
from ..operators.sast_settings_operators import (
    SASTDebugSave,
    SASTClearLogger
)

class SASTSettingsProperties(bpy.types.AddonPreferences):
    '''Global Settings for the SAST Addon'''
    bl_idname = __package__.split('.')[0]

    def update_enable_logger(self, context: bpy.types.Context):
        from ..logger.sast_logger import SASTLogger
        if (self.enable_logger == True):
            SASTLogger.enable_logger()
            print('Debug Logger Enabled')
        elif (self.enable_logger == False):
            SASTLogger.disable_logger()
            print('Debug Logger Disabled')
        else:
            SASTLogger.disable_logger()

    enable_logger: BoolProperty(
        name='Enable Debug Logger',
        description='Enables Debug Logging for the addon.',
        update=update_enable_logger
    )

    def update_disp_point_links(self, context: bpy.types.Context):
        if (self.disp_point_links == True):
            SASTLogger.log('Turning on Points Shader Drawing')
        elif (self.disp_point_links == False):
            SASTLogger.log('Turning off Points Shader Drawing.')
        else:
            SASTLogger.log(f'Something went wrong: {self.disp_point_links}')

    disp_point_links: BoolProperty(
        name='Display Point Links',
        description='Displays a line between connected SA2 Points.',
        default=True,
        update=update_disp_point_links
    )

    def update_disp_point_cam_links(self, context: bpy.types.Context):
        if (self.disp_point_links == True):
            SASTLogger.log('Turning on Points Camera Shader Drawing')
        elif (self.disp_point_links == False):
            SASTLogger.log('Turning off Points Camera Shader Drawing.')
        else:
            SASTLogger.log(f'Something went wrong: {self.disp_point_cam_links}')

    disp_point_cam_links: BoolProperty(
        name='Display Point Camera Links',
        description='Displays a line between connected SA2 Point cameras.',
        default=True,
        update=update_disp_point_cam_links
    )

    def draw_ui(self, layout: bpy.types.UILayout):
        info_box = layout.box()
        info_box.label(text='The following settings are settings for the addon', icon='INFO')
        info_box.label(text='You can save these changes using the Save Preferences button in the Preferences window.')
        prefs_header, prefs_body = layout.panel(idname='pt_sastpreferences', default_closed=True)
        prefs_header.label(text='Debugging', icon='SETTINGS')
        if (prefs_body != None):
            prefs_body.prop(data=self, property='enable_logger')
            debug_ops_columns = prefs_body.column_flow(columns=2, align=True)
            debug_ops_columns.enabled = self.enable_logger
            debug_ops_columns.operator(operator=SASTDebugSave.bl_idname, text=SASTDebugSave.bl_label)
            debug_ops_columns.operator(operator=SASTClearLogger.bl_idname, text=SASTClearLogger.bl_label)
        layout.separator(factor=1, type='LINE')
        shader_header, shader_body = layout.panel(idname='pt_sastshadersettings', default_closed=True)
        shader_header.label(text='Shader Preferences', icon='MATSHADERBALL')
        if (shader_body != None):
            shader_body.prop(data=self, property='disp_point_links')
            shader_body.prop(data=self, property='disp_point_cam_links')

    def draw(self, context: bpy.types.Context):
        self.draw_ui(self.layout)

    @staticmethod
    def get_settings():
        return bpy.context.preferences.addons[__package__.split('.')[0]].preferences
        