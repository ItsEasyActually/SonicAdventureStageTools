import bpy
from ...utilities.geonode.geometry_node_manager import GeometryNodeManager
from .sast_geonode_base import SASTGeonodeBase
from ...utilities.logger.sast_logger import SASTLogger
import os

class SA2PointNode(SASTGeonodeBase):
    '''Class to handle the SA2PointNode from Blender.'''

    modifier_file: str          = os.path.join('blend', 'cam', 'SA2CamPoint.blend')
    modifier_name: str          = 'SA2PointNode'

    player_point_radius: str    = 'Socket_2'
    camera_x_point: str         = 'Socket_3'
    camera_y_point: str         = 'Socket_4'
    camera_z_point: str         = 'Socket_5'
    camera_point_radius: str    = 'Socket_6'

    enable_player_point: str    = 'Socket_7'
    enable_player_tracking: str = 'Socket_8'

    @staticmethod
    def poll(obj: bpy.types.Object) -> bool:
        return GeometryNodeManager.has_geometry_node(obj, SA2PointNode.modifier_name)

    @staticmethod
    def make(obj: bpy.types.Object) -> bpy.types.NodesModifier:
        if (obj.type == 'MESH'):
            SASTLogger.log(f'Valid object, adding {SA2PointNode.modifier_name} Geometry Node')
            return GeometryNodeManager.create_node(obj, SA2PointNode.modifier_file, SA2PointNode.modifier_name)
        else:
            SASTLogger.log('Object Data Type is not MESH. Invalid Object!')

    def reset_properties(self):
        '''Resets the properties of the SA2 Point Node'''
        SASTLogger.log('Resetting Geometry Node Properties')
        self.set_player_point_radius(10)
        self.set_camera_x_point(0)
        self.set_camera_y_point(0)
        self.set_camera_z_point(0)
        self.set_camera_point_radius(0)
        self.set_enable_player_point(False)
        self.set_enable_player_tracking(False)

    def draw_ui(self, layout: bpy.types.UILayout):
        '''Draws the settings into a UILayout.'''
        layout.prop(data=self.node.properties.inputs.Socket_2, property='value', text='Player Point Radius')
        layout.prop(data=self.node.properties.inputs.Socket_3, property='value', text='Camera X Position')
        layout.prop(data=self.node.properties.inputs.Socket_4, property='value', text='Camera Y Position')
        layout.prop(data=self.node.properties.inputs.Socket_5, property='value', text='Camera Z Position')
        #layout.prop(data=self.node.properties.inputs.Socket_6, property='value', text='Camera Point Radius')
        layout.prop(data=self.node.properties.inputs.Socket_7, property='value', text='Enable Player Point')
        layout.prop(data=self.node.properties.inputs.Socket_8, property='value', text='Enable Player Tracking')

    def set_player_point_radius(self, value: float):
        self.node.properties.inputs.Socket_2.value = value
    
    def set_camera_x_point(self, value: float):
        self.node.properties.inputs.Socket_3.value = value
    
    def set_camera_y_point(self, value: float):
        self.node.properties.inputs.Socket_4.value = value
    
    def set_camera_z_point(self, value: float):
        self.node.properties.inputs.Socket_5.value = value
    
    def set_camera_point_radius(self, value: float):
        self.node.properties.inputs.Socket_6.value = value
    
    def set_enable_player_point(self, value: float):
        self.node.properties.inputs.Socket_7.value = value
    
    def set_enable_player_tracking(self, value: bool):
        self.node.properties.inputs.Socket_8.value = value

    def get_player_point_radius(self) -> float:
        return self.node.properties.inputs.Socket_2.value
    
    def get_camera_x_point(self) -> float:
        return self.node.properties.inputs.Socket_3.value
    
    def get_camera_y_point(self) -> float:
        return self.node.properties.inputs.Socket_4.value
    
    def get_camera_z_point(self) -> float:
        return self.node.properties.inputs.Socket_5.value
    
    def get_camera_point_radius(self) -> float:
        return self.node.properties.inputs.Socket_6.value
    
    def get_enable_player_point(self) -> bool:
        return self.node.properties.inputs.Socket_7.value
    
    def get_enable_player_tracking(self) -> bool:
        return self.node.properties.inputs.Socket_8.value

    