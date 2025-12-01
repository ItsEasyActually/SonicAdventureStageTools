import bpy
import os
from bpy.props import (
    StringProperty,
    CollectionProperty,
    EnumProperty
)
from ..geonode import GeometryNodeManager
from ..properties.sast_scene_properties import SASTSceneProperties
from ..properties.sast_object_properties import SASTObjectProperties
from ..geonode.sa1cameranode import SA1CameraNode
from ..geonode.sa2cameranode import SA2CameraNode
from ..geonode.sa2pointnode import SA2PointNode
from ..io.sast_import import SASTImportManager

class SASTSceneOperators:
    @staticmethod
    def draw_ui(layout: bpy.types.UILayout, context: bpy.types.Context, imp_op: str, exp_op: str):
        layout.operator(imp_op, text='Import Camera File', icon='IMPORT')
        layout.operator(exp_op, text='Export Camera File', icon='EXPORT')
    
    @staticmethod
    def draw_ui_manual(layout: bpy.types.UILayout, context: bpy.types.Context):
        '''Draws the Manual Operators for the Scene.'''
        SASTSceneOperators.draw_ui(layout, context, SASTImportCameraManual.bl_idname, SASTExportCameraManual.bl_idname)

    @staticmethod
    def draw_ui_auto(layout: bpy.types.UILayout, context: bpy.types.Context):
        '''Draws the Automatic Operators for the Scene.'''
        SASTSceneOperators.draw_ui(layout, context, SASTImportCameraAutomatic.bl_idname, SASTExportCameraAutomatic.bl_idname)

class SASTImportBase(bpy.types.Operator):
    '''Base Import Operations'''

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

class SASTExportBase(bpy.types.Operator):
    '''Base Export Operations'''

    filepath: StringProperty(
        name='File Path',
        description='Filepath to the exported file.',
        maxlen=1024,
        subtype='FILE_PATH'
    )

    collection_mode: EnumProperty(
        name='Object Collection Mode',
        description='Select the method for collected objects for export.',
        items=[
            ('ALL','Scene','Exports valid objects from the entire scene.'),
            ('SELECTION','Selection','Exports valid selected objects only.'),
            ('COLLECTION','Collection','Exports valid objects in the selected collection.')
        ],
        default='ALL'
    )

    def populate_object_collection(self, context: bpy.types.Context):
        items = []

        for col in context.scene.collection.children:
            item = [(col.name, col.name, '')]
            items.append(item)

        return items

    object_collection: EnumProperty(
        name='Collection to Export',
        description='Select the collection to use for exporting objects from.',
        items=populate_object_collection,
        default=0
    )

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def get_objects(self, context: bpy.types.Context, geonodename: str) -> list[bpy.types.Object]:
        objs = []
        search_collection = []

        match (self.collection_mode):
            case 'ALL':
                search_collection = context.scene.objects
            case 'SELECTION':
                search_collection = context.selected_objects
            case 'COLLECTION':
                search_collection = context.scene.collection.get(self.object_collection)

        if (len(search_collection) > 0):
            for obj in search_collection:
                if (obj.type == 'MESH'):
                    if (GeometryNodeManager.has_geometry_node(obj, geonodename)):
                        objs.append(obj)

        return objs

class SASTImportCameraManual(SASTImportBase):
    '''Manual Camera File Import'''
    bl_idname='sastimport.cameramanual'
    bl_label='Import CAM File'

    filter_glob: StringProperty(
        default='*.bin;*.prs;'
    )

    def execute(self, context: bpy.types.Context):
        try:
            SASTImportManager.import_cam_manual(self.files, os.path.dirname(self.filepath), context)
        except Exception as error:
            print('Import Failed')
            raise error

        return {'FINISHED'}

class SASTImportSETManual(bpy.types.Operator):
    '''Manual SET File Import'''
    bl_idname='sastimport.setmanual'
    bl_label='Import SET File'

    def execute(self, context: bpy.types.Context):
        return {'FINISHED'}

