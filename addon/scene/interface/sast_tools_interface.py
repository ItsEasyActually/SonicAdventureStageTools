import bpy
from ...utilities.interface.sast_viewport_panel_base import SASTViewportPanelBase
from ...scene.properties.sast_scene_properties import SASTSceneProperties
from ..operators.sast_scene_operators import (
    SASTImportSETAutomatic,
    SASTImportSETManual,
    SASTImportCameraAutomatic,
    SASTImportCameraManual,
    SASTExportSETAutomatic,
    SASTExportSETManual,
    SASTExportCameraAutomatic,
    SASTExportCameraManual
)

class SASTSceneToolsInterface(SASTViewportPanelBase):
    ''''''
    bl_idname='VIEW_PT_SASTSceneToolsInterface'
    bl_label = 'Utilities'
    bl_description='Tooling operators including import, export, and helper utilities.'

    def draw_import_operators(self, layout: bpy.types.UILayout, mode: str):
        imp_set_text: str = 'Import SET File'
        imp_cam_text: str = 'Import CAM File'
        imp_icon: str = 'IMPORT'
        match (mode):
            case 'AUTO':
                layout.operator(SASTImportSETAutomatic.bl_idname, text=imp_set_text, icon=imp_icon)
                layout.operator(SASTImportCameraAutomatic.bl_idname, text=imp_cam_text, icon=imp_icon)
            case 'MANUAL':
                layout.operator(SASTImportSETManual.bl_idname, text=imp_set_text, icon=imp_icon)
                layout.operator(SASTImportCameraManual.bl_idname, text=imp_cam_text, icon=imp_icon)

    def draw_export_operators(self, layout: bpy.types.UILayout, mode: str):
        exp_set_text: str = 'Export SET File'
        exp_cam_text: str = 'Export CAM File'
        exp_icon: str = 'EXPORT'
        match (mode):
            case 'AUTO':
                layout.operator(SASTExportSETAutomatic.bl_idname, text=exp_set_text, icon=exp_icon)
                layout.operator(SASTExportCameraAutomatic.bl_idname, text=exp_cam_text, icon=exp_icon)
            case 'MANUAL':
                layout.operator(SASTExportSETManual.bl_idname, text=exp_set_text, icon=exp_icon)
                layout.operator(SASTExportCameraManual.bl_idname, text=exp_cam_text, icon=exp_icon)

    def draw(self, context: bpy.types.Context):
        layout: bpy.types.UILayout = self.layout
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()

        imp_header: bpy.types.UILayout
        imp_layout: bpy.types.UILayout
        imp_header, imp_layout = layout.panel(idname='pt_impscene', default_closed=True)
        imp_header.label(text='Import Tools')
        if (imp_layout != None):
            self.draw_import_operators(imp_layout, scene_props.mode)

        layout.separator(type='LINE')

        exp_header: bpy.types.UILayout
        exp_layout: bpy.types.UILayout
        exp_header, exp_layout = layout.panel(idname='pt_expscene', default_closed=True)
        exp_header.label(text='Export Tools')
        if (exp_layout != None):
            self.draw_export_operators(exp_layout, scene_props.mode)
