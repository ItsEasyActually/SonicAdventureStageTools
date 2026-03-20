class GameCameraInfo:
    camera_modes = []

    adjustment_mode = []

    def get_camera_modes(self):
        return self.camera_modes

    def get_adjust_modes(self):
        return self.adjustment_mode

class SADXPCCameraInfo(GameCameraInfo):
    camera_modes = [
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

    camera_levels = [
        ('Normal',      'Normal',    'Camera becomes active when the Player interacts with the volume.'),
        ('Area',        'Area',      'Camera is only active while the Player is within the volume.'),
        ('Compulsion',  'Compulsion','Functions identically to Area'),
        ('Collision',   'Collision', 'Camera is only active while the Player is within the volume, but the camera itself cannot enter the volume.')
    ]

    adjustment_mode = [
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

    def get_camera_levels(self):
        return self.camera_levels

class SA2BPCCameraInfo(GameCameraInfo):
    camera_modes = [
        ('None',        'None',         'No Camera'),
        ('User',        'User',         'User specified camera (Usage unknown)'),
        ('Follow',      'Follow',       'Follows the player, no LR controls.'),
        ('Knuckles',    'Knuckles',     'Follows the player with respect to the player movement.'),
        ('Carmel',      'Carmel',       'Similar to Knuckles but has slightly better level geometry collision detection.'),
        ('Knuckles_L',  'KnucklesL',    'Same as the Knuckles mode except it is further away from the player and turns more smoothly.'),
        ('Klamath',     'Klamath',      'Target based camera using the XY Target positions.'),
        ('Point',       'Point',        'Points to a specified target while keeping the player in view.'),
        ('Ashland',     'Ashland',      'Fixed point camera that tracks the player.'),
        ('Fix',         'Fix',          'Fixed camera that focuses on a single target. Does not move with the player.'),
        ('Space',       'Space',        'Utilizes any Points in the scene that the player enters to create a camera that moves along a spline when camera mode is active.'),
        ('Leave',       'Leave',        'Locks the camera position to where it was when volume is activated. Camera tracks player like the Ashland mode.'),
        ('GakuGaku',    'GakuGaku',     'Locks the camera position and rotation to where it was when the volume is activated.'),

        ('Collision',   'Collision',    'Camera Collider'),
        ('Colli_LR',    'Colli_LR',     'Camera Collider when using the LR triggers to rotate the camera. Does not collide with the camera unless the Triggers are pressed.'),

        ('PStone',      'PStone',       'Similar to the Leave camera except it eases to a stop while the player moves.'),
        ('Fix2',        'Fix2',         'Similar to the Leave camera except it eases to a stop while the player moves.'),
        ('SnapShot',    'SnapShot',     'Special camera that the player can control with the DPad. Not advised for use in normal play.'),
        ('Init',        'Init',         'Immediate reaction camera, follows the rotation of the joystick. Not advised for use in normal play.')    
    ]

    adjustment_mode = [
        ('None',        'None',        ''),
        ('User',        'User',        ''),
        ('Half',        'Half',        ''),
        ('Three1',      'Three1',      ''),
        ('Three2',      'Three2',      ''),
        ('Three3',      'Three3',      ''),
        ('Three4',      'Three4',      ''),
        ('Three5',      'Three5',      ''),
        ('Relative1',   'Relative1',   ''),
        ('Relative2',   'Relative2',   ''),
        ('Relative3',   'Relative3',   ''),
        ('Relative4',   'Relative4',   ''),
        ('Relative5',   'Relative5',   ''),
        ('Relative6',   'Relative6',   '')
    ]

class CameraInfo:
    '''Class with static accessors for getting a game's Camera Information'''

    entries = [
        { 'SADXPC', SADXPCCameraInfo() },
        { 'SA2BPC', SA2BPCCameraInfo() }
    ]

    @staticmethod
    def get_camera_modes(gameid: str) -> tuple:
        if CameraInfo.entries.__contains__(gameid):
            return CameraInfo.entries[gameid].camera_modes
        else:
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