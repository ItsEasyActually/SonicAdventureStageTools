import bpy
from bpy.props import (
    EnumProperty,
    IntProperty,
    BoolProperty
)

from .sast_set_object_properties import SASTSETObjectProperties
from ...scene.properties.sast_scene_properties import SASTSceneProperties
from ...scene.properties.sast_set_definition_properties import SASTSETDefinitionProperties

class SASTMissionObjectProperties(SASTSETObjectProperties):
    '''SADX Mission Mode Object Properties for SAST.'''

    mi_missionid: EnumProperty(
        name='Mission ID',
        description='The Mission that these object\'s belong to.',
        items=(
            { 'Mission1', 'Mission 1', '' },
            { 'Mission2', 'Mission 2', '' },
            { 'Mission3', 'Mission 3', '' },
            { 'Mission4', 'Mission 4', '' },
            { 'Mission5', 'Mission 5', '' },
            { 'Mission6', 'Mission 6', '' },
            { 'Mission7', 'Mission 7', '' },
            { 'Mission8', 'Mission 8', '' },
            { 'Mission9', 'Mission 9', '' },
            { 'Mission10', 'Mission 10', '' },
            { 'Mission11', 'Mission 11', '' },
            { 'Mission12', 'Mission 12', '' },
            { 'Mission13', 'Mission 13', '' },
            { 'Mission14', 'Mission 14', '' },
            { 'Mission15', 'Mission 15', '' },
            { 'Mission16', 'Mission 16', '' },
            { 'Mission17', 'Mission 17', '' },
            { 'Mission18', 'Mission 18', '' },
            { 'Mission19', 'Mission 19', '' },
            { 'Mission20', 'Mission 20', '' },
            { 'Mission21', 'Mission 21', '' },
            { 'Mission22', 'Mission 22', '' },
            { 'Mission23', 'Mission 23', '' },
            { 'Mission24', 'Mission 24', '' },
            { 'Mission25', 'Mission 25', '' },
            { 'Mission26', 'Mission 26', '' },
            { 'Mission27', 'Mission 27', '' },
            { 'Mission28', 'Mission 28', '' },
            { 'Mission29', 'Mission 29', '' },
            { 'Mission30', 'Mission 30', '' },
            { 'Mission31', 'Mission 31', '' },
            { 'Mission32', 'Mission 32', '' },
            { 'Mission33', 'Mission 33', '' },
            { 'Mission34', 'Mission 34', '' },
            { 'Mission35', 'Mission 35', '' },
            { 'Mission36', 'Mission 36', '' },
            { 'Mission37', 'Mission 37', '' },
            { 'Mission38', 'Mission 38', '' },
            { 'Mission39', 'Mission 39', '' },
            { 'Mission40', 'Mission 40', '' },
            { 'Mission41', 'Mission 41', '' },
            { 'Mission42', 'Mission 42', '' },
            { 'Mission43', 'Mission 43', '' },
            { 'Mission44', 'Mission 44', '' },
            { 'Mission45', 'Mission 45', '' },
            { 'Mission46', 'Mission 46', '' },
            { 'Mission47', 'Mission 47', '' },
            { 'Mission48', 'Mission 48', '' },
            { 'Mission49', 'Mission 49', '' },
            { 'Mission50', 'Mission 50', '' },
            { 'Mission51', 'Mission 51', '' },
            { 'Mission52', 'Mission 52', '' },
            { 'Mission53', 'Mission 53', '' },
            { 'Mission54', 'Mission 54', '' },
            { 'Mission55', 'Mission 55', '' },
            { 'Mission56', 'Mission 56', '' },
            { 'Mission57', 'Mission 57', '' },
            { 'Mission58', 'Mission 58', '' },
            { 'Mission59', 'Mission 59', '' },
            { 'Mission60', 'Mission 60', '' },
        ),
        default='Mission1'
    )

    mi_dispflag: EnumProperty(
        name='Display Flag',
        description='Sets the visibility of the object for the Mission.',
        items=(
            { 'BeforeMission',  'Mission Inactive', 'Displays when a mission has not been activated yet.' },
            { 'DuringMission',  'Mission Active',   'Displays when a mission is active with no other specifications.' },
            { 'DuringTimer',    'Mission Timer',    'Displays when a Mission Timer is actively running.' }
        ),
        default='DuringMission'
    )

    mi_objlist: EnumProperty(
        name='Source Object List',
        description='Object List which the object is pulled from.',
        items=(
            { 'LevelObjectList',    'Stage Object List',    'Sources the object from the level\'s Object List.' },
            { 'MissionObjectList',  'Mission Object List',  'Source the object from the Mission Mode Object List.' }
        ),
        default='MissionObjectList'
    )

    mi_timer: IntProperty(
        name='Timer',
        description='This property is only known by its name, seemingly goes unused.',
        default=0,
        max=255,
        min=0
    )

    def populate_objectid(self, context: bpy.types.Context):
        pass

    def update_objectid(self, context: bpy.types.Context):
        pass

    def draw_ui(self, layout: bpy.types.UILayout):
        pass

    @classmethod
    def register(cls):
        bpy.types.Object.sast_mi_properties = bpy.props.PointerProperty(type=cls)

    @staticmethod
    def get_properties(obj: bpy.types.Object):
        '''Returns SAST Mission Item Properties from the supplied object. If type is not Mesh or Object is not a SET Object, None will be returned.'''
        from .sast_object_properties import SASTObjectProperties
        props = SASTObjectProperties.get_properties(obj)
        if (props != None) and (props.objtype == 'SA1_MISSION'):
            return obj.sast_mi_properties
            
        return None