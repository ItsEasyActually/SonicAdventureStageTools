import bpy
from ..pynet import PyNetManager
from ..geonode.sa1cameranode import SA1CameraNode
from ..geonode.sa2cameranode import SA2CameraNode
from ..geonode.sa2pointnode import SA2PointNode
from ..properties.sast_scene_properties import SASTSceneProperties
from ..properties.sast_point_object_properties import SASTPointObjectProperties
from ..properties.sast_cam_object_properties import SASTCAMObjectProperties

class SASTExportManager:
    '''Export management'''

    #region SA1 Camera Export
    @staticmethod
    def get_sa1_camera(geonode: SA1CameraNode, camprops: SASTCAMObjectProperties) :
        '''Processes Blender data and updates an SA1CAMObject'''
        from SAST.Lib.CAM.SA1 import SA1CAMObject
        camobject = SA1CAMObject()
        cammode: str = f'{camprops.cameramode}'
        if (camprops.cameralevel != 'Normal'):
            cammode = f'{camprops.cameramode}_{camprops.cameralevel}'
        camobject.Mode = SA1CAMObject.GetCamModeFromString(cammode)
        camobject.AdjustMode = SA1CAMObject.GetAdjustModeFromString(camprops.adjustmode)
        camobject.CollisionShape = SA1CAMObject.GetCollisionShapeFromInt(geonode.get_collision_shape())
        camobject.Priority = camprops.priority
        camobject.Collision.Rotation.X.FromRadians(geonode.get_collision_x_rotation())
        camobject.Collision.Rotation.Y.FromRadians(geonode.get_collision_y_rotation())
        camobject.Collision.Scale.X = geonode.get_collision_x_scale()
        camobject.Collision.Scale.Y = geonode.get_collision_y_scale()
        camobject.Collision.Scale.Z = geonode.get_collision_z_scale()
        camobject.CameraRotation.X.Angle = geonode.get_camera_x_rotation()
        camobject.CameraRotation.Y.Angle = geonode.get_camera_y_rotation()
        camobject.CameraPosition.X = geonode.get_camera_x_position()
        camobject.CameraPosition.Y = geonode.get_camera_y_position()

        camobject.CameraTarget.X = geonode.get_target_x_position()
        camobject.CameraTarget.Y = geonode.get_target_y_position()
        
        camobject.CameraDistance = geonode.get_camera_distance()

        if (camprops.cameramode == 'SonicP'):
            camobject.CameraPosition.Z = geonode.get_camera_z_position()
            camobject.CameraTarget.Z = geonode.get_target_z_position()
        else:
            camobject.CameraPosition.Z = -geonode.get_camera_z_position()
            camobject.CameraTarget.Z = -geonode.get_target_z_position()

        return camobject
    
    @staticmethod
    def process_sa1_cameras(objs: list[bpy.types.Object]) :
        from SAST.Lib.CAM.SA1 import SA1CAMFile
        file = SA1CAMFile()
        for obj in objs:
            from ..geonode.sa1cameranode import SA1CameraNode
            geonode: SA1CameraNode = SA1CameraNode(obj)
            if (geonode.node is not None):
                from ..properties.sast_cam_object_properties import SASTCAMObjectProperties
                camprops: SASTCAMObjectProperties = SASTCAMObjectProperties.get_properties(obj)
                if (camprops is not None):
                    camobject = SASTExportManager.get_sa1_camera(geonode, camprops)
                    camobject.Collision.Position.X = obj.location[0]
                    camobject.Collision.Position.Y = obj.location[2]
                    camobject.Collision.Position.Z = -obj.location[1]
                    file.AddCamera(camobject)

        return file
    
    @staticmethod
    def export_sa1_camera(path: str, objs: list[bpy.types.Object]):
        '''Exports an SA1 Camera.'''

        PyNetManager.load_dll()
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            from SAST.Lib.Blender import ExportManager
            
            output = SASTExportManager.process_sa1_cameras(objs)

            ExportManager.ExportSA1CamFile(output, path, False)
        else:
            print('Scene Properties were None! Nothing exported.')

    @staticmethod
    def export_sa1_camera_auto(path: str, objs: list[bpy.types.Object], scene_props: SASTSceneProperties):
        '''Exports an SA1 Camera.'''

        PyNetManager.load_dll()
        if (scene_props is not None):
            from System.Collections.Generic import Dictionary
            from SAST.Lib.CAM.SA1 import SA1CAMFile
            from SAST.Lib.Blender import ExportManager

            sonicobjs = list[bpy.types.Object]()
            tailsobjs = list[bpy.types.Object]()
            knucklesobjs = list[bpy.types.Object]()
            amyobjs = list[bpy.types.Object]()
            gammaobjs = list[bpy.types.Object]()
            bigobjs = list[bpy.types.Object]()
            eggmanobjs = list[bpy.types.Object]()
            tikalobjs = list[bpy.types.Object]()
            lastobjs = list[bpy.types.Object]()

            output = Dictionary[str, SA1CAMFile]()
            
            from ..properties.sast_object_properties import SASTObjectProperties
            for obj in objs:
                props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)

                if (props.for_sonic):
                    sonicobjs.append(obj)

                if (props.for_tails):
                    tailsobjs.append(obj)

                if (props.for_knuckles):
                    knucklesobjs.append(obj)
                
                if (props.for_amy):
                    amyobjs.append(obj)

                if (props.for_gamma):
                    gammaobjs.append(obj)

                if (props.for_big):
                    bigobjs.append(obj)

                if (props.for_eggman):
                    eggmanobjs.append(obj)

                if (props.for_tikal):
                    tikalobjs.append(obj)

                if (props.for_last):
                    lastobjs.append(obj)

            if (len(sonicobjs) > 0):
                output.Add('Sonic', SASTExportManager.process_sa1_cameras(sonicobjs))
            if (len(tailsobjs) > 0):
                output.Add('Tails', SASTExportManager.process_sa1_cameras(tailsobjs))
            if (len(knucklesobjs) > 0):
                output.Add('Knuckles', SASTExportManager.process_sa1_cameras(knucklesobjs))
            if (len(amyobjs) > 0):
                output.Add('Amy', SASTExportManager.process_sa1_cameras(amyobjs))
            if (len(gammaobjs) > 0):
                output.Add('Gamma', SASTExportManager.process_sa1_cameras(gammaobjs))
            if (len(bigobjs) > 0):
                output.Add('Big', SASTExportManager.process_sa1_cameras(bigobjs))
            if (len(eggmanobjs) > 0):
                output.Add('Eggman', SASTExportManager.process_sa1_cameras(eggmanobjs))
            if (len(tikalobjs) > 0):
                output.Add('Tikal', SASTExportManager.process_sa1_cameras(tikalobjs))
            if (len(lastobjs) > 0):
                output.Add('Last', SASTExportManager.process_sa1_cameras(lastobjs))

            ExportManager.ExportSA1CamFileAuto(output, path, scene_props.stage_id, scene_props.act_id, False)
        else:
            print('Scene Properties were None! Nothing exported.')

    #endregion

    #region SA2 Camera Export
    @staticmethod
    def get_sa2_camera(geonode: SA2CameraNode, camprops: SASTCAMObjectProperties) :
        '''Get an SA2 Camera'''
        from SAST.Lib.CAM.SA2 import SA2CAMObject
        camera = SA2CAMObject()
        camera.Mode = SA2CAMObject.GetCamModeFromString(camprops.cameramode)
        camera.AdjustMode = SA2CAMObject.GetAdjustModeFromString(camprops.adjustmode)
        match (geonode.get_collision_shape()):
            case 0:
                camera.CollisionShape = SA2CAMObject.GetCollisionShapeFromInt(1)
            case 1:
                camera.CollisionShape = SA2CAMObject.GetCollisionShapeFromInt(2)
            case 2:
                camera.CollisionShape = SA2CAMObject.GetCollisionShapeFromInt(3)
        camera.Priority = camprops.priority

        camera.Collision.Rotation.X.FromRadians(geonode.get_collision_x_angle())
        camera.Collision.Rotation.Y.FromRadians(geonode.get_collision_y_angle())
        camera.Collision.Rotation.Z.FromRadians(-geonode.get_collision_z_angle())
        camera.Collision.Scale.X = geonode.get_collision_x_scale()
        camera.Collision.Scale.Y = geonode.get_collision_y_scale()
        camera.Collision.Scale.Z = geonode.get_collision_z_scale()

        camera.CameraRotation.X.FromRadians(geonode.get_camera_x_angle())
        camera.CameraRotation.Y.FromRadians(geonode.get_camera_y_angle())
        camera.CameraRotation.Z.FromRadians(-geonode.get_camera_z_angle())
        camera.CameraPosition.X = geonode.get_camera_x_position()
        camera.CameraPosition.Y = geonode.get_camera_y_position()
        camera.CameraPosition.Z = -geonode.get_camera_z_position()
        camera.CameraTarget.X = geonode.get_target_x_position()
        camera.CameraTarget.Y = geonode.get_target_y_position()
        camera.CameraTarget.Z = -geonode.get_target_z_position()

        camera.IntProperty1 = camprops.int_prop1
        camera.IntProperty2 = camprops.int_prop2
        camera.IntProperty3 = camprops.int_prop3
        camera.IntProperty4 = camprops.int_prop4
        camera.IntProperty5 = camprops.int_prop5
        camera.IntProperty6 = camprops.int_prop6
        camera.IntProperty7 = camprops.int_prop7
        camera.IntProperty8 = camprops.int_prop8
        camera.FloatProperty1 = camprops.float_prop1
        camera.FloatProperty2 = camprops.float_prop2
        camera.FloatProperty3 = camprops.float_prop3
        camera.FloatProperty4 = camprops.float_prop4
        camera.FloatProperty5 = camprops.float_prop5
        camera.FloatProperty6 = camprops.float_prop6
        camera.FloatProperty7 = camprops.float_prop7
        camera.FloatProperty8 = camprops.float_prop8

        return camera

    @staticmethod
    def get_sa2_point(geonode: SA2PointNode, pointprops: SASTPointObjectProperties, points: list[bpy.types.Object]):
        '''Get an SA2 Point'''
        from SAST.Lib.CAM.SA2 import SA2PointObject
        point = SA2PointObject()
        point.PlayerPointRadius = geonode.get_player_point_radius()
        point.CameraPoint.X = geonode.get_camera_x_point()
        point.CameraPoint.Y = geonode.get_camera_y_point()
        point.CameraPoint.Z = -geonode.get_camera_z_point()
        point.IsPlayerPointEnabled = geonode.get_enable_player_point()
        point.TrackPlayer = geonode.get_enable_player_tracking()

        # Link Processing
        if (geonode.get_enable_player_tracking()):
            if (pointprops.link1 != None):
                point.Links[0] = points.index(pointprops.link1)
                if (pointprops.link2 != None):
                    point.Links[1] = points.index(pointprops.link2)
                    point.FlowIndex = point.Links[1]
                else:
                    point.FlowIndex = point.Links[0]
        else:
            if (pointprops.link1 != None):
                point.Links[0] = points.index(pointprops.link1)
                if (pointprops.link2 != None):
                    point.Links[1] = points.index(pointprops.link2)
                    if (pointprops.link3 != None):
                        point.Links[2] = points.index(pointprops.link3)
                        if (pointprops.link4 != None):
                            point.Links[3] = points.index(pointprops.link4)
                            if (pointprops.link5 != None):
                                point.Links[4] = points.index(pointprops.link5)
                                if (pointprops.link6 != None):
                                    point.Links[5] = points.index(pointprops.link6)

        return point

    @staticmethod
    def process_sa2_group(camobjs: list[bpy.types.Object], pointobjs: list[bpy.types.Object]) :
        '''Processes Cam and Point objects and returns an SA2CAMGroup'''
        from SAST.Lib.CAM.SA2 import SA2CAMGroup
        group = SA2CAMGroup()
        if (len(camobjs) > 0):
            for cam in camobjs:
                cam_props: SASTCAMObjectProperties = SASTCAMObjectProperties.get_properties(cam)
                geonode: SA2CameraNode = SA2CameraNode(cam)
                if (geonode.node != None):
                    camera = SASTExportManager.get_sa2_camera(geonode, cam_props)
                    camera.Collision.Position.X = cam.location[0]
                    camera.Collision.Position.Y = cam.location[2]
                    camera.Collision.Position.Z = -cam.location[1]
                    group.AddCamera(camera)
            if (len(pointobjs) > 0):
                for point in pointobjs:
                    point_props: SASTPointObjectProperties = SASTPointObjectProperties.get_properties(point)
                    geonode: SA2PointNode = SA2PointNode(point)
                    if (geonode.node != None):
                        output = SASTExportManager.get_sa2_point(geonode, point_props, pointobjs)
                        output.PlayerPoint.X = point.location[0]
                        output.PlayerPoint.Y = point.location[2]
                        output.PlayerPoint.Z = -point.location[1]
                        group.AddPoint(output)

        return group

    @staticmethod
    def process_sa2_file(objects: list[bpy.types.Object]):
        '''Process an SA2 Camera File'''
        from SAST.Lib.CAM.SA2 import SA2CAMFile

        sp_cams: list[bpy.types.Object] = []
        sp_points: list[bpy.types.Object] = []
        dm_cams: list[bpy.types.Object] = []
        dm_points: list[bpy.types.Object] = []
        mp_cams: list[bpy.types.Object] = []
        mp_points: list[bpy.types.Object] = []

        from ..properties.sast_object_properties import SASTObjectProperties
        for obj in objects:
            props: SASTObjectProperties = SASTObjectProperties.get_properties(obj)

            match (props.objtype):
                case 'CAM':
                    if (props.for_singleplayer):
                        sp_cams.append(obj)
                    if (props.for_demo):
                        dm_cams.append(obj)
                    if (props.for_multiplayer):
                        mp_cams.append(obj)
                case 'POINT':
                    if (props.for_singleplayer):
                        sp_points.append(obj)
                    if (props.for_demo):
                        dm_points.append(obj)
                    if (props.for_multiplayer):
                        mp_points.append(obj)
            
        camfile = SA2CAMFile()

        camfile.SinglePlayerCameraGroup = SASTExportManager.process_sa2_group(sp_cams, sp_points)
        camfile.DemoPlayerCameraGroup = SASTExportManager.process_sa2_group(dm_cams, dm_points)
        camfile.MultiplayerCameraGroup = SASTExportManager.process_sa2_group(mp_cams, mp_points)

        return camfile

    @staticmethod
    def export_sa2_camera(path: str, objs: list[bpy.types.Object]):
        '''Manually export an SA2 Camera'''

        PyNetManager.load_dll()
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        if (scene_props is not None):
            from SAST.Lib.Blender import ExportManager
            
            output = SASTExportManager.process_sa2_file(objs)

            ExportManager.ExportSA2CamFile(output, path, True)
        else:
            print('Scene Properties were None! Nothing exported.')

    @staticmethod
    def export_sa2_camera_auto(path: str, objs: list[bpy.types.Object], scene_props: SASTSceneProperties):
        '''Automatically Export an SA2 Camera'''
        PyNetManager.load_dll()
        if (scene_props is not None):
            from System.Collections.Generic import List
            from SAST.Lib.CAM.SA2 import SA2CAMFile
            from SAST.Lib.Blender import ExportManager

            output = List[SA2CAMFile]()

            outfile = SASTExportManager.process_sa2_file(objs)

            output.Add(outfile)

            ExportManager.ExportSA2CamFileAuto(output, path, scene_props.stage_id, scene_props.act_id, True)
        else:
            print('Something went horribly wrong.')

    #endregion

    @staticmethod
    def export_camera(path: str, objs: list[bpy.types.Object]):
        '''Export a Camera File'''
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        match (scene_props.game_id):
            case 'SADXPC':
                SASTExportManager.export_sa1_camera(path, objs)
            case 'SA2BPC':
                SASTExportManager.export_sa2_camera(path, objs)

    @staticmethod
    def export_camera_auto(path: str, objs: list[bpy.types.Object]):
        scene_props: SASTSceneProperties = SASTSceneProperties.get_properties()
        match (scene_props.game_id):
            case 'SADXPC':
                SASTExportManager.export_sa1_camera_auto(path, objs, scene_props)
            case 'SA2BPC':
                SASTExportManager.export_sa2_camera_auto(path, objs, scene_props)