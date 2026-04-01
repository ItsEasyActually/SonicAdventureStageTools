import bpy

from ...utilities.interface.sast_viewport_panel_base import SASTViewportPanelBase
from ...scene.properties.sast_scene_properties import SASTSceneProperties
from ...scene.properties.sast_set_definition_properties import SASTSETDefinitionProperties
from ...object.properties.sast_object_properties import SASTObjectProperties
from ...object.properties.sast_set_object_properties import SASTSETObjectProperties
from ...object.properties.sast_cam_object_properties import SASTCAMObjectProperties
from ...object.properties.sast_point_object_properties import SASTPointObjectProperties
from ...object.geonode.sa1cameranode import SA1CameraNode
from ...object.geonode.sa2cameranode import SA2CameraNode
from ...object.geonode.sa2pointnode import SA2PointNode
from ...object.geonode.setitemnode import SetItemNode
from ...object.operators.sast_cam_object_operators import SASTCamObjectOperators

class SASTObjectInterface(SASTViewportPanelBase):
    '''Object Properties Panel for SAST items.'''
    bl_label = 'Object Settings'
    bl_idname = 'VIEW_PT_SASTObjectInterface'
    bl_description='Object specific settings and helper tools.'

    @classmethod
    def poll(self, context: bpy.types.Context) -> bool:
        '''Poll Processing for if this panel should be displayed.'''
        obj: bpy.types.Object = context.active_object
        if (obj != None):
            if (obj.type == 'MESH'):
                return True
        
        return False
    
    def draw(self, context: bpy.types.Context):
        '''SAST Object Properties Panel Draw Function'''
        layout = self.layout
        scene_properties: SASTSceneProperties = SASTSceneProperties.get_properties()

        if (scene_properties is not None):
            obj: bpy.types.Object = context.active_object
            obj_properties: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
            obj_properties.draw_ui(layout, context)
            match (obj_properties.objtype):
                case 'POINT':
                    layout.separator(factor=2, type='LINE')
                    header: bpy.types.UILayout
                    body: bpy.types.UILayout
                    header, body = layout.panel('pt_pointprops', default_closed=False)
                    header.label(text='Point Properties')
                    if (body != None):
                        point_props: SASTPointObjectProperties = SASTPointObjectProperties.get_properties(obj)
                        if (point_props is not None):
                            point_props.draw_ui(body)
                            geonode: SA2PointNode = SA2PointNode(obj)
                            if (geonode.node != None):
                                geonode.draw_ui(body)
                case 'CAM':
                    layout.separator(factor=2, type='LINE')
                    header: bpy.types.UILayout
                    body: bpy.types.UILayout
                    header, body = layout.panel('pt_camprops', default_closed=False)
                    header.label(text='Camera Properties')
                    if (body != None):
                        cam_properties: SASTCAMObjectProperties = SASTCAMObjectProperties.get_properties(obj)
                        if (cam_properties is not None):
                            cam_properties.draw_ui(body, context)
                            match (scene_properties.game_id):
                                case 'SADXPC':
                                    cam_node: SA1CameraNode = SA1CameraNode(obj)
                                case 'SA2BPC':
                                    cam_node: SA2CameraNode = SA2CameraNode(obj)
                            if (cam_node.node is not None):
                                cam_node.draw_ui(body, cam_properties.cameramode)
                                if (scene_properties.game_id == 'SA2BPC'):
                                    cam_properties.draw_sa2props_ui(body, context)
                        opheader: bpy.types.UILayout
                        opbody: bpy.types.UILayout
                        opheader, opbody = layout.panel('pt_camops',default_closed=False)
                        opheader.label(text='Camera Item Tools', icon='TOOL_SETTINGS')
                        if (opbody != None):
                            SASTCamObjectOperators.draw_ui(opbody, context)
                case 'SET':
                    layout.separator(factor=2, type='LINE')
                    setitem_properties: SASTSETObjectProperties = SASTSETObjectProperties.get_properties(obj)
                    setitem_properties.draw_ui(layout)
                    set_item_node: SetItemNode = SetItemNode(obj)
                    if (set_item_node.node != None):
                        setitem: SASTSETDefinitionProperties = scene_properties.objlist[int(setitem_properties.objectid)]
                        set_item_node.draw_ui(layout, setitem)

            obj_properties.draw_export_flags(layout, context)
        else:
            layout.label(text='Scene Properties do not exist!', icon='WARNING_LARGE')