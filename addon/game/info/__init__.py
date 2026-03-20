from .game_info import GameInfo
from .sadxpc_game_info import SADXPCGameInfo
from .sa2bpc_game_info import SA2BPCGameInfo

class GameInfoManager:
    games: dict[str, GameInfo] = {
        'SADXPC': SADXPCGameInfo(),
        'SA2BPC': SA2BPCGameInfo()
    }

    @staticmethod
    def _is_valid_game(key: str):
        return (GameInfoManager.games.__contains__(key))

    @staticmethod
    def get_stage_list(key: str):
        if (GameInfoManager._is_valid_game(key)):
            return GameInfoManager.games[key].get_stage_list()
        else:
            return []

    @staticmethod
    def get_act_list(key: str, stage_id: str):
        if (GameInfoManager._is_valid_game(key)):
            return GameInfoManager.games[key].get_act_list(stage_id)
        else:
            return []

    @staticmethod
    def get_camera_mode_list(key: str):
        if (GameInfoManager._is_valid_game(key)):
            return GameInfoManager.games[key].get_camera_mode_list()
        else:
            return []

    @staticmethod
    def get_camera_level_list(key: str, camera_mode: str):
        if (GameInfoManager._is_valid_game(key)):
            return GameInfoManager.games[key].get_camera_level_list(camera_mode)
        else:
            return []

    @staticmethod
    def get_camera_adjustment_list(key: str):
        if (GameInfoManager._is_valid_game(key)):
            return GameInfoManager.games[key].get_camera_adjustment_list()
        else:
            return []