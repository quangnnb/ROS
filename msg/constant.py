
from enum import Enum


class AutoNumber(Enum):
	def __new__(cls):
		value 		= len(cls.__members__) + 1
		obj 		= object.__new__(cls)
		obj._value_ = value
		return obj


class MESSAGE_TYPE(AutoNumber):
	MSG_STRING  = ()
	MSG_INT 	= ()
	MSG_DOUBLE	= ()

	def __init__(self):
		pass