from ..utilities.logger.sast_logger import SASTLogger
import bpy
import pip

class PyNetInstallOperator(bpy.types.Operator):
    '''Manages installing PythonNET.'''
    bl_idname='pynet.install'
    bl_label='Install PythonNET'
    bl_description='Installs the PythonNET Dependency.'

    @classmethod
    def poll(cls, context: bpy.types.Context):
        from . import PyNetManager
        is_installed: bool = PyNetManager.is_installed()
        if (is_installed):
            return False
        else:
            return True
        
    def execute(self, context: bpy.types.Context):
        if (hasattr(pip, 'main')):
            SASTLogger.log('Attempting to install PythonNET.')
            pip.main(['install', 'pythonnet'])
        else:
            SASTLogger.log('Attempting to install PythonNET.')
            pip._internal.main(['install','pythonnet'])
            
        return {'FINISHED'}
    