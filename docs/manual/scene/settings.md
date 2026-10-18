# Scene Properties
These are properties that are directly tied to the current scene. 

## General Information
Scene properties are found in the SA Stage Tools>Scene Settings & Properties panel within Blender. These settings are scene independent meaning you will need to update your settings if/when you make a new scene. 

---
## Property Reference

### <u>SAST Scene Properties</u>

#### Editor Mode
This defines the operation mode for the addon. 

When set to `Automatic Mode`, the addon can automatically import and export to preset directories. These are set in the [`Load Directory`](#load-directory) and [`Save Directory`](#save-directory). This will handle all filenames properly.

When set to `Manual Mode`, importing and exporting is all managed by the user.

#### Game ID
This defines the game which sets additional setup in the addon, notably some of the additional available tools and how to handle camera data. 

Currently only SADX (2004) and SA2B PC (2012) are in the list. When the [`Editor Mode`](#editor-mode), the user can select files from other versions of the selected game (SA1 files for SADX for example). This will mean you need to be mindful to handle anything in little or big endian.

#### Load Directory
This sets the directory that is used for loading files from when in [`Automatic Mode`](#editor-mode). 

#### Save Directory
This sets the directory that used for saving files from when in [`Automatic Mode`](#editor-mode). If this is not set, files will be exported to the [`Load Directory`](#load-directory).

#### Project Mode
This enables Project Mode which adds support for importing from SA Tools created project files. 

#### Project Directory
This is the directory of the project data. This is only able to be set by importing an SAP Project file using the corresponding operator button.

#### Stage ID
This sets the stage in which the data will be loaded from. **This is only available in [`Automatic Mode`](#editor-mode)**

#### Act ID
This sets the act in which the data will be loaded from. **This is only available in [`Automatic Mode`](#editor-mode)**

#### Object List
This is a collection of [SET Definition Properties](object-definitions.md) that makes up the definitions for the objects when loading a SET file. Please see [Object List Editor](object-list.md) for more information on this property.

#### Active Object
This is the set index for the selected item in the [`Object List`](#object-list). Please see [Object List Editor](object-list.md) for more information on this property.