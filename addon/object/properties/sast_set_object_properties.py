import bpy
from bpy.props import (
    EnumProperty,
    IntProperty,
    BoolProperty
)
from ...scene.properties.sast_scene_properties import SASTSceneProperties

class SASTSETObjectProperties(bpy.types.PropertyGroup):
    '''Set Object Properties for SAST.'''

    override_id: BoolProperty(
        name='Override Object ID',
        description='When checked, the fallback ID will be used in place of the selected object ID.',
        default=False
    )

    fallback_objid: IntProperty(
        name='Fallback Object ID',
        description='Actual value of the object ID, used when the Override Object ID toggle is enabled or when the Object ID is 0 while this value is higher than 0.',
        default=0
    )

    def populate_objectid(self, context: bpy.types.Context):
        return []

    def update_objectid(self, context: bpy.types.Context):
        pass

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
                flaglist.append(('NoFlags', 'High Draw Distance',   'Draws the object at the highest distance from the player.'))
                flaglist.append(('Flag1',   'Medium Draw Distance', 'Draws the object at the medium distance from the player.'))
                flaglist.append(('Flag2',   'Low Draw Distance',    'Draws the object at the lowest distance from the player.'))
            case ('SA2BPC'):
                flaglist.append(('NoFlags', 'Primary SET File',     'The _s set file, also known as Substansive.'))
                flaglist.append(('Flag4',   'Decoration SET File',  'The _u set file, also known as Unsubstansive. Objects in this file have no known difference to the primary layout.'))
        
        return flaglist

    objectflags: EnumProperty(
        name='Object Flags',
        description='Object Flags stored in the SET File. Read the description for each item for more information.',
        default=0,
        items=populate_objectflags
    )

    def draw_ui(self, layout: bpy.types.UILayout):
        pass

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