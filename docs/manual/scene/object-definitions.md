# SET Object Definitions
These are the properties that define an object within the Object List itself, including its information from the game directly as well as the Blender Asset information for the actual object within the scene.

---

## Property Reference

### <u>SAST Object Definition Properties - Object List Information</u>
The following properties are generally required properties for creating an Object List that is compatible with the game. This data will be filled in when importing a pre-existing Object List in the INI format from the games. 

??? note
    While it's stated this is required, all but the Function Address, and Common Name are required for generating a valid Object List INI file for use with the SA Tools. This is because the Common Name is not used by the game and the Function Address needs to be supplied as a valid function address or it needs to be a pointer to a custom function in custom Object Lists.

??? warning
    The Internal Name **can** be left blank, but it's advised to not leave this blank.


#### Internal Name
The internal name of the object. This is used by the game's object editor, but it has no real purpose in the final game. The addon uses this as a "key" for Object Lists.

#### Initialization Mode
This is the creation flag used to initialize the new Task in the game when an object is generated.

| Display label | Description | Value |
|---|---|---:|
| Task Worker   | Initializes the Task Worker of the task.      | 2 |
| Motion Worker | Initializes the Motion Worker of the task.    | 1 |
| Force Worker  | Initializes the Force Worker of the task.     | 4 |
| Any Worker    | Initializes the Any Worker of the task.       | 8 |

#### Task Level
This is the level in which the Task is created. For SET Objects, typically 2 is used and is the default.

| Display label | Description | Value |
|---|---|---:|
| Level 0 | Top-level task, used by controller-type items such as levels. | 0 |
| Level 1 | Secondary top-level task, usually used for things run by the top-level task, such as skyboxes, bosses, and some non-SET level objects. | 1 |
| **Level 2** | Primarily used for SET objects. | 2 |
| Level 3 | Sound effects and player actions; also used for some SET objects. | 3 |
| Level 4 | Effects such as explosions and lens flares. | 4 |
| Level 5 | Cutscenes and level results, where player control is mostly disabled. | 5 |
| Level 6 | Effects tied to the player and other scene entities. | 6 |
| Level 7 | Child tasks. | 7 |

#### Load Attributes
This sets how the object is setup to load within a level.

| Display label | Description | Value |
|---|---|---:|
| Load By Distance | Loads when the player is within the distance set by `Load Distance`. | 1 |
| Load Instantly | Loads instantly, regardless of the object's distance from the player. | 2 |
| Load Once | Loads instantly, but only once. | 4 |

#### Load Distance
This defines how far away the player can be before the object loads. This only applies if the `Load Attributes` property is set to `Load by Distance`.

#### Function Address
This is the address within the executable where the function for the function is stored. The address is stored in hexadecimal. For custom objects, you can leave this value set to 0.

#### Common Name
This is a more descriptive name for the object it corresponds to. This will override the `Internal Name` property in UI elements or imported objects when it's not empty.

### <u>SAST SET Definition Properties - Blender Asset Information</u>
The following properties define the Blender Asset that is loaded for the object within the scene. These also define how the object information is imported or exported to SET files.

#### Rotation Order
This defines the rotation order in which the object will use. This will enforce the object to use real rotations within the scene. If an axis is not included in the set Rotation Order, it will be locked and the data will be pulled from the Geometry Node instead of the Object's Rotation value for that axis.

!!! note
    Due to the flip of axis between the games and Blender, please note that you need to flip the Y and Z axis for defining the Rotation Order. e.g. If an Object uses Y only rotation, set the mode to Z only. For two axis rotations, flip the Z and Y axis. If the rotation order uses all three axis, keep it matching to the game's order. 

| Mode | Description |
|---|---|
| None | No rotation. |
| X Only | Object uses real rotation on the X axis only. |
| Y Only | Object uses real rotation on the Y axis only. |
| Z Only | Object uses real rotation on the Z axis only. |
| XY | Object rotates on the X and Y axis. |
| XZ | Object rotates on the X and Z axis. |
| YX | Object rotates on the Y and X axis. |
| YZ | Object rotates on the Y and Z axis. |
| ZX | Object rotates on the Z and X axis. |
| ZY | Object rotates on the Z and Y axis. |
| XYZ | Object rotates in XYZ order. |
| XZY | Object rotates in XZY order. |
| YXZ | Object rotates in YXZ order. |
| YZX | Object rotates in YZX order. |
| ZXY | Object rotates in ZXY order. |
| ZYX | Object rotates in ZYX order. |

#### Asset Name
This is the name of the object asset that will be linked into the scene. This will match the name of the object in the source blend file. 

#### Asset File
This is the path to the corresponding blend file that contains the object asset. If this is invalid or empty, the addon will import a default ? cube into the scene.

#### Is Relative File
When enabled, this sets the object to be relative to the addon itself. This should only be enabled for objects that come bundled with the addon itself. Custom objects can set the path to any file on their local system. 

#### Item Description
This is a description of the object itself. Any additional information can be placed here and it will be displayed within the Object Editor panel for the SET object when one is selected within the scene.

#### Use X Rotation Property & X Angle Property Name
These properties enable and set a custom label for the X Rotation property if the object makes use of the X Angle property within the SET Object Geometry Node. If the `Use X Rotation Property` is disabled, the Object Editor Panel will not display the property in the editor panel. If it is enabled, setting the `X Angle Property Name` will customize the label that is displayed for the property in the Object Editor Panel.

#### Use Y Rotation Property & Y Angle Property Name
These properties enable and set a custom label for the Y Rotation property if the object makes use of the Y Angle property within the SET Object Geometry Node. If the `Use Y Rotation Property` is disabled, the Object Editor Panel will not display the property in the editor panel. If it is enabled, setting the `Y Angle Property Name` will customize the label that is displayed for the property in the Object Editor Panel.

#### Use Z Rotation Property & Z Angle Property Name
These properties enable and set a custom label for the Z Rotation property if the object makes use of the Z Angle property within the SET Object Geometry Node. If the `Use Z Rotation Property` is disabled, the Object Editor Panel will not display the property in the editor panel. If it is enabled, setting the `Z Angle Property Name` will customize the label that is displayed for the property in the Object Editor Panel.

#### Use X Scale Property & X Scale Property Name
These properties enable and set a custom label for the X Scale property if the object makes use of the X Scale property within the SET Object Geometry Node. If the `Use X Scale Property` is disabled, the Object Editor Panel will not display the property in the editor panel. If it is enabled, setting the `X Scale Property Name` will customize the label that is displayed for the property in the Object Editor Panel.

#### Use Y Scale Property & Y Scale Property Name
These properties enable and set a custom label for the Y Scale property if the object makes use of the Y Scale property within the SET Object Geometry Node. If the `Use Y Scale Property` is disabled, the Object Editor Panel will not display the property in the editor panel. If it is enabled, setting the `Y Scale Property Name` will customize the label that is displayed for the property in the Object Editor Panel.

#### Use Z Scale Property & Z Scale Property Name
These properties enable and set a custom label for the Z Scale property if the object makes use of the Z Scale property within the SET Object Geometry Node. If the `Use Z Scale Property` is disabled, the Object Editor Panel will not display the property in the editor panel. If it is enabled, setting the `Z Scale Property Name` will customize the label that is displayed for the property in the Object Editor Panel.
