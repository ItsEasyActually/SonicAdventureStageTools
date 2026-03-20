from .sast_object_properties import SASTObjectProperties
from .sast_cam_object_properties import SASTCAMObjectProperties
from .sast_set_object_properties import SASTSETObjectProperties
from .sast_point_object_properties import SASTPointObjectProperties

cls_register = [
    SASTObjectProperties,
    SASTCAMObjectProperties,
    SASTSETObjectProperties,
    SASTPointObjectProperties
]