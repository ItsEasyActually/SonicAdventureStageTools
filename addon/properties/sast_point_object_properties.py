import bpy
from bpy.props import (
    PointerProperty
)
import gpu
from gpu.types import (
    GPUShader
)
from gpu_extras.batch import batch_for_shader
from ..geonode.sa2pointnode import SA2PointNode
from ..geonode import GeometryNodeManager

class SASTPointObjectProperties(bpy.types.PropertyGroup):
    '''Sonic Adventure Stage Tools Point Object Properties'''

    def valid_object(self, object: bpy.types.Object):
        if (GeometryNodeManager.has_geometry_node(object, SA2PointNode.modifier_name)):
            return True
        else:
            return False

    link1: PointerProperty(
        type=bpy.types.Object,
        name='Linked Point',
        description='A point linked to this point.',
        poll=valid_object
    )

    link2: PointerProperty(
        type=bpy.types.Object,
        name='Linked Point',
        description='A point linked to this point.',
        poll=valid_object
    )

    link3: PointerProperty(
        type=bpy.types.Object,
        name='Linked Point',
        description='A point linked to this point.',
        poll=valid_object
    )

    link4: PointerProperty(
        type=bpy.types.Object,
        name='Linked Point',
        description='A point linked to this point.',
        poll=valid_object
    )

    link5: PointerProperty(
        type=bpy.types.Object,
        name='Linked Point',
        description='A point linked to this point.',
        poll=valid_object
    )

    link6: PointerProperty(
        type=bpy.types.Object,
        name='Linked Point',
        description='A point linked to this point.',
        poll=valid_object
    )

    pathlink: PointerProperty(
        type=bpy.types.Object,
        name='Direction Point',
        description='A point indicating the direction of the connected points.',
        poll=valid_object
    )

    def draw_ui(self, layout: bpy.types.UILayout):
        '''Draws the properties UI Panel'''
        geonode: SA2PointNode = SA2PointNode(bpy.context.active_object)
        if (geonode.node != None):
            if (geonode.get_enable_player_tracking() == False):
                layout.prop(data=self, property='link1', text='Link Point 1')
                if (self.link1 != None):
                    layout.prop(data=self, property='link2', text='Link Point 2')
                    if (self.link2 != None):
                        layout.prop(data=self, property='link3', text='Link Point 3')
                        if (self.link3 != None):
                            layout.prop(data=self, property='link4', text='Link Point 4')
                            if (self.link4 != None):
                                layout.prop(data=self, property='link5', text='Link Point 5')
                                if (self.link5 != None):
                                    layout.prop(data=self, property='link6', text='Link Point 6')
            else:
                layout.prop(data=self, property='link1', text='Previous Link')
                layout.prop(data=self, property='link2', text='Next Link')

    @classmethod
    def register(cls):
        bpy.types.Object.sast_point_properties = bpy.props.PointerProperty(type=cls)

    @staticmethod
    def get_properties(obj: bpy.types.Object):
        '''Returns the SAST Point Properties'''
        from .sast_object_properties import SASTObjectProperties
        props = SASTObjectProperties.get_properties(obj)
        if (props != None) and (props.objtype == 'POINT'):
            return obj.sast_point_properties
            
        return None

    @staticmethod
    def draw_shader(obj: bpy.types.Object, is_selected: bool, shader: GPUShader):
        shader.uniform_float("viewportSize", gpu.state.viewport_get()[2:])
        props: SASTPointObjectProperties = SASTPointObjectProperties.get_properties(obj)
        points: list = []
        indices: list = []
        geonode: SA2PointNode = SA2PointNode(obj)
        points.append(obj.location)
        if (geonode.node != None):
            if (geonode.get_enable_player_tracking() == True):
                if (props.link2 != None):
                    shader.uniform_float("lineWidth", 1.0)
                    shader.uniform_float("color",(0,1,0,1))
                    dp: list = []
                    di: list = []
                    dp.append(obj.location)
                    dp.append(props.link2.location)
                    di.append((0,1))
                    forward_batch = batch_for_shader(shader, 'LINES', content={"pos": dp}, indices=di)
                    forward_batch.draw(shader)

                    shader.uniform_float("lineWidth", 1.0)
                    shader.uniform_float("color",(0,0,1,1))
                    bp: list = []
                    bi: list = []
                    bp.append(obj.location)
                    bp.append(props.link1.location)
                    bi.append((0,1))
                    backward_batch = batch_for_shader(shader, 'LINES', content={"pos": bp}, indices=bi)
                    backward_batch.draw(shader)
                else:
                    shader.uniform_float("lineWidth", 1.0)
                    shader.uniform_float("color",(0,1,0,1))
                    points.append(props.link1.location)
                    indices.append((0,1))
                    backward_batch = batch_for_shader(shader, 'LINES', content={"pos": points}, indices=indices)
                    backward_batch.draw(shader)
            else:
                if (props.link1 != None):
                    points.append(props.link1.location)
                    indices.append((0,1))
                    if (props.link2 != None):
                        points.append(props.link2.location)
                        indices.append((0,2))
                        if (props.link3 != None):
                            points.append(props.link3.location)
                            indices.append((0,3))
                            if (props.link4 != None):
                                points.append(props.link4.location)
                                indices.append((0,4))
                                if (props.link5 != None):
                                    points.append(props.link5.location)
                                    indices.append((0,5))
                                    if (props.link6 != None):
                                        points.append(props.link6.location)
                                        indices.append((0,6))

                shader.uniform_float("lineWidth", 1.0)
                shader.uniform_float("color",(1,1,1,1))
                link_batch =  batch_for_shader(shader, 'LINES', content={"pos": points}, indices=indices)
                link_batch.draw(shader)

    