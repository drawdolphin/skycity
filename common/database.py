import KBEngine
from KBEDebug import *

def getChessUnit(unitName,callback):
    sqlString="select * from chessdata.unit where resourceName="+unitName
    KBEngine.executeRawDatabaseCommand(sqlString,callback)
