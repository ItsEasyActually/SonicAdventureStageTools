import bpy
from bpy.props import (
    EnumProperty,
    IntProperty,
    FloatProperty
)

from ..gameinfo.camerainfo import CameraInfo
from .sast_scene_properties import SASTSceneProperties
from ..geonode.sa1cameranode import SA1CameraNode
from ..geonode.sa2cameranode import SA2CameraNode

class SASTCAMObjectProperties(bpy.types.PropertyGroup):
    '''Sonic Adventure Stage Tools Camera Object Properties'''

    def populate_cameramode(self, context: bpy.types.Context) -> tuple:
        '''Populates the Camera Mode List.'''
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            return CameraInfo.get_camera_modes(scene_props.game_id)
        else:
            return []

    def update_cameramode(self, context: bpy.types.Context):
        '''Runs whenever the Camera Mode Selection is changed.'''
        from ..io.sast_import import SASTImportManager
        if (SASTImportManager.importing == True):
            return
        obj: bpy.types.Object = context.active_object
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        match (scene_props.game_id):
            case 'SADXPC':
                geonode: SA1CameraNode = SA1CameraNode(obj)
                geonode.update_camera_mode(self.cameramode)
                items = CameraInfo.get_camera_levels(self.cameramode)
                for (x,y,z) in items:
                    if (self.cameralevel == x):
                        return
                self.cameralevel = 'Normal'
            case 'SA2BPC':
                geonode: SA2CameraNode = SA2CameraNode(obj)
                geonode.update_camera_mode(self.cameramode)

    cameramode: EnumProperty(
        name='Camera Mode',
        description='Mode for the camera volume.',
        default=0,
        items=populate_cameramode,
        update=update_cameramode
    )

    def populate_cameralevel(self, context: bpy.types.Context):
        '''Populates the Camera List List.'''
        return CameraInfo.get_camera_levels(self.cameramode)

    def update_cameralevel(self, context: bpy.types.Context):
        '''Runs whenever the Camera Level selection is changed.'''
        from ..io.sast_import import SASTImportManager
        if (SASTImportManager.importing == True):
            return
        obj: bpy.types.Object = context.active_object
        geonode: SA1CameraNode = SA1CameraNode(obj)
        if (geonode.node is not None):
            geonode.update_camera_level(self.cameralevel)

    cameralevel: EnumProperty(
        name='Camera Level',
        description='Method used by the camera volume on how it interacts with the player and the camera.',
        default=0,
        items=populate_cameralevel,
        update=update_cameralevel
    )

    def populate_adjustmode(self, context: bpy.types.Context):
        '''Populates the items for the Adjust Mode list.'''
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            return CameraInfo.get_adjustment_modes(scene_props.game_id)
        else:
            return []

    def update_adjustmode(self, context: bpy.types.Context):
        '''Runs whenever the Adjust Mode selection is changed.'''
        pass

    adjustmode: EnumProperty(
        name='Adjustment Mode',
        description='Set the method in which a camera will transition from one volume to another.',
        default=0,
        items=populate_adjustmode,
        update=update_adjustmode
    )

    priority: IntProperty(
        name='Priority Level',
        description='Priority of the volume for controlling the camera. Higher values take priority.',
        default=0
    )

    #region SA2 Camera Properties
    int_prop1: IntProperty(
        name='Integer Property 1',
        description='',
        default=0
    )

    int_prop2: IntProperty(
        name='Integer Property 2',
        description='',
        default=0
    )

    int_prop3: IntProperty(
        name='Integer Property 3',
        description='',
        default=0
    )

    int_prop4: IntProperty(
        name='Integer Property 4',
        description='',
        default=0
    )

    int_prop5: IntProperty(
        name='Integer Property 5',
        description='',
        default=0
    )

    int_prop6: IntProperty(
        name='Integer Property 6',
        description='',
        default=0
    )

    int_prop7: IntProperty(
        name='Integer Property 7',
        description='',
        default=0
    )

    int_prop8: IntProperty(
        name='Integer Property 8',
        description='',
        default=0
    )

    float_prop1: FloatProperty(
        name='Float Property 1',
        description='',
        default=0
    )

    float_prop2: FloatProperty(
        name='Float Property 2',
        description='',
        default=0
    )

    float_prop3: FloatProperty(
        name='Float Property 3',
        description='',
        default=0
    )

    float_prop4: FloatProperty(
        name='Float Property 4',
        description='',
        default=0
    )

    float_prop5: FloatProperty(
        name='Float Property 5',
        description='',
        default=0
    )

    float_prop6: FloatProperty(
        name='Float Property 6',
        description='',
        default=0
    )

    float_prop7: FloatProperty(
        name='Float Property 7',
        description='',
        default=0
    )

    float_prop8: FloatProperty(
        name='Float Property 8',
        description='',
        default=0
    )

    #endregion

    def draw_sa2props_ui(self, layout: bpy.types.UILayout, context: bpy.types.Context):
        '''Draws the SA2 Specific Properties'''
        # TODO: Add in cases per camera mode to show/hide properties that are actively used once research on this is done.
        match (self.cameramode):
            case 'Ashland':
                layout.prop(data=self, property='int_prop1', text='Camera FOV')
                header, body = layout.panel(idname='pt_sa2props', default_closed=True)
                header.label(text='Additional SA2 Properties')
                if (body != None):
                    body.prop(data=self, property='float_prop1')
                    body.prop(data=self, property='float_prop2')
                    body.prop(data=self, property='float_prop3')
                    body.prop(data=self, property='float_prop4')
                    body.prop(data=self, property='float_prop5')
                    body.prop(data=self, property='float_prop6')
                    body.prop(data=self, property='float_prop7')
                    body.prop(data=self, property='float_prop8')
                    body.prop(data=self, property='int_prop2')
                    body.prop(data=self, property='int_prop3')
                    body.prop(data=self, property='int_prop4')
                    body.prop(data=self, property='int_prop5')
                    body.prop(data=self, property='int_prop6')
                    body.prop(data=self, property='int_prop7')
                    body.prop(data=self, property='int_prop8')
            case 'Point':
                layout.prop(data=self, property='float_prop1', text='Distance to Player')
                layout.prop(data=self, property='float_prop2', text='Additional Vertical Height')
                header, body = layout.panel(idname='pt_sa2props', default_closed=True)
                header.label(text='Additional SA2 Properties')
                if (body != None):
                    body.prop(data=self, property='float_prop3')
                    body.prop(data=self, property='float_prop4')
                    body.prop(data=self, property='float_prop5')
                    body.prop(data=self, property='float_prop6')
                    body.prop(data=self, property='float_prop7')
                    body.prop(data=self, property='float_prop8')
                    body.prop(data=self, property='int_prop1')
                    body.prop(data=self, property='int_prop2')
                    body.prop(data=self, property='int_prop3')
                    body.prop(data=self, property='int_prop4')
                    body.prop(data=self, property='int_prop5')
                    body.prop(data=self, property='int_prop6')
                    body.prop(data=self, property='int_prop7')
                    body.prop(data=self, property='int_prop8')
            case 'Klamath':
                layout.prop(data=self, property='float_prop1', text='Distance to Player')
                layout.prop(data=self, property='float_prop2', text='Vertical Height')
                header, body = layout.panel(idname='pt_sa2props', default_closed=True)
                header.label(text='Additional SA2 Properties')
                if (body != None):
                    body.prop(data=self, property='float_prop3')
                    body.prop(data=self, property='float_prop4')
                    body.prop(data=self, property='float_prop5')
                    body.prop(data=self, property='float_prop6')
                    body.prop(data=self, property='float_prop7')
                    body.prop(data=self, property='float_prop8')
                    body.prop(data=self, property='int_prop1')
                    body.prop(data=self, property='int_prop2')
                    body.prop(data=self, property='int_prop3')
                    body.prop(data=self, property='int_prop4')
                    body.prop(data=self, property='int_prop5')
                    body.prop(data=self, property='int_prop6')
                    body.prop(data=self, property='int_prop7')
                    body.prop(data=self, property='int_prop8')
            case _:
                header, body = layout.panel(idname='pt_sa2props')
                header.label(text='Additional SA2 Properties')
                if (body != None):
                    body.prop(data=self, property='float_prop1')
                    body.prop(data=self, property='float_prop2')
                    body.prop(data=self, property='float_prop3')
                    body.prop(data=self, property='float_prop4')
                    body.prop(data=self, property='float_prop5')
                    body.prop(data=self, property='float_prop6')
                    body.prop(data=self, property='float_prop7')
                    body.prop(data=self, property='float_prop8')
                    body.prop(data=self, property='int_prop1')
                    body.prop(data=self, property='int_prop2')
                    body.prop(data=self, property='int_prop3')
                    body.prop(data=self, property='int_prop4')
                    body.prop(data=self, property='int_prop5')
                    body.prop(data=self, property='int_prop6')
                    body.prop(data=self, property='int_prop7')
                    body.prop(data=self, property='int_prop8')

    def draw_ui(self, layout: bpy.types.UILayout, context: bpy.types.Context):
        '''Draws the corresponding UI element for the selected object.'''
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        layout.prop(data=self, property='cameramode')
        if (scene_props.game_id == 'SADXPC'):
            layout.prop(data=self, property='cameralevel')
        layout.prop(data=self, property='adjustmode')
        layout.prop(data=self, property='priority')

    def reset_properties(self, context: bpy.types.Context):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            match (scene_props.game_id):
                case 'SADXPC':
                    self.cameramode = 'Follow'
                    self.cameralevel = 'Normal'
                    self.adjustmode = 'None'
                    self.priority = 0
                    geonode: SA1CameraNode = SA1CameraNode(context.active_object)
                    geonode.reset_properties()
                case 'SA2BPC':
                    pass

    @classmethod
    def register(cls):
        bpy.types.Object.sast_cam_properties = bpy.props.PointerProperty(type=cls)

    @staticmethod
    def get_properties(obj: bpy.types.Object):
        '''Returns SAST Camera Properties from the supplied object. If type is not Mesh or Object is not a Cam Object, None will be returned.'''
        from .sast_object_properties import SASTObjectProperties
        props = SASTObjectProperties.get_properties(obj)
        if (props != None) and (props.objtype == 'CAM'):
            return obj.sast_cam_properties
            
        return None
    
