import bpy
from ...utilities.geonode.geometry_node_manager import GeometryNodeManager
from .sast_geonode_base import SASTGeonodeBase
from ...utilities.logger.sast_logger import SASTLogger
import os

class SA2CameraNode(SASTGeonodeBase):
    '''SA2 Camera Node'''

    modifier_file: str      = os.path.join('blend', 'cam', 'SA2Camera.blend')
    modifier_name: str      = 'SA2CameraNode'

    camera_mode: str        = 'Socket_2'
    collision_shape: str    = 'Socket_3'

    collision_x_angle: str  = 'Socket_4'
    collision_y_angle: str  = 'Socket_5'
    collision_z_angle: str  = 'Socket_6'
    collision_x_scale: str  = 'Socket_7'
    collision_y_scale: str  = 'Socket_8'
    collision_z_scale: str  = 'Socket_9'

    camera_x_angle: str     = 'Socket_10'
    camera_y_angle: str     = 'Socket_11'
    camera_z_angle: str     = 'Socket_12'
    camera_x_position: str  = 'Socket_13'
    camera_y_position: str  = 'Socket_14'
    camera_z_position: str  = 'Socket_15'
    target_x_position: str  = 'Socket_16'
    target_y_position: str  = 'Socket_17'
    target_z_position: str  = 'Socket_18'

    @staticmethod
    def poll(obj: bpy.types.Object) -> bool:
        return GeometryNodeManager.has_geometry_node(obj, SA2CameraNode.modifier_name)

    @staticmethod
    def make(obj: bpy.types.Object) -> bpy.types.NodesModifier:
        if (obj.type == 'MESH'):
            SASTLogger.log(f'Valid object, adding {SA2CameraNode.modifier_name} Geometry Node')
            return GeometryNodeManager.create_node(obj, SA2CameraNode.modifier_file, SA2CameraNode.modifier_name)
        else:
            SASTLogger.log('Object Data Type is not MESH. Invalid Object!')

    def reset_properties(self):
        SASTLogger.log('Resetting Geometry Node Properties')
        self.set_collision_shape(0)
        self.set_collision_x_scale(10)
        self.set_collision_y_scale(10)
        self.set_collision_z_scale(10)
        self.set_collision_x_angle(0)
        self.set_collision_y_angle(0)
        self.set_collision_z_angle(0)
        self.set_camera_x_position(0)
        self.set_camera_y_position(0)
        self.set_camera_z_position(0)
        self.set_camera_x_angle(0)
        self.set_camera_y_angle(0)
        self.set_camera_z_angle(0)
        self.set_target_x_position(0)
        self.set_target_y_position(0)
        self.set_target_z_position(0)

    def draw_ui(self, layout: bpy.types.UILayout, cammode: str):
        '''Draws the properties menu.'''
        layout.prop(data=self.node, property=self.get_layout_prop(self.collision_shape), text='Volume Shape')
        layout.separator(factor=1, type='LINE')
        match (cammode):
            case 'Klamath':
                layout.prop(data=self.node, property=self.get_layout_prop(self.target_x_position), text='Target X Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.target_z_position), text='Target Y Position')
            case 'Fix':
                layout.prop(data=self.node, property=self.get_layout_prop(self.camera_x_position), text='Camera X Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.camera_z_position), text='Camera Y Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.camera_y_position), text='Camera Z Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.target_x_position), text='Target X Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.target_z_position), text='Target Y Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.target_y_position), text='Target Z Position')
            case 'Ashland':
                layout.prop(data=self.node, property=self.get_layout_prop(self.camera_x_position), text='Camera X Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.camera_z_position), text='Camera Y Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.camera_y_position), text='Camera Z Position')
            case 'Point':
                layout.prop(data=self.node, property=self.get_layout_prop(self.target_x_position), text='Target X Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.target_z_position), text='Target Y Position')
                layout.prop(data=self.node, property=self.get_layout_prop(self.target_y_position), text='Target Z Position')
            case _:
                layout.label(text='This camera mode does not make use of the default properties.')

    def update_camera_mode(self, cammode: str):
        SASTLogger.log(f'Updating Camera Mode: {cammode}')
        match (cammode):
            case 'Klamath':
                self.set_camera_mode(5)
            case 'Fix':
                self.set_camera_mode(4)
            case 'Ashland':
                self.set_camera_mode(3)
            case 'Point':
                self.set_camera_mode(2)
            case 'Collision' | 'Colli_LR':
                self.set_camera_mode(1)
            case _:
                self.set_camera_mode(0)

    def set_camera_mode(self, value: int):
        self.node[self.camera_mode] = value

    def set_collision_shape(self, value: int):
        self.node[self.collision_shape] = value

    def set_collision_x_angle(self, value: float):
        self.node[self.collision_x_angle] = value

    def set_collision_y_angle(self, value: float):
        self.node[self.collision_y_angle] = value

    def set_collision_z_angle(self, value: float):
        self.node[self.collision_z_angle] = value

    def set_collision_x_scale(self, value: float):
        self.node[self.collision_x_scale] = value

    def set_collision_y_scale(self, value: float):
        self.node[self.collision_y_scale] = value

    def set_collision_z_scale(self, value: float):
        self.node[self.collision_z_scale] = value

    def set_camera_x_angle(self, value: float):
        self.node[self.camera_x_angle] = value

    def set_camera_y_angle(self, value: float):
        self.node[self.camera_y_angle] = value

    def set_camera_z_angle(self, value: float):
        self.node[self.camera_z_angle] = value

    def set_camera_x_position(self, value: float):
        self.node[self.camera_x_position] = value

    def set_camera_y_position(self, value: float):
        self.node[self.camera_y_position] = value

    def set_camera_z_position(self, value: float):
        self.node[self.camera_z_position] = value
        
    def set_target_x_position(self, value: float):
        self.node[self.target_x_position] = value

    def set_target_y_position(self, value: float):
        self.node[self.target_y_position] = value

    def set_target_z_position(self, value: float):
        self.node[self.target_z_position] = value

    def get_collision_shape(self):
        return self.node[self.collision_shape]

    def get_collision_x_angle(self) -> float:
        return self.node[self.collision_x_angle]
    
    def get_collision_y_angle(self) -> float:
        return self.node[self.collision_y_angle]
    
    def get_collision_z_angle(self) -> float:
        return self.node[self.collision_z_angle]
    
    def get_collision_x_scale(self) -> float:
        return self.node[self.collision_x_scale]
    
    def get_collision_y_scale(self) -> float:
        return self.node[self.collision_y_scale]
    
    def get_collision_z_scale(self) -> float:
        return self.node[self.collision_z_scale]
    
    def get_camera_x_angle(self) -> float:
        return self.node[self.camera_x_angle]
    
    def get_camera_y_angle(self) -> float:
        return self.node[self.camera_y_angle]
    
    def get_camera_z_angle(self) -> float:
        return self.node[self.camera_z_angle]
    
    def get_camera_x_position(self) -> float:
        return self.node[self.camera_x_position]
    
    def get_camera_y_position(self) -> float:
        return self.node[self.camera_y_position]
    
    def get_camera_z_position(self) -> float:
        return self.node[self.camera_z_position]
    
    def get_target_x_position(self) -> float:
        return self.node[self.target_x_position]
    
    def get_target_y_position(self) -> float:
        return self.node[self.target_y_position]
    
    def get_target_z_position(self) -> float:
        return self.node[self.target_z_position]