import bpy
from ..geonode import GeometryNodeManager
from ..geonode.sa2cameranode import SA2CameraNode
from ..geonode.sa2pointnode import SA2PointNode
from ..geonode.sa1cameranode import SA1CameraNode
from ..properties.sast_object_properties import SASTObjectProperties
from ..properties.sast_cam_object_properties import SASTCAMObjectProperties
from ..properties.sast_scene_properties import SASTSceneProperties

class SASTCamObjectOperators:
    '''Wrapping class to run the draw function for the operators in this file.'''

    @staticmethod
    def draw_ui(layout: bpy.types.UILayout, context: bpy.types.Context):
        layout.operator(operator=SASTAddGeometryNode.bl_idname, text='Add Geometry Node', icon='GEOMETRY_NODES')
        layout.operator(operator=SASTResetProperties.bl_idname, text='Reset Camera Properties', icon='FILE_REFRESH')

class SASTAddGeometryNode(bpy.types.Operator):
    '''Adds the specific camera node to the currently selected object.'''
    bl_description='Clears any existing geometry nodes from the object and adds the selected game\'s Geometry Node.'
    bl_idname='sastexecute.addgeometrynode'
    bl_label='Add Geometry Node'

    @classmethod
    def poll(cls, context: bpy.types.Context):
        obj: bpy.types.Object = context.active_object
        props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
        if (props is not None):
            if (props.objtype == 'CAM' or props.objtype == 'POINT'):
                if (SA1CameraNode.poll(obj) or SA2CameraNode.poll(obj) or SA2PointNode.poll(obj)):
                    return False
                else:
                    return True
            
        return False
    
    def execute(self, context: bpy.types.Context):
        obj: bpy.types.Object = context.active_object
        props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
        GeometryNodeManager.clear_geometry_node(obj)
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        match (scene_props):
            case 'SADXPC':
                if (props.objtype == 'CAM'):
                    SA1CameraNode.make(obj)
            case 'SA2BPC':
                if (props.objtype == 'CAM'):
                    SA2CameraNode.make(obj)
                elif (props.objtype == 'POINT'):
                    SA2PointNode.make(obj)

        return {'FINISHED'}

class SASTResetProperties(bpy.types.Operator):
    '''Resets the properties on the currently selected camera.'''
    bl_idname='sastexecute.resetcamproperties'
    bl_label='Reset Camera Properties'
    bl_description='Resets the properties of the selected CAM object to their defaults.'

    @classmethod
    def poll(cls, context: bpy.types.Context):
        obj: bpy.types.Object = context.active_object
        props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
        if (props is not None):
            if (props.objtype == 'CAM'):
                camprops: SASTCAMObjectProperties = SASTCAMObjectProperties.get_properties(obj)
                if (camprops is not None):
                    return True

        return False
    
    def execute(self, context: bpy.types.Context):
        obj: bpy.types.Object = context.active_object
        camprops: SASTCAMObjectProperties = SASTCAMObjectProperties.get_properties(obj)
        camprops.reset_properties(context)

        return {'FINISHED'}