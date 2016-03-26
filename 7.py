from pp import*
from constantList_KP4_1 import *
PP_Open()
pb=PP_Pos()
pb.x=1792
pb.y=256
u=PP_GetUnitAt(MY_COALITION,0)
i=0
while PP_Unit_GetType(u)!=ASSEMBLER:
    i+=1
    u=PP_GetUnitAt(MY_COALITION,i)
#assembler est en u
i=0
maxi=PP_GetNumUnits(MY_COALITION)
for i in range(maxi):
    o=PP_GetUnitAt(MY_COALITION,i)
    if(PP_Unit_GetType(o)!=ASSEMBLER):
        ##PP_Unit_ActionOnUnit(u,REPAIR,o)
        #while(PP_Unit_GetHealth(o)!=PP_Unit_GetMaxHealth(o)):
         #     True
        PP_Unit_ActionOnPosition(o,ATTACK,pb)
PP_Close()
    
