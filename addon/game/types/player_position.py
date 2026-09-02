import configparser
import os

class PlayerPosition:
    y_rot: int = 0
    x_pos: float = 0.0
    y_pos: float = 0.0
    z_pos: float = 0.0

    def __init__(self, yang: int, xpos: float, ypos: float, zpos: float) -> None:
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

    @staticmethod
    def sa2_startpositions(filepath: str, key: str) -> dict:
        '''Returns a dict of PlayerPositions using the specified file and key.'''
        config: configparser.ConfigParser = PlayerPosition.load_file(filepath)

    @staticmethod
    def sa2_endpositions(filepath: str, key: str) -> dict:
        '''Returns a dict of PlayerPositions using the specified file and key.'''
        config: configparser.ConfigParser = PlayerPosition.load_file(filepath)

    @staticmethod
    def sa2_missionpositions(filepath: str, key: str) -> dict:
        '''Returns a dict of PlayerPositions using the specified file and key.'''
        config: configparser.ConfigParser = PlayerPosition.load_file(filepath)

    @staticmethod
    def sa2_intropositions(filepath: str, key: str) -> dict:
        '''Returns a dict of PlayerPositions using the specified file and key.'''
        config: configparser.ConfigParser = PlayerPosition.load_file(filepath)