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
        self.node[self.rot_x] = value

    def set_rot_y(self, value: int):
        self.node[self.rot_y] = value

    def set_rot_z(self, value: int):
        self.node[self.rot_z] = value

    def set_scl_x(self, value: float):
        self.node[self.scl_x] = value

    def set_scl_y(self, value: float):
        self.node[self.scl_y] = value

    def set_scl_z(self, value: float):
        self.node[self.scl_z] = value

    def get_rot_x(self) -> int:
        return self.node[self.rot_x]

    def get_rot_y(self) -> int:
        return self.node[self.rot_y]

    def get_rot_z(self) -> int:
        return self.node[self.rot_z]

    def get_scl_x(self) -> float:
        return self.node[self.scl_x]

    def get_scl_y(self) -> float:
        return self.node[self.scl_y]

    def get_scl_z(self) -> float:
        return self.node[self.scl_z]

    def draw_rotation_properties(self, layout: bpy.types.UILayout, rotation_order: str):
        if (rotation_order.__contains__('X') == False):
            layout.prop(data=self.node, property=self.get_layout_prop(self.rot_x), text='X Angle Property')
        if (rotation_order.__contains__('Y') == False):
            layout.prop(data=self.node, property=self.get_layout_prop(self.rot_y), text='Y Angle Property')
        if (rotation_order.__contains__('Z') == False):
            layout.prop(data=self.node, property=self.get_layout_prop(self.rot_z), text='Z Angle Property')

    def draw_ui(self, layout: bpy.types.UILayout, setitem: SASTSETDefinitionProperties):
        raw_props_header: bpy.types.UILayout
        raw_props_layout: bpy.types.UILayout
        raw_props_header, raw_props_layout = layout.panel(idname='pt_rawitemprops', default_closed=True)
        raw_props_header.label(text='Set Item Properties', icon='OPTIONS')
        if (raw_props_layout != None):
            self.draw_rotation_properties(raw_props_layout, setitem.rotation_order)
            raw_props_layout.prop(data=self.node, property=self.get_layout_prop(self.scl_x), text='X Scale Property')
            raw_props_layout.prop(data=self.node, property=self.get_layout_prop(self.scl_y), text='Y Scale Property')
            raw_props_layout.prop(data=self.node, property=self.get_layout_prop(self.scl_z), text='Z Scale Property')