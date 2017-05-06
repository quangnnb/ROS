
from constant  import MESSAGE_TYPE as msg_type

class MessageString(object):
	def __init__(self):
		self.msg_id = msg_type.MSG_STRING
		self.value 	= ""


class MessageInt(object):
	def __init__(self):
		self.msg_id = msg_type.MSG_INT
		self.value 	= 0


class MessageDouble(object):
	def __init__(self):
		self.msg_id = msg_type.MSG_DOUBLE
		self.value 	= 0
