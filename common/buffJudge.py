# -*- coding: utf-8 -*-
from damage import * 
from UNIT_ATTRIBUTE import UnitAttribute

def DefenseBuffJudge(damage,target):
    #判断对手的减伤脚本#

    damage=SubDefense(damage,target.getDataByString('defense'))
    return damage

def MagicDefenseBuffJudge(damage,target):
    #判断对手的减伤脚本#

    damage=SubMagicDefense(damage,target.getDataByString('magicDefense'))
    return damage