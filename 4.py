from pp import*
from constantList_KP4_1 import *
PP_Open()
u=PP_GetUnitAt(MY_COALITION,0)
pb=PP_Pos()
if PP_Unit_GetType(u)==BIT:
    pb.x=1400
    pb.y=1371
    PP_Unit_ActionOnPosition(u,MOVE,pb)
    u=PP_GetUnitAt(MY_COALITION,1)
    pb.x=479
    pb.y=1825
    PP_Unit_ActionOnPosition(u,MOVE,pb)
    PP_Close()
elif PP_Unit_GetType(u)==BYTE:
    pb.x=479
    pb.y=1825
    PP_Unit_ActionOnPosition(u,MOVE,pb)
    PP_Close()
    u=PP_GetUnitAt(MY_COALITION,1)
    pb.x=1400
    pb.y=1371
    PP_Unit_ActionOnPosition(u,MOVE,pb)
    

