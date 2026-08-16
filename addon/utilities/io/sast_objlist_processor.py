import os
import configparser
import json
from ... import ADDON_DIR
from ...game.info.game_info import GameInfo
from ...game.info.sadxpc_game_info import SADXPCGameInfo
from ...game.info.sa2bpc_game_info import SA2BPCGameInfo
from bpy.types import CollectionProperty
from ...scene.properties.sast_set_definition_properties import SASTSETDefinitionProperties

class SASTObjListProcessor:
    '''Processes INI or JSON files containing Object List data.'''

    @staticmethod
    def get_task_level(value: int) -> str:
        return f'Level{value}'

    @staticmethod
    def get_attributes(value: int) -> set[str]:
        output: set[str] = set[str]()
        match (value):
            case 1:
                output.add('LoadByDistance')
            case 2:
                output.add('LoadInstant')
            case 3:
                output.add('LoadByDistance')
                output.add('LoadInstant')
            case 4:
                output.add('LoadOnce')
            case 5:
                output.add('LoadByDistance')
                output.add('LoadOnce')
            case 6:
                output.add('LoadInstant')
                output.add('LoadOnce')
            case 7:
                output.add('LoadByDistance')
                output.add('LoadInstant')
                output.add('LoadOnce')

        return output

    @staticmethod
    def get_init_mode(value: int) -> set[str]:
        output: set[str] = set[str]()
        match (value):
            case 1:
                output.add('MotionWork')
            case 2:
                output.add('TaskWork')
            case 3:
                output.add('MotionWork')
                output.add('TaskWork')
            case 4:
                output.add('ForceWork')
            case 5:
                output.add('MotionWork')
                output.add('ForceWork')
            case 6:
                output.add('TaskWork')
                output.add('ForceWork')
            case 7:
                output.add('MotionWork')
                output.add('TaskWork')
                output.add('ForceWork')
            case 8:
                output.add('AnyWork')
            case 9:
                output.add('MotionWork')
                output.add('AnyWork')
            case 10:
                output.add('TaskWork')
                output.add('AnyWork')
            case 11:
                output.add('MotionWork')
                output.add('TaskWork')
                output.add('AnyWork')
            case 12:
                output.add('ForceWork')
                output.add('AnyWork')
            case 13:
                output.add('MotionWork')
                output.add('ForceWork')
                output.add('AnyWork')
            case 14:
                output.add('TaskWork')
                output.add('ForceWork')
                output.add('AnyWork')
            case 15:
                output.add('MotionWork')
                output.add('TaskWork')
                output.add('ForceWork')
                output.add('AnyWork')

        return output

    @staticmethod
    def set_task_level(value: str) -> int:
        match (value):
            case 'Level0':
                return 0
            case 'Level1':
                return 1
            case 'Level2':
                return 2
            case 'Level3':
                return 3
            case 'Level4':
                return 4
            case 'Level5':
                return 5
            case 'Level6':
                return 6
            case 'Level7':
                return 7

    @staticmethod
    def set_attributes(value: set[str]) -> int:
        retval: int = 0
        for flag in value:
            match (flag):
                case 'LoadByDistance':
                    retval += 1
                case 'LoadInstant':
                    retval += 2
                case 'LoadOnce':
                    retval += 4

        return retval

    @staticmethod
    def set_init_mode(value: set[str]) -> int:
        retval: int = 0

        for flag in value:
            match (flag):
                case 'MotionWork':
                    retval += 1
                case 'TaskWork':
                    retval += 2
                case 'ForceWork':
                    retval += 4
                case 'AnyWork':
                    retval += 8

        return retval

    #region Readers
    @staticmethod
    def read_ini_file(objlist: CollectionProperty, filepath: str):
        '''Reads an INI formatted Object List file and adds the objects to the supplied object list.'''
        print(f'File: {filepath}')
        config: configparser.ConfigParser = configparser.ConfigParser()
        config.read(filepath)

        if (len(config) > 0):
            for section in config.sections():
                entry: SASTSETDefinitionProperties = objlist.add()
                entry.internal_name = config.get(section, 'Name')
                entry.function_address = config.get(section, 'Code')
                entry.task_level = SASTObjListProcessor.get_task_level(config.getint(section, 'Arg2'))
                entry.load_attributes = SASTObjListProcessor.get_attributes(config.getint(section, 'Flags'))
                entry.init_mode = SASTObjListProcessor.get_init_mode(config.getint(section, 'Arg1'))
                if config.has_option(section, 'Distance'):
                    entry.load_range = config.getfloat(section, 'Distance')
        else:
            print('File length was less than 0')

    @staticmethod
    def read_json_file(objlist: CollectionProperty, filepath: str):
        '''Reads a JSON formatted Object List file and adds the objects to the supplied object list.'''
        with open(filepath, 'r') as f:
            data: dict = json.load(f)

            for key in data.keys():
                item: dict = data[key]
                object_info: dict = item['ObjectInfo']
                blender_info: dict = item['BlenderInfo']
                property_info: dict = blender_info['PropertyInfo']

                entry: SASTSETDefinitionProperties = objlist.add()
                entry.internal_name     = key
                entry.load_range        = object_info['LoadDistance']
                entry.function_address  = object_info['FunctionAddress']
                entry.task_level        = SASTObjListProcessor.get_task_level(object_info['TaskLevel'])
                entry.init_mode         = SASTObjListProcessor.get_init_mode(object_info['InitializationMode'])
                entry.load_attributes   = SASTObjListProcessor.get_attributes(object_info['LoadAttributes'])
                entry.name              = blender_info['CommonName']
                entry.rotation_order    = blender_info['RotationMode']
                entry.asset_name        = blender_info['AssetName']
                entry.asset_file        = blender_info['AssetFile']
                entry.is_relative_file  = blender_info['RelativeAssetFile']
                entry.item_description  = blender_info['ItemInfo']

                entry.use_x_angle_property  = property_info['UseXAngleProperty']
                entry.x_angle_name          = property_info['XAnglePropertyName']
                entry.use_y_angle_property  = property_info['UseYAngleProperty']
                entry.y_angle_name          = property_info['YAnglePropertyName']
                entry.use_z_angle_property  = property_info['UseZAngleProperty']
                entry.z_angle_name          = property_info['ZAnglePropertyName']
                entry.use_x_scale_property  = property_info['UseXScaleProperty']
                entry.x_scale_name          = property_info['XScalePropertyName']
                entry.use_y_scale_property  = property_info['UseYScaleProperty']
                entry.y_scale_name          = property_info['YScalePropertyName']
                entry.use_z_scale_property  = property_info['UseZScaleProperty']
                entry.z_scale_name          = property_info['ZScalePropertyName']

    @staticmethod
    def get_list_file(game_id: str, stage_id: str, act_id: str):
        name: str = ''
        gamefolder: str = ''
        gameinfo: GameInfo = GameInfo()
        match (game_id):
            case 'SADXPC':
                gameinfo = SADXPCGameInfo()
                gamefolder = 'adv1'
            case 'SA2BPC':
                gameinfo = SA2BPCGameInfo()
                gamefolder = 'adv2'

        name = f'{gameinfo.get_objlist_name(stageid=stage_id, actid=act_id)}'
        if len(name) <= 0:
            return ''
        else:
            return os.path.join(ADDON_DIR, 'game', 'definitions', gamefolder, f'{name}.json')

    #endregion

    #region Writers
    @staticmethod
    def write_ini_file(objlist: CollectionProperty, filepath: str):
        '''Writes an INI formatted Object List file using the supplied object list.'''

    @staticmethod
    def write_json_file(objlist: CollectionProperty, filepath: str):
        '''Writes a JSON formatted Object List file using the supplied object list.'''
        data: dict = {}

        item: SASTSETDefinitionProperties
        for item in objlist:
            object_info: dict = {}

            object_info['FunctionAddress'] = item.function_address
            object_info['TaskLevel'] = SASTObjListProcessor.set_task_level(item.task_level)
            object_info['InitializationMode'] = SASTObjListProcessor.set_init_mode(item.init_mode)
            object_info['LoadAttributes'] = SASTObjListProcessor.set_attributes(item.load_attributes)
            object_info['LoadDistance'] = item.load_range

            property_info: dict = {}

            property_info['UseXAngleProperty'] = item.use_x_angle_property
            property_info['XAnglePropertyName'] = item.x_angle_name
            property_info['UseYAngleProperty'] = item.use_y_angle_property
            property_info['YAnglePropertyName'] = item.y_angle_name
            property_info['UseZAngleProperty'] = item.use_z_angle_property
            property_info['ZAnglePropertyName'] = item.z_angle_name
            property_info['UseXScaleProperty'] = item.use_x_scale_property
            property_info['XScalePropertyName'] = item.x_scale_name
            property_info['UseYScaleProperty'] = item.use_y_scale_property
            property_info['YScalePropertyName'] = item.y_scale_name
            property_info['UseZScaleProperty'] = item.use_z_scale_property
            property_info['ZScalePropertyName'] = item.z_scale_name

            blender_info: dict = {}

            blender_info['CommonName'] = item.name
            blender_info['RotationMode'] = item.rotation_order
            blender_info['AssetName'] = item.asset_name
            blender_info['AssetFile'] = item.asset_file
            blender_info['RelativeAssetFile'] = item.is_relative_file
            blender_info['ItemInfo'] = item.item_description
            blender_info['PropertyInfo'] = property_info

            entry: dict = {}
            entry['ObjectInfo'] = object_info
            entry['BlenderInfo'] = blender_info

            data[item.internal_name] = entry

        if (len(data) > 0):
            json_str: str = json.dumps(data, indent=4)
            with open(filepath, 'w') as f:
                f.write(json_str)

    #endregion

