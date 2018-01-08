# -*- coding: utf-8 -*-
import KBEngine
import random
import skills
from KBEDebug import *
from UNIT_ATTRIBUTE import UnitAttribute
from ATTACK_RESUALT import AttackResualt

class ClientManager(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        self.gameBegin=True
        self.turnFlag=True

        self.initGame()
        DEBUG_MSG("unit value:",self.unit)
        self.client.SetAllUnit(self.unit)

        self.addTimer(0,0.5,0)

    def initGame(self):
        #加载棋子数据#
        newUnit=UnitAttribute()
        newUnit.extend(['Chess Unit',2,0,0,0.5,10,3,4,0,5,2,0,0,0,'',2,0,2,0.0,10])
        self.inserUnit(newUnit)

        newUnit=UnitAttribute()
        newUnit.extend(['Chess Unit',2,9,1,0.5,10,3,4,0,5,2,0,0,0,'',2,0,2,0.0,10])
        self.inserUnit(newUnit)

        newUnit=UnitAttribute()
        newUnit.extend(['Long Range',4,0,0,0.5,6,2,3,1,2,1,5,5,1,'LongRangeAttack',1,0,2,0.0,6])
        self.inserUnit(newUnit)

        newUnit=UnitAttribute()
        newUnit.extend(['Long Range',4,9,1,0.5,6,2,3,1,2,1,5,5,1,'LongRangeAttack',1,0,2,0.0,6])
        self.inserUnit(newUnit)

        newUnit=UnitAttribute()
        newUnit.extend(['Long Range Magic',6,0,0,0.5,6,1,2,1,2,1,5,3,1,'MagicAttack',1,1,2,0.0,5])
        self.inserUnit(newUnit)

        newUnit=UnitAttribute()
        newUnit.extend(['Long Range Magic',6,9,1,0.5,6,1,2,1,2,1,5,3,1,'MagicAttack',1,1,2,0.0,5])
        self.inserUnit(newUnit)

        self.gameBegin=False

    def inserUnit(self,newUnit):
        newUnit.AddSpeedCount()
        speedCount=newUnit.getDataByString('speedCount')
        f=len(self.unit['values'])
        i=0
        while i<f:
            if speedCount<self.unit['values'][i].getDataByString('speedCount'):
                self.unit["values"].insert(i,newUnit)
                break
            elif self.gameBegin and speedCount==self.unit['values'][i].getDataByString('speedCount'):
                if random.random()<0.5:
                    self.unit['values'].insert(i,newUnit)
                    break
            i+=1
        if f==len(self.unit['values']):
            self.unit['values'].append(newUnit)

    #--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
    def onTimer(self, id, userArg):
        if userArg==0:
            if self.turnFlag:
                self.turnFlag=False
                #这应加上判断胜负#
                self.turnUnit=self.unit['values'][0]
                del self.unit['values'][0]
                self.client.SetTurnUnit(self.turnUnit)
    
    def SetTurnFlag(self, clientID, first, second):
        self.turnFlag=True
        self.turnUnit[1]=first
        self.turnUnit[2]=second
        self.inserUnit(self.turnUnit)

    def UnitAttack(self, clientID,first,second,flag):
        #选择攻击脚本#
        if flag:
            skill=skills.getSkill('Attack')
        else:
            skill=skills.getSkill(self.turnUnit.getDataByString('attackTypeName'))

        self.attackResualtList['values']=[]
        i=0
        while i<len(first):
            deadFlag=False
            j=0
            while j<len(self.unit['values']):
                if self.unit['values'][j][1]==first[i] and self.unit['values'][j][2]==second[i]:    #u v 1 2 最好不动#
                    break
                j+=1
            attribute=self.unit['values'][j]
            damage=int(skill.UseSkill(self,attribute,i))
            attribute.SubHP(damage)
            if attribute.getDataByString('HP')<=0:
                del self.unit['values'][j]
                deadFlag=True
            else:
                self.unit['values'][j]=attribute
            attackResualt=AttackResualt()
            attackResualt.extend([damage,deadFlag])
            self.attackResualtList['values'].append(attackResualt)
            i+=1
        self.client.UnitListUnderAttack(self.attackResualtList)

        