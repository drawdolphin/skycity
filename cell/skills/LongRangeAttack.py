# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 
from damage import * 
from buffJudge import *

class LongRangeAttack:
    def __init__(self):
        pass

    def UseSkill(self, target, index):
        damage=Damage(self.turnUnit.getDataByString('longRangeStandard'),self.turnUnit.getDataByString('longRangeDeviation'))
        distance = self.turnUnit.GetDistance(target)
        longRange=self.turnUnit.getDataByString('longRange')
        if distance>longRange:
            if distance>=longRange*2:
                damage*=3/10
            else:
                damage*=(1.7-distance*7/10/longRange)
        damage=DefenseBuffJudge(damage,target)
        #判断自己的加伤脚本#

        damage=AddLuckyDamage(damage,self.turnUnit.getDataByString('luck'))
        return damage