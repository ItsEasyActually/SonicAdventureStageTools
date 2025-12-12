from ..logger.sast_logger import SASTLogger
import bpy
import os
from .pynet_install_operator import PyNetInstallOperator

_LOADED = False

to_register = [
    PyNetInstallOperator
]
    
class PyNetManager:
    '''Manager static class for things related to PythonNET.'''

    @staticmethod
    def is_installed() -> bool:
        '''Checks if PythonNET is installed.'''
        try:
            import pythonnet
            return True
        except:
            return False
        
    @staticmethod
    def draw_ui(layout: bpy.types.UILayout, context: bpy.types.Context):
        layout.operator(operator=PyNetInstallOperator.bl_idname, text='Install PythonNET', icon='FILE_SCRIPT')

    @staticmethod
    def load_dll():
        '''Loads the SAST DLL Library using PythonNET.'''
        global _LOADED
        if _LOADED:
            print('pythonnet is loaded!')
            SASTLogger.log('PythonNET is Loaded!')
            return
        
        if (PyNetManager.is_installed() == False):
            print('pythonnet is not installed')
            SASTLogger.log('PythonNET is not installed!')
            return
        
        from .. import get_directory
        path: str = os.path.join(get_directory(), 'dll')
        runtime_path: str = os.path.join(path, 'SAST.Lib.runtimeconfig.json')
        dll_path: str = os.path.join(path, 'SAST.Lib.dll')

        print(f'Loaded DLL Path {dll_path}')
        SASTLogger.log(f'Loaded DLL Path {dll_path}')
        
        import pythonnet
        pythonnet.load("coreclr", runtime_config=runtime_path)

        import clr
        clr.AddReference(dll_path)

        _LOADED = True

        print('SAST Library Loaded!')
        SASTLogger.log('SAST Library is Loaded!')

    @staticmethod
    def unload_dll():
        '''Unloads the SAST DLL.'''
        SASTLogger.log('Unloading PtyhonNET')

        global _LOADED
        if not _LOADED:
            return
        
        import pythonnet
        pythonnet.unload()

        _LOADED = False