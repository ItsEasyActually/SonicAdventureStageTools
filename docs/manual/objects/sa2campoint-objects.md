# Camera Path Points (Sonic Adventure 2)
The information here covers how the SA2 Space Camera Points are implemented within the SAST addon. For more information regarding the camera data, please [follow this](https://sadocs.unreliable.network/wiki/Sonic_Adventure_2/Camera_Information#Camera_Point_Data) link over to the SA Docs wiki.

## General Information

---

## Property Reference

### <u>Object Properties</u>

#### Position
The underlying object's real position is used for setting the point's position in the scene. This acts as the "volume" space where the player will be able to interact with the trigger.

### <u>SAST Properties</u>

#### Linked Points 1-6
These indices set which other Points the current point is linked to. A camera can have up to 6 links in total. These are not required for a Point, but they do ensure that cameras will move between active points correctly within a Camera volume when the mode is set to `Space`.

#### Direction Point
This is the link to a Point that sets the intended direction for the camera to travel. This is akin to the "next point" on a path. This typically needs to be a point that is also linked within the [Linked Points](#linked-points-1-6).

### <u>Geometry Nodes Properties</u>

#### Player Point Radius
This sets the size of the sphere volume that the player will interact with. These typically do not need to be very big.

#### Camera X, Y, and Z Point
This is the position of the Camera attached to this Point. 

#### Camera Point Radius
Retained for posterity, it appears to be a radius size for the camera within the Point. It goes unused in-game and is not available for editing.

#### Enable Player Point
When enabled, the point will be active an interactable with the player in the scene. If it is not enabled, the point is still available for linking but cannot be triggered by the player.

#### Enable Player Tracking
When a [Direction Point](#direction-point) is set, this property changes the way the cameras will move through a Point based path. When it's enabled, it will attempt to keep the player within the view of the camera and track them. When disabled, the camera will follow the Point path and not fully track the player. 

For in-game usage, you can see the setup used within Radical Highway.