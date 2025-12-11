from typing import Iterable
from datetime import datetime

class SASTLogger:
    '''Class for handling logging debug information from the addon.'''

    enabled: bool = False

    logtext = [str]

    @staticmethod
    def write(text: str = ''):
        if (len(text) > 0):
            time = datetime.now()
            SASTLogger.logtext.append(f'{time}: {text}\n')
        else:
            SASTLogger.logtext.append('\n')

    @staticmethod
    def log(text: str = ''):
        if (SASTLogger.enabled):
            SASTLogger.write(text)

    @staticmethod
    def log_lines(text: Iterable[str]):
        if (SASTLogger.enabled):
            for line in text:
                SASTLogger.write(line)

    @staticmethod
    def clear_logger():
        SASTLogger.logtext.clear()

    @staticmethod
    def enable_logger():
        SASTLogger.clear_logger()
        SASTLogger.enabled = True
        SASTLogger.log('Logger Enabled!')

    @staticmethod
    def disable_logger():
        SASTLogger.clear_logger()
        SASTLogger.enabled = False

    @staticmethod
    def save_log(path: str):
        SASTLogger.log(f'Writing to file @ {path}')
        with open(path, 'w') as file:
            file.writelines(SASTLogger.logtext)

