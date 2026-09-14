from .game_info import GameInfo

class SADXPCGameInfo(GameInfo):
    '''Game Info for SADXPC'''

    stage_list = [
        ('EmeraldCoast',        'Emerald Coast',                ''),
        ('WindyValley',         'Windy Valley',                 ''),
        ('TwinklePark',         'Twinkle Park',                 ''),
        ('SpeedHighway',        'Speed Highway',                ''),
        ('RedMountain',         'Red Mountain',                 ''),
        ('SkyDeck',             'Sky Deck',                     ''),
        ('LostWorld',           'Lost World',                   ''),
        ('Icecap',              'Icecap',                       ''),
        ('Casinopolis',         'Casinpolis',                   ''),
        ('FinalEgg',            'Final Egg',                    ''),
        ('HotShelter',          'Hot Shelter',                  ''),
        ('Chaos0',              'Chaos 0',                      ''),
        ('Chaos2',              'Chaos 2',                      ''),
        ('Chaos4',              'Chaos 4',                      ''),
        ('Chaos6',              'Chaos 6',                      ''),
        ('Chaos7',              'Perfect Chaos',                ''),
        ('EggHornet',           'Egg Hornet',                   ''),
        ('EggWalker',           'Egg Walker',                   ''),
        ('EggViper',            'Egg Viper',                    ''),
        ('ZERO',                'ZERO',                         ''),
        ('E101',                'E-101 Beta',                   ''),
        ('E101R',               'E-101r mkII',                  ''),
        ('StationSquare',       'Station Square',               ''),
        ('EggCarrierExterior',  'Egg Carrier (Exterior)',       ''),
        ('EggCarrierInterior',  'Egg Carrier (Interior)',       ''),
        ('MysticRuins',         'Mysic Ruins',                  ''),
        ('ThePast',             'The Past',                     ''),
        ('TwinkleCircuit',      'Twinkle Circuit',              ''),
        ('Sandhill',            'Sandhill',                     ''),
        ('SkyChase',            'Sky Chase',                    ''),
        ('HedgehogHammer',      'Hedgehog Hammer',              ''),
        ('ChaoGardenSS',        'Chao Garden (Station Square)', ''),
        ('ChaoGardenEC',        'Chao Garden (Egg Carrier)',    ''),
        ('ChaoGardenMR',        'Chao Garden (Mystic Ruins)',   ''),
        ('ChaoRace',            'Chao Race',                    '')
    ]

    act_list = [
        ('Act1','Act 1',''),
        ('Act2','Act 2',''),
        ('Act3','Act 3',''),
        ('Act4','Act 4',''),
        ('Act5','Act 5',''),
        ('Act6','Act 6','')
    ]

    ss_act_list = [
        ('Act1','City Hall',            ''),
        ('Act2','Casino Area',          ''),
        ('Act3','Sewer Area',           ''),
        ('Act4','Main Area',            ''),
        ('Act5','Hotel',                ''),
        ('Act6','Twinkle Park Entrance','')
    ]

    ecab_act_list = [
        ('Act1','Ammuniation Room',     ''),
        ('Act2','Main Hall',            ''),
        ('Act3','Hedgehog Hammer Area', ''),
        ('Act4','Prison Cells',         ''),
        ('Act5','Resevoir Room',        ''),
        ('Act6','Teleporter Room',      '')
    ]

    ecc_act_list = [
        ('Act1','Main Deck',                ''),
        ('Act2','Transformed Deck (Front)', ''),
        ('Act3','Transformed Deck (Back)',  ''),
        ('Act4','Captain Seat',             ''),
        ('Act5','Private Room',             ''),
        ('Act6','Pool',                     '')
    ]

    mr_act_list = [
        ('Act1','Main Area',        ''),
        ('Act2','Angel Island',     ''),
        ('Act3','Mystic Jungle',    ''),
        ('Act4','Final Egg Base',   ''),
        ('Act5','Act 5',            ''),
        ('Act6','Act 6',            '')
    ]

    past_act_list = [
        ('Act1','Village',                          ''),
        ('Act2','Master Emerald Shrine',            ''),
        ('Act3','Master Emerald Shrine (On Fire)',  ''),
        ('Act4','Act 4',                            ''),
        ('Act5','Act 5',                            ''),
        ('Act6','Act 6',                            '')
    ]

    character_list = [
        ('Sonic',       'Sonic the Hedgehog',   ''),
        ('Miles',       'Miles Tails Prower',   ''),
        ('Knuckles',    'Knuckles the Echidna', ''),
        ('Amy',         'Amy Rose',             ''),
        ('E102',        'E-102 Gamma',          ''),
        ('Big',         'Big the Cat',          ''),
        ('Tikal',       'Tikal',                ''),
        ('Eggman',      'Eggman',               ''),
        ('Last',        'Last Story',           '')
    ]

    camera_mode_list = [
        ('Follow',      'Follow',                       'Follows the Player, can be rotated using the triggers.'),
        ('FollowG',     'Follow (General)',             'Functions identically to the Follow mode.'),
        ('LeftRight',   'Follow (Controllable)',        'Functions the same as Follow except it has additional checks for level geometry and object collision.'),
        ('Knuckles',    'Knuckles',                     'Follows the Player and adjusts the rotation based on the player movement.'),
        ('Knuckles2',   'Knuckles2',                    'Same as Knuckles but with some additional calculations'),
        ('Magonote',    'Magonote',                     'Close camera to the Player, will calculate its focal point to just ahead of the Player.'),
        ('Sonic',       'Sonic',                        'Follows the Player with respect to their rotation. Zooms out based on Player speed.'),
        ('SonicP',      'Sonic (Parameter)',            'Same as Sonic except the parameters can be customized.'),
        ('Point',       'Point',                        'Camera focuses on a target point while keeping the player in the center of the view.'),
        ('Ashland',     'Ashland',                      'Fixed point that focuses on the Player when active.'),
        ('AshlandI',    'Ashland I',                    'Same as Ashland without the LR controls check.'),
        ('Fixed',       'Fixed',                        'Fixed camera position that will focus on the target point.'),
        ('Klamath',     'Klamath',                      'Focuses on a target in the horizontal plane while keeping the Player within the center of the view.'),
        ('Line',        'Line',                         'Follows the player similarly to Kalamth, utilizes a target point on the horizontal plane.'),
        
        ('Survey',      'Survey',                       'Top down camera view of the player in a level.'),

        ('Collision',   'Collision',                    'Volume Collider.'),

        ('Leave',       'Leave',                        ''),
        ('Avoid',       'Avoid',                        'Changes the camera mode based on what the current avoid flag is set to.'),
        ('Building',    'Speed Highway Act 2 Building', 'Used in Speed Highway Act 2.'),
        ('Cart',        'Twinkle Cart',                 'Used in Twinkle Park Act 1 and Twinkle Circuit.'),
        ('Snowboard',   'Snowboard',                    'Used for Snowboarding in game (Icecap Act 3 and Sandboarding).'),
        ('Tornado',     'Tornado',                      'Used in Windy Valley Act 2, The Tornado.'),
        ('NewFollow',   'New Follow',                   'DO NOT USE')
    ]

    camera_level_list = [
        ('Normal',      'Normal',    'Camera becomes active when the Player interacts with the volume.'),
        ('Area',        'Area',      'Camera is only active while the Player is within the volume.'),
        ('Compulsion',  'Compulsion','Functions identically to Area'),
        ('Collision',   'Collision', 'Camera is only active while the Player is within the volume, but the camera itself cannot enter the volume.')
    ]

    camera_adjustment_list = [
        ('None',         'No Adjustment',   ''),
        ('Normal',       'Normal',          ''),
        ('NormalS',      'Normal (S)',      ''),
        ('Slow',         'Slow',            ''),
        ('SlowS',        'Slow (S)',        ''),
        ('Time',         'Time',            ''),
        ('Three1',       'Three1',          ''),
        ('Three1C',      'Three1 (C)',      ''),
        ('Three2',       'Three2',          ''),
        ('Three2C',      'Three2 (C)',      ''),
        ('Three3',       'Three3',          ''),
        ('Three3C',      'Three3 (C)',      ''),
        ('Three4',       'Three4',          ''),
        ('Three4C',      'Three4 (C)',      ''),
        ('Three5',       'Three5',          ''),
        ('Three5C',      'Three5 (C)',      ''),
        ('Relative1',    'Relative1',       ''),
        ('Relative1C',   'Relative1 (C)',   ''),
        ('Relative2',    'Relative2',       ''),
        ('Relative2C',   'Relative2 (C)',   ''),
        ('Relative3',    'Relative3',       ''),
        ('Relative3C',   'Relative3 (C)',   ''),
        ('Relative4',    'Relative4',       ''),
        ('Relative4C',   'Relative4 (C)',   ''),
        ('Relative5',    'Relative5',       ''),
        ('Relative5C',   'Relative5 (C)',   ''),
        ('Relative6C',   'Relative6 (C)',   ''),
        ('FreeCamera',   'Free Camera',     '')
    ]

    objlists: dict = {
        'EmeraldCoast':         'stg01',
        'WindyValley':          'stg02',
        'TwinklePark':          'stg03',
        'SpeedHighway':         'stg04',
        'RedMountain':          'stg05',
        'SkyDeck':              'stg06',
        'LostWorld':            'stg07',
        'Icecap':               'stg08',
        'Casinopolis':          'stg09',
        'FinalEgg':             'stg10',
        'HotShelter':           'stg12',
        'Chaos0':               'boss_chaos0',
        'Chaos2':               'boss_chaos2',
        'Chaos4':               'boss_chaos4',
        'Chaos6':               'boss_chaos6',
        'Chaos7':               'boss_chaos7',
        'EggHornet':            'boss_egm1',
        'EggWalker':            'boss_egm2',
        'EggViper':             'boss_egm3',
        'ZERO':                 'boss_robo',
        'E101':                 'boss_e101',
        'E101R':                'boss_e101r',
        'StationSquare':        'adv00',
        'EggCarrierExterior':   'adv01ab',
        'EggCarrierInterior':   'adv01c',
        'MysticRuins':          'adv02',
        'ThePast':              'adv03',
        'TwinkleCircuit':       'minicart',
        'Sandhill':             'sandboard',
        'HedgehogHammer':       'stg00',
        'SkyChase':             'shooting',
        'ChaoRace':             'chao_race'        
    }

    actids: dict = {
        'Act1': '0',
        'Act2': '1',
        'Act3': '2',
        'Act4': '3',
        'Act5': '4',
        'Act6': '5'
    }

    projectfolders: dict = {
        'Sonic':    'sonic',
        'Miles':    'miles',
        'Knuckles': 'knuckles',
        'Amy':      'amy',
        'Big':      'big',
        'E102':     'e102',
        'Tikal':    'tikal',
        'Eggman':   'eggman',

        'EmeraldCoast': 'stg01_beach',
        'WindyValley':  'stg02_windy',
        'TwinklePark':  'stg03_twinkle',
        'SpeedHighway': 'stg04_highway',
        'RedMountain':  'stg05_mountain',
        'SkyDeck':      'stg06_skydeck',
        'LostWorld':    'stg07_ruin',
        'Icecap':       'stg08_icecap',
        'Casinopolis':  'stg09_casino',
        'FinalEgg':     'stg10_finalegg',
        'HotShelter':   'stg12_hotshelter',

        'Chaos0':       'boss00_chaos0',
        'Chaos2':       'boss_chaos2',
        'Chaos4':       'boss_chaos4',
        'Chaos6':       'boss_chaos6',
        'Chaos7':       'boss_chaos7',
        'EggHornet':    'bossegm1',
        'EggWalker':    'bossegm2',
        'EggViper':     'bossegm3',
        'ZERO':         'bossrobo',
        'E101':         'boss_e101',
        'E101R':        'boss_e101r',

        'StationSquare':        'adv00_stationsquare',
        'EggCarrierExterior':   'adv01_eggcarrierab',
        'EggCarrierInterior':   'adv01_eggcarrierc',
        'MysticRuins':          'adv02_mysticruins',
        'ThePast':              'adv03_past',

        'TwinkleCircuit':   'mini_cart',
        'Sandhill':         'sandboarding',
        'SkyChase':         'shooting',
        'HedgehogHammer':   'stg00_practice',

        'ChaoGardenSS': 'stg_garden00_ss',
        'ChaoGardenEC': 'stg_garden01_ec',
        'ChaoGardenMR': 'stg_garden02_mr',
        'ChaoRace':     'stg_race1',

        'Act1': 'act01',
        'Act2': 'act02',
        'Act3': 'act03',
        'Act4': 'act04',
        'Act5': 'act05',
        'Act6': 'act06'
    }

    def get_act_list(self, stage_id: str):
        match (stage_id):
            case 'StationSquare':
                return self.ss_act_list
            case 'EggCarrierExterior':
                return self.ecc_act_list
            case 'EggCarrierInterior':
                return self.ecab_act_list
            case 'MysticRuins':
                return self.mr_act_list
            case 'ThePast':
                return self.past_act_list
            case _:
                return self.act_list

    def get_camera_level_list(self, camera_mode: str):
        items = []
        match (camera_mode):
            case 'Follow' |'Knuckles' | 'Knuckles2' | 'Magonote' | 'Sonic' | 'Ashland' | 'AshlandI' |'Avoid':
                items.extend(self.camera_level_list)
            case 'Fixed' | 'Klamath' | 'Point' | 'SonicP':
                items.append(self.camera_level_list[0])
                items.append(self.camera_level_list[1])
                items.append(self.camera_level_list[2])
            case 'Line' | 'FollowG':
                items.append(self.camera_level_list[0])
                items.append(self.camera_level_list[1])
            case _:
                items.append(self.camera_level_list[0])

        return items

    def get_objlist_name(self, stageid: str, actid: str):
        extension: str = ''
        match (stageid):
            case 'ChaoGardenSS' | 'ChaoGardenEC' | 'ChaoGardenMR':
                raise Exception('Chao Gardens are not supported for SET Import.')
            case _:
                if (stageid == 'HotShelter'):
                    extension = '_'
                    match (actid):
                        case 'Act2':
                            extension += '02'
                        case 'Act3':
                            extension += '03'
                        case 'Act4':
                            extension += '04'
                        case 'Act1' | _:
                            extension += '01'

        return f'{self.objlists[stageid]}{extension}'

    def get_stage_and_act_key(self, stageid: str, actid: str)-> str:
        return f'{stageid} {self.actids[actid]}'

    def get_project_folder(self, type: str, item: str, suffix: str = '') -> str:
        folderpath: str = ''
        item: str = f'{self.projectfolders[item]}\\'
        if (len(suffix) > 0):
            item += f'{self.projectfolders[suffix]}\\'
        match (type):
            case 'Character':
                folderpath = f'figure\\{item}'
            case 'Stage':
                folderpath= item

        return folderpath

