# SET Objects
SET Objects are the interactable or "dressing" objects in a level for the player, ie springs, rings, spikes, enemies, etc. While many do get shared, there is a lot of variety in how they work across both games. 

## General Info
SET Objects are all handled using a base setup from a Geometry Node. The choice to use Geometry Nodes is due to it allowing a lot of leeway in creating custom gizmos and features for a SET object to make it look correct in a scene.

---

## Property Reference

### <u>Object Properties</u>
These properties directly relate to the properties of the actual Blender Object in the scene.

#### Position
These objects will always make use of the location/position property of the object it is assigned to. Remember that in Blender, the Z and Y axis are flipped compared to the game. This means all Y axis in Blender as -Z from the game and the Z axis in Blender is the Y axis from the game.

#### Rotation
When possible, objects will almost always opt to use the real rotations on a SET Object. This is handled through an Object Definition which defines the behavior of how the SET Object is handled. 

The Rotation Order will be set to match the game when necessary and any axis not used for rotation data will have its lock enabled. If a rotation axis is locked, it will not be used to export a value to the SET file and instead the corresponding Geometry Node property will be used.

!!! warning 
    Please note that there is some lossy conversion if you swap between objects that use rotations. While the addon will attempt to preserve the rotation data when possible, it may end up lost from locking and unlocking axis or due to an object using the Geometry Node for rotation values.

!!! note
    An Object's scale values are all locked to 1.0. If an object does use scaling of some variety, that must be handled through the [Geometry Node](#geometry-node-properties) and its properties.

### <u>SAST Properties</u>
These are the extended properties that the addon creates for Blender Objects.

#### Object ID
The Object's ID from the Object List. This sets what the object actually is. When switching objects, it will attempt to match whatever the incoming Object ID is to a loaded Object Definition. If one does not exist, it will set it to the Default SET Object (the Questionmark cube) template as a fallback.

#### Override ID
Enabling this will force the [Object ID](#fallback-object-id) on export to be the ID set in the [Fallback Object ID](#override-id)

#### Fallback Object ID
A custom integer value that will be used to set the [Object ID](#fallback-object-id) in the event [Override ID](#object-id) is enabled. This will not be verified to be within the bounds of the Object IDs for a stage, so be cautious if using this. 

#### Object Flags
Flags that can be set per object. These options switch on the context of which game is set. See the table below for more info on the options.

=== "SA1"
    * High Draw Distance: Draws the object at the highest draw distance to the player.
    * Medium Draw Distance: Draws the object at a medium distance to the player.
    * Low Draw Distance: Draws the object closest distance to the player.

=== "SA2"
    * Primary SET File: This is a misnomer and the object will always be exported to the primary set file if [Dependent SET File](#dependent-set-file) is not checked.
    * Flag 1: Unknown if this flag does anything at this time.
    * Flag 2: Unknown if this flag does anything at this time.

#### Dependent SET File
This toggles the object do one of the following.

In SA1/DX, this will set the "Player Dependent" flag that is used on objects that may be dependent on specific players.

In SA2/B, this will set the file to be exported to the _u or unsubstansive layout. 

### <u>Geometry Node Properties</u>
These properties are all bound to the Geometry Node for SET Objects.

??? danger "Required Properties"
    These properties are required per any object acting like a SET Object in the scene. The Geometry Nodes are customizable and are allowed to have additional properties, but the following six must exist and need to correspond to the following Socket values for the addon to properly apply and pull the data for SET Objects.

    * Rotation X - socket_2
    * Rotation Y - socket_3
    * Rotation Z - socket_4
    * Scale X - socket_5
    * Scale Y - socket_6
    * Scale Z - socket_7

#### Rotation X
This stores the raw short value from the Rotation X field in the SET Object. This is often used when this property is not used for real rotation and is instead used as some other type of data. This is only utilized for exports when the Object's real X Rotation axis is not locked.

#### Rotation Y
This stores the raw short value from the Rotation Y field in the SET Object. This is often used when this property is not used for real rotation and is instead used as some other type of data. This is only utilized for exports when the Object's real Z Rotation axis is not locked. This slight change is due to the swapped axis between the games and Blender.

#### Rotation Z
This stores the raw short value from the Rotation Z field in the SET Object. This is often used when this property is not used for real rotation and is instead used as some other type of data. This is only utilized for exports when the Object's real Y Rotation axis is not locked. This slight change is due to the swapped axis between the games and Blender.

#### Scale X
This stores the value from the X Scale field in the SET Object and is the only way to access this property. These values regularly differ in their use in both titles. 

#### Scale Y
This stores the value from the Y Scale field in the SET Object and is the only way to access this property. These values regularly differ in their use in both titles. 

#### Scale Z
This stores the value from the Z Scale field in the SET Object and is the only way to access this property. These values regularly differ in their use in both titles.

!!! note
    Some SET objects may use the Scale Y and Scale Z axis for position data. Generally speaking, these will not reflect values that look correct in Blender due to needing to switch the axis in the Geometry Node's nodes. Please keep this in mind when you're editing values like this.

---

## Technical Info

### Filename Conventions
In SA1 and SA2, the SET file naming conventions differ due to the lack of different characters per level and SA2 not having any acts. Below is how the names are structured.

=== "SA1"
    ```
    SET[SS][AA][C].bin
    ```
    ??? note "Info"
        SS is the Stage ID, AA is the Act ID, and C is the Character ID.

        Most stages use a 2 digit identifier for the Stage ID and the Act ID. Minigames, some bosses, and Adventure Fields do not.

        For further information, you can check out info on the filenames [here](https://sadocs.unreliable.network/wiki/Sonic_Adventure/CAM_%26_SET_Files)

=== "SA2" 
    ```
    SET[SSSS][_M]_[G].bin
    ```
    ??? note "Info"
        SSSS is the Stage ID, _M is the Mode ID, and G is the Group ID.

        Stage IDs are typically a 4 digit identifier for the stage. Bosses and the Kart stages use unique markers. 

        The Mode ID will either not exist or be for Hard Mode or 2P. Bosses do not use these and only the Story Cart levels use Hard Mode.
        
        * None (e.g. SET0013_S.bin)
        * _HD (e.g. SET0013_HD_S.bin)
        * _2P (e.g. SET0013_2P_S.bin)

        Group ID denotes which grouping of objects the file is for. S for Substansive and U for Unsubstansive. These only differ in their general contents but are all treated exactly the same in-game.

        For further information, you can check out the list [here](https://sadocs.unreliable.network/wiki/Sonic_Adventure_2/Levels)