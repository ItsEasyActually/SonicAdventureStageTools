import bpy
import os

from ..logger.sast_logger import SASTLogger
from ..properties.sast_scene_properties import SASTSceneProperties
from ..pynet import PyNetManager
from ..properties.sast_object_properties import SASTObjectProperties

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

    #endregion

    #region SA1 Import
    #region SA1 Camera
    @staticmethod
    def process_sa1_camera(camobject, index: int, mesh: bpy.types.Mesh, collection: bpy.types.Collection, context: bpy.types.Context):
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
        SASTImportManager.get_object_flag(props, collection.name)
        from ..geonode.sa1cameranode import SA1CameraNode
        SA1CameraNode.make(obj)
        geonode: SA1CameraNode = SA1CameraNode(obj)
        if (geonode.node is not None):
            modes: list[str] = str.split(camobject.Mode.ToString(), "_")
            geonode.update_camera_mode(modes[0])
            if (len(modes) > 1):
                geonode.update_camera_level(modes[1])
            match (camobject.CollisionShape.ToString()):
                case 'Sphere':
                    geonode.set_collision_shape(0)
                case 'Block':
                    geonode.set_collision_shape(2)
                case 'Plane':
                    geonode.set_collision_shape(1)
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

            from ..properties.sast_cam_object_properties import SASTCAMObjectProperties
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
            file_collection: bpy.types.Collection = bpy.data.collections.new(name=file.Key)
            mesh: bpy.types.Mesh = SASTImportManager.get_mesh()
            index: int = 0
            for cam in file.Value.Cameras:
                SASTImportManager.process_sa1_camera(cam, index, mesh, file_collection, context)
                index += 1
            base_collection.children.link(file_collection)
    
    #endregion

    #endregion

    #region SA2 Import
    #region SA2 Camera
    @staticmethod
    def process_sa2_cameras(cams, mesh: bpy.types.Mesh, collection: bpy.types.Collection, context: bpy.types.Context, colname: str):
        '''Processes an SA2CAMObject'''
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
            SASTImportManager.get_object_flag(props, collection.name)
            from ..geonode.sa2cameranode import SA2CameraNode
            SA2CameraNode.make(obj)
            geonode: SA2CameraNode = SA2CameraNode(obj)
            if (geonode.node != None):
                geonode.update_camera_mode(cam.Mode.ToString())
                match (cam.CollisionShape.ToString()):
                    case 'Sphere':
                        geonode.set_collision_shape(0)
                    case 'Plane':
                        geonode.set_collision_shape(1)
                    case 'Block':
                        geonode.set_collision_shape(2)

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

                from ..properties.sast_cam_object_properties import SASTCAMObjectProperties
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
            SASTImportManager.get_object_flag(props, collection.name)
            from ..geonode.sa2pointnode import SA2PointNode
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
                from ..properties.sast_point_object_properties import SASTPointObjectProperties
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

    #endregion

    #region Import Processing
    @staticmethod
    def import_cam_manual(files, directory: str, context: bpy.types.Context):
        '''Manual Camera Import'''
        SASTImportManager.importing = True
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

        if (len(directory) > 0):
            scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
            match (scene_props.game_id):
                case 'SADXPC':
                    SASTLogger.log(f'Importing {stage_id} {act_id} Camera Files: AUTO MODE')
                    if (len(base_collection_name) <= 0):
                        base_collection_name = f'{stage_id}_{act_id}'
                    base_collection: bpy.types.Collection = bpy.data.collections.new(name=base_collection_name)
                    SASTImportManager.import_sa1_camera_auto(context, directory, stage_id, act_id, base_collection)
                case 'SA2BPC':
                    SASTLogger.log(f'Importing {stage_id} Camera Files: AUTO MODE')
                    if (len(base_collection_name) <= 0):
                        base_collection_name = f'{stage_id}'
                    base_collection: bpy.types.Collection = bpy.data.collections.new(name=base_collection_name)
                    SASTImportManager.import_sa2_camera_auto(context, directory, stage_id, act_id, base_collection)

            context.scene.collection.children.link(base_collection)

        SASTImportManager.importing = False
        SASTLogger.log('Camera Import Complete!')

    #endregion

