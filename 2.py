from pp import*
from constantList_KP4_1 import *
PP_Open()
u=PP_GetUnitAt(MY_COALITION,0)
a=PP_Unit_GetPosition(u)
print(a.x,a.y)
a.x-=927
a.y+=513
PP_Unit_ActionOnPosition(u,MOVE,a)
PP_Close()
