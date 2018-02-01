# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 

class UnitAttribute(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		list.__init__(self)
		
	def asDict(self):
		data = {
			"resourceName"			: self[0],
			"UValue"			: self[1],
			"VValue"			: self[2],
			"ascription"		: self[3],
			"higth"			: self[4],
			"maxHP"			: self[5],
            "speed"			: self[6],
            "moveLenth"			: self[7],
            "attackType"			: self[8],
            "attackStandard"			: self[9],
            "attackDeviation"			: self[10],
            "longRange"			: self[11],
            "longRangeStandard"			: self[12],
            "longRangeDeviation"			: self[13],
            "attackTypeName"			: self[14],
            "defense"			: self[15],
            "magicDefense"			: self[16],
            "luck"			: self[17],
            "speedCount"			: self[18],
			"HP"              :self[19]
		}
		
		return data

	def createFromDict(self, dictData):
		self.extend([dictData["resourceName"], dictData["UValue"], dictData["VValue"], dictData["ascription"], dictData["higth"], dictData["maxHP"], dictData["speed"], dictData["moveLenth"], dictData["attackType"], dictData["attackStandard"], dictData["attackDeviation"], dictData["longRange"], dictData["longRangeStandard"], dictData["longRangeDeviation"], dictData["attackTypeName"], dictData["defense"], dictData["magicDefense"], dictData["luck"], dictData["speedCount"], dictData["HP"]])
		return self

	def setAttribute(self,data,u,v,ascription):
		self.extend([data[0][1].decode(encoding="utf8"),u,v,ascription,float(data[0][15]),int(data[0][2]),int(data[0][3]),int(data[0][4]),int(data[0][5]),int(data[0][6]),int(data[0][7]),int(data[0][8]),int(data[0][9]),int(data[0][10]),data[0][11].decode(encoding="utf8"),int(data[0][12]),int(data[0][13]),int(data[0][14]),0.0,int(data[0][2])])

	def getDataByString(self,dictString):
		if dictString=="resourceName":
			return self[0]
		elif dictString=="UValue":
			return self[1]
		elif dictString=="VValue":
			return self[2]
		elif dictString=="ascription":
			return self[3]
		elif dictString=="higth":
			return self[4]
		elif dictString=="maxHP":
			return self[5]
		elif dictString=="speed":
			return self[6]
		elif dictString=="moveLenth":
			return self[7]
		elif dictString=="attackType":
			return self[8]
		elif dictString=="attackStandard":
			return self[9]
		elif dictString=="attackDeviation":
			return self[10]
		elif dictString=="longRange":
			return self[11]
		elif dictString=="longRangeStandard":
			return self[12]
		elif dictString=="longRangeDeviation":
			return self[13]
		elif dictString=="attackTypeName":
			return self[14]
		elif dictString=="defense":
			return self[15]
		elif dictString=="magicDefense":
			return self[16]
		elif dictString=="luck":
			return self[17]
		elif dictString=="speedCount":
			return self[18]
		elif dictString=="HP":
			return self[19]	

	def AddSpeedCount(self):
		self[18]+=100/float(self[6])

	def GetDistance(self,target):
		u=abs(self[1]-target[1])
		v=abs(self[2]-target[2])
		if u>v:
			return u+1
		else:
			return v+1
	
	def SubHP(self,damage):
		self[19]-=damage

		
class UnitAttributePickler:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return UnitAttribute().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, UnitAttribute)

unit_attribute_inst = UnitAttributePickler()

class UnitAttributeList(dict):
	"""
	"""
	def __init__(self):
		"""
		"""
		dict.__init__(self)
		
	def asDict(self):
		datas = []
		dct = {"values" : datas}

		for key, val in self.items():
			datas.append(val)
			
		return dct

	def createFromDict(self, dictData):
		for data in dictData["values"]:
			self[data[0]] = data
		return self
		
class UnitAttributeListPickler:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return UnitAttributeList().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, UnitAttributeList)

unit_attribute_list_inst = UnitAttributeListPickler()