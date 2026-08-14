from .sast_scene_operators import (
    SASTProjectFileImport,
    SASTImportCameraAutomatic,
    SASTImportCameraManual,
    SASTExportCameraAutomatic,
    SASTExportCameraManual,
    SASTImportSETAutomatic,
    SASTImportSETManual,
    SASTExportSETAutomatic,
    SASTExportSETManual
)

from .sast_objlist_operators import (
    SASTObjListAddItem,
    SASTObjListDeleteItem,
    SASTObjListMoveItemUp,
    SASTObjListMoveItemDown,
    SASTObjListMoveItemTop,
    SASTObjListMoveItemBottom,
    SASTObjListImport,
    SASTObjListExport,
    SASTObjListLoad,
    SASTObjListClear,
    SASTObjListLinkAssets
)

cls_register = [
    SASTProjectFileImport,
    SASTImportCameraAutomatic,
    SASTImportCameraManual,
    SASTExportCameraAutomatic,
    SASTExportCameraManual,
    SASTImportSETAutomatic,
    SASTImportSETManual,
    SASTExportSETAutomatic,
    SASTExportSETManual,
    SASTObjListAddItem,
    SASTObjListDeleteItem,
    SASTObjListMoveItemUp,
    SASTObjListMoveItemDown,
    SASTObjListMoveItemTop,
    SASTObjListMoveItemBottom,
    SASTObjListImport,
    SASTObjListExport,
    SASTObjListLoad,
    SASTObjListClear,
    SASTObjListLinkAssets
]

