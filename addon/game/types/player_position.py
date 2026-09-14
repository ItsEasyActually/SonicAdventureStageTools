import configparser
import os
from sys import ps1

class PlayerPosition:
    y_rot: int = 0
    x_pos: float = 0.0
    y_pos: float = 0.0
    z_pos: float = 0.0

    def __init__(self, type: str, yang: int, xpos: float, ypos: float, zpos: float) -> None:
        self.y_rot = yang
        self.x_pos = xpos
        self.y_pos = ypos
        self.z_pos = zpos

    def sa1_writeposition(self, filepath: str, key: str):
        '''Write Start Positions to the supplied filepath. If the file exists, it will be updated.'''
        pass

    def sa2_writestartpositions(self, filepath: str, key: str):
        '''Write Start Positions to the supplied filepath. If the file exists, it will be updated.'''
        pass

    def sa2_writeendpositions(self, filepath: str, key: str):
        '''Write End Positions to the supplied filepath. If the file exists, it will be updated.'''
        pass

    def sa2_writemissionpositions(self, filepath: str, key: str):
        '''Write Mission End Positions to the supplied filepath. If the file exists, it will be updated.'''
        pass

    def sa2_writeintropositions(self, filepath: str, key: str):
        '''Write Intro Positions to the supplied filepath. If the file exists, it will be updated.'''
        pass

    @staticmethod
    def load_file(filepath: str) -> configparser.ConfigParser | None:
        if (os.path.exists(filepath)):
            config: configparser.ConfigParser = configparser.ConfigParser()
            config.read(filepath)
            return config
        else:
            return None

    @staticmethod
    def sa1_startposition(filepath: str, key: str) -> PlayerPosition:
        '''Returns a PlayerPosition using the specified file and key.'''
        config: configparser.ConfigParser = PlayerPosition.load_file(filepath)
        if (config == None):
            return None

        position: [str] = config.get(key, 'Position').split(',')
        rotation: int = config.getint(key, 'YRotation', fallback=0)

        return PlayerPosition(rotation, float(position[0]), float(position[1]), float(position[2]))        

    @staticmethod
    def sa2_positions(filepath: str, key: str) -> dict[str, PlayerPosition]:
        '''Returns a dict of PlayerPositions using the specified file and key.'''
        config: configparser.ConfigParser = PlayerPosition.load_file(filepath)
        output: dict = dict[str, PlayerPosition]()

        sp_pos: [str] = config.get(key, 'Position').split(',')
        sp_pp = PlayerPosition(config.getint(key, 'YRotation', fallback=0), float(sp_pos[0]), float(sp_pos[1]), float(sp_pos[2]))

        p1_pos: [str] = config.get(key, 'P1Position').split(',')
        p1_pp = PlayerPosition(config.getint(key, 'P1YRotation', fallback=0), float(p1_pos[0]), float(p1_pos[1]), float(p1_pos[2]))

        p2_pos: [str] = config.get(key, 'P2Position').split(',')
        p2_pp = PlayerPosition(config.getint(key, 'P2YRotation', fallback=0), float(p2_pos[0]), float(p2_pos[1]), float(p2_pos[2]))

        output['SinglePlayer'] = sp_pp
        output['Player1'] = p1_pp
        output['Player2'] = p2_pp

        return output

    @staticmethod
    def sa2_missionpositions(filepath: str, key: str) -> dict[str, PlayerPosition]:
        '''Returns a dict of Mission2 and Mission3 positions. Also used for P1 and P2 Intro positions (M2=P1, M3=P2).'''
        config: configparser.ConfigParser = PlayerPosition.load_file(filepath)
        output: dict = dict[str, PlayerPosition]()

        p1_pos: [str] = config.get(key, 'Mission2Position').split(',')
        p1_pp = PlayerPosition(config.getint(key, 'Mission2YRotation', fallback=0), float(p1_pos[0]), float(p1_pos[1]), float(p1_pos[2]))

        p2_pos: [str] = config.get(key, 'Mission3Position').split(',')
        p2_pp = PlayerPosition(config.getint(key, 'Mission3YRotation', fallback=0), float(p2_pos[0]), float(p2_pos[1]), float(p2_pos[2]))

        output['Mission2'] = p1_pp
        output['Mission3'] = p2_pp

        return output