class SASTImportCameraAutomatic(bpy.types.Operator):
    '''Automatic Camera File Import'''
    bl_idname='sastimport.cameraauto'
    bl_label='Import CAM File Auto'

    def execute(self, context: bpy.types.Context):
        try:
            scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
            stage_id: str = scene_props.stage_id
            act_id: str = scene_props.act_id
            SASTImportManager.import_cam_auto(context, scene_props.load_directory, stage_id, act_id)
        except Exception as error:
            raise error

        return {'FINISHED'}

class SASTImportSETAutomatic(bpy.types.Operator):
    '''Automatic SET File Import'''
    bl_idname='sastimport.setauto'
    bl_label='Import SET File Auto'

    def execute(self, context: bpy.types.Context):
        return {'FINISHED'}

class SASTExportCameraManual(SASTExportBase):
    '''Manual Camera File Export'''
    bl_idname='sastexport.cameramanual'
    bl_label='Export CAM File'

    filter_glob: StringProperty(
        default='*.bin;*.prs;'
    )

    def draw(self, context: bpy.types.Context):
        layout: bpy.types.UILayout = self.layout
        layout.prop(data=self, property='collection_mode')
        if (self.collection_mode == 'COLLECTION'):
            layout.prop(data=self, property='object_collection')

    def execute(self, context: bpy.types.Context):
        try:
            from ..properties.sast_scene_properties import SASTSceneProperties
            scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
            objs = []
            match (scene_props.game_id):
                case 'SADXPC':
                    objs.extend(self.get_objects(context, SA1CameraNode.modifier_name))
                case 'SA2BPC':
                    objs.extend(self.get_objects(context, SA2CameraNode.modifier_name))
                    objs.extend(self.get_objects(context, SA2PointNode.modifier_name))

            if (len(objs) > 0):
                from ..io.sast_export import SASTExportManager
                SASTExportManager.export_camera(self.filepath, objs)
        except Exception as error:
            raise error

        return {'FINISHED'}

class SASTExportSETManual(bpy.types.Operator):
    '''Manual SET File Export'''
    bl_idname='sastexport.setmanual'
    bl_label='Export SET File'

    def execute(self, context: bpy.types.Context):
        return {'FINISHED'}
    
class SASTExportCameraAutomatic(bpy.types.Operator):
    '''Automatic Camera File Export'''
    bl_idname='sastexport.cameraauto'
    bl_label='Export CAM File Auto'

    def execute(self, context: bpy.types.Context):
        try:
            from ..properties.sast_scene_properties import SASTSceneProperties
            scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
            objs = []

            for obj in context.scene.objects:
                if (obj.type == 'MESH'):
                    props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
                    match (scene_props.game_id):
                        case 'SADXPC':
                            if (props.objtype == 'CAM'):
                                if (GeometryNodeManager.has_geometry_node(obj, SA1CameraNode.modifier_name)):
                                    objs.append(obj)
                        case 'SA2BPC':
                            if (props.objtype == 'CAM'):
                                if (GeometryNodeManager.has_geometry_node(obj, SA2CameraNode.modifier_name)):
                                    objs.append(obj)
                            elif (props.objtype == 'POINT'):
                                if (GeometryNodeManager.has_geometry_node(obj, SA2PointNode.modifier_name)):
                                    objs.append(obj)

            from ..io.sast_export import SASTExportManager
            output_dir: str = scene_props.load_directory
            if (len(scene_props.save_directory) > 0):
                output_dir = scene_props.save_directory

            SASTExportManager.export_camera_auto(output_dir, objs)
        except Exception as error:
            raise error

        return {'FINISHED'}

class SASTExportSETAutomatic(bpy.types.Operator):
    '''Automatic SET File Export'''
    bl_idname='sastexport.setauto'
    bl_label='Export SET File Auto'

    def execute(self, context: bpy.types.Context):
        return {'FINISHED'}
