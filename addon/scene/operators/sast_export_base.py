import bpy
import os
from bpy.props import (
    StringProperty,
    CollectionProperty,
    EnumProperty
)
from ...utilities.geonode.geometry_node_manager import GeometryNodeManager

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