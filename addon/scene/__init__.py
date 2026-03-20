from . import interface
from . import operators
from . import properties

cls_register = []

cls_register.extend(properties.cls_register)
cls_register.extend(interface.cls_register)
cls_register.extend(operators.cls_register)
