import bpy
from bpy.types import (
    Object
)

class GeometryNodeManager:
    '''Static Manager for Geometry Node processing'''

    @staticmethod
    def has_geometry_node(obj: Object, name: str) -> bool:
        '''Checks if the supplied object has a modifier and group matching the supplied name.'''
        if (len(obj.modifiers) > 0):
            if (obj.modifiers.__contains__(name)):
                node: bpy.types.NodesModifier = obj.modifiers[name]
                if (node.node_group is not None):
                    if (node.node_group.name == name):
                        return True
                
        return False

    @staticmethod
    def clear_geometry_node(obj: Object):
        '''Clears all modifiers from the specified object'''
        if (len(obj.modifiers) > 0):
            obj.modifiers.clear()

    @staticmethod
    def create_node(obj: Object, file_path: str, node_group: str) -> bpy.types.NodesModifier:
        from ..io.sast_asset_import import SASTAssetImport
        if (not bpy.data.node_groups.__contains__(node_group)):
            SASTAssetImport.link_asset(file_path, 'NodeTree', node_group)
        
        if (bpy.data.node_groups.__contains__(node_group)):
            GeometryNodeManager.clear_geometry_node(obj)
            geonode: bpy.types.NodesModifier = obj.modifiers.new(node_group, 'NODES')
            geonode.node_group = bpy.data.node_groups[node_group]
            return geonode
        else:
            return None

    @staticmethod
    def get_geometry_node(node_tree: str, default_tree: str = None):
        '''Gets the supplied node tree if it exists. A default can be provided. If it fails to find either supplied tree in bpy.data.node_groups, None is returned.'''
        if bpy.data.node_groups.__contains__(node_tree):
            return bpy.data.node_groups[node_tree]
        elif default_tree != None: 
            if bpy.data.node_groups.__contains__(default_tree):
                return bpy.data.node_groups[default_tree]
        
        return None
    
    @staticmethod
    def get_geometry_node_from_object(obj: Object):
        if obj.modifiers.__contains__(GeometryNodeManager.modifier_name):
            return obj.modifiers[GeometryNodeManager.modifier_name]
        else:
            return None