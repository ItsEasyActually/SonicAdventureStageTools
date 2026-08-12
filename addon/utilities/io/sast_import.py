from __future__ import annotations
import bpy
import os

from ..logger.sast_logger import SASTLogger
from ...scene.properties import (
    SASTSceneProperties,
    SASTSETDefinitionProperties
)
from ...pynet import PyNetManager
from ..set.set_asset_manager import SetAssetManager

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...object.properties.sast_object_properties import SASTObjectProperties

class SASTImportManager:
    '''Managment functions for importing files.'''

    importing = False

    #region Helpers
    @staticmethod
    def get_mesh() -> bpy.types.Mesh:
        '''Gets the default mesh to use for any object.'''
        mesh: bpy.types.Mesh
        SASTLogger.log('Getting SACAM Mesh')
        if (bpy.data.meshes.__contains__('sacam')):
            mesh = bpy.data.meshes.get('sacam')
        else:
            mesh = bpy.data.meshes.new(f'sacam')

        return mesh
    
    @staticmethod
    def get_object_flag(props: SASTObjectProperties, name: str):
        SASTLogger.log(f'Processing Flags for {name}')
        match (name):
            case 'Sonic':
                props.for_sonic = True
            case 'Tails':
                props.for_tails = True
                props.for_sonic = False
            case 'Knuckles':
                props.for_knuckles = True
                props.for_sonic = False
            case 'Amy':
                props.for_amy = True
                props.for_sonic = False
            case 'Gamma':
                props.for_gamma = True
                props.for_sonic = False
            case 'Big':
                props.for_big = True
                props.for_sonic = False
            case 'Last':
                props.for_last = True
                props.for_sonic = False
            case 'Eggman':
                props.for_eggman = True
                props.for_sonic = False
            case 'Tikal':
                props.for_tikal = True
                props.for_sonic = False
            case 'SinglePlayer':
                props.for_singleplayer = True
            case 'Multiplayer':
                props.for_multiplayer = True
                props.for_singleplayer = False
            case 'Demo':
                props.for_demo = True
                props.for_singleplayer = False

    @staticmethod
    def get_set_item_flags(flags: int) -> set[str]:
        retflags: set[str] = set[str]()
        match (flags):
            case 0:
                retflags.add('NoFlags')
            case 1:
                retflags.add('Flag1')
            case 2:
                retflags.add('Flag2')
            case 4:
                retflags.add('Flag4')
            case 8:
                pass

    #endregion

    #region Camera Import
    #region SA1 Camera
    @staticmethod
    def process_sa1_camera(camobject, index: int, mesh: bpy.types.Mesh, collection: bpy.types.Collection, context: bpy.types.Context):
        from ...object.properties.sast_object_properties import SASTObjectProperties
        SASTLogger.log('Processing Camera Object...')
        cam_name: str = f'{index:03d}_SA1CAM_{camobject.Mode.ToString()}'
        SASTLogger.log(f'Camera Name: {cam_name}')
        obj: bpy.types.Object = bpy.data.objects.new(cam_name, mesh)
        obj.location[0] = camobject.Collision.Position.X
        obj.location[1] = -camobject.Collision.Position.Z
        obj.location[2] = camobject.Collision.Position.Y
        obj.lock_rotation[0] = True
        obj.lock_rotation[1] = True
        obj.lock_rotation[2] = True
        obj.lock_scale[0] = True
        obj.lock_scale[1] = True
        obj.lock_scale[2] = True
        props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
        props.objtype = 'CAM'
        SASTImportManager.get_object_flag(props, collection.name.split('_')[0])
        from ...object.geonode.sa1cameranode import SA1CameraNode
        SA1CameraNode.make(obj)
        geonode: SA1CameraNode = SA1CameraNode(obj)
        if (geonode.node is not None):
            modes: list[str] = str.split(camobject.Mode.ToString(), "_")
            geonode.update_camera_mode(modes[0])
            if (len(modes) > 1):
                geonode.set_camera_level(modes[1])
            geonode.set_collision_shape(camobject.CollisionShape.ToString())
            geonode.set_collision_x_rotation(camobject.Collision.Rotation.X.Radians)
            geonode.set_collision_y_rotation(camobject.Collision.Rotation.Y.Radians)
            
            geonode.set_collision_x_scale(camobject.Collision.Scale.X)
            geonode.set_collision_y_scale(camobject.Collision.Scale.Y)
            geonode.set_collision_z_scale(camobject.Collision.Scale.Z)
            
            geonode.set_camera_x_position(camobject.CameraPosition.X)
            geonode.set_camera_y_position(camobject.CameraPosition.Y)
            
            geonode.set_camera_x_rotation(camobject.CameraRotation.X.Angle)
            geonode.set_camera_y_rotation(camobject.CameraRotation.Y.Angle)

            geonode.set_target_x_position(camobject.CameraTarget.X)
            geonode.set_target_y_position(camobject.CameraTarget.Y)
            geonode.set_camera_distance(camobject.CameraDistance)

            if (modes[0] == 'SonicP'):
                geonode.set_camera_z_position(camobject.CameraPosition.Z)
                geonode.set_target_z_position(camobject.CameraTarget.Z)
            else:
                geonode.set_camera_z_position(-camobject.CameraPosition.Z)
                geonode.set_target_z_position(-camobject.CameraTarget.Z)

            from ...object.properties.sast_cam_object_properties import SASTCAMObjectProperties
            camprops: SASTCAMObjectProperties = SASTCAMObjectProperties.get_properties(obj)
            camprops.cameramode = modes[0]
            if (len(modes) > 1):
                camprops.cameralevel = modes[1]
            camprops.adjustmode = camobject.AdjustMode.ToString()
            camprops.priority = camobject.Priority

        SASTLogger.log(f'Linking {obj} to {collection}')
        collection.objects.link(obj)

    @staticmethod
    def import_sa1_camera(file, mesh: bpy.types.Mesh, collection: bpy.types.Collection, context: bpy.types.Context):
        '''Imports an SA1 Camera File'''
        SASTLogger.log(f'Importing SA1 Camera File: {file}')
        PyNetManager.load_dll()
        from SAST.Lib.Blender import ImportManager
        index: int = 0
        camfile = ImportManager.ImportSA1CAMFile(file)
        for cam in camfile.Cameras:
            SASTImportManager.process_sa1_camera(cam, index, mesh, collection, context)
            index += 1

    @staticmethod
    def import_sa1_camera_auto(context: bpy.types.Context, directory: str, stage_id: str, act_id: str, base_collection: bpy.types.Collection):
        '''Imports all SA1 Cameras for a set Stage and Act'''
        PyNetManager.load_dll()
        from SAST.Lib.Blender import ImportManager

        files = ImportManager.ImportSA1CAMFileAuto(directory, stage_id, act_id)
        for file in files:
            SASTLogger.log(f'Importing SA1 Camera File: {file}')
            file_collection: bpy.types.Collection = bpy.data.collections.new(name=f'{file.Key}_Cameras')
            mesh: bpy.types.Mesh = SASTImportManager.get_mesh()
            index: int = 0
            for cam in file.Value.Cameras:
                SASTImportManager.process_sa1_camera(cam, index, mesh, file_collection, context)
                index += 1
            base_collection.children.link(file_collection)
    
    #endregion

    #region SA2 Camera
    @staticmethod
    def process_sa2_cameras(cams, mesh: bpy.types.Mesh, collection: bpy.types.Collection, context: bpy.types.Context, colname: str):
        '''Processes an SA2CAMObject'''
        from ...object.properties.sast_object_properties import SASTObjectProperties
        camcollection: bpy.types.Collection = bpy.data.collections.new(colname)
        i: int = 0
        for cam in cams:
            obj: bpy.types.Object = bpy.data.objects.new(name=f'{i:03d}_SA2CAM_{cam.Mode.ToString()}', object_data=mesh)
            obj.location[0] = cam.Collision.Position.X
            obj.location[1] = -cam.Collision.Position.Z
            obj.location[2] = cam.Collision.Position.Y
            obj.lock_rotation[0] = True
            obj.lock_rotation[1] = True
            obj.lock_rotation[2] = True
            obj.lock_scale[0] = True
            obj.lock_scale[1] = True
            obj.lock_scale[2] = True
            props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
            props.objtype = 'CAM'
            SASTImportManager.get_object_flag(props, collection.name.split('_')[0])
            from ...object.geonode.sa2cameranode import SA2CameraNode
            SA2CameraNode.make(obj)
            geonode: SA2CameraNode = SA2CameraNode(obj)
            if (geonode.node != None):
                geonode.update_camera_mode(cam.Mode.ToString())
                geonode.set_collision_shape(cam.CollisionShape.ToString())
                geonode.set_collision_x_angle(cam.Collision.Rotation.X.Radians)
                geonode.set_collision_y_angle(cam.Collision.Rotation.Y.Radians)
                geonode.set_collision_z_angle(-cam.Collision.Rotation.Z.Radians)

                geonode.set_collision_x_scale(cam.Collision.Scale.X)
                geonode.set_collision_y_scale(cam.Collision.Scale.Y)
                geonode.set_collision_z_scale(cam.Collision.Scale.Z)

                geonode.set_camera_x_angle(cam.CameraRotation.X.Radians)
                geonode.set_camera_y_angle(cam.CameraRotation.Y.Radians)
                geonode.set_camera_z_angle(-cam.CameraRotation.Z.Radians)

                geonode.set_camera_x_position(cam.CameraPosition.X)
                geonode.set_camera_y_position(cam.CameraPosition.Y)
                geonode.set_camera_z_position(-cam.CameraPosition.Z)

                geonode.set_target_x_position(cam.CameraTarget.X)
                geonode.set_target_y_position(cam.CameraTarget.Y)
                geonode.set_target_z_position(-cam.CameraTarget.Z)

                from ...object.properties.sast_cam_object_properties import SASTCAMObjectProperties
                camprops: SASTCAMObjectProperties = SASTCAMObjectProperties.get_properties(obj)
                camprops.cameramode = cam.Mode.ToString()
                camprops.adjustmode = cam.AdjustMode.ToString()
                camprops.priority = cam.Priority

                camprops.int_prop1 = cam.IntProperty1
                camprops.int_prop2 = cam.IntProperty2
                camprops.int_prop3 = cam.IntProperty3
                camprops.int_prop4 = cam.IntProperty4
                camprops.int_prop5 = cam.IntProperty5
                camprops.int_prop6 = cam.IntProperty6
                camprops.int_prop7 = cam.IntProperty7
                camprops.int_prop8 = cam.IntProperty8
                camprops.float_prop1 = cam.FloatProperty1
                camprops.float_prop2 = cam.FloatProperty2
                camprops.float_prop3 = cam.FloatProperty3
                camprops.float_prop4 = cam.FloatProperty4
                camprops.float_prop5 = cam.FloatProperty5
                camprops.float_prop6 = cam.FloatProperty6
                camprops.float_prop7 = cam.FloatProperty7
                camprops.float_prop8 = cam.FloatProperty8

            camcollection.objects.link(obj)
            i += 1

        collection.children.link(camcollection)

    @staticmethod
    def process_sa2_campoints(points, mesh: bpy.types.Mesh, collection: bpy.types.Collection, context: bpy.types.Context, colname: str, suffix: str):
        '''Processes and SA2CAMPointObject'''
        from ...object.properties.sast_object_properties import SASTObjectProperties
        pointcollection: bpy.types.Collection = bpy.data.collections.new(name=colname)
        point_objects: dict = dict[str, list[str]]()
        print(f'Length of Points: {points.Count}')
        i: int = 0
        for point in points:
            point_name: str = f'{i:03d}_SA2POINT_{suffix}'
            obj: bpy.types.Object = bpy.data.objects.new(name=point_name, object_data=mesh)
            obj.location[0] = point.PlayerPoint.X
            obj.location[1] = -point.PlayerPoint.Z
            obj.location[2] = point.PlayerPoint.Y
            obj.lock_rotation[0] = True
            obj.lock_rotation[1] = True
            obj.lock_rotation[2] = True
            obj.lock_scale[0] = True
            obj.lock_scale[1] = True
            obj.lock_scale[2] = True
            props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
            props.objtype = 'POINT'
            SASTImportManager.get_object_flag(props, collection.name.split('_')[0])
            from ...object.geonode.sa2pointnode import SA2PointNode
            SA2PointNode.make(obj)
            geonode: SA2PointNode = SA2PointNode(obj)
            if (geonode.node != None):
                geonode.set_player_point_radius(point.PlayerPointRadius)
                geonode.set_camera_x_point(point.CameraPoint.X)
                geonode.set_camera_y_point(point.CameraPoint.Y)
                geonode.set_camera_z_point(-point.CameraPoint.Z)
                geonode.set_camera_point_radius(point.CameraPointRadius)
                geonode.set_enable_player_point(point.IsPlayerPointEnabled)
                geonode.set_enable_player_tracking(point.TrackPlayer)

            links= []
            for link in point.Links:
                if (link > -1):
                    links.append(f'{link:03d}_SA2POINT_{suffix}')
                else:
                    links.append('None')

            if point.FlowIndex > -1:
                links.append(f'{point.FlowIndex:03d}_SA2POINT_{suffix}')
            else:
                links.append('None')

            if (len(links) > 0):
                point_objects[point_name] = links

            pointcollection.objects.link(obj)
            i += 1

        if (len(point_objects) > 0):
            for k, v in point_objects.items():
                from ...object.properties.sast_point_object_properties import SASTPointObjectProperties
                obj: bpy.types.Object = bpy.data.objects[k]
                point_props: SASTPointObjectProperties = SASTPointObjectProperties.get_properties(obj)
                if (v[0] != 'None'):
                    point_props.link1 = bpy.data.objects[v[0]]
                if (v[1] != 'None'):
                    point_props.link2 = bpy.data.objects[v[1]]
                if (v[2] != 'None'):
                    point_props.link3 = bpy.data.objects[v[2]]
                if (v[3] != 'None'):
                    point_props.link4 = bpy.data.objects[v[3]]
                if (v[4] != 'None'):
                    point_props.link5 = bpy.data.objects[v[4]]
                if (v[5] != 'None'):
                    point_props.link6 = bpy.data.objects[v[5]]
                if (v[6] != 'None'):
                    point_props.pathlink = bpy.data.objects[v[6]]

        collection.children.link(pointcollection)

    @staticmethod
    def process_sa2_cam_groups(cam, mesh: bpy.types.Mesh, collection: bpy.types.Collection, context: bpy.types.Context):
        if (cam.SinglePlayerCameraGroup.CameraCount > 0):
            # Run everything for single player cameras and cam points here.
            spcollection: bpy.types.Collection = bpy.data.collections.new(name='SinglePlayer')
            collection.children.link(spcollection)
            SASTImportManager.process_sa2_cameras(cam.SinglePlayerCameraGroup.GetCameras(), mesh, spcollection, context, 'SP Cameras')
            if (cam.SinglePlayerCameraGroup.PointCount > 0):
                SASTImportManager.process_sa2_campoints(cam.SinglePlayerCameraGroup.GetPoints(), mesh, spcollection, context, 'SP Points', 'SP')

        if (cam.DemoCameraGroup.CameraCount > 0):
            # Run everything for demo cameras and cam points here.
            dmcollection: bpy.types.Collection = bpy.data.collections.new(name='Demo')
            collection.children.link(dmcollection)
            SASTImportManager.process_sa2_cameras(cam.DemoCameraGroup.GetCameras(), mesh, dmcollection, context, 'DM Cameras')
            if (cam.DemoCameraGroup.PointCount > 0):
                SASTImportManager.process_sa2_campoints(cam.DemoCameraGroup.GetPoints(), mesh, dmcollection, context, 'DM Points', 'DM')

        if (cam.MultiplayerCameraGroup.CameraCount > 0):
            # Run everything for multiplayer cameras and cam points here.
            mpcollection: bpy.types.Collection = bpy.data.collections.new(name='Multiplayer')
            collection.children.link(mpcollection)
            SASTImportManager.process_sa2_cameras(cam.MultiplayerCameraGroup.GetCameras(), mesh, mpcollection, context, 'MP Cameras')
            if (cam.MultiplayerCameraGroup.PointCount > 0):
                SASTImportManager.process_sa2_campoints(cam.MultiplayerCameraGroup.GetPoints(), mesh, mpcollection, context, 'MP Points', 'MP')

    @staticmethod
    def import_sa2_camera(file, mesh: bpy.types.Mesh, collection: bpy.types.Collection, context: bpy.types.Context):
        '''Imports an SA2CAMFile.'''
        PyNetManager.load_dll()
        from SAST.Lib.Blender import ImportManager
        
        SASTLogger.log(f'Importing SA1 Camera File: {file}')
        camfile = ImportManager.ImportSA2CAMFile(file)
        SASTImportManager.process_sa2_cam_groups(camfile, mesh, collection, context)     

    @staticmethod
    def import_sa2_camera_auto(context: bpy.types.Context, directory: str, stage_id: str, sub_id: str, base_collection: bpy.types.Collection):
        '''Auto import handler for an SA2CAMFile'''
        PyNetManager.load_dll()
        from SAST.Lib.Blender import ImportManager

        files = ImportManager.ImportSA2CAMFileAuto(directory, stage_id, sub_id)
        for file in files:
            SASTLogger.log(f'Importing SA1 Camera File: {file}')
            SASTImportManager.process_sa2_cam_groups(file, SASTImportManager.get_mesh(), base_collection, context)
        
    #endregion

    @staticmethod
    def import_cam_manual(files, directory: str, context: bpy.types.Context):
        '''Manual Camera Import'''
        SASTImportManager.importing = True
        bpy.context.view_layer.objects.active = None
        SASTLogger.log(f'Importing {len(files)} Camera Files: MANUAL MODE')

        if (len(files) > 0):
            for file in files:
                path: str = os.path.join(directory, file.name)
                collection: bpy.types.Collection = bpy.data.collections.new(name=file.name)
                context.scene.collection.children.link(collection)
                mesh: bpy.types.Mesh = SASTImportManager.get_mesh()
                scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
                match (scene_props.game_id):
                    case 'SADXPC':
                        SASTImportManager.import_sa1_camera(path, mesh, collection, context)
                    case 'SA2BPC':
                        SASTImportManager.import_sa2_camera(path, mesh, collection, context)

        SASTImportManager.importing = False
        SASTLogger.log('Camera Import Complete!')

    @staticmethod
    def import_cam_auto(context: bpy.types.Context, directory: str, stage_id: str, act_id: str, base_collection_name: str = ""):
        '''Automatic Camera Import'''
        SASTImportManager.importing = True
        bpy.context.view_layer.objects.active = None

        if (len(directory) > 0):
            scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
            match (scene_props.game_id):
                case 'SADXPC':
                    SASTLogger.log(f'Importing {stage_id} {act_id} Camera Files: AUTO MODE')
                    if (len(base_collection_name) <= 0):
                        base_collection_name = f'{stage_id}_{act_id}'
                    base_collection: bpy.types.Collection = bpy.data.collections.new(name=f'CAM_{base_collection_name}')
                    SASTImportManager.import_sa1_camera_auto(context, directory, stage_id, act_id, base_collection)
                case 'SA2BPC':
                    SASTLogger.log(f'Importing {stage_id} Camera Files: AUTO MODE')
                    if (len(base_collection_name) <= 0):
                        base_collection_name = f'{stage_id}'
                    base_collection: bpy.types.Collection = bpy.data.collections.new(name=f'CAM_{base_collection_name}')
                    SASTImportManager.import_sa2_camera_auto(context, directory, stage_id, act_id, base_collection)

            context.scene.collection.children.link(base_collection)

        SASTImportManager.importing = False
        SASTLogger.log('Camera Import Complete!')

    #endregion

    #region SET Import
    @staticmethod
    def process_setitem_flags(props, flags: str):
        for flag in flags.split(','):
            flag = flag.strip()
            if (flag == 'NoFlag'):
                props.objectflags = '0'
            if (flag == 'Flag1'):
                props.objectflags = '1'
            if (flag == 'Flag2'):
                props.objectflags = '2'
            if (flag == 'Flag4'):
                props.dependent_set = True

    @staticmethod
    def process_set_item(setitem, index: int, collection: bpy.types.Collection, scene_props: SASTSceneProperties):
        from ...object.properties.sast_object_properties import SASTObjectProperties
        from ...object.properties.sast_set_object_properties import SASTSETObjectProperties
        from ...object.geonode.setitemnode import SetItemNode
        if (setitem.ObjectID < scene_props.get_objlist_size()):
            iteminfo: SASTSETDefinitionProperties = scene_props.objlist[setitem.ObjectID]
        else:
            iteminfo: SASTSETDefinitionProperties = scene_props.objlist[0]

        item_name: str = iteminfo.internal_name
        if (len(iteminfo.name) > 0):
            item_name = iteminfo.name
        obj: bpy.types.Object = SetAssetManager.get_object(iteminfo.asset_name)
        if (obj is not None):
            obj.name = f'{index:03d}_{item_name}'
            SASTLogger.log(f'Adding Object: {obj.name}')
            obj.location[0] = setitem.Node.Position.X
            obj.location[1] = -setitem.Node.Position.Z
            obj.location[2] = setitem.Node.Position.Y
            obj.rotation_euler[0] = setitem.Node.Rotation.X.Radians
            obj.rotation_euler[1] = -setitem.Node.Rotation.Z.Radians
            obj.rotation_euler[2] = setitem.Node.Rotation.Y.Radians
            SetItemNode.handle_set_item_rotation(obj, iteminfo.rotation_order)
            obj.lock_scale[0] = True
            obj.lock_scale[1] = True
            obj.lock_scale[2] = True

            obj_props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)
            SASTImportManager.get_object_flag(obj_props, collection.name.split('_')[0])
            obj_props.objtype = 'SET'

            set_props: SASTSETObjectProperties = SASTSETObjectProperties.get_properties(obj)
            if (setitem.ObjectID < len(scene_props.objlist)):
                set_props.objectid = str(setitem.ObjectID)
            else:
                set_props.objectid = '0'
                set_props.override_id = True
            set_props.fallback_objid = setitem.ObjectID
            SASTImportManager.process_setitem_flags(set_props, setitem.Flags.ToString())

            node: SetItemNode = SetItemNode(obj)
            node.set_rot_x(setitem.Node.Rotation.X.Angle)
            node.set_rot_y(setitem.Node.Rotation.Y.Angle)
            node.set_rot_z(setitem.Node.Rotation.Z.Angle)
            node.set_scl_x(setitem.Node.Scale.X)
            node.set_scl_y(setitem.Node.Scale.Y)
            node.set_scl_z(setitem.Node.Scale.Z)
            
            collection.objects.link(obj)

    @staticmethod
    def get_set_files(game_id: str, directory: str, stage_id: str, act_id: str) -> Any:
        from SAST.Lib.Blender import ImportManager
        match (game_id):
            case 'SADXPC':
                return ImportManager.ImportSA1SETFileAuto(directory, stage_id, act_id)
            case 'SA2BPC':
                return ImportManager.ImportSA2SETFileAuto(directory, stage_id, act_id)

    @staticmethod
    def import_set_manual(files, directory: str, context: bpy.types.Context):
        SASTImportManager.importing = True
        bpy.context.view_layer.objects.active = None
        SASTLogger.log(f'Import {len(files)} SET Files: MANUAL MODE')

        if (len(files) > 0):
            for file in files:
                path: str = os.path.join(directory, file.name)
                collection: bpy.types.Collection = bpy.data.collections.new(name=file.name)
                context.scene.collection.children.link(collection)
                scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
                SASTLogger.log(f'Importing SET File: {file}')
                PyNetManager.load_dll()
                from SAST.Lib.Blender import ImportManager
                index: int = 0
                setfile = ImportManager.ImportSETFile(path)
                for item in setfile.GetObjects():
                    SASTImportManager.process_set_item(item, index, collection, scene_props)
                    index += 1

        SASTImportManager.importing = False
        SASTLogger.log('SET File Import Complete!')

    @staticmethod
    def import_set_auto(context: bpy.types.Context, directory: str, stage_id: str, act_id: str, base_collection_name: str = ""):
        SASTImportManager.importing = True
        bpy.context.view_layer.objects.active = None

        if (len(directory) > 0):
            scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
            SASTLogger.log(f'Import {stage_id} {act_id} SET Files: AUTO MODE')
            if (len(base_collection_name) <= 0):
                base_collection_name = f'{stage_id}_{act_id}'
            base_collection: bpy.types.Collection = bpy.data.collections.new(name=f'SET_{base_collection_name}')

            PyNetManager.load_dll()

            files = SASTImportManager.get_set_files(scene_props.game_id, directory, stage_id, act_id)
            for file in files:
                SASTLogger.log(f'Importing SET File: {file.Value}')
                file_collection: bpy.types.Collection = bpy.data.collections.new(name=f'{file.Key}_Objects')
                index: int = 0
                for item in file.Value.GetObjects():
                    SASTImportManager.process_set_item(item, index, file_collection, scene_props)
                    index += 1
                base_collection.children.link(file_collection)

            context.scene.collection.children.link(base_collection)
        
        SASTImportManager.importing = False
        SASTLogger.log('SET File Import Complete!')

    #endregion