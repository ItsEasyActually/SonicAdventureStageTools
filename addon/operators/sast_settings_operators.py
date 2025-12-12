import bpy
from bpy.props import (
    StringProperty
)
from ..logger.sast_logger import SASTLogger

class SASTDebugSave(bpy.types.Operator):
    '''Save Operator for the Logger information.'''
    bl_idname='sastdebug.savelog'
    bl_label='Save Debug Logger Information'

    filepath: StringProperty(
        name='File Path',
        description='Filepath for the saved log file.',
        maxlen=1024,
        subtype='FILE_PATH'
    )

    filter_glob: StringProperty(
        default='*.txt',
        options={'HIDDEN'}
    )

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context: bpy.types.Context):
        try:
            SASTLogger.log('Exporting Log')
            SASTLogger.save_log(self.filepath)
        except Exception as error:
            raise error

        return {'FINISHED'}

class SASTClearLogger(bpy.types.Operator):
    '''Operator for clearing the Logger.'''
    bl_idname='sastdebug.clearlogger'
    bl_label='Clear Debug Logger Info'

    def execute(self, context: bpy.types.Context):
        SASTLogger.clear_logger()
        return {'FINISHED'}