import json
import pandas as pd
from pyfunction import CharReady

#########################################################################################################
# JSON
#########################################################################################################
json_char           =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/character_table.json").read())
json_mod_battle     =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/battle_equip_table.json").read())
json_mod_table      =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/uniequip_table.json").read())

#########################################################################################################
# Expected Mod
#########################################################################################################
expected=[["Horn","002"],["Ashlock","002"],["Firewhistle","002"],["Delphine","002"],["Verdant","002"],["Fiammetta","003"],["Ebenholz","004"]]
#########################################################################################################
# Char Prep
#########################################################################################################
Chardict=CharReady(json_char,1)
err=[]
expectedmod=[]
for char in expected:
    noterr=0
    for key in json_char.keys():
        if char[0].lower()==Chardict[key].lower():
            char.append(key.split("_")[2])
            expectedmod.append(("_").join(["uniequip"]+char[1:]))
            noterr=1
    if not noterr :
        err.append(char[0])
error = (" ").join(err)
if err :
    print(f"\nError {error} not found")

print("\nExpected = ",expected)
print(expectedmod)

#########################################################################################################
# mod mission/upgrade list
#########################################################################################################
moddict = {}

modmissionlist={}
maxpara=0
modlist=[]
missionlist=[]
templatelist=[]
desclist=[]
paramlist=[]

