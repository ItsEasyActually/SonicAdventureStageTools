import bpy
from bpy.props import (
    EnumProperty,
    IntProperty,
    BoolProperty
)

from ...scene.properties.sast_scene_properties import SASTSceneProperties
from ...scene.properties.sast_set_definition_properties import SASTSETDefinitionProperties
from ..geonode.setitemnode import SetItemNode

class SASTSETObjectProperties(bpy.types.PropertyGroup):
    '''Set Object Properties for SAST.'''

    override_id: BoolProperty(
        name='Override Object ID',
        description='When checked, the fallback ID will be used in place of the selected object ID.',
        default=False
    )

    fallback_objid: IntProperty(
        name='Fallback Object ID',
        description='Actual value of the object ID, used when the Override Object ID toggle is enabled.',
        default=0
    )

    def populate_objectid(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        items = []
        if (scene_props.get_objlist_size() > 0):
            index: int = 0
            for item in scene_props.objlist:
                name: str = item.internal_name
                if (len(item.name) > 0):
                    name = item.name
                items.append((str(index), name, '', index))
                index += 1
            
        return items

    def update_objectid(self, context: bpy.types.Context):
        obj: bpy.types.Object = bpy.context.active_object
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        item: SASTSETDefinitionProperties = scene_props.objlist[int(self.objectid)]
        xr: float = 0 
        yr: float = 0 
        zr: float = 0
        if (obj.lock_rotation[0] == False):
            xr = obj.rotation_euler[0]
        if (obj.lock_rotation[1] == False):
            yr = obj.rotation_euler[1]
        if (obj.lock_rotation[2] == False):
            zr = obj.rotation_euler[2]
        obj.lock_rotation[0] = False
        obj.lock_rotation[1] = False
        obj.lock_rotation[2] = False

        xa: int = 0
        ya: int = 0 
        za: int = 0
        xs: float = 0 
        ys: float = 0 
        zs: float = 0
        if (len(obj.modifiers) > 0):
            setitem: SetItemNode = SetItemNode(obj)
            xa = setitem.get_rot_x()
            ya = setitem.get_rot_y()
            za = setitem.get_rot_z()
            xs = setitem.get_scl_x()
            ys = setitem.get_scl_y()
            zs = setitem.get_scl_z()

        SetItemNode.create(obj, item)
        SetItemNode.handle_set_item_rotation(obj, item.rotation_order)
        if (obj.lock_rotation[0] == False):
            obj.rotation_euler = xr
        if (obj.lock_rotation[1] == False):
            obj.rotation_euler = yr
        if (obj.lock_rotation[2] == False):
            obj.rotation_euler = zr
        setitem = SetItemNode(obj)
        setitem.set_rot_x(xa)
        setitem.set_rot_y(ya)
        setitem.set_rot_z(za)
        setitem.set_scl_x(xs)
        setitem.set_scl_y(ys)
        setitem.set_scl_z(zs)
        

    objectid: EnumProperty(
        name='Object ID',
        description='ID of the object within the Scene Object List.',
        default=0,
        items=populate_objectid,
        update=update_objectid
    )

    def populate_objectflags(self, context: bpy.types.Context):
        flaglist = []
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        match (scene_props.game_id):
            case ('SADXPC'):
                flaglist.append(('0', 'High Draw Distance',   'Draws the object at the highest distance from the player.', 0))
                flaglist.append(('1', 'Medium Draw Distance', 'Draws the object at the medium distance from the player.',  1))
                flaglist.append(('2', 'Low Draw Distance',    'Draws the object at the lowest distance from the player.',  2))
            case ('SA2BPC'):
                flaglist.append(('0', 'Primary SET File', 'The _s set file, also known as Substansive.', 0))
                flaglist.append(('1', 'Flag 1',           'If this is set, it is an unknown flag.',      1))
                flaglist.append(('2', 'Flag 2',           'If this is set, it is an unknown flag.',      2))
        
        return flaglist

    objectflags: EnumProperty(
        name='Object Flags',
        description='Object Flags stored in the SET File. Read the description for each item for more information.',
        default=0,
        items=populate_objectflags
    )

    dependent_set: BoolProperty(
        name='Dependent SET File',
        description='Set the file the item belongs to. In SA1/DX, this toggles the Player Dependent set flag, but it has effect in-game. In SA2/B, this will output an object to the unsubstansive layout (_u).',
        default=False
    )

    def draw_ui(self, layout: bpy.types.UILayout):
        layout.prop(data=self, property='objectid')
        layout.prop(data=self, property='override_id')
        row: bpy.types.UILayout = layout.row()
        row.enabled = self.override_id
        row.prop(data=self, property='fallback_objid')
        layout.prop(data=self, property='objectflags')
        layout.prop(data=self, property='dependent_set')

    @classmethod
    def register(cls):
        bpy.types.Object.sast_set_properties = bpy.props.PointerProperty(type=cls)

    @staticmethod
    def get_properties(obj: bpy.types.Object):
        '''Returns SAST SET Properties from the supplied object. If type is not Mesh or Object is not a SET Object, None will be returned.'''
        from .sast_object_properties import SASTObjectProperties
        props = SASTObjectProperties.get_properties(obj)
        if (props != None) and (props.objtype == 'SET'):
            return obj.sast_set_properties
            
        return None