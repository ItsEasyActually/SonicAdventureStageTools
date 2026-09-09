# Editor Objects
The SAST addon comes with multiple types of objects that are utilized for editing stage related files for Sonic Adventure and its sequel.

Mesh Objects within a scene in Blender have an extended set of properties that are the foundation of Editor based objects in a scene. By default, mesh objects are set to a `None` type. Only imported objects have any other default set.

Editor Objects, in general, are powered by Geometry Nodes. As such, even if an object in a scene is a specific type of object, it will not be included in exports if the Geometry Node it requires is missing.

## General 

## Property Reference
Below is a list of the properties that are shared by all Editor Objects.

### Object Type
![Object Menu](../../_sitedev/assets/images/manual/objects/object_settings_none.png)

This sets what the object represents in the scene. 

* None: This is the default for any mesh object in the scene. 
* Set Object: This will make the object act as a SET object in the scene. This will remove any existing modifiers for the object and replace it with either the loaded Geometry Node for the SET item in slot 0 or the default set object if nothing is loaded.
* Cam Object: This will convert the object to a Camera object in the scene. This will switch context based on which game is selected as the Camera objects between both titles are not the same. 
* Camera Point: **SA2 ONLY**, This will convert the object to a Camera point in the scene.

### Export Properties
The following properties are all boolean properties that assign what files the object should be exported to. This applies to SET and CAM files at this time.

#### Sonic Adventure Export Properties
* Sonic
* Tails
* Knuckles
* Amy
* Big
* Gamma
* Last
* Eggman
* Tikal

#### Sonic Adventure 2 Export Properties
<div class="annotate" markdown>
* Single Player
* Multiplayer
* Demo (1)
</div>

1. This is only used for Camera Files.