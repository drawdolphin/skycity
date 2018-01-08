# -*- coding: utf-8 -*-
import random

def Damage(Standard, Deviation):
    return random.randint(Standard-Deviation,Standard+Deviation)

def SubDefense(damage,defense):
    if damage-defense>=0:
        return damage-defense
    else:
        return 0

def SubMagicDefense(damage,defense):
    if defense>=10:
        return 0
    return damage*((10-defense)/10)

def AddLuckyDamage(damage,luck):
    if random.randint(0,10)>=luck:
        return damage
    else:
        return int(damage*1.5)