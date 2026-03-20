import bpy

class SASTGeonodeBase:
    '''Base class for Geometry Node integration.'''

    modifier_file: str = ''
    modifier_name: str = ''
    node: bpy.types.NodesModifier = None

    @classmethod
    def get_layout_prop(cls, prop: str):
        return f'["{prop}"]'
    
    def __init__(self, obj: bpy.types.Object):
        if (len(obj.modifiers) > 0):
            modifier: bpy.types.NodesModifier = obj.modifiers[self.modifier_name]
            if (modifier is not None):
                self.node = modifier