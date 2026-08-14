from .sast_scene_interface import SASTSceneInterface
from .sast_objlist_interface import (
    SAST_UL_objlist
)
from .sast_tools_interface import SASTSceneToolsInterface

cls_register = [
    SASTSceneInterface,
    SAST_UL_objlist,
    SASTSceneToolsInterface
]