import bpy
from bpy.props import (
    EnumProperty,
    StringProperty
)

from ..gameinfo.stageinfo import StageInfo

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
        return StageInfo.get_stage_list(self.game_id)

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
        return StageInfo.get_act_list(self.game_id, self.stage_id)

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

    @staticmethod
    def get_properties():
        '''Returns the Sonic Adventure Stage Tools Properties for the current Scene.'''
        return bpy.context.scene.sast_properties