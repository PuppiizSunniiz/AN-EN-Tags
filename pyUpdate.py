import pandas
import json
from pyfunction import CharReady

#########################################################################################################
# JSON
#########################################################################################################
json_building       =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/building_data.json").read())

json_char           =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/character_table.json").read())
json_charEN         =   json.loads(open("json/gamedata/en_US/gamedata/excel/character_table.json").read())
json_charJP         =   json.loads(open("json/gamedata/ja_JP/gamedata/excel/character_table.json").read())
json_charKR         =   json.loads(open("json/gamedata/ko_KR/gamedata/excel/character_table.json").read())

json_skill           =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/skill_table.json").read())
json_skillEN         =   json.loads(open("json/gamedata/en_US/gamedata/excel/skill_table.json").read())

json_handbook       =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/handbook_info_table.json").read())
json_mod_battle     =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/battle_equip_table.json").read())
json_mod_battleEN    =   json.loads(open("json/gamedata/en_US/gamedata/excel/battle_equip_table.json").read())
json_mod_table      =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/uniequip_table.json").read())
json_stage          =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/stage_table.json").read())

json_constructEN    =   json.loads(open("json/gamedata/en_US/gamedata/excel/gamedata_const.json").read())

json_item           =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/item_table.json").read())
json_itemEN         =   json.loads(open("json/gamedata/en_US/gamedata/excel/item_table.json").read())
json_itemJP         =   json.loads(open("json/gamedata/ja_JP/gamedata/excel/item_table.json").read())
json_itemKR         =   json.loads(open("json/gamedata/ko_KR/gamedata/excel/item_table.json").read())

json_akhr           =   json.loads(open("json/tl-akhr.json").read())
json_akmaterial     =   json.loads(open("json/akmaterial.json").read())
json_trait          =   json.loads(open("json/tl-attacktype.json").read())
json_term           =   json.loads(open("json/named_effects.json").read())
json_skillTL        =   json.loads(open("json/ace/tl-skills.json").read())

json_tl_item        =   json.loads(open("json/tl-item.json").read())
json_tempmod        =   json.loads(open("json/TempModuletalentsTL.json").read())

#########################################################################################################
# New
#########################################################################################################
#["OpsName#1","OpsName#2", ...]
newchars = ["Ascalon","Aroma","Odda","Lutonada"]

#[["OpsName#1",num(Mod)],["OpsName#2",num(Mod)], ...]
newmods = [["Muelsyse",1],["Vigil",1],["Blacknight",1],["Beanstalk",1],["Ascalon",1],["Aroma",1],["Lutonada",1],["Ho'olheyak",2]]

#["ItemID#1","ItemID#2", ...]
newmats = []

#["OpsName#1","OpsName#2", ...]
recruitCN=[]
recruitEN=[]

#########################################################################################################
# Prep
#########################################################################################################
newtrait ={}

CharReady=CharReady(json_char)

Classparse= {'SNIPER':"狙击", 'PIONEER':"先锋", 'TANK':"重装",  'MEDIC':"医疗", 'SUPPORT':"辅助", 'SPECIAL':"特种", 'WARRIOR':"近卫",  'CASTER':"术师"}

charlist=[]
for char in json_akhr:
    charlist.append(char["name_en"])
itemlist=[]
for item in json_akmaterial:
    itemlist.append(item["itemId"])


#########################################################################################################
# Test
#########################################################################################################


#########################################################################################################
# Chars
#########################################################################################################
skipchar=[]
talenttl={}
skilltl={}
for newchar in newchars:
    chartalent=[]
    if newchar not in charlist:
        try:
            newcode=CharReady["Name2Code"][newchar]
            ## AKHR
            json_akhr.append({
                                    "id": newcode,
                                    "name_cn": json_char[newcode]["name"],
                                    "name_en": newchar,
                                    "name_jp": "",
                                    "name_kr": "",
                                    "characteristic_cn": "",
                                    "characteristic_en": "",
                                    "characteristic_jp": "",
                                    "characteristic_kr": "",
                                    "camp": "",
                                    "type": Classparse[json_char[newcode]["profession"]],
                                    "level": int(json_char[newcode]["rarity"][-1]),
                                    "sex": ''.join(json_handbook["handbookDict"][newcode]["storyTextAudio"][0]["stories"][0]["storyText"].split("\n")[1].split("】")[1].split()),
                                    "tags": ["高级资深干员" for x in range(1) if json_char[newcode]["rarity"][-1]=="6"]+ \
                                            ["资深干员" for x in range(1) if json_char[newcode]["rarity"][-1]=="5"]+ \
                                            ###["新手" for x in range(1) if json_char[newcode]["rarity"][-1]=="2"]+ \
                                            ["近战位" for x in range(1) if json_char[newcode]["position"]=="MELEE"]+ \
                                            ["远程位" for x in range(1) if json_char[newcode]["position"]=="RANGED"]+ \
                                            json_char[newcode]["tagList"],
                                    "hidden": True,
                                    "globalHidden": True
            })
            ## Trait
            newtrait[json_char[newcode]["description"]]={"name":newchar,
                                                        "code":newcode,
                                                        "mode":"newchars"}
            ## Talent
            for eachtalent in json_char[newcode]["talents"]:
                eachchartalent=[]
                for talent in eachtalent['candidates']:
                    eachchartalent.append({
                                        "name": talent["name"],
                                        "descCN": talent['description'],
                                        "desc": ""
                                    })
                chartalent.append(eachchartalent)
            talenttl[newcode]=chartalent
            
            ## Skill
            for skill in json_char[newcode]["skills"]:
                skillid = skill["skillId"]
                if skillid not in json_skillTL.keys():
                    skilltl[skillid]={
                                        "name" : json_skill[skillid]["levels"][0]["name"],
                                        "desc": [json_skill[skillid]["levels"][x]["description"] for x in range(len(json_skill[skillid]["levels"]))]
                                    }
        except:
            skipchar.append(newchar)

if skipchar:
    print('\nNEW CHAR skip list =', skipchar)

#Update old char localization
for char in json_akhr:
    for lang in [["name_jp",json_charJP],["name_kr",json_charKR]]:
        if char[lang[0]]=="":
            if char["id"] in lang[1].keys():
                char[lang[0]]=lang[1][char["id"]]["name"]
#Update recruitment
##CN
if recruitCN:
    for char in recruitCN:
        for chars in json_akhr:
            if char.lower()==chars["name_en"].lower():
                chars["hidden"]=False
                break
##EN
if recruitEN:
    for char in recruitEN:
        for chars in json_akhr:
            if char.lower()==chars["name_en"].lower():
                chars["globalHidden"]=False
                break
dumpling=json.dumps(json_akhr,indent=4, ensure_ascii=False)
with open("json/tl-akhr.json",'w') as JSON :
    JSON.write(dumpling)
    
dumpling=json.dumps(talenttl,indent=4, ensure_ascii=False)
with open("temp/tl-talent.json",'w') as JSON :
    JSON.write(dumpling)

dumpling=json.dumps(skilltl,indent=4, ensure_ascii=False)
with open("temp/tl-skill.json",'w') as JSON :
    JSON.write(dumpling)

#########################################################################################################
# Mats
#########################################################################################################
#akmatuses.html
matbotton=[]
for mat in newmats:
    matbotton.append("<button type=\"button\" onclick=\"clickBtnTag(this)\" class=\"btn btn-sm btn-secondary ak-btn btn-tag my-1 button-tag\" data-toggle=\"tooltip\" data-placement=\"top\" title=\""+json_item["items"][mat]["name"]+"\" mat-id=\""+mat+"\"></button>")

matbotton.sort(reverse=False,key=lambda mat : mat.split("\"")[-2][0:-1]) #sort mat id
matbotton.sort(reverse=True,key=lambda mat : mat.split("\"")[-2][-1]) #sort rarity

with open("update/akmatuses.txt",'w') as writer:
    writer.write("\n\n".join(matbotton))

Dropparse={"ALWAYS":"Always","ALMOST":"Common","USUAL":"Medium","OFTEN":"Rare","SOMETIMES":"Very Rare"}
for i in range(len(newmats)):
    mat=newmats[i]
    if mat not in itemlist:
        matsource={}
        for stage in json_item["items"][mat]["stageDropList"]:
            matsource[json_stage["stages"][stage["stageId"]]["code"]]=Dropparse[stage["occPer"]]
        matcraft={}
        for recipe in json_building["workshopFormulas"].keys():
            if json_building["workshopFormulas"][recipe]["itemId"]==mat:
                for cost in json_building["workshopFormulas"][recipe]["costs"]:
                    matcraft[json_item["items"][cost["id"]]["name"]]=cost["count"]
        #json/akmaterial.json
        json_akmaterial.append({
                        "id": len(json_akmaterial),
                        "itemId": mat,
                        "IconID": json_item["items"][mat]["iconId"],
                        "name_cn": json_item["items"][mat]["name"],
                        "name_en": "",
                        "name_jp": "",
                        "name_kr": "",
                        "name_tw": "",
                        "level": int(json_item["items"][mat]["rarity"][-1]),
                        "source": matsource,
                        "madeof": matcraft
        })
        #json/tl-item.json
        json_tl_item.append({
                        "itemId":  mat,
                        "name_cn": json_item["items"][mat]["name"],
                        "name_en": "",
                        "name_jp": "",
                        "name_kr": "",
                        "name_tw": ""
        })

#Update Old item localization
##akmaterial.json
temp=""
for item in json_akmaterial:
    for lang in [["name_en",json_itemEN],["name_jp",json_itemJP],["name_kr",json_itemKR]]:
        if item[lang[0]]=="":
            if item["itemId"] in lang[1]["items"].keys():
                item[lang[0]]=lang[1]["items"][item["itemId"]]["name"]
    item["IconID"]=json_item["items"][item["itemId"]]["iconId"]
    for key in ["id", "itemId", "IconID", "name_cn", "name_en", "name_jp", "name_kr", "name_tw", "level", "source", "madeof"]:
        temp=item[key]
        item.pop(key)
        item[key]=temp
dumpling=json.dumps(json_akmaterial,indent=4, ensure_ascii=False)
with open("json/akmaterial.json",'w') as JSON :
    JSON.write(dumpling)
    
##tl-item.json
for item in json_tl_item:
    for lang in [["name_en",json_itemEN],["name_jp",json_itemJP],["name_kr",json_itemKR]]:
        if item[lang[0]]=="":
            if item["itemId"] in lang[1]["items"].keys():
                item[lang[0]]=lang[1]["items"][item["itemId"]]["name"]
dumpling=json.dumps(json_tl_item,indent=4, ensure_ascii=False)
with open("json/tl-item.json",'w') as JSON :
    JSON.write(dumpling)
        
#########################################################################################################
# Mod
#########################################################################################################   
skipmod=[]
modtl={}
for charlist in newmods:
    try:
        char=CharReady["Name2Code"][charlist[0]]
        modcode=json_mod_table["charEquip"][char][charlist[1]]
        if json_mod_battle[modcode]["phases"][0]["parts"][0]["overrideTraitDataBundle"]["candidates"][0]["additionalDescription"]:
            newtrait[json_mod_battle[modcode]["phases"][0]["parts"][0]["overrideTraitDataBundle"]["candidates"][0]["additionalDescription"]]={"name":charlist[0],
                                                        "code":modcode,
                                                        "mode":"newmods"}
        else :
            newtrait[json_mod_battle[modcode]["phases"][0]["parts"][0]["overrideTraitDataBundle"]["candidates"][0]["overrideDescripton"]]={"name":charlist[0],
                                                        "code":modcode,
                                                        "mode":"newmods"}
        tempphase=[]
        for phase in [1,2]:
            for part in json_mod_battle[modcode]["phases"][phase]["parts"]:
                temppart=[]
                if part["target"] in ["TALENT_DATA_ONLY","TALENT"] and not part["isToken"] and part["addOrOverrideTalentDataBundle"]["candidates"][0]["upgradeDescription"]!="":
                    for pot in range(len(part["addOrOverrideTalentDataBundle"]["candidates"])):
                        candidate = part["addOrOverrideTalentDataBundle"]["candidates"][pot]
                        if char in json_charEN and candidate["talentIndex"]!=-1:
                            temppart.append({
                                    "name":json_charEN[char]["talents"][candidate["talentIndex"]]["candidates"][pot-len(part["addOrOverrideTalentDataBundle"]["candidates"])]["name"],
                                    "EN":json_charEN[char]["talents"][candidate["talentIndex"]]["candidates"][pot-len(part["addOrOverrideTalentDataBundle"]["candidates"])]["description"],
                                    "CN":json_char[char]["talents"][candidate["talentIndex"]]["candidates"][pot-len(part["addOrOverrideTalentDataBundle"]["candidates"])]["description"],
                                    "mod":candidate["upgradeDescription"],
                                    "upgradeDescription":""
                            })
                        else:
                            temppart.append({
                                    "name":candidate["name"],
                                    "CN":json_char[char]["talents"][candidate["talentIndex"]]["candidates"][pot-len(part["addOrOverrideTalentDataBundle"]["candidates"])]["description"],
                                    "mod":candidate["upgradeDescription"],
                                    "upgradeDescription":""
                            })
            tempphase.append(temppart)
        modtl[modcode]=tempphase
    except:
        skipmod.append(charlist)
        
if skipmod:
    print('NEW MOD skip list = ',skipmod)

dumpling=json.dumps(modtl,indent=4, ensure_ascii=False)
with open("update/TempModuletalentsTL.json",'w') as JSON :
    JSON.write(dumpling)

poplist=[]
for mod in json_tempmod.keys():
    if mod in json_mod_battleEN.keys():
        poplist.append(mod)
for mod in poplist:
    json_tempmod.pop(mod)

dumpling=json.dumps(json_tempmod,indent=4, ensure_ascii=False)
with open("json/TempModuletalentsTL.json",'w') as JSON :
    JSON.write(dumpling)

#########################################################################################################
# Trait
#########################################################################################################
pop=[]
for key in newtrait.keys():
    if key in json_trait["full"].keys():
        pop.append(key)
for key in pop:
    newtrait.pop(key)

dumpling=json.dumps(newtrait,indent=4, ensure_ascii=False)
with open("update/tl-attacktype.json",'w') as JSON :
    JSON.write(dumpling)

#########################################################################################################
# Termology Update
#########################################################################################################

for term in json_term["termDescriptionDict"].keys():
    if term in json_constructEN["termDescriptionDict"].keys() and 'cc.' not in term :
        json_term["termDescriptionDict"][term]=json_constructEN["termDescriptionDict"][term]
        
dumpling=json.dumps(json_term,indent=4, ensure_ascii=False)
with open("json/named_effects.json",'w') as JSON :
    JSON.write(dumpling)


print("\nUpdate Completed !!!\n")