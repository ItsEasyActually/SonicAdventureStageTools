from .sast_scene_interface import SASTSceneInterface
from .sast_object_interface import SASTObjectInterface
from .sast_settings_interface import SASTSettingsInterface
from .test_area import TestArea

to_register = [
    SASTSceneInterface,
    SASTObjectInterface,
    SASTSettingsInterface
]