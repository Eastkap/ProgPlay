from pp import*
from constantList_KP4_1 import *
PP_Open()
u=PP_GetUnitAt(MY_COALITION,0)
a=PP_Unit_GetPosition(u)
print(a.x,a.y)
o=PP_GetUnitAt(ENEMY_COALITION,0)
#o=PP_Unit_GetPosition(o)
PP_Unit_ActionOnUnit(u,ATTACK,o)
PP_Close()
