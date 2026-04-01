import bpy
from ... import get_directory as get_addon_directory
from ... import get_name as get_addon_name
import os
from ..logger.sast_logger import SASTLogger

class SASTAssetImport:
    '''Class with static functions to help load in assets from external blend files.'''

    @staticmethod
    def compare_paths(a: str, b: str):
        absolute = bpy.path.abspath(b)
        absolute = os.path.abspath(absolute)
        return a == absolute

    @staticmethod
    def make_path(items: [str]) -> str:
        path: str = ''
        for i in items:
            path += f'{i}{os.path.sep}'

        return path

    @staticmethod
    def link_asset(relative_path: str, library_path: str, link_item_name: str):
        '''Links an asset from the supplied relative path. Paths are expected to be relative to the addon's root.'''
        SASTLogger.log(f'Linking Asset: {link_item_name}')
        path: str = os.path.join(get_addon_directory(), relative_path)
        if (os.path.exists(path) == False):
            return

        found: bool = False
        for library in bpy.data.libraries:
            if (SASTAssetImport.compare_paths(path, library.filepath)):
                SASTLogger.log(f'File is already in library: {path}')
                found = True
                break

        if not found:
            path = f'{path}{os.path.sep}{library_path}{os.path.sep}'
            SASTLogger.log(f'Linking {link_item_name} from {path}')
            bpy.ops.wm.link(filename=link_item_name, directory=path, active_collection=False)

    @staticmethod
    def append_asset(relative_path: str, library_path: str, append_item_name: str):
        '''Appends an asset from the supplied relative path. Paths are expected to be relative to the addon's root.'''
        SASTLogger.log(f'Appending Asset: {append_item_name}')
        path: str = os.path.join(get_addon_directory(), relative_path)
        if (os.path.exists(path) == False):
            return

        found: bool = False
        for library in bpy.data.libraries:
            if (SASTAssetImport.compare_paths(path, library.filepath)):
                SASTLogger.log(f'File is already in library: {path}')
                found = True
                break

        if not found:
            path = SASTAssetImport.make_path(path, library_path)
            SASTLogger.log(f'Appending {append_item_name} from {path}')
            bpy.ops.wm.append(filename=append_item_name, directory=path, instance_collections=True)
