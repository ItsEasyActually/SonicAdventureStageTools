@echo off

set addon_src="addon"
set addon_dst="build"
set addon_dll="SAST.Lib\bin"
set addon_dlldst="build\dll"

REM Ensure source directory exists
echo Source Directory: %addon_src%
echo Destination Directory: %addon_dst%

if not exist %addon_src% (
    echo Source directory does not exist: %addon_src%
    goto end
)

if not exist %addon_dll% (
    echo C# Library build does not exist: %addon_dll%
    goto end
)

if not exist %addon_dst% (
    echo Destination directory does not exist...creating: %addon_dst%
    mkdir %addon_dst%
)

if not exist %addon_dlldst% (
    echo DLL Directory does not exist...creating: %addon_dlldst%
    mkdir %addon_dlldst%
)

REM Copy contents from source to destination
echo Copying contents from %addon_src% to %addon_dst%
xcopy /s /e /y %addon_src%\* %addon_dst%

REM Copy contents from dll to destination
echo Copying contents from %addon_dll% to %addon_dlldst%
xcopy /y %addon_dll%\* %addon_dlldst%

REM Delete excess blend files.
echo Deleting *.blend1 files from %addon_dst%
del /S *.blend1

echo Applying Updates to addon
xcopy /s /e /y %addon_dst%\* "%APPDATA%\Blender Foundation\Blender\5.2\scripts\addons\SonicAdventureStageTools"

:end