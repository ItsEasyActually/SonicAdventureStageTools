from ...utilities.logger.sast_logger import SASTLogger
import bpy
from ...utilities.geonode.geometry_node_manager import GeometryNodeManager
from .sast_geonode_base import SASTGeonodeBase
import os

class SA1CameraNode(SASTGeonodeBase):
    '''SA1 Camera Node Geometry Manager Class'''

    modifier_file: str          = os.path.join('blend', 'cam', 'SA1Camera.blend')
    modifier_name: str          = 'SA1CameraNode'

    camera_mode: str            = 'Socket_2'
    camera_level: str           = 'Socket_3'
    collision_shape: str        = 'Socket_4'

    collision_x_rotation: str   = 'Socket_6'
    collision_y_rotation: str   = 'Socket_7'
    collision_x_scale: str      = 'Socket_8'
    collision_y_scale: str      = 'Socket_9'
    collision_z_scale: str      = 'Socket_10'
    camera_x_rotation: str      = 'Socket_11'
    camera_y_rotation: str      = 'Socket_12'
    camera_x_position: str      = 'Socket_13'
    camera_y_position: str      = 'Socket_14'
    camera_z_position: str      = 'Socket_15'
    target_x_position: str      = 'Socket_16'
    target_y_position: str      = 'Socket_17'
    target_z_position: str      = 'Socket_18'
    camera_distance: str        = 'Socket_19'

    @staticmethod
    def poll(obj: bpy.types.Object) -> bool:
        return GeometryNodeManager.has_geometry_node(obj, SA1CameraNode.modifier_name)

    @staticmethod
    def make(obj: bpy.types.Object) -> bpy.types.NodesModifier:
        if (obj.type == 'MESH'):
            SASTLogger.log(f'Valid object, adding {SA1CameraNode.modifier_name} Geometry Node')
            return GeometryNodeManager.create_node(obj, SA1CameraNode.modifier_file, SA1CameraNode.modifier_name)
        else:
            SASTLogger.log('Object Data Type is not MESH. Invalid Object!')

    def reset_properties(self):
        SASTLogger.log('Resetting Geometry Node Properties')
        self.set_collision_shape(0)
        self.set_collision_x_scale(10)
        self.set_collision_y_scale(10)
        self.set_collision_z_scale(10)
        self.set_collision_x_rotation(0)
        self.set_collision_y_rotation(0)
        self.set_camera_x_position(0)
        self.set_camera_y_position(0)
        self.set_camera_z_position(0)
        self.set_camera_x_rotation(0)
        self.set_camera_y_rotation(0)
        self.set_target_x_position(0)
        self.set_target_y_position(0)
        self.set_target_z_position(0)
        self.set_camera_distance(0)

    def draw_ui(self, layout: bpy.types.UILayout, cammode: str):
        '''Draws the properties menu.'''
        layout.prop(data=self.node, property='value', text='Volume Shape')
        layout.separator(factor=1, type='LINE')
        match (cammode):
            case 'Ashland' | 'AshlandI':
                layout.prop(data=self.node.properties.inputs.Socket_13, property='value', text='Camera X Position')
                layout.prop(data=self.node.properties.inputs.Socket_15, property='value', text='Camera Y Position')
                layout.prop(data=self.node.properties.inputs.Socket_14, property='value', text='Camera Z Position')
            case 'Fixed':
                layout.prop(data=self.node.properties.inputs.Socket_13, property='value', text='Camera X Position')
                layout.prop(data=self.node.properties.inputs.Socket_15, property='value', text='Camera Y Position')
                layout.prop(data=self.node.properties.inputs.Socket_14, property='value', text='Camera Z Position')
                layout.prop(data=self.node.properties.inputs.Socket_16, property='value', text='Target X Position')
                layout.prop(data=self.node.properties.inputs.Socket_18, property='value', text='Target Y Position')
                layout.prop(data=self.node.properties.inputs.Socket_17, property='value', text='Target Z Position')
            case 'Klamath':
                layout.prop(data=self.node.properties.inputs.Socket_16, property='value', text='Target X Position')
                layout.prop(data=self.node.properties.inputs.Socket_18, property='value', text='Target Y Position')
                layout.prop(data=self.node.properties.inputs.Socket_11, property='value', text='Vertical Distance Modifier')
                layout.prop(data=self.node.properties.inputs.Socket_19, property='value', text='Distance to Player')
            case 'Line':
                layout.prop(data=self.node.properties.inputs.Socket_16, property='value', text='Target X Position')
                layout.prop(data=self.node.properties.inputs.Socket_18, property='value', text='Target Y Position')
            case 'Point':
                layout.prop(data=self.node.properties.inputs.Socket_16, property='value', text='Target X Position')
                layout.prop(data=self.node.properties.inputs.Socket_18, property='value', text='Target Y Position')
                layout.prop(data=self.node.properties.inputs.Socket_17, property='value', text='Target Z Position')
                layout.prop(data=self.node.properties.inputs.Socket_11, property='value', text='Disable Geometry Collision')
                layout.prop(data=self.node.properties.inputs.Socket_19, property='value', text='Distance to Player')
            case 'SonicP':
                layout.prop(data=self.node.properties.inputs.Socket_19, property='value', text='Deadzone (MIN)')
                layout.prop(data=self.node.properties.inputs.Socket_16, property='value', text='Deadzone (MAX)')
                layout.prop(data=self.node.properties.inputs.Socket_17, property='value', text='Distance to Player (MIN)')
                layout.prop(data=self.node.properties.inputs.Socket_18, property='value', text='Distance to Player (MAX)')
                layout.prop(data=self.node.properties.inputs.Socket_11, property='value', text='Viewpoint Angle')
                layout.prop(data=self.node.properties.inputs.Socket_12, property='value', text='Camera Steady')
            case 'Tornado':
                layout.prop(data=self.node.properties.inputs.Socket_16, property='value', text='Target X Position')
                layout.prop(data=self.node.properties.inputs.Socket_18, property='value', text='Target Y Position')
                layout.prop(data=self.node.properties.inputs.Socket_17, property='value', text='Target Z Position')
                layout.prop(data=self.node.properties.inputs.Socket_14, property='value', text='Additional Camera Height')
                layout.prop(data=self.node.properties.inputs.Socket_19, property='value', text='Modify Distance Calculation')
            case _:
                layout.label(text='This camera mode does not have custom properties.')

    def update_camera_mode(self, cammode: str):
        SASTLogger.log(f'Updating Camera Mode: {cammode}')
        match (cammode):
            case 'Klamath' | 'Line':
                # Camera Mode has XZ Target controls.
                self.set_camera_mode(43)
            case 'Point' | 'Tornado':
                # Camera Mode has Camera Target controls.
                self.set_camera_mode(42)
            case 'Fixed':
                # Camera Mode has Camera Position and Target controls.
                self.set_camera_mode(3)
            case 'Ashland' | 'AshlandI':
                # Camera Mode has Camera Position only controls.
                self.set_camera_mode(2)
            case 'Collision':
                # Camera Mode is Camera Collision
                self.set_camera_mode(1)
            case _:
                # Camera Mode has  No Controls
                self.set_camera_mode(0)

    def update_camera_level(self, camlevel: str):
        SASTLogger.log(f'Updating Camera Level: {camlevel}')
        match (camlevel):
                case 'Normal':
                    self.set_camera_level(0)
                case 'Area':
                    self.set_camera_level(1)
                case 'Compulsion':
                    self.set_camera_level(2)
                case 'Collision':
                    self.set_camera_level(3)

    def set_camera_mode(self, value: int):
        self.node.properties.inputs.Socket_2 = value

    def set_camera_level(self, value: int):
        self.node.properties.inputs.Socket_3 = value

    def set_collision_shape(self, value: int):
        self.node.properties.inputs.Socket_4 = value

    def set_collision_x_rotation(self, value: float):
        self.node.properties.inputs.Socket_6 = value

    def set_collision_y_rotation(self, value: float):
        self.node.properties.inputs.Socket_7 = value

    def set_collision_x_scale(self, value: float):
        self.node.properties.inputs.Socket_8 = value

    def set_collision_y_scale(self, value: float):
        self.node.properties.inputs.Socket_9 = value

    def set_collision_z_scale(self, value: float):
        self.node.properties.inputs.Socket_10 = value

    def set_camera_x_rotation(self, value: int):
        self.node.properties.inputs.Socket_11 = value

    def set_camera_y_rotation(self, value: int):
        self.node.properties.inputs.Socket_12 = value

    def set_camera_x_position(self, value: float):
        self.node.properties.inputs.Socket_13 = value

    def set_camera_y_position(self, value: float):
        self.node.properties.inputs.Socket_14 = value

    def set_camera_z_position(self, value: float):
        self.node.properties.inputs.Socket_15 = value

    def set_target_x_position(self, value: float):
        self.node.properties.inputs.Socket_16 = value

    def set_target_y_position(self, value: float):
        self.node.properties.inputs.Socket_17 = value

    def set_target_z_position(self, value: float):
        self.node.properties.inputs.Socket_18 = value

    def set_camera_distance(self, value: float):
        self.node.properties.inputs.Socket_19 = value

    def get_collision_shape(self) -> int:
        return self.node.properties.inputs.Socket_4

    def get_collision_x_rotation(self) -> int:
        return self.node.properties.inputs.Socket_6

    def get_collision_y_rotation(self) -> int:
        return self.node.properties.inputs.Socket_7

    def get_collision_x_scale(self) -> float:
        return self.node.properties.inputs.Socket_8

    def get_collision_y_scale(self) -> float:
        return self.node.properties.inputs.Socket_9

    def get_collision_z_scale(self) -> float:
        return self.node.properties.inputs.Socket_10

    def get_camera_x_rotation(self) -> int:
        return self.node.properties.inputs.Socket_11

    def get_camera_y_rotation(self) -> int:
        return self.node.properties.inputs.Socket_12

    def get_camera_x_position(self) -> float:
        return self.node.properties.inputs.Socket_13

    def get_camera_y_position(self) -> float:
        return self.node.properties.inputs.Socket_14

    def get_camera_z_position(self) -> float:
        return self.node.properties.inputs.Socket_15

    def get_target_x_position(self) -> float:
        return self.node.properties.inputs.Socket_16

    def get_target_y_position(self) -> float:
        return self.node.properties.inputs.Socket_17

    def get_target_z_position(self) -> float:
        return self.node.properties.inputs.Socket_18

    def get_camera_distance(self) -> float:
        return self.node.properties.inputs.Socket_19
    