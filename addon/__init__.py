from .utilities.logger.sast_logger import SASTLogger
bl_info = {
	"name": "Sonic Adventure Stage Tools",
	"author": "ItsEasyActually",
	"description": "Stage Editor Toolset for Sonic Adventure and Sonic Adventure 2.",
	"version": (0, 3, 2),
	"blender": (5, 2, 0),
	"location": "Tools Sidbar",
	"category": "Tools"
}

# Credit to Justin113D for this setup.
import os
from os.path import dirname
ADDON_DIR = dirname(os.path.realpath(__file__))
ADDON_NAME = os.path.basename(ADDON_DIR)

def get_directory():
    return ADDON_DIR

def get_name():
    return ADDON_NAME
    

import bpy
from . import pynet
from . import object
from . import scene
from . import settings
from .sagpu.SASTShader import SASTShader
classes = []
classes.extend(pynet.to_register)
classes.extend(scene.cls_register)
classes.extend(object.cls_register)
classes.extend(settings.cls_register)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    SASTShader.register()

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

LOADED = True