from .sast_cam_object_operators import (
    SASTAddGeometryNode,
    SASTResetProperties
)
from .sast_scene_operators import (
    SASTExportCameraAutomatic,
    SASTExportCameraManual,
    SASTExportSETAutomatic,
    SASTExportSETManual,
    SASTImportCameraAutomatic,
    SASTImportCameraManual,
    SASTImportSETAutomatic,
    SASTImportSETManual
)
from .sast_settings_operators import (
    SASTDebugSave,
    SASTClearLogger
)

to_register = [
    SASTAddGeometryNode,
    SASTResetProperties,
    
    SASTExportCameraAutomatic,
    SASTExportCameraManual,
    SASTExportSETAutomatic,
    SASTExportSETManual,
    SASTImportCameraAutomatic,
    SASTImportCameraManual,
    SASTImportSETAutomatic,
    SASTImportSETManual,

    SASTDebugSave,
    SASTClearLogger
]