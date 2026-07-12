import bpy
from bpy.props import (
    EnumProperty,
    IntProperty,
    StringProperty,
    CollectionProperty,
    BoolProperty
)
from ...game.info import GameInfoManager
from ...game.info.stageinfo import StageInfo
from .sast_set_definition_properties import SASTSETDefinitionProperties

class SASTSceneProperties(bpy.types.PropertyGroup):
    '''Sonic Adventure Stage Tools Scene Properties'''

    mode: EnumProperty(
        name='Editor Mode',
        description='Defines whether the addon is operating in Manual or Automatic Mode.',
        default='AUTO',
        items=[
            ('MANUAL', 'Manual Mode','User has complete control on import and export options.','FILE',0),
            ('AUTO', 'Automatic Mode','Enables options for automatically loading files associated with the automatic options.','AUTO',1)
        ]
    )

    def update_game_id(self, context: bpy.types.Context):
        '''Runs when the Game ID selection is updated.'''
        pass

    game_id: EnumProperty(
        name='Game ID',
        description='Select the Game which you are looking to import/export stage data for.',
        items=[
            ('SADXPC', 'Sonic Adventure DX (PC)', 'Sonic Adventure DX PC 2004, the primary version that is modded.'),
            ('SA2BPC', 'Sonic Adventure 2 (PC)', 'Sonic Adventure 2 (Battle) on PC, the primary version that is modded.')
        ],
        default='SADXPC'
    )

    load_directory: StringProperty(
        name='Load Directory',
        description='The directory where files are loaded from in Automatic Mode.',
        subtype='DIR_PATH'
    )

    save_directory: StringProperty(
        name='Save Directory',
        description='The directory where files will be saved to when using Automatic Mode. If not supplied, the Load Directory will be used.',
        subtype='DIR_PATH'
    )

    def populate_stage_id(self, context: bpy.types.Context) -> list:
        '''Populates the Stage ID selection list.'''
        return GameInfoManager.get_stage_list(self.game_id)

    def update_stage_id(self, context: bpy.types.Context):
        '''Runs when the Stage ID selection is changed.'''
        pass

    stage_id: EnumProperty(
        name='Stage ID',
        description='Select the Stage you want to edit in the current scene.',
        items=populate_stage_id,
        update=update_stage_id,
        default=0
    )

    def populate_act_id(self, context: bpy.types.Context) -> list:
        '''Populates the Sub ID selection list.'''
        return GameInfoManager.get_act_list(self.game_id, self.stage_id)

    def update_act_id(self, context: bpy.types.Context):
        '''Runs when the Sub ID selection is changed.'''
        pass

    act_id: EnumProperty(
        name='Act ID',
        description='Select the Act you want to edit in the current scene.',
        items=populate_act_id,
        update=update_act_id,
        default=0
    )

    objlist: CollectionProperty(
        name='Object List',
        description='The SET Object list for this scene.',
        type=SASTSETDefinitionProperties
    )

    active_object: IntProperty(
        name='Active Set Item',
        description='The selected Set Item in the Set Object List',
        default=-1
    )

    @classmethod
    def register(cls):
        bpy.types.Scene.sast_properties = bpy.props.PointerProperty(type=cls)

    def draw_auto_ui(self, layout: bpy.types.UILayout, context: bpy.types.Context):
        '''Draws the Automatic Mode UI Items'''
        layout.prop(data=self, property='load_directory')
        layout.prop(data=self, property='save_directory')
        row1: bpy.types.UILayout = layout.row()
        row2: bpy.types.UILayout = layout.row()
        row1.enabled = (len(self.load_directory) > 0)
        row2.enabled = (len(self.load_directory) > 0)
        row1.prop(data=self, property='stage_id')
        if (self.game_id == 'SADXPC'):
            row2.prop(data=self, property='act_id')

    def draw_ui(self, layout: bpy.types.UILayout, context: bpy.types.Context):
        '''Draws the corresponding UI element for the selected object.'''
        layout.prop(data=self, property='game_id')
        grid: bpy.types.UILayout = layout.grid_flow(columns=2, even_columns=True, align=True)
        grid.prop_enum(data=self, property='mode', value='MANUAL')
        grid.prop_enum(data=self, property='mode', value='AUTO')
        if (self.mode == 'AUTO'):
            self.draw_auto_ui(layout, context)

    #region Directory Checkers
    def is_directory_set(self) -> bool:
        return len(self.load_directory) > 0

    #endregion

    #region Object List Functions
    def get_objlist_size(self) -> int:
        return len(self.objlist)

    def get_active_object(self) -> SASTSETDefinitionProperties | None:
        '''Returns the current active object from the Object List.'''
        if (self.active_object > -1):
            return self.objlist[self.active_object]
        else:
            return None

    def add_object(self):
        '''Adds a new object to the Object List.'''
        item: SASTSETDefinitionProperties = self.objlist.add()
        item.internal_name = 'OBJECT'
        self.active_object = len(self.objlist) - 1

    def remove_object(self):
        '''Removes the currently selected object from the Object List.'''
        if (self.active_object > -1):
            index: int = self.active_object
            self.active_object = self.active_object - 1
            self.objlist.remove(index)

    def clear_objectlist(self):
        self.active_object = -1
        self.objlist.clear()

    def move_object(self, direction: str):
        '''Moves the object in a specified direction. Only UP and DOWN are valid inputs for the direction.'''
        current_index: int = self.active_object
        next_index = None
        match (direction):
            case 'UP':
                next_index: int = current_index - 1
                if (next_index <= -1):
                    next_index = None
            case 'DOWN':
                next_index: int = current_index + 1
                if (next_index > len(self.objlist)-1):
                    next_index = None

        if (next_index is not None):
            self.objlist.move(current_index, next_index)
            if (self.active_object == current_index):
                self.active_object = next_index

    def move_object_max(self, direction: str):
        '''Moves the object to the first or last position depending on the direction. Only UP and DOWN are valid inputs for the direction.'''
        current_index: int = self.active_object
        match (direction):
            case 'UP':
                self.objlist.move(current_index, 0)
                if (self.active_object == current_index):
                    self.active_object = 0
            case 'DOWN':
                bottom: int = len(self.objlist) - 1
                self.objlist.move(current_index, bottom)
                if (self.active_object == current_index):
                    self.active_object = bottom

    #endregion

    @staticmethod
    def get_properties():
        '''Returns the Sonic Adventure Stage Tools Properties for the current Scene.'''
        return bpy.context.scene.sast_properties