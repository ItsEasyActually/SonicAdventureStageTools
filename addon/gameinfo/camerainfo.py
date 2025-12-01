class CameraInfo:
    '''Class with static accessors for getting a game's Camera Information'''

    #region SA1 Information
    sa1_cameramodes = [
        ('Follow',      'Follow',                       'Follows the Player, can be rotated using the triggers.'),
        ('Knuckles',    'Knuckles',                     'Follows the Player and adjusts the rotation based on the player movement.'),
        ('Knuckles2',   'Kncukles2',                    'Same as Knuckles but with some additional calculations'),
        ('Magonote',    'Magonote',                     'Close camera to the Player, will calculate its focal point to just ahead of the Player.'),
        ('Sonic',       'Sonic',                        'Follows the Player with respect to their rotation. Zooms out based on Player speed.'),
        ('Ashland',     'Ashland',                      'Fixed point that focuses on the Player when active.'),
        ('AshlandI',    'Ashland I',                    'Same as Ashland without the LR controls check.'),
        ('Fixed',       'Fixed',                        'Fixed camera position that will focus on the target point.'),
        ('Klamath',     'Klamath',                      'Focuses on a target in the horizontal plane while keeping the Player within the center of the view.'),
        ('Line',        'Line',                         'Follows the player similarly to Kalamth, utilizes a target point on the horizontal plane.'),
        ('NewFollow',   'New Follow',                   ''),
        ('Point',       'Point',                        'Camera focuses on a target point while keeping the player in the center of the view.'),
        ('SonicP',      'Sonic (Parameter)',            'Same as Sonic except the parameters can be customized.'),
        ('Building',    'Speed Highway Act 2 Building', 'Used in Speed Highway Act 2.'),
        ('Cart',        'Twinkle Cart',                 'Used in Twinkle Park Act 1 and Twinkle Circuit.'),
        ('FollowG',     'Follow (General)',             'Functions identically to the Follow mode.'),
        ('LeftRight',   'Follow (Controllable)',        'Functions the same as Follow except it has additional checks for level geometry and object collision.'),
        ('Collision',   'Collision',                    'Acts as a collision obstacle to prevent the camera from entering the volume.'),
        ('Snowboard',   'Snowboard',                    'Used for Snowboarding in game (Icecap Act 3 and Sandboarding).'),
        ('Survey',      'Survey',                       'Top down camera view of the player in a level.'),
        ('Tornado',     'Tornado',                      'Used in Windy Valley Act 2, The Tornado.'),
        ('Leave',       'Leave',                        ''),
        ('Avoid',       'Avoid',                        'Changes the camera mode based on what the current avoid flag is set to.')
    ]

    sa1_cameralevels = [
        ('Normal',      'Normal',    'Camera becomes active when the Player interacts with the volume.'),
        ('Area',        'Area',      'Camera is only active while the Player is within the volume.'),
        ('Compulsion',  'Compulsion','Functions identically to Area'),
        ('Collision',   'Collision', 'Camera is only active while the Player is within the volume, but the camera itself cannot enter the volume.')
    ]

    sa1_adjustmentmodes = [
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
    #endregion

    #region SA2 Information
    sa2_cameramodes = [
        ('None',        'None',         ''),
        ('User',        'User',         ''),
        ('Follow',      'Follow',       ''),
        ('Knuckles',    'Knuckles',     ''),
        ('Editor',      'Editor',       ''),
        ('Editor2',     'Editor2',      ''),
        ('SnapShot',    'SnapShot',     ''),
        ('Klamath',     'Klamath',      ''),
        ('Point',       'Point',        ''),
        ('Ashland',     'Ashland',      ''),
        ('Fix',         'Fix',          ''),
        ('Leave',       'Leave',        ''),
        ('Space',       'Space',        ''),
        ('Carmel',      'Carmel',       ''),
        ('Motion',      'Motion',       ''),
        ('BossInit',    'BossInit',     ''),
        ('BossPoint',   'BossPoint',    ''),
        ('Collision',   'Collision',    ''),
        ('PStone',      'PStone',       ''),
        ('Init',        'Init',         ''),
        ('EasySet',     'EasySet',      ''),
        ('BossKlamath', 'BossKlamath',  ''),
        ('GakuGaku',    'GakuGaku',     ''),
        ('Knuckles_L',  'KnucklesL',    ''),
        ('Fix2',        'Fix2',         ''),
        ('PStone2',     'PStone2',      ''),
        ('SS',          'SS',           ''),
        ('Colli_LR',    'Colli_LR',     '')
    ]

    sa2_adjustmentmodes = [
        ('None','None',             ''),
        ('User','User',             ''),
        ('Half','Half',             ''),
        ('Three1','Three1',         ''),
        ('Three2','Three2',         ''),
        ('Three3','Three3',         ''),
        ('Three4','Three4',         ''),
        ('Three5','Three5',         ''),
        ('Relative1','Relative1',   ''),
        ('Relative2','Relative2',   ''),
        ('Relative3','Relative3',   ''),
        ('Relative4','Relative4',   ''),
        ('Relative5','Relative5',   ''),
        ('Relative6','Relative6',   '')
    ]
    #endregion

    @staticmethod
    def get_camera_modes(gameid: str) -> tuple:
        match (gameid):
            case 'SADXPC':
                return CameraInfo.sa1_cameramodes
            case 'SA2BPC':
                return CameraInfo.sa2_cameramodes
            case _:
                return []

    @staticmethod
    def get_camera_levels(cameramode: str) -> tuple:
        items = []
        accl = {'Follow','Knuckles','Knuckles2','Magonote','Sonic','Ashland','AshlandI','Avoid'}
        ac = {'Fixed','Klamath','Point','SonicP'}
        a = {'Line', 'FollowG'}
        
        if (cameramode in accl):
            items.extend(CameraInfo.sa1_cameralevels)
        elif (cameramode in ac):
            items.append(CameraInfo.sa1_cameralevels[0])
            items.append(CameraInfo.sa1_cameralevels[1])
            items.append(CameraInfo.sa1_cameralevels[2])
        elif (cameramode in a):
            items.append(CameraInfo.sa1_cameralevels[0])
            items.append(CameraInfo.sa1_cameralevels[1])
        else:
            items.append(CameraInfo.sa1_cameralevels[0])

        return items

    @staticmethod
    def get_adjustment_modes(gameid: str) -> tuple:
        match (gameid):
            case 'SADXPC':
                return CameraInfo.sa1_adjustmentmodes
            case 'SA2BPC':
                return CameraInfo.sa2_adjustmentmodes
            case _:
                return []