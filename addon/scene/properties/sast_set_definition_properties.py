import bpy
from bpy.props import (
    StringProperty,
    IntProperty,
    FloatProperty,
    EnumProperty,
    BoolProperty
)

class SASTSETDefinitionProperties(bpy.types.PropertyGroup):
    '''SET Object Definition Property Group'''

    #region Object List Information
    internal_name: StringProperty(
        name='Internal Name',
        description='Internal Name of the item from the game. This is the only name exported for INI Object List files.'
    )

    init_mode: EnumProperty(
        name='Initialization Mode',
        description='The creation flags used for creating the Task for the object on its initialization.',
        items=[
            ('TaskWork',    'Task Worker',      'Initializations the Task Worker of the Task.',     2),
            ('MotionWork',  'Motion Worker',    'Initializations the Motion Worker of the Task.',   1),
            ('ForceWork',   'Force Worker',     'Initializations the Force Worker of the Task.',    4),
            ('AnyWork',     'Any Worker',       'Initializations the Any Worker of the Task.',      8)
        ],
        default={'TaskWork'},
        options={'ENUM_FLAG'}
    )

    task_level: EnumProperty(
        name='Task Level',
        description='The level of Task Worker creation on object initiatialization.',
        items=[
            ('Level0', 'Level 0', 'Top level task, used by cntroller type items (Levels, etc).',                                                                0),
            ('Level1', 'Level 1', 'Secondary top level task, usually used things run by the top level task (Skyboxes, bosses, some non-set level objects).',    1),
            ('Level2', 'Level 2', 'Primarily used for Set Objects.',                                                                                            2),
            ('Level3', 'Level 3', 'Sound Effects and Player Actions, also used for some Set Objects.',                                                          3),
            ('Level4', 'Level 4', 'Effects like explosions and lens flares.',                                                                                   4),
            ('Level5', 'Level 5', 'Cutscenes and Level Results, sections where players have control disabled mostly.',                                          5),
            ('Level6', 'Level 6', 'Effects tied to the player and other scene entities.',                                                                       6),
            ('Level7', 'Level 7', 'Child Tasks.',                                                                                                               7)
        ],
        default='Level2'
    )

    load_attributes: EnumProperty(
        name='Load Attribute Flags',
        description='Attributes associated with how the object is loaded.',
        items=[
            ('LoadByDistance',  'Load By Distance', 'Loads when the player is within a distance set by the Load Distance variable.',    1),
            ('LoadInstant',     'Load Instantly',   'Loads instantly regardless of the distance of the object to the player.',          2),
            ('LoadOnce',        'Load Once',        'Loads instantly, but only loads once.',                                            4)
        ],
        default={'LoadByDistance'},
        options={'ENUM_FLAG'}
    )

    load_range: FloatProperty(
        name='Load Distance',
        description='Distance from the player in which the object will load. Only applicable if the Load Attribute used is Load By Distance.',
        default=0
    )

    function_address: StringProperty(
        name='Function Address',
        description='Written string of the ram address of the object function.',
        default='0'
    )

    name: StringProperty(
        name='Common Name',
        description='Common Name of the Set Item. Overrides the internal name in the UI if provided.',
        default=''
    )

    #endregion

    #region Blender Asset Information
    asset_name: StringProperty(
        name='Asset Name',
        description='Name of the Object Asset to be appended to the file.'
    )

    asset_file: StringProperty(
        name='Asset File',
        description='The file containing the Asset used for this object.'
    )

    is_relative_file: BoolProperty(
        name='Relative Filepath',
        description='Sets if the filepath is relative to the addon root folder or not.',
        default=True
    )

    #endregion

    #region Editor Panel Settings
    rotation_order: EnumProperty(
        name='Rotation Order',
        description='The rotation order from the source game. This defines how the object rotation is set within Blender.',
        items=[
            ( 'NONE',   'None',     '' ),
            ( 'X',      'X Only',   '' ),
            ( 'Y',      'Y Only',   '' ),
            ( 'Z',      'Z Only',   '' ),
            ( 'XY',     'XY',       '' ),
            ( 'XZ',     'XZ',       '' ),
            ( 'YX',     'YX',       '' ),
            ( 'YZ',     'YZ',       '' ),
            ( 'ZX',     'ZX',       '' ),
            ( 'ZY',     'XY',       '' ),
            ( 'XYZ',    'XYZ',      '' ),
            ( 'XZY',    'XZY',      '' ),
            ( 'YXZ',    'YXZ',      '' ),
            ( 'YZX',    'YZX',      '' ),
            ( 'ZXY',    'ZXY',      '' ),
            ( 'ZYX',    'ZYX',      '' )
        ],
        default='NONE'
    )

    #endregion

    def draw_ui(self, layout: bpy.types.UILayout):
        objinfo_header, objinfo_layout = layout.panel('pt_objinfo', default_closed=False)
        objinfo_header.label(text='Object Information')
        if (objinfo_layout != None):
            objinfo_layout.prop(data=self, property='internal_name')
            objinfo_layout.prop(data=self, property='function_address')
            objinfo_layout.prop(data=self, property='task_level')
            objinfo_layout.prop_menu_enum(data=self, property='init_mode')
            objinfo_layout.prop_menu_enum(data=self, property='load_attributes')
            objinfo_layout.prop(data=self, property='load_range')

        binfo_header, binfo_layout = layout.panel('pt_assetinfo', default_closed=False)
        binfo_header.label(text='Blender Asset Information')
        if (binfo_layout != None):
            binfo_layout.prop(data=self, property='name')
            binfo_layout.prop(data=self, property='asset_name')
            binfo_layout.prop(data=self, property='asset_file')
            binfo_layout.prop(data=self, property='is_relative_file')

        settings_header, settings_layout = layout.panel('pt_iteminfo', default_closed=True)
        settings_header.label(text='SET Item Property Settings')
        if (settings_layout != None):
            settings_layout.prop(data=self, property='rotation_order')
            settings_layout.separator(type='LINE')
            #settings_layout.prop(data=self, property='display_rotation_x_property')
            #settings_layout.prop(data=self, property='display_rotation_y_property')
            #settings_layout.prop(data=self, property='display_rotation_z_property')
            #settings_layout.prop(data=self, property='display_scale_x_property')
            #settings_layout.prop(data=self, property='display_scale_y_property')
            #settings_layout.prop(data=self, property='display_scale_z_property')