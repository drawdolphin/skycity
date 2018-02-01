# -*- coding: utf-8 -*-
import KBEngine
import random
import skills
from KBEDebug import *
from database import *
from UNIT_ATTRIBUTE import UnitAttribute
from ATTACK_RESUALT import AttackResualt

class ClientManager(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        self.gameBegin=True
        self.turnFlag=True

        self.initGame()
        
        self.addTimer(0,0.1,0)
        self.addTimer(3,0.5,1)
        self.addTimer(5,0.5,2)

    def initGame(self):
        #加载棋子数据#
        self.unitlist=[["'Chess unit'",2,0,0],["'Chess unit'",2,9,1]]
        self.listIndex=0
        self.sqlFlag=True

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
        #获得要载入的棋子名称和位置信息后，查询棋子属性#
        if userArg==0:
            if self.sqlFlag:
                self.sqlFlag=False
                if self.listIndex>=len(self.unitlist):
                    self.gameBegin=False
                    self.delTimer(id)                   
                    return
                getChessUnit(self.unitlist[self.listIndex][0],self.setChessData)
        #载入所有棋子数据，传递给服务器#
        elif userArg==1:
            if self.gameBegin==False:
                DEBUG_MSG("unit value:",self.unit)
                self.client.SetAllUnit(self.unit)
                self.delTimer(id)
        #判断一回合是否运行结束，并判断胜负和执行下一回合#
        elif userArg==2:
            if self.turnFlag:
                self.turnFlag=False
                #这应加上判断胜负#
                self.turnUnit=self.unit['values'][0]
                del self.unit['values'][0]
                self.client.SetTurnUnit(self.turnUnit)

    #数据库查询语句的回调函数#
    def setChessData(self,result, rows, insertid, error):
        newUnit=UnitAttribute()
        newUnit.setAttribute(result,self.unitlist[self.listIndex][1],self.unitlist[self.listIndex][2],self.unitlist[self.listIndex][3])
        DEBUG_MSG("set unit value:",newUnit)
        self.inserUnit(newUnit)
        self.listIndex+=1
        self.sqlFlag=True
    
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

        