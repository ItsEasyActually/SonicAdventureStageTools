import bpy
from bpy.props import (
    EnumProperty,
    BoolProperty
)
from .sast_scene_properties import SASTSceneProperties
from ..geonode.sa1cameranode import SA1CameraNode
from ..geonode.sa2cameranode import SA2CameraNode
from ..geonode.sa2pointnode import SA2PointNode
from ..geonode import GeometryNodeManager

class SASTObjectProperties(bpy.types.PropertyGroup):
    '''Sonic Adventure Stage Tools Base Object Properties'''

    def populate_objtype(self, context: bpy.types.Context):
        '''Populates the objtype items.'''
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        items = []
        if (scene_props is not None):
            match (scene_props.game_id):
                case 'SADXPC':
                    items.append(('NONE','None','Object is not an SAST Object.', 'X', 0))
                    items.append(('CAM','Camera Object','Object represents an SAST Camera Object.', 'OUTLINER_OB_CAMERA', 1))
                    items.append(('SET','Set Object','CURRENTLY NOT SUPPORTED', 'GEOMETRY_SET', 2))
                case 'SA2BPC':
                    items.append(('NONE','None','Object is not an SAST Object.', 'X', 0))
                    items.append(('CAM','Camera Object','Object represents an SAST Camera Object.', 'OUTLINER_OB_CAMERA', 1))
                    items.append(('SET','Set Object','CURRENTLY NOT SUPPORTED.', 'GEOMETRY_SET', 2))
                    items.append(('POINT','Camera Point', 'Object represents an SAST Camera Point. Only used in SA2.', 'OUTLINER_OB_POINTCLOUD', 3))

        return items

    def update_objtype(self, context: bpy.types.Context):
        '''Runs when the objtype is updated.'''
        from ..io.sast_import import SASTImportManager
        if (SASTImportManager.importing == True):
            return
        obj = context.active_object
        if (self.objtype == 'NONE'):
            GeometryNodeManager.clear_geometry_node(obj)
            return
        
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        match (self.objtype):
            case 'SET':
                #TODO: SET Object Support
                pass
            case 'CAM':
                match (scene_props.game_id):
                    case 'SADXPC':
                        if (self.objtype == 'CAM'):
                            GeometryNodeManager.create_node(obj, SA1CameraNode.modifier_name)
                    case 'SA2BPC':
                        if (self.objtype == 'CAM'):
                            GeometryNodeManager.create_node(obj, SA2CameraNode.modifier_name)
            case 'POINT':
                if (scene_props.game_id == 'SA2BPC'):
                    GeometryNodeManager.create_node(obj, SA2PointNode.modifier_name)
            case 'NONE':
                GeometryNodeManager.clear_geometry_node(obj)

    objtype: EnumProperty(
        name='Object Type',
        description='Select the type of SAST Object this object is meant to represent.',
        default=0,
        items=populate_objtype,
        update=update_objtype
    )

    #region SA1 Flags
    for_sonic: BoolProperty(
        name='Sonic',
        description='Object will be exported for Sonic.',
        default=True,
    )

    for_eggman: BoolProperty(
        name='Eggman',
        description='Object will be exported for Eggman.',
        default=False
    )

    for_tails: BoolProperty(
        name='Tails',
        description='Object will be exported for Tails.',
        default=False
    )

    for_knuckles: BoolProperty(
        name='Knuckles',
        description='Object will be exported for Knuckles.',
        default=False
    )

    for_tikal: BoolProperty(
        name='Tikal',
        description='Object will be exported for Tikal.',
        default=False
    )

    for_amy: BoolProperty(
        name='Amy',
        description='Object will be exported for Amy.',
        default=False
    )

    for_gamma: BoolProperty(
        name='Gamma',
        description='Object will be exported for Gamma.',
        default=False
    )

    for_big: BoolProperty(
        name='Big',
        description='Object will be exported for Big.',
        default=False
    )

    for_last: BoolProperty(
        name='Last Story',
        description='Object will be exported for the Last Story.',
        default=False
    )

    #endregion

    #region SA2 Flags
    for_singleplayer: BoolProperty(
        name='Single Player',
        description='Object will be exported for use in Single Player.',
        default=True
    )

    for_multiplayer: BoolProperty(
        name='Multiplayer',
        description='Object will be exported for use in Multiplayer.',
        default=False
    )

    for_demo: BoolProperty(
        name='Demo',
        description='Object will be exported for use in the Demo for the stage.',
        default=False
    )
    
    #endregion
    
    @classmethod
    def register(cls):
        bpy.types.Object.sast_properties = bpy.props.PointerProperty(type=cls)

    def draw_export_flags(self, layout: bpy.types.UILayout, context: bpy.types.Context):
        '''Draws the Export Flag filters in the object properties UI'''
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if self.objtype != 'NONE':
            header: bpy.types.UILayout
            body: bpy.types.UILayout
            header, body = layout.panel(idname='sast_flags', default_closed=True)
            header.label(text='Export Flags', icon='FILTER')
            if (body is not None):
                match (scene_props.game_id):
                    case 'SADXPC':
                        body.prop(data=self, property='for_sonic')
                        body.prop(data=self, property='for_tails')
                        body.prop(data=self, property='for_knuckles')
                        body.prop(data=self, property='for_amy')
                        body.prop(data=self, property='for_gamma')
                        body.prop(data=self, property='for_big')
                        body.prop(data=self, property='for_eggman')
                        body.prop(data=self, property='for_tikal')
                        body.prop(data=self, property='for_last')
                    case 'SA2BPC':
                        body.prop(data=self, property='for_singleplayer')
                        body.prop(data=self, property='for_multiplayer')
                        if (self.objtype != 'SET'):
                            body.prop(data=self, property='for_demo')

    def draw_ui(self, layout: bpy.types.UILayout, context: bpy.types.Context):
        '''Draws the corresponding UI element for the selected object.'''
        layout.prop(data=self, property='objtype')

    @staticmethod
    def get_properties(obj: bpy.types.Object):
        '''Returns the base SAST properties of supplied object. If the object is not a Mesh type object, it will return None.'''
        if (obj.type == 'MESH'):
            return obj.sast_properties
        else:
            return None
        
    