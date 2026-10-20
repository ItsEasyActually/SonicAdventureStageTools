# CAM Objects (Sonic Adventure 2)
The information here covers how the SA2 Camera Volumes are implemented within the SAST addon. For more information regarding the camera data, please [follow this](https://sadocs.unreliable.network/wiki/Sonic_Adventure_2/Camera_Information) link over to the SA Docs wiki.


## General Information

---

## Property Reference

### <u>Object Properties</u>

#### Position
The object's position is used to set the position of the collision volume itself. This will not move the [Camera Position](#camera-x-y-and-z-position) or [Target Position](#target-x-y-and-z-position).

### <u>SAST Properties</u>

#### Camera Mode
This sets the mode which sets how the camera will act when the player is within the volume.

| Camera Mode | Description                                                                                                                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None        | Has no impact if the player enters the volume.                                                                                                                                                                                                 |
| Follow      | Follows the player without any rotation. The camera will be locked to the direction it was facing when the player enters the volume. The camera will not respect Level Geometry and will clip into it.                                         |
| Knuckles    | Often used as the default camera mode. It follows the player and rotates based on player movement. It also respects level geometry and collision.                                                                                              |
| Camel       | Similar to the Knuckles camera mode, but it has better player tracking when turning corners and often better respects the level geometry.                                                                                                      |
| KnucklesL   | Same as Knuckles but it's further from the player.                                                                                                                                                                                             |
| Klamath     | This mode focuses on a point along the same XZ plane as the camera itself.                                                                                                                                                                     |
| Point       | The camera will point to at a target while keeping the player within the camera view.                                                                                                                                                          |
| Ashland     | The camera will stay in a fixed location while tracking the player.                                                                                                                                                                            |
| Fix         | Camera is in a fixed position and points to a target. It will not track the player in the view.                                                                                                                                                |
| Space       | This mode utilizes the [Camera Points](sa2campoint-objects.md). Please see that page for more information.                                                                                                                                    |
| Leave       | When active, the camera will lock itself to its last set location and track the player similar to the Ashland camera.                                                                                                                          |
| GakuGaku    | Similar to Leave except the camera gets locked for both position and rotation, and it will not track the player when the volume is active.                                                                                                     |
| Collision   | This acts as a collider for the camera itself rather than an active camera mode.                                                                                                                                                               |
| Colli_LR    | Another volume collider but this one is only active when the player is using the L and R triggers. Otherwise it is ignored.                                                                                                                    |
| PStone      | Similar to the GakuGaku camera mode, but the camera slowly settles into place when the volume is active. It will keep tracking the player.                                                                                                     |
| Fix2        | Similar to PStone, but it will stop in a fixed position and will not track the player once it stops moving.                                                                                                                                    |
| SnapShot    | Player controlled camera mode for taking screenshots. Use the DPad to move the camera, L and R triggers move the camera up and down. Holding Start and using the left joystick will rotate the camera. This is not recommended for normal use. |
| Init        | Extremely snappy movements when active. It will rotate at the same rate the player rotates. This camera is not recommended for normal use.                                                                                                     |

#### Adjustment Mode
Sets the method used to switch from this camera mode to another. Documentation on these modes is not complete and will be updated as more research is done on how these all work.

| Adjustment Mode | Description |
|-----------------|-------------|
| None            |             |
| User            |             |
| Half            |             |
| Three1          |             |
| Three2          |             |
| Three3          |             |
| Three4          |             |
| Three5          |             |
| Relative1       |             |
| Relative2       |             |
| Relative3       |             |
| Relative4       |             |
| Relative5       |             |
| Relative6       |             |

#### Priority
Sets the priority of the camera against other cameras. Higher values take priority.

#### Extended Integer Properties 1-8
These cameras have additional properties stored within an array of 8 integer values. Below is a table for [Camera Modes](#camera-mode) that are known to use which values. This information is still a work in progress so the information here may change at a later date. If a specific mode is not present, that means the current understanding is that it does not utilize these properties.

| Camera Mode | Property 1                                                                             | Property 2 | Property 3 | Property 4 | Property 5 | Property 6 | Property 7 | Property 8 |
|-------------|----------------------------------------------------------------------------------------|------------|------------|------------|------------|------------|------------|------------|
| Ashland     | Sets the Camera FOV, treated as a direct Degree value rather than BAMS (e.g. 90 = 90d) | Unused     | Unused     | Unused     | Unused     | Unused     | Unused     | Unused     |

#### Extended Float Properties 1-8
These cameras have additional properties stored within an array of 8 float values. Below is a table for [Camera Modes](#camera-mode) that are known to use which values. This information is still a work in progress so the information here may change at a later date. If a specific mode is not present, that means the current understanding is that it does not utilize these properties.

| Camera Mode | Property 1         | Property 2                 | Property 3 | Property 4 | Property 5 | Property 6 | Property 7 | Property 8 |
|-------------|--------------------|----------------------------|------------|------------|------------|------------|------------|------------|
| Klamath     | Distance to Player | Additional Vertical Height | Unused     | Unused     | Unused     | Unused     | Unused     | Unused     |
| Point       | Distance to Player | Additional Vertical Height | Unused     | Unused     | Unused     | Unused     | Unused     | Unused     |

### <u>Geometry Nodes Properties</u>

#### Collision Shape
This sets the shape of the volume. Available types are `Sphere`, `Plane`, and `Block`.

#### Collision X, Y, and Z Rotation
The collision volume is able to be rotated on all three axis. This only applies to `Plane` and `Block` volume shapes as the `Sphere` shape does not use rotation.

#### Collision X, Y, and Z Scale
This sets the scale of the volume itself. Each shape uses different values for setting their scale. `Sphere` uses the Z scale value, `Plane` uses X and Y. `Block` makes use of all three.

#### Camera X, Y, and Z Rotation
These properties do exist per camera, but most [Camera Modes](#camera-mode) do not use them. `Ashland` is the only one known to use them.

#### Camera X, Y, and Z Position
These properties do exist per camera, but many [Camera Modes](#camera-mode) do not use them. `Fix` and `Ashland` are the only two camera types that use them.

#### Target X, Y, and Z Position
These properties do exist per camera, but many [Camera Modes](#camera-mode) do not use them. `Fix` and `Point` make use of all three while `Klamath` makes use of the X and Z properties.