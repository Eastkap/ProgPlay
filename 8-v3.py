##on debug et ameliore

from pp import*
from constantList_KP4_1 import *
from math import *

def trouver(quoi,combien):
    for i in range(combien):
        u=PP_GetUnitAt(MY_COALITION,i)
        if(PP_Unit_GetType(u)==quoi):
            return u
    return -1

def asante(i):
    while(PP_Unit_GetHealth(i)!=PP_Unit_GetMaxHealth(i)):
        True

def distance(acteur,cible):
    return sqrt((cible.x-acteur.x)**2+(cible.y-acteur.y)**2)

def baseproche(dejaconstruites):
    daa=list()
    for k in range(20):
        daa+=[k,distance(PP_Unit_GetPosition(u),PP_GetSpecialAreaPosition(k))]
    mini=100000
    indicem=0
    for k in range(0,len(daa),2):
            if(mini>daa[k+1] and daa[a] not in dejaconstruites):
                mini=daa[k+1]
                indicem=daa[k]
    return indicem

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
#on cherche aire special la plus proche
#on cherche la plus proche
dc=set()
o=baseproche(dc)
dc.add(o)
xx=PP_GetSpecialAreaPosition(o)
PP_Unit_ActionOnPosition(u,BUILD_SOCKET,xx)
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
