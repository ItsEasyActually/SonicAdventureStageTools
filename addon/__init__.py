bl_info = {
	"name": "Sonic Adventure Stage Tools",
	"author": "ItsEasyActually",
	"description": "Stage Editor Toolset for Sonic Adventure and Sonic Adventure 2.",
	"version": (0, 1, 0),
	"blender": (5, 0, 0),
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

def compare_paths(a: str, b: str):
    absolute = bpy.path.abspath(b)
    absolute = os.path.abspath(absolute)
    return a == absolute

def link_assets():
    path: str = os.path.join(ADDON_DIR, 'blend', 'Cameras.blend')
    found: bool = False
    for library in bpy.data.libraries:
        if (compare_paths(path, library.filepath)):
            found = True
            break
    
    if not found:
        path = f'{path}{os.path.sep}NodeTree{os.path.sep}'
        bpy.ops.wm.link(filename='SA1CameraNode', directory=path)
        bpy.ops.wm.link(filename='SA2CameraNode', directory=path)
        bpy.ops.wm.link(filename='SA2PointNode', directory=path)
        # TODO: Add other Nodes to be linked as they are created.
    

import bpy
from . import pynet
from . import properties
from . import interface
from . import operators
from .sagpu.SASTShader import SASTShader
classes = []
classes.extend(pynet.to_register)
classes.extend(properties.to_register)
classes.extend(interface.to_register)
classes.extend(operators.to_register)

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