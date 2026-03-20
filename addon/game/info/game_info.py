class GameInfo:
    '''Base class for storing game related information.'''

    stage_list = []

    act_list = []

    character_list = []

    camera_mode_list = []

    camera_level_list = []

    camera_adjustment_list = []

    def get_stage_list(self):
        return self.stage_list

    def get_act_list(self, stage_id: str):
        return self.act_list

    def get_character_list(self):
        return self.character_list

    def get_camera_mode_list(self):
        return self.camera_mode_list

    def get_camera_level_list(self, camera_mode: str):
        return self.camera_level_list

    def get_camera_adjustment_list(self):
        return self.camera_adjustment_list