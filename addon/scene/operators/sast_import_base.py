import bpy
import os
from bpy.props import (
    StringProperty,
    CollectionProperty
)

class SASTImportBase(bpy.types.Operator):
    filepath: StringProperty(
        name='File Path',
        description='Filepath to the file to import.',
        maxlen=1024,
        subtype='FILE_PATH'
    )

    files: CollectionProperty(
        name='File Paths',
        type=bpy.types.OperatorFileListElement
    )

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.mode == 'OBJECT'

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
    def draw(self, context: bpy.types.Context):
        layout: bpy.types.UILayout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
