import bpy
from bpy.props import (
    StringProperty,
    IntProperty,
    FloatProperty,
    EnumProperty
)

class SASTSETDefinitionProperties(bpy.types.PropertyGroup):
    '''SET Object Definition Property Group'''

    name: StringProperty(
        name='Common Name',
        description='Common Name of the Set Item'
    )

    internal_name: StringProperty(
        name='Internal Name',
        description='Internal Name from the game.'
    )

    init_mode: EnumProperty(
        name='Initialization Mode',
        description='The creation flags used for creating the Task for the object on its initialization.',
        items=[
            ('TaskWork',    'Task Worker',      'Initializations the Task Worker of the Task.'),
            ('MotionWork',  'Motion Worker',    'Initializations the Motion Worker of the Task.'),
            ('ForceWork',   'Force Worker',     'Initializations the Force Worker of the Task.'),
            ('AnyWork',     'Any Worker',       'Initializations the Any Worker of the Task.')
        ],
        default='TaskWork'
    )

    task_level: EnumProperty(
        name='Task Level',
        description='The level of Task Worker creation on object initiatialization.',
        items=[
            ('Level0', 'Level 0', 'Top level task, used by cntroller type items (Levels, etc).'),
            ('Level1', 'Level 1', 'Secondary top level task, usually used things run by the top level task (Skyboxes, bosses, some non-set level objects).'),
            ('Level2', 'Level 2', 'Primarily used for Set Objects.'),
            ('Level3', 'Level 3', 'Sound Effects and Player Actions, also used for some Set Objects.'),
            ('Level4', 'Level 4', 'Effects like explosions and lens flares.'),
            ('Level5', 'Level 5', 'Cutscenes and Level Results, sections where players have control disabled mostly.'),
            ('Level6', 'Level 6', 'Effects tied to the player and other scene entities.'),
            ('Level7', 'Level 7', 'Child Tasks.')
        ],
        default='Level2'
    )

    load_attributes: EnumProperty(
        name='Load Attribute Flags',
        description='Attributes associated with how the object is loaded.',
        items=[
            ('LoadByDistance',  'Load By Distance', 'Loads when the player is within a distance set by the Load Distance variable.'),
            ('LoadInstant',     'Load Instantly',   'Loads instantly regardless of the distance of the object to the player.'),
            ('LoadOnce',        'Load Once',        'Loads instantly, but only loads once.')
        ],
        default='LoadByDistance'
    )

    load_range: FloatProperty(
        name='Load Distance',
        description='Distance from the player in which the object will load. Only applicable if the Load Attribute used is Load By Distance.',
        default=360000
    )

    function_address: StringProperty(
        name='Function Address',
        description='Written string of the ram address of the object function.',
        default='0'
    )

    def draw_ui(self, layout: bpy.types.UILayout):
        layout.prop(data=self, property='internal_name')
        layout.prop(data=self, property='name')
        layout.prop(data=self, property='function_address')
        layout.prop(data=self, property='task_level')
        layout.prop_menu_enum(data=self, property='init_mode')
        layout.prop_menu_enum(data=self, property='load_attributes')
        layout.prop(data=self, property='load_range')