from pp import*
from constantList_KP4_1 import *
PP_Open()
pb=PP_Pos()
pb.x=256
pb.y=1024
for i in range(10):
    u=PP_GetUnitAt(MY_COALITION,i)
    PP_Unit_ActionOnPosition(u,MOVE,pb)
PP_Close()
    

