from nt import link
import os
import bpy
from bpy.props import (
    StringProperty,
    EnumProperty
)
from ...utilities.logger.sast_logger import SASTLogger
from ...scene.properties.sast_scene_properties import SASTSceneProperties
from .sast_import_base import SASTImportBase
from .sast_export_base import SASTExportBase
from ...utilities.io.sast_objlist_processor import SASTObjListProcessor

#region Object List IO
class SASTObjListImport(SASTImportBase):
    '''Imports an Object List for the scene.'''
    bl_idname = 'sastobjlist.import'
    bl_label = 'Import Object List'
    
    filter_glob: StringProperty(
        default='*.ini;*.json;'
    )

    def execute(self, context: bpy.types.Context):
        filename, ext = os.path.splitext(self.filepath)
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        SASTLogger.log(f'Reading file: {self.filepath}')
        match (ext):
            case '.ini' | '.INI':
                SASTObjListProcessor.read_ini_file(scene_props.objlist, self.filepath)
            case '.json' | '.JSON':
                SASTObjListProcessor.read_json_file(scene_props.objlist, self.filepath)
        
        return {'FINISHED'}

class SASTObjListLoad(bpy.types.Operator):
    '''Loads the Object List for the selected level from the addon.'''
    bl_idname='sastobjlist.load'
    bl_label='Load Object List'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        return scene_props.is_directory_set()

    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()

        file: str = SASTObjListProcessor.get_list_file(scene_props.stage_id, scene_props.act_id)
        SASTObjListProcessor.read_json_file(scene_props.objlist, file)

        return {'FINISHED'}

class SASTObjListExport(bpy.types.Operator):
    '''Exports an Object List file from the scene.'''
    bl_idname='sastobjlist.export'
    bl_label='Export Object List'

    filepath: StringProperty(
        name='File Path',
        description='Filepath to the exported file.',
        maxlen=1024,
        subtype='FILE_PATH'
    )

    filter_glob: StringProperty(
        default='*.ini;*.json;',
        options={'HIDDEN'}
    )

    filetype: EnumProperty(
        name='Object List Type',
        description='Type of Object List file to export from Blender.',
        items=[
            ('INI', 'INI Object List',  'Object List for use with the SA Tools and changing an Object List in the game.'),
            ('JSON','JSON Object List', 'Object List for use with this addon.')
        ],
        default='INI'
    )

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        return scene_props.get_objlist_size() > 0

    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        match (self.filetype):
            case 'INI':
                pass
            case 'JSON':
                SASTObjListProcessor.write_json_file(scene_props.objlist, self.filepath)
        return {'FINISHED'}

#endregion

#region Object List Manual Operators
class SASTObjListAddItem(bpy.types.Operator):
    '''Add an item to the Scene Object List'''
    bl_description='Add a new SET Object Item to the Object List'
    bl_idname='sastoblist.additem'
    bl_label='Add SET Item'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        return SASTSceneProperties.get_properties() is not None

    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        scene_props.add_object()

        return {'FINISHED'}

class SASTObjListDeleteItem(bpy.types.Operator):
    '''Delete an item from the Scene Object List'''
    bl_description='Deletes selected SET Object Items from the Object List.'
    bl_idname='sastobjlist.deleteitem'
    bl_label='Delete SET Item'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            if (scene_props.active_object > -1):
                return True

        return False
    
    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        scene_props.remove_object()

        return {'FINISHED'}

class SASTObjListClear(bpy.types.Operator):
    '''Clears the Object List'''
    bl_description='Clears the scene Object List.'
    bl_idname='sastobjlist.clearlist'
    bl_label='Clear SET Item List'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            if (scene_props.active_object > -1):
                return True

        return False
    
    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        scene_props.clear_objectlist()

        return {'FINISHED'}

class SASTObjListMoveItemTop(bpy.types.Operator):
    '''Moves an item in the Scene Object List to the top of the list.'''
    bl_description='Moves the currently selected to the top of the list.'
    bl_idname='sastobjlist.moveitemtop'
    bl_label='Move SET Item to Top'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            if (scene_props.active_object > -1):
                return True

        return False

    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        scene_props.move_object_max('UP')

        return {'FINISHED'}

class SASTObjListMoveItemUp(bpy.types.Operator):
    '''Moves an item in the Scene Object List up from its current index.'''
    bl_description='Moves the currently selected item up in the Object List.'
    bl_idname='sastobjlist.moveitemup'
    bl_label='Move SET Item Up'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            if (scene_props.active_object > -1):
                return True

        return False

    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        scene_props.move_object('UP')

        return {'FINISHED'}

class SASTObjListMoveItemDown(bpy.types.Operator):
    '''Moves an item in the Scene Object List down from its current index.'''
    bl_description='Moves the currently selected item down in the Object List.'
    bl_idname='sastobjlist.moveitemdown'
    bl_label='Move SET Item Down'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            if (scene_props.active_object > -1):
                return True

        return False

    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        scene_props.move_object('DOWN')
        
        return {'FINISHED'}

class SASTObjListMoveItemBottom(bpy.types.Operator):
    '''Moves an item in the Scene Object List to the bottom of the list.'''
    bl_description='Moves the currently selected to the top of the list.'
    bl_idname='sastobjlist.moveitembottom'
    bl_label='Move SET Item to Bottom'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            if (scene_props.active_object > -1):
                return True

        return False

    def execute(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        scene_props.move_object_max('DOWN')

        return {'FINISHED'}

#endregion

#region Object List Asset Linking
class SASTObjListLinkAssets(bpy.types.Operator):
    '''Links all referenced asset files from the object list.'''
    bl_idname='sastobjlist.linkassets'
    bl_description='Loads all Asset Files referenced in the loaded Object List.'
    bl_label='Load Object Assets'

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        return scene_props.get_objlist_size() > 0

    def execute(self, context: bpy.types.Context):
        from ...utilities.set.set_asset_manager import SetAssetManager
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        SetAssetManager.load_object_files(scene_props.objlist)

        # Because of weird Blender shenanigans, we have to make sure to delete this collection.
        for collection in bpy.context.scene.collection.children:
            if (collection.name.__contains__('Linked Data')):
                bpy.data.collections.remove(collection, do_unlink=True)
        
        return {'FINISHED'}

#endregion