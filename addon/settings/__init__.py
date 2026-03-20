from . import properties
from . import operators
from . import interface

cls_register = []
cls_register.extend(properties.cls_register)
cls_register.extend(operators.cls_register)
cls_register.extend(interface.cls_register)