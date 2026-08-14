import bpy
from ...utilities.interface.sast_viewport_panel_base import SASTViewportPanelBase
from ..properties.sast_scene_properties import (
    SASTSETDefinitionProperties,
    SASTSceneProperties
)
from ..operators.sast_objlist_operators import (
    SASTObjListAddItem,
    SASTObjListDeleteItem,
    SASTObjListMoveItemUp,
    SASTObjListMoveItemDown,
    SASTObjListMoveItemTop,
    SASTObjListMoveItemBottom,
    SASTObjListImport,
    SASTObjListLoad,
    SASTObjListExport,
    SASTObjListClear,
    SASTObjListLinkAssets
)

class SAST_UL_objlist(bpy.types.UIList):
    '''The UI List Handler for the Object List Editor'''

    def draw_item(self, context: bpy.types.Context, layout: bpy.types.UILayout, data, item, icon: int | None, active_data, active_property: str | None, index: int | None, flt_flag: int | None):
        objitem: SASTSETDefinitionProperties = item

        if (len(objitem.name) > 0):
            layout.label(text=objitem.name)
        else:
            layout.label(text=objitem.internal_name)

class SASTObjListInterface:
    @staticmethod
    def draw(layout: bpy.types.UILayout, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            if (scene_props.mode == 'AUTO'):
                layout.operator(SASTObjListLoad.bl_idname, icon='APPEND_BLEND')
            header: bpy.types.UILayout = layout.row()
            header.operator(SASTObjListImport.bl_idname, icon='IMPORT')
            header.operator(SASTObjListExport.bl_idname, icon='EXPORT')
            layout.operator(SASTObjListLinkAssets.bl_idname, icon='LINK_BLEND')
            group: bpy.types.UILayout = layout.row()
            group.template_list('SAST_UL_objlist', '', scene_props, 'objlist', scene_props, 'active_object', rows=7)
            column: bpy.types.UILayout = group.column()
            column.operator(SASTObjListAddItem.bl_idname, text='', icon='ADD')
            column.operator(SASTObjListDeleteItem.bl_idname, text='', icon='REMOVE')
            column.operator(SASTObjListClear.bl_idname, text='', icon='CANCEL_LARGE')
            column.separator(type='LINE')
            column.operator(SASTObjListMoveItemTop.bl_idname, text='', icon='TRIA_UP_BAR')
            column.operator(SASTObjListMoveItemUp.bl_idname, text='', icon='TRIA_UP')
            column.operator(SASTObjListMoveItemDown.bl_idname, text='', icon='TRIA_UP')
            column.operator(SASTObjListMoveItemBottom.bl_idname, text='', icon='TRIA_DOWN_BAR')

            if (scene_props.active_object > -1):
                objitem: SASTSETDefinitionProperties = scene_props.objlist[scene_props.active_object]
                if (objitem is not None):
                    objitem.draw_ui(layout)