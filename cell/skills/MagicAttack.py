# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 
from damage import * 
from buffJudge import *

class MagicAttack:
    def __init__(self):
        pass

    def UseSkill(self, target, index):
        damage=Damage(self.turnUnit.getDataByString('longRangeStandard'),self.turnUnit.getDataByString('longRangeDeviation'))
        if index==0:
            damage+=1
        damage=MagicDefenseBuffJudge(damage,target)
        #判断自己的加伤脚本#

        damage=AddLuckyDamage(damage,self.turnUnit.getDataByString('luck'))
        return damage