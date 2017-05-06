

from msg import constant as constant
from msg import Message

class MsgFactory(object):
	def __init__(self):
		pass

	def build_msg(self, msg_id):
		"""
		return a msg obj of msg_id
		"""
		if msg_id == constant.MESSAGE_TYPE.MSG_STRING.value:
			return Message.MessageString()
		if msg_id == constant.MESSAGE_TYPE.MSG_INT.value:
			return Message.MessageInt()
		if msg_id == constant.MESSAGE_TYPE.MSG_DOUBLE.value:
			return Message.MessageDouble()


	def parse_msg(self, msg)
