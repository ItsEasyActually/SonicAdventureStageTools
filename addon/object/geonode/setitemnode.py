import bpy
from .sast_geonode_base import SASTGeonodeBase
from ...utilities.geonode.geometry_node_manager import GeometryNodeManager
from ...scene.properties.sast_set_definition_properties import SASTSETDefinitionProperties

class SetItemNode(SASTGeonodeBase):
    '''Basic class storage for SET Item Geometry Node processing.'''

    rot_x: str = 'Socket_2'
    rot_y: str = 'Socket_3'
    rot_z: str = 'Socket_4'
    scl_x: str = 'Socket_5'
    scl_y: str = 'Socket_6'
    scl_z: str = 'Socket_7'

    @staticmethod
    def poll(obj: bpy.types.Object) -> bool:
        return GeometryNodeManager.has_geometry_node(obj)

    def __init__(self, obj: bpy.types.Object) -> None:
        if (len(obj.modifiers) > 0):
            modifier: bpy.types.NodesModifier = obj.modifiers[0]
            if (modifier is not None):
                self.node = modifier

    def set_rot_x(self, value: int):
        self.node.properties.inputs.Socket_2.value = value

    def set_rot_y(self, value: int):
        self.node.properties.inputs.Socket_3.value = value

    def set_rot_z(self, value: int):
        self.node.properties.inputs.Socket_4.value = value

    def set_scl_x(self, value: float):
        self.node.properties.inputs.Socket_5.value = value

    def set_scl_y(self, value: float):
        self.node.properties.inputs.Socket_6.value = value

    def set_scl_z(self, value: float):
        self.node.properties.inputs.Socket_7.value = value

    def get_rot_x(self) -> int:
        return self.node.properties.inputs.Socket_2.value

    def get_rot_y(self) -> int:
        return self.node.properties.inputs.Socket_3.value

    def get_rot_z(self) -> int:
        return self.node.properties.inputs.Socket_4.value

    def get_scl_x(self) -> float:
        return self.node.properties.inputs.Socket_5.value

    def get_scl_y(self) -> float:
        return self.node.properties.inputs.Socket_6.value

    def get_scl_z(self) -> float:
        return self.node.properties.inputs.Socket_7.value

    def draw_rotation_properties(self, layout: bpy.types.UILayout, rotation_order: str, use_x_angle: bool, use_y_angle: bool, use_z_angle: bool, x_angle_prop_name: str, y_angle_prop_name: str, z_angle_prop_name: str):
        if ((rotation_order.__contains__('X') == False) and (use_x_angle == True)):
            x_name: str = 'X Angle Property'
            if (len(x_angle_prop_name) > 0):
                x_name = x_angle_prop_name
            layout.prop(data=self.node.properties.inputs.Socket_2, property='value', text=x_name)
        if ((rotation_order.__contains__('Y') == False) and (use_y_angle == True)):
            y_name: str = 'Y Angle Property'
            if (len(y_angle_prop_name) > 0):
                y_name = y_angle_prop_name
            layout.prop(data=self.node.properties.inputs.Socket_3, property='value', text=y_name)
        if ((rotation_order.__contains__('Z') == False) and (use_z_angle == True)):
            z_name: str = 'Z Angle Property'
            if (len(z_angle_prop_name) > 0):
                z_name = z_angle_prop_name
            layout.prop(data=self.node.properties.inputs.Socket_4, property='value', text=z_name)

    def draw_ui(self, layout: bpy.types.UILayout, setitem: SASTSETDefinitionProperties):
        if (len(setitem.item_description) > 0):
            layout.label(text='Item Information:')
            box: bpy.types.UILayout = layout.box()
            description = setitem.item_description.split('\n')
            for line in description:
                row: bpy.types.UILayout = box.row()
                row.label(text=line)
        raw_props_header: bpy.types.UILayout
        raw_props_layout: bpy.types.UILayout
        raw_props_header, raw_props_layout = layout.panel(idname='pt_rawitemprops', default_closed=True)
        raw_props_header.label(text='Set Item Properties', icon='OPTIONS')
        if (raw_props_layout != None):
            if ((setitem.use_x_angle_property == False) and (setitem.use_y_angle_property == False) and (setitem.use_z_angle_property == False) and (setitem.use_x_scale_property == False) and (setitem.use_y_scale_property == False) and (setitem.use_z_scale_property == False)):
                raw_props_layout.label(text='Object has no modifiable properties!')
            else:
                self.draw_rotation_properties(raw_props_layout, setitem.rotation_order, setitem.use_x_angle_property, setitem.use_y_angle_property, setitem.use_z_angle_property, setitem.x_angle_name, setitem.y_angle_name, setitem.z_angle_name)
                if (setitem.use_x_scale_property == True):
                    x_scl_name: str = 'X Scale Property'
                    if (len(setitem.x_scale_name) > 0):
                        x_scl_name = setitem.x_scale_name
                    raw_props_layout.prop(data=self.node.properties.inputs.Socket_5, property='value', text=x_scl_name)
                if (setitem.use_y_scale_property == True):
                    y_scl_name: str = 'Y Scale Property'
                    if (len(setitem.y_scale_name) > 0):
                        y_scl_name = setitem.y_scale_name
                    raw_props_layout.prop(data=self.node.properties.inputs.Socket_6, property='value', text=y_scl_name)
                if (setitem.use_z_scale_property == True):
                    z_scl_name: str = 'Z Scale Property'
                    if (len(setitem.z_scale_name) > 0):
                        z_scl_name = setitem.z_scale_name
                    raw_props_layout.prop(data=self.node.properties.inputs.Socket_7, property='value', text=z_scl_name)