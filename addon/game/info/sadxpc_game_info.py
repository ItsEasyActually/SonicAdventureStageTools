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

    def get_act_list(self, stage_id: str):
        match (stage_id):
            case 'StationSquare':
                return self.ss_act_list
            case 'EggCarrierExterior':
                return self.ecab_act_list
            case 'EggCarrierInterior':
                return self.ecc_act_list
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