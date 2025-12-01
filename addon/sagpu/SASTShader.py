import bpy
from gpu.types import (
    GPUShader
)
import gpu
from ..properties.sast_point_object_properties import SASTPointObjectProperties
from ..properties.sast_object_properties import SASTObjectProperties

# This is the base class to inheret from. This should not be registered on its own.
class SASTShader():
    '''Base SAST GPU Shader'''

    point_shader: GPUShader = None

    @staticmethod
    def draw():
        '''Shader Draw Function'''
        objects = bpy.context.selected_objects

        for object in objects:
            if (object.type == 'MESH'):
                props: SASTObjectProperties = SASTObjectProperties.get_properties(object)
                is_selected: bool = True
                match (props.objtype):
                    case 'POINT':
                        if (SASTShader.point_shader == None):
                            SASTShader.point_shader = gpu.shader.from_builtin('POLYLINE_UNIFORM_COLOR')
                        SASTPointObjectProperties.draw_shader(object, is_selected, SASTShader.point_shader)

    @staticmethod
    def register():
        '''Register Shader in Scene'''
        bpy.types.SpaceView3D.draw_handler_add(SASTShader.draw, (), 'WINDOW', 'POST_VIEW')