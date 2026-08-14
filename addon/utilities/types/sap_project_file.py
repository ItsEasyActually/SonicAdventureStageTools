import xml.etree.cElementTree as et
import os

class SAPProjectFile:
    '''Python version of the SAP Project File.'''

    game_type: str = 'NONE'
    project_folder: str
    project_system_folder: str

    def readfile(self, path: str):
        if (os.path.exists(path)):
            file = et.parse(path)
            root = file.getroot()

            gameinfo = root.find('GameInfo')
            self.game_type = gameinfo.get('gameName')
            self.project_folder = os.path.join(os.path.dirname(path), gameinfo.get('projectFolder'))
            self.project_system_folder = os.path.join(self.project_folder, gameinfo.get('gameDataFolder'))