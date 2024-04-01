import json
from pyfunction import CharReady

#########################################################################################################
# JSON
#########################################################################################################
json_char           =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/character_table.json").read())
json_charEN         =   json.loads(open("json/gamedata/en_US/gamedata/excel/character_table.json").read())

json_mod_battle     =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/battle_equip_table.json").read())
json_mod_battleEN   =   json.loads(open("json/gamedata/en_US/gamedata/excel/battle_equip_table.json").read())

json_attacktype     =   json.loads(open("json/tl-attacktype.json").read())
#########################################################################################################
# Prep
#########################################################################################################
#newmods = [['Mountain',1],['Chongyue',1],['Dagda',1],['Flint',1],['Indra',1],['Beehunter',1],['Jackie',1],['Kestrel',1],['Wan Qing',1],['Grain Buds',1],['Zuo Le',1],['Shu',1]]
newmods=[['Mountain',1,1],['Chongyue',1,2],['Dagda',1,1],['Flint',1,1],['Indra',1,1],['Beehunter',1,1],['Jackie',1,1],['Kestrel',1],['Wan Qing',1],['Grain Buds',1],['Zuo Le',1],['Shu',1]]

CharCode=CharReady(json_char)

#########################################################################################################
# Mod
#########################################################################################################
temp=0

modDict={}

for mod in newmods :
    try:
        OpsCode=CharCode["Name2Code"][mod[0]]
        modcode = "uniequip_00"+str(mod[1]+1)+"_"+OpsCode.split("_")[2]
        talentlen=len(json_charEN[OpsCode]["talents"][mod[2]-1]["candidates"])
        talentpot=json_charEN[OpsCode]["talents"][mod[2]-1]["candidates"][-1]["requiredPotentialRank"]==0
        #print(talentpot)
        modDict[modcode]=[[{'name':json_charEN[OpsCode]["talents"][mod[2]-1]["candidates"][-2+x+talentpot]['name'],"upgradeDescription":json_charEN[OpsCode]["talents"][mod[2]-1]["candidates"][-2+x+talentpot]['description'] } for x in range(2-talentpot)]]*2
    except:
        #print(mod[0])
        modcode = "uniequip_00"+str(mod[1]+1)+"_"+mod[0]
        modDict[modcode]=[[{'name':"","upgradeDescription":"" } for x in range(2)]]*2
        temp+=1
        
#print(modDict)

dumpling=json.dumps(modDict,indent=4, ensure_ascii=False)
with open("temp/newmod.json",'w') as JSON :
    JSON.write(dumpling)

#########################################################################################################
# Trait
#########################################################################################################
'''            
    TraitDict={"Fix":{},"Fixed":{},"Checked":{}}
            TraitList=[]

            for Ops in json_char.keys():
                if "char_" in Ops and int(json_char[Ops]["rarity"][-1])>3:
                    trait=json_char[Ops]["description"]
                    traitEN=json_charEN[Ops]["description"] if Ops in json_charEN.keys() else None
                    #print(Ops+" | "+json_char[Ops]["appellation"]+" | "+json_char[Ops]["subProfessionId"])
                    
                    if trait not in TraitList and json_attacktype["full"][trait]["en"]==traitEN :
                        TraitDict["Checked"][trait]={
                                                        "Name"      : CharCode["Code2Name"][Ops],
                                                        "Code"      : Ops,
                                                        "Archetype" : json_char[Ops]["subProfessionId"],
                                                        "en"        : traitEN
                                                    }
                    else :
                            TraitDict["Fixed"][trait]={
                                                        "Name"      : CharCode["Code2Name"][Ops],
                                                        "Code"      : Ops,
                                                        "Archetype" : json_char[Ops]["subProfessionId"],
                                                        "en"        : traitEN
                                                    }
                            TraitDict["Fix"][trait]={
                                                        "en"        : traitEN,
                                                        "color"     : ""
                                                    }
                        
                    TraitList.append(trait)
                    

            dumpling=json.dumps(TraitDict,indent=4, ensure_ascii=False)
            with open("temp/attaktype.json",'w') as JSON :
                JSON.write(dumpling)'''
