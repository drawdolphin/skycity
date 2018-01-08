# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 
from damage import * 
from buffJudge import * 

class Attack:
    def __init__(self):
        pass

    def UseSkill(self, target, index):
        damage=Damage(self.turnUnit.getDataByString('attackStandard'),self.turnUnit.getDataByString('attackDeviation'))
        damage=DefenseBuffJudge(damage,target)
        #判断自己的加伤脚本#

        damage=AddLuckyDamage(damage,self.turnUnit.getDataByString('luck'))
        return damage