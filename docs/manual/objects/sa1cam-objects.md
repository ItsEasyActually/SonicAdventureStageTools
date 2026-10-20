# CAM Objects (Sonic Adventure)
The information here covers how the SA1 Cameras are implemented within the SAST addon. For more information regarding the camera data, please [follow this](https://sadocs.unreliable.network/wiki/Sonic_Adventure/Camera_Data) link over to the SA Docs wiki.

## General Information
All camera editing can be performed under the SA Stage Tools>Object Settings panel. They will appear under in a panel named Camera Properties. The UI will update based on the selected [Camera Mode](#camera-mode). Each [Collision Shape](#collision-shape) is editable using the gizmos that appear on the object within the Viewport or in the UI for editing the camera's properties.

---

## Property Reference

### <u>Object Properties</u>

#### Position
The object's position is used to set the position of the collision volume itself. This will not move the [Camera Position](#camera-x-y-and-z-position) or [Target Position](#target-x-y-and-z-position).

### <u>SAST Properties</u>

#### Camera Mode
This sets the mode which sets how the camera will act when the player is within the volume. For ease of use, the only available camera modes within the addon are those properly supported within CAM files. Broken camera modes or those hardcoded in the game are not available for selection.

| Camera Mode | Description |
|---|---|
| Follow | Simply follows the player. Can be rotated using the triggers. Does not rotate on its own. |
| Follow (General) | Functions almost identically to the normal `Follow` cam. |
| Follow (Controllable) | Functions similarly to `Follow` except it will respect level geometry and collision. It will get stuck in walls and sometimes snap into position if the player moves away too quickly. |
| Knuckles | Follows the player and adjusts rotation based on player movement. |
| Knuckles2 | Same as `Knuckles` except it has additional angle and position calculations. |
| Maganote | Very close to the player. Attempts to calculate a little bit ahead of the player when the player moves. |
| Sonic | Follows the player and will zoom in and out based on player speed. |
| Sonic (Parameter) | Same as the `Sonic` camera except it's customizable. |
| Point | Targets a point and keeps the player between the camera and the point. Checks geometry and camera collisions. |
| Ashland | Fixed point camera, follows the player's movement while active. |
| Ashland I | Just like `Ashland` except it does not check the LR flag. |
| Fixed | Fixed camera position and target. No influence from the player. |
| Klamath | Focuses on target horizontally, keeps the player in the center of the view. Checks geometry and camera collisions. |
| Line | Follows player and has a target point. Camera doesn't move vertically. |
| Survey | Top down camera that follows the player. |
| Collision | This is used only for helping prevent the camera from phasing into level geometry. It acts as collision that only the camera will react to. |
| Leave |  |
| Avoid | Change the Camera's mode based on the avoid flag currently set. Examples of this can be found in Casinopolis being used for doorways. |
| Speed Highway Act 2 Building | Specialized camera for SH Act 2. This is included as it is a non-hardcoded special camera type used in the CAM file for this act. It should generally not be used outside of that act or a stage doing the same thing. |
| Twinkle Cart | Specialized camera for when riding in a Cart. This is included as it's used as non-hardcoded special camera type. |
| Snowboard | Specialized camera for snowboarding. It's included as it's a non-hardcoded special camera type. |
| Tornado | Specialized camera type for Windy Valley Act 2. It's included as it's a non-hardcoded special camera type. |
| New Follow | Technically broken, but it is included within some CAM files from the base game. Generally use one of the other Follow modes and not this one due to it being broken. |

#### Camera Level
This sets how the camera volume interacts with the player. Only valid options are included as selectable options. These will update based on the [Camera Mode](#camera-mode) that's currently set.

| Camera Level | Description |
|---|---|
| Normal | Standard, activates the camera when interacting with the bounds  |
| Area | Camera is only active when inside the camera bounds  |
| Compulsion | No functional difference from `Area`  |
| Collision | Pushes the camera outside of the of bounds  |

#### Adjustment Mode
Sets the method used to switch from this camera mode to another. They are currently lacking descriptions due to more research being necessary.

| Adjustment Mode | Description |
|---|---|
| No Adjustment | No adjustment period, camera will snap into the mode for the next volume. |
| Normal |  |
| Normal (S) |  |
| Slow |  |
| Slow (S) |  |
| Time |  |
| Three1 |  |
| Three1 (C) |  |
| Three2 |  |
| Three2 (C) |  |
| Three3 |  |
| Three3 (C) |  |
| Three4 |  |
| Three4 (C) |  |
| Three5 |  |
| Three5 (C) |  |
| Relative1 |  |
| Relative1 (C) |  |
| Relative2 |  |
| Relative2 (C) |  |
| Relative3 |  |
| Relative3 (C) |  |
| Relative4 |  |
| Relative4 (C) |  |
| Relative5 |  |
| Relative5 (C) |  |
| Relative6 (C) |  |
| Free Camera |  |

#### Priority
Sets the priority of the camera against other cameras. Higher values take priority.

### <u>Geometry Nodes Properties</u>

#### Collision Shape
This sets the Collision Volume Shape. Supported volume shapes are `Sphere`, `Plane`, and `Block`.

#### Collision X, Y, and Z Scale
Sets the scale of the collision volume. Each shape makes different use of each of these values, so some volumes may not have one or more of these properties available to be edited.

`Sphere` makes use of the Z scale property. `Plane` uses the X and Y scale properties. `Block` uses all three scale properties.

#### Collision X and Y Rotation
Sets the rotation of the collision volume. `Block` and `Plane` volumes make use of these. `Sphere` volumes does not.

#### Camera X, Y, and Z Position
These three properties are named for the Camera Position, but they are often used for different things depending on the [Camera Mode](#camera-mode). Please refer to the chart below for more information.

| Camera Mode | X Position | Y Position | Z Position |
|---|---|---|---| 
| Ashland | Sets Camera X Position | Sets Camera Y Position | Sets Camera Z Position |
| Ashland I | Sets Camera X Position | Sets Camera Y Position | Sets Camera Z Position |
| Fixed | Sets Camera X Position | Sets Camera Y Position | Sets Camera Z Position |
| Tornado | Unused | Sets Camera Y Position | Unused |

If a [Camera Mode](#camera-mode) is not in the list above, these properties go unused for that mode.

#### Camera X and Y Rotation
These two properties are named Camera Rotation, but they are often used for different things depending on the [Camera Mode](#camera-mode). Please refer to the chart below for more information.

| Camera Mode | X Rotation | Y Rotation |
|---|---|---|
| Klamath | Vertical Distance override, multiplied by 0.1f | Unused |
| Point | If not 0, ignores collision with geometry | Unused |
| Sonic (Parameter) | Camera Center X Angle | Camera Steady Amount |

If a [Camera Mode](#camera-mode) is not in the list above, these properties go unused for that mode.

#### Target X, Y, and Z Position
Just like the [Camera Position](#camera-x-y-and-z-position), these properties are often used for different things depending on the [Camera Mode](#camera-mode). Please refer to the chart below for more information.

| Camera Mode | X Target | Y Target | Z Target |
|---|---|---|---|
| Fixed | Sets Target X Position | Sets Target Y Position | Sets Target Z Position |
| Klamath | Sets Target X Position | Unused | Sets Target Z Position |
| Line | Sets Target X Position | Unused | Sets Target Z Position |
| Point | Sets Target X Position | Sets Target Y Position | Sets Target Z Position |
| Sonic (Parameter) | Maximum Deadzone | Minimum Distance | Maximum Distance |
| Tornado | Sets Target X Position | Sets Target Y Position | Sets Target Z Position |

If a [Camera Mode](#camera-mode) is not in the list above, these properties go unused for that mode.

#### Camera Distance
While named Camera Distance, this property is also often used for different things depending on the [Camera Mode](#camera-mode)

| Camera Mode | Camera Distance |
|---|---|
| Klamath | Sets the distance from the player, multiplied by 0.5f except vertically if the Camera X Rotation is set |
| Point | Sets the distance from the player |
| Sonic (Parameter) | Minimum Deadzone |
| Tornado | Sets a modifier for calculating distance between the Camera and Target position |

If a [Camera Mode](#camera-mode) is not in the list above, these properties go unused for that mode.