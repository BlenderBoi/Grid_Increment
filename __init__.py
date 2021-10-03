
bl_info = {
    "name": "Grid Increment",
    "author": "BlenderBoi",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "description": "Increment Button for Grid Scale",
    "warning": "",
    "doc_url": "",
    "category": "Overlay",
}

import bpy
from . import Grid_Increment

modules = [Grid_Increment]


def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()