for mod in expectedmod:
    moddict[mod]={"mission":{}}

    for mission in json_mod_table["equipDict"][mod]["missionList"]:
        moddict[mod]["mission"][mission] = {
                                    "template":json_mod_table["missionList"][mission]["template"],
                                    "desc":json_mod_table["missionList"][mission]["desc"],
                                    "paramList":json_mod_table["missionList"][mission]["paramList"]
                                }
        
        modlist.append(mod)
        missionlist.append(mission)
        templatelist.append(json_mod_table["missionList"][mission]["template"])
        desclist.append(json_mod_table["missionList"][mission]["desc"])
        paramlist.append(json_mod_table["missionList"][mission]["paramList"])
        
        if len(json_mod_table["missionList"][mission]["paramList"]) > maxpara:
            maxpara = len(json_mod_table["missionList"][mission]["paramList"])
            
    modmissionlist[mod]=moddict[mod]["mission"]
        
    for modlevel in [0,1,2]:
        temp=[[],[]]
        talentpot=1
        moddict[mod][modlevel] ={
                                    "TRAIT":{},
                                    "TRAIT_DATA_ONLY":{},
                                    "TALENT":{},
                                    "TALENT_DATA_ONLY":{},
                                    "DISPLAY":{}
                                }
        removelist=["TRAIT","TRAIT_DATA_ONLY","TALENT","TALENT_DATA_ONLY","DISPLAY"]
        for part in range(len(json_mod_battle[mod]["phases"][modlevel]["parts"])):
            if not json_mod_battle[mod]["phases"][modlevel]["parts"][part]["isToken"] or json_mod_battle[mod]["phases"][modlevel]["parts"][part]["target"] in ["TALENT","TALENT_DATA_ONLY"]:
                match json_mod_battle[mod]["phases"][modlevel]["parts"][part]["target"]:
                    case "TRAIT":
                        moddict[mod][modlevel]["TRAIT"] = {
                                                    "overrideDescripton":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["overrideTraitDataBundle"]["candidates"][0]["overrideDescripton"],
                                                    "additionalDescription":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["overrideTraitDataBundle"]["candidates"][0]["additionalDescription"],
                                                    "rangeId":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["overrideTraitDataBundle"]["candidates"][0]["rangeId"],
                                                    "blackboard":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["overrideTraitDataBundle"]["candidates"][0]["blackboard"]
                                                }
                        if "TRAIT" in removelist:
                            removelist.remove("TRAIT")
                    case "TRAIT_DATA_ONLY":
                        moddict[mod][modlevel]["TRAIT_DATA_ONLY"] = {
                                                    "overrideDescripton":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["overrideTraitDataBundle"]["candidates"][0]["overrideDescripton"],
                                                    "additionalDescription":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["overrideTraitDataBundle"]["candidates"][0]["additionalDescription"],
                                                    "rangeId":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["overrideTraitDataBundle"]["candidates"][0]["rangeId"],
                                                    "blackboard":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["overrideTraitDataBundle"]["candidates"][0]["blackboard"]
                                                }
                        if "TRAIT_DATA_ONLY" in removelist:
                            removelist.remove("TRAIT_DATA_ONLY")
                    case "TALENT":
                        resKey=json_mod_battle[mod]["phases"][modlevel]["parts"][part]["resKey"]
                        moddict[mod][modlevel]["TALENT"][resKey] = {}
                        for pot in range(len(json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"])):
                            potential=json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["requiredPotentialRank"]
                            moddict[mod][modlevel]["TALENT"][resKey][potential]={
                                                    "talentIndex":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["talentIndex"],
                                                    "name":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["name"],
                                                    "description":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["description"],
                                                    "upgradeDescription":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["upgradeDescription"],
                                                    "rangeId":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["rangeId"],
                                                    "blackboard":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["blackboard"]
                                                }
                        if "TALENT" in removelist:
                            removelist.remove("TALENT")
                    case "TALENT_DATA_ONLY":
                        for pot in range(len(json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"])):
                            token=str(json_mod_battle[mod]["phases"][modlevel]["parts"][part]["isToken"])
                            temp[pot].append({
                                "TokenID":"Token"+token,
                                "Token":[json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["talentIndex"],
                                                    json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["name"],
                                                    json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["description"],
                                                    json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["upgradeDescription"],
                                                    json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["rangeId"],
                                                    json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["blackboard"]],
                                "potential":json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"][pot]["requiredPotentialRank"]
                            })
                            if len(json_mod_battle[mod]["phases"][modlevel]["parts"][part]["addOrOverrideTalentDataBundle"]["candidates"]) > 1:
                                talentpot=2
                        if "TALENT_DATA_ONLY" in removelist:
                            removelist.remove("TALENT_DATA_ONLY")
                    case "DISPLAY":
                        if "DISPLAY" in removelist:
                            removelist.remove("DISPLAY")
                    case _ :
                        pass
                    
        if "TALENT_DATA_ONLY" not in removelist:
            for x in range(talentpot):
                potential=temp[x][0]['potential']
                moddict[mod][modlevel]["TALENT_DATA_ONLY"][potential] = {
                        "token":[temp[x][y]["TokenID"] for y in range(len(temp[0]))],
                        "talentIndex":[temp[x][y]["Token"][0] for y in range(len(temp[0]))],
                        "name":[temp[x][y]["Token"][1] for y in range(len(temp[0]))],
                        "description":[temp[x][y]["Token"][2] for y in range(len(temp[0]))],
                        "upgradeDescription":[temp[x][y]["Token"][3] for y in range(len(temp[0]))],
                        "rangeId":[temp[x][y]["Token"][4] for y in range(len(temp[0]))],
                        "blackboard":[temp[x][y]["Token"][5] for y in range(len(temp[0]))]
                }              
        for removing in removelist:
            moddict[mod][modlevel].pop(removing)
            
dumpling=json.dumps(moddict,indent=4, ensure_ascii=False)
with open("py/moddict.json",'w') as JSON :
    JSON.write(dumpling)

dfList=[modlist,missionlist,templatelist,desclist]
dfindex=['Module','Mission','template','Desc']

parasplitlist=[[] for x in range(maxpara)]
for x in range(maxpara):
    for para in paramlist:
        if x < len(para):
            parasplitlist[x].append(para[x].split(";")[0])
        else :
            parasplitlist[x].append("")
for x in range(maxpara):
    dfList.append(parasplitlist[x])
    dfindex.append("para"+str(x))

df=pd.DataFrame(dfList,index=dfindex).transpose()
df.to_csv('excel/Pynewmod.csv',sep='|', index=False)

line = 'sep=|' 
with open('excel/Pynewmod.csv', 'r+') as file: 
    file_data = file.read() 
    file.seek(0, 0) 
    file.write(line  +'\n'+ file_data)

print("\nDataframe Completed !!!")
#########################################################################################################
# test
#########################################################################################################
'''
    #maxtrait = 0
    #maxtraitonly =0
    #maxtalent = 0
    #maxtalentonly = 0

    maxTRAIT= 0
    maxTRAIT_DATA_ONLY= 0
    maxTALENT= 0
    maxTALENT_DATA_ONLY= 0
    maxDISPLAY= 0

    for key in json_mod_battle.keys():
        for phase in range(len(json_mod_battle[key]["phases"])):
            countTRAIT= 0
            countTRAIT_DATA_ONLY= 0
            countTALENT= 0
            countTALENT_DATA_ONLY= 0
            countDISPLAY= 0
            for part in range(len(json_mod_battle[key]["phases"][phase]["parts"])):
                match json_mod_battle[key]["phases"][phase]["parts"][part]["target"]:
                    case "TRAIT" :
                        #if len (json_mod_battle[key]["phases"][phase]["parts"][part]["overrideTraitDataBundle"]["candidates"])>maxtrait:
                            #maxtrait=len (json_mod_battle[key]["phases"][phase]["parts"][part]["overrideTraitDataBundle"]["candidates"])
                        countTRAIT+=1
                    case "TRAIT_DATA_ONLY":
                        countTRAIT_DATA_ONLY+=1
                    case "TALENT":
                        countTALENT+=1
                    case "TALENT_DATA_ONLY":
                        countTALENT_DATA_ONLY+=1
                    case "DISPLAY":
                        countDISPLAY+=1
            if countTRAIT > maxTRAIT :
                TRAIT = [key,phase,countTRAIT]
                maxTRAIT = countTRAIT
            if countTRAIT_DATA_ONLY > maxTRAIT_DATA_ONLY :
                TRAIT_DATA_ONLY = [key,phase,countTRAIT_DATA_ONLY]
                maxTRAIT_DATA_ONLY = countTRAIT_DATA_ONLY
            if countTALENT > maxTALENT :
                TALENT = [key,phase,countTALENT]
                maxTALENT = countTALENT
            if countTALENT_DATA_ONLY > maxTALENT_DATA_ONLY :
                TALENT_DATA_ONLY = [key,phase,countTALENT_DATA_ONLY]
                maxTALENT_DATA_ONLY = countTALENT_DATA_ONLY
            if countDISPLAY > maxDISPLAY :
                DISPLAY = [key,phase,countDISPLAY]
                maxDISPLAY = countDISPLAY

    #print (maxtrait)
    print(f"TRAIT = {TRAIT}\nTRAIT_DATA_ONLY = {TRAIT_DATA_ONLY}\nTALENT= {TALENT}\nTALENT_DATA_ONLY = {TALENT_DATA_ONLY}\nDISPLAY={DISPLAY}")
'''