# -*- coding: utf-8 -*-
from KBEDebug import *
from skills import *
import d_skills

skillsList = {}

def onInit():
	"""
	init skills.
	"""
	for key, datas in d_skills.datas.items():
		script = datas['script']
		try:
			DEBUG_MSG("skills.onInit::tryToLoad:[%s]" % (script))
			exec('from skills.'+script+' import '+script)
			scriptinst = eval(script)
			skillsList[key] = scriptinst
		except IOError:
			pass
	DEBUG_MSG("skills.onInit::lenOfDic:[%s]" % (len(skillsList)))

def getSkill(skillID):
	DEBUG_MSG("getSkill:[%s]" % (skillID))
	return skillsList.get(skillID)