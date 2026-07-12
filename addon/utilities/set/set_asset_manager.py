import bpy
import os
from ..io.sast_asset_import import SASTAssetImport
from ...scene.properties.sast_set_definition_properties import SASTSETDefinitionProperties

class SetAssetManager:
    '''The Static Class Manager for handling import of SET File "Definitions"'''

    default_object: str = 'DefaultSetObject'
    default_file: str = os.path.join('blend', 'set', 'DefaultSetObject.blend')
    set_scene: str = 'Object List'

    @staticmethod
    def load_object(path: str, name: str) -> bpy.types.Object:
        SASTAssetImport.link_asset(path, 'Object', name)
        if (bpy.data.objects.__contains__(name)):
            return bpy.data.objects.get(name)
        else:
            return None

    @staticmethod
    def load_default_object():
        '''Appends the default object asset.'''
        return SetAssetManager.load_object(SetAssetManager.default_file, SetAssetManager.default_object)

    @staticmethod
    def link_object(item: SASTSETDefinitionProperties) -> bpy.types.Object | None:
        if (item.is_relative_file):
            return SetAssetManager.load_object(item.asset_file, item.asset_name)
        else:
            # Currently only relative reading is implemented.
            return None

    @staticmethod
    def load_object_files(items: bpy.types.CollectionProperty):
        '''Loads all of the objects from their respective loose blend files.'''
        scene: bpy.types.Scene = bpy.data.scenes.new(SetAssetManager.set_scene)
        default_obj = SetAssetManager.load_default_object()
        if (default_obj is not None):
            scene.collection.objects.link(default_obj)
        for item in items:
            if (len(item.asset_file) > 0):
                obj: bpy.types.Object = SetAssetManager.link_object(item)
                if (obj is not None):
                    if (scene.objects.__contains__(obj.name) == False):
                        scene.collection.objects.link(obj)

    @staticmethod
    def get_object(key: str) -> bpy.types.Object | None:
        '''Returns a copy of the object the supplied name is for. 
        \nIf the object does not exist, it will return the default object.
        \nIf neither the specified object or default object exist, it will return None.'''
        if (bpy.data.scenes.__contains__(SetAssetManager.set_scene)):
            scene: bpy.types.Scene = bpy.data.scenes.get(SetAssetManager.set_scene)
            if (scene.objects.__contains__(key)):
                return scene.objects.get(key).copy()
            elif (scene.objects.__contains__(SetAssetManager.default_object)):
                return scene.objects.get(SetAssetManager.default_object).copy()

        return None

