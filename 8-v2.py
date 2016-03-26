##on debug et ameliore

from pp import*
from constantList_KP4_1 import *

def trouver(quoi,combien):
    for i in range(combien):
        u=PP_GetUnitAt(MY_COALITION,i)
        if(PP_Unit_GetType(u)==quoi):
            return u
    return -1

def asante(i):
    while(PP_Unit_GetHealth(i)!=PP_Unit_GetMaxHealth(i)):
        True


PP_Open()
pb=PP_Pos()
pb.x=224
pb.y=800
u=PP_GetUnitAt(MY_COALITION,0)
i=0
bases=set()
while PP_Unit_GetType(u)!=ASSEMBLER:
    i+=1
    u=PP_GetUnitAt(MY_COALITION,i)
#assembler est en u, on cree beaucoup dunites
xx=PP_GetSpecialAreaPosition(5)
PP_Unit_ActionOnPosition(u,BUILD_SOCKET,xx)
maxi=PP_GetNumUnits(MY_COALITION)
s1=trouver(SOCKET,maxi)
print(s1)
while(s1==-1):
    print(s1)
    maxi=PP_GetNumUnits(MY_COALITION)
    s1=trouver(SOCKET,maxi)
asante(s1)
    ##ensuite asante
xx=PP_GetSpecialAreaPosition(6)
PP_Unit_ActionOnPosition(u,BUILD_TERMINAL,xx)
s2=trouver(TERMINAL,maxi)
while(s2==-1):
    maxi=PP_GetNumUnits(MY_COALITION)
    s2=trouver(TERMINAL,maxi)
asante(s2)
xx=PP_GetSpecialAreaPosition(7)
PP_Unit_ActionOnPosition(u,BUILD_SOCKET,xx)

while(PP_GetNumUnits(MY_COALITION)!=100):
    True



i=0
maxi=PP_GetNumUnits(MY_COALITION)






pb.x=1792
pb.y=256

for i in range(maxi):
    o=PP_GetUnitAt(MY_COALITION,i)
    if(PP_Unit_GetType(o)!=ASSEMBLER):
        ##PP_Unit_ActionOnUnit(u,REPAIR,o)
        #while(PP_Unit_GetHealth(o)!=PP_Unit_GetMaxHealth(o)):
         #     True
        PP_Unit_ActionOnPosition(o,FIGHT,pb)
        PP_Unit_ActionOnPosition(s2,SIGTERM,pb)
PP_Close()
    
