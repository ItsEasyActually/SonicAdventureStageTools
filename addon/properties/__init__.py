from .sast_scene_properties import SASTSceneProperties
from .sast_object_properties import SASTObjectProperties
from .sast_cam_object_properties import SASTCAMObjectProperties
from .sast_point_object_properties import SASTPointObjectProperties

to_register = [
    SASTSceneProperties,
    SASTObjectProperties,
    SASTCAMObjectProperties,
    SASTPointObjectProperties
]