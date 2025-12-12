from .sast_scene_properties import SASTSceneProperties
from .sast_object_properties import SASTObjectProperties
from .sast_cam_object_properties import SASTCAMObjectProperties
from .sast_point_object_properties import SASTPointObjectProperties
from .sast_settings_properties import SASTSettingsProperties

to_register = [
    SASTSettingsProperties,
    SASTSceneProperties,
    SASTObjectProperties,
    SASTCAMObjectProperties,
    SASTPointObjectProperties
]