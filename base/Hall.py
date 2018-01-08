# -*- coding: utf-8 -*-
import KBEngine
import random
import time
from KBEDebug import *

class Hall(KBEngine.Base):
	"""
	大厅管理器实体
	该实体管理该服务组上所有的大厅
	"""
	def __init__(self):
		DEBUG_MSG("Hall init")
		KBEngine.Base.__init__(self)

		#储存大厅
		KBEngine.globalData["Halls"] = self
		
		# 存放所有在线玩家mailbox
		self.player = []

		#self.addTimer(3, 6, 1)

	def PlayerLogin(self,player):

		#此函数添加上线玩家入列表

		if player in self.player: 
			return
		DEBUG_MSG("Account[%i].PlayerLogin:" % player.id)
		self.player.append(player)
#--------------------------------------------------------------------------------------------
#                              Callbacks
#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		if len(self.player)>0:
			KBEngine.createBaseAnywhere("ClientManager")