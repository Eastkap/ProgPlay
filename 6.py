from pp import*
from constantList_KP4_1 import *
PP_Open()
pb=PP_Pos()
pb.x=256
pb.y=811
u=PP_GetUnitAt(MY_COALITION,0)
i=0
while PP_Unit_GetType(u)!=ASSEMBLER:
    i+=1

u=PP_GetUnitAt(MY_COALITION,i)
PP_Unit_ActionOnPosition(u,MOVE,pb)
PP_Close()
    

