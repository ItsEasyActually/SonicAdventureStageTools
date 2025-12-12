import bpy
from . import GeometryNodeManager
from .geonodebase import GeoNodeBase
from ..logger.sast_logger import SASTLogger

class SA2PointNode(GeoNodeBase):
    '''Class to handle the SA2PointNode from Blender.'''

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
            return GeometryNodeManager.create_node(obj, SA2PointNode.modifier_name)
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
        layout.prop(data=self.node, property=self.get_layout_prop(self.player_point_radius), text='Player Point Radius')
        layout.prop(data=self.node, property=self.get_layout_prop(self.camera_x_point), text='Camera X Position')
        layout.prop(data=self.node, property=self.get_layout_prop(self.camera_y_point), text='Camera Y Position')
        layout.prop(data=self.node, property=self.get_layout_prop(self.camera_z_point), text='Camera Z Position')
        #layout.prop(data=self.node, property=self.get_layout_prop(self.camera_point_radius), text='Camera Point Radius')
        layout.prop(data=self.node, property=self.get_layout_prop(self.enable_player_point), text='Enable Player Point')
        layout.prop(data=self.node, property=self.get_layout_prop(self.enable_player_tracking), text='Enable Player Tracking')

    def set_player_point_radius(self, value: float):
        self.node[self.player_point_radius] = value
    
    def set_camera_x_point(self, value: float):
        self.node[self.camera_x_point] = value
    
    def set_camera_y_point(self, value: float):
        self.node[self.camera_y_point] = value
    
    def set_camera_z_point(self, value: float):
        self.node[self.camera_z_point] = value
    
    def set_camera_point_radius(self, value: float):
        self.node[self.camera_point_radius] = value
    
    def set_enable_player_point(self, value: float):
        self.node[self.enable_player_point] = value
    
    def set_enable_player_tracking(self, value: bool):
        self.node[self.enable_player_tracking] = value

    def get_player_point_radius(self) -> float:
        return self.node[self.player_point_radius]
    
    def get_camera_x_point(self) -> float:
        return self.node[self.camera_x_point]
    
    def get_camera_y_point(self) -> float:
        return self.node[self.camera_y_point]
    
    def get_camera_z_point(self) -> float:
        return self.node[self.camera_z_point]
    
    def get_camera_point_radius(self) -> float:
        return self.node[self.camera_point_radius]
    
    def get_enable_player_point(self) -> bool:
        return self.node[self.enable_player_point]
    
    def get_enable_player_tracking(self) -> bool:
        return self.node[self.enable_player_tracking]

    