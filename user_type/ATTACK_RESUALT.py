# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 

class AttackResualt(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		list.__init__(self)
		
	def asDict(self):
		data = {
			"damage"			: self[0],
			"deadFlag"			: self[1]
		}
		
		return data

	def createFromDict(self, dictData):
		self.extend([dictData["damage"], dictData["deadFlag"]])
		return self
		
class  AttackResualtPickler:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return  AttackResualt().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj,  AttackResualt)

attack_resualt_inst =  AttackResualtPickler()