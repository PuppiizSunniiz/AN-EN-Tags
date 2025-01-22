import re
import json
from pyfunction import char_ready, name_check, json_load
from pyAkenemy import Akenemy
from py import Ready

Ready()
#########################################################################################################
# JSON
#########################################################################################################
json_building       =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/building_data.json")
json_buildingEN     =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/building_data.json")

json_char_patch     =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/char_patch_table.json")

json_char           =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/character_table.json")
json_charEN         =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/character_table.json")
json_charJP         =   json_load("json/gamedata/ArknightsGameData_YoStar/ja_JP/gamedata/excel/character_table.json")
json_charKR         =   json_load("json/gamedata/ArknightsGameData_YoStar/ko_KR/gamedata/excel/character_table.json")

json_gacha          =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/gacha_table.json")
json_gachaEN        =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/gacha_table.json")

json_skill          =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/skill_table.json")
json_skillEN        =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/skill_table.json")

json_handbook       =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_info_table.json")
json_mod_battle     =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/battle_equip_table.json")
json_mod_battleEN   =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/battle_equip_table.json")
json_mod_table      =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/uniequip_table.json")
json_stage          =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/stage_table.json")

json_construct      =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/gamedata_const.json")
json_constructEN    =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/gamedata_const.json")

json_item           =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/item_table.json")
json_itemEN         =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/item_table.json")
json_itemJP         =   json_load("json/gamedata/ArknightsGameData_YoStar/ja_JP/gamedata/excel/item_table.json")
json_itemKR         =   json_load("json/gamedata/ArknightsGameData_YoStar/ko_KR/gamedata/excel/item_table.json")

json_akhr           =   json_load("json/tl-akhr.json")
json_akmaterial     =   json_load("json/akmaterial.json")
json_trait          =   json_load("json/tl-attacktype.json")
json_term           =   json_load("json/named_effects.json")
json_skillTL        =   json_load("json/ace/tl-skills.json")
json_riicTL         =   json_load("json/ace/riic.json")

json_tl_item        =   json_load("json/tl-item.json")
json_temp_mod       =   json_load("json/tl-module.json")

json_dict           =   json_load("py/dict.json")

#########################################################################################################
# New
#########################################################################################################
#["OpsName#1","OpsName#2", ...]
NEW_CHARS = ["Yu","Blaze the Igniting Spark","Xingzhu","Surfer"] # "", 

#["ItemID#1","ItemID#2", ...]
NEW_MATS = [] # "",

Rechecked = True # True False

#########################################################################################################
# Prep
#########################################################################################################
new_trait ={}

CLASS_PARSE_EN = {
                    "MEDIC"   : "Medic",          "WARRIOR"   : "Guard",
                    "SPECIAL" : "Specialist",     "SNIPER"    : "Sniper",
                    "PIONEER" : "Vanguard",       "CASTER"    : "Caster",
                    "SUPPORT" : "Supporter",      "TANK"      : "Defender"}

CLASS_PARSE_CN = {
                    'SNIPER' :"狙击", 'PIONEER':"先锋", 'TANK'   :"重装",  'MEDIC'   :"医疗",
                    'SUPPORT':"辅助", 'SPECIAL':"特种", 'WARRIOR':"近卫",  'CASTER'  :"术师"}

for char_key in json_char_patch["patchChars"]:
    json_char_patch["patchChars"][char_key]["appellation"] += f' ({CLASS_PARSE_EN[json_char_patch["patchChars"][char_key]["profession"]]})'
json_char.update(json_char_patch["patchChars"])

char_ready  = char_ready(json_char)

char_list   = [char_data["name_en"] for char_data in json_akhr]
MAT_LIST    = [mat_data["itemId"] for mat_data in json_akmaterial]

#########################################################################################################
# Def function
#########################################################################################################
def get_new_akhr(new_char_id : str, new_char_name : str) -> dict:
    return  {
                                    "id"            :   new_char_id,
                                    "name_cn"       :   json_char[new_char_id]["name"],
                                    "name_en"       :   new_char_name,
                                    "name_jp"       :   "",
                                    "name_kr"       :   "",
                                    "nationId"      :   json_char[new_char_id]["nationId"],
                                    "groupId"       :   json_char[new_char_id]["groupId"],
                                    "teamId"        :   json_char[new_char_id]["teamId"],
                                    "type"          :   CLASS_PARSE_CN[json_char[new_char_id]["profession"]],
                                    "level"         :   int(json_char[new_char_id]["rarity"][-1]),
                                    "sex"           :   ''.join(json_handbook["handbookDict"][new_char_id]["storyTextAudio"][0]["stories"][0]["storyText"].split("\n")[1].split("】")[1].split()) if new_char_id in json_handbook["handbookDict"] else "temp",
                                    "tags"          :   (["高级资深干员"] if json_char[new_char_id]["rarity"][-1] == "6" else []) + \
                                                        (["资深干员"] if json_char[new_char_id]["rarity"][-1] == "5" else []) + \
                                                        (["近战位"] if json_char[new_char_id]["position"] == "MELEE" else []) + \
                                                        (["远程位"] if json_char[new_char_id]["position"] == "RANGED" else []) + \
                                                        json_char[new_char_id]["tagList"],
                                    "hidden"        :   True,
                                    "globalHidden"  :   True,
                                    "gamemode"      :   "BASE"
            }

def update_new_trait(mode : str, new_id : str, new_char_name : str, extra = "") -> dict:
    '''
    ### Mode
        "char", "token", "mod"
    ### New_id
        new_char_id     for     "char", "token"
        
        new_mod_id      for     "mod"
    ### Extra
        char    new archetype
        Token   new_token_key
        Mode    Mod Code
    '''
    match mode:
        case "char":
            return  {
                        "en"    : "",
                        "color" : "",
                        "note"  : f'new Ops "{extra}" Archetype trait',
                        "name"  : new_char_name,
                        "code"  : new_id
                    }
        case "token":
            return  {
                        "en"    : "",
                        "color" : "",
                        "note"  : f'{new_char_name} \'s Token ({json_char[extra]["appellation"]})',
                        "name"  : json_char[extra]["appellation"],
                        "code"  : extra
                    }
        case "mod" :
            return  {
                        "en"    : "",
                        "color" : "",
                        "note"  : f'new mods {extra}',
                        "name"  : new_char_name,
                        "code"  : new_id,
                    }

def update_char_TraitSkillTalent(new_char_name : str) :
    new_char_id = char_ready["Name2Code"][new_char_name]
    ## AKHR
    if new_char_id not in [char["id"] for char in json_akhr]:
        json_akhr.append(get_new_akhr(new_char_id,new_char_name))
    ## Trait
    new_trait[json_char[new_char_id]["description"]] = update_new_trait("char",new_char_id,new_char_name,json_char[new_char_id]["subProfessionId"])
    ## Talent
    talent_tl[new_char_id] = [
                                [
                                    {
                                        "name"  : candidate["name"],
                                        "descCN": candidate['description'],
                                        "desc"  : ""
                                    } for candidate in talent['candidates'] if not candidate["isHideTalent"]
                                ]  for talent in json_char[new_char_id]["talents"] 
                            ]
    
    ## Skill
    for skill in json_char[new_char_id]["skills"]:
        skill_id = skill["skillId"]
        if skill_id not in json_skillTL.keys():
            skill_tl[skill_id] = {
                                    "name"  : json_skill[skill_id]["levels"][0]["name"],
                                    "desc"  : [json_skill[skill_id]["levels"][x]["description"] for x in range(len(json_skill[skill_id]["levels"]))]
                                }
    
    ## Token Find
    if json_char[new_char_id]["displayTokenDict"] :
        for new_token_key in json_char[new_char_id]["displayTokenDict"]:
        #### Token trait
            new_trait[json_char[new_token_key]["description"]] = update_new_trait("token",new_char_id,new_char_name,new_token_key)
        #### Token Skill
            for skill in json_char[new_token_key]["skills"]:
                if skill["skillId"] :
                    skill_id = skill["skillId"]
                    skill_tl[skill_id] = {
                                            "name"  : json_skill[skill_id]["levels"][0]["name"],
                                            "desc"  : [json_skill[skill_id]["levels"][x]["description"] if len(json_skill[skill_id]["levels"]) == 10 else json_skill[skill_id]["levels"][0]["description"] for x in range(10)]
                                        }

#########################################################################################################
# Chars
#########################################################################################################
skip_char   = ""
talent_tl   = {}
skill_tl    = {}
for new_char_name in NEW_CHARS:
    if new_char_name not in char_list:
        try:
            update_char_TraitSkillTalent(new_char_name)
        except:
            skip_char += f'{new_char_name}'

    if Rechecked and new_char_name in char_list:
        update_char_TraitSkillTalent(new_char_name)



#Update old char localization
for char_data in json_akhr:
    for lang in [["name_jp",json_charJP],["name_kr",json_charKR]]:
        if char_data[lang[0]] == "":
            if char_data["id"] in lang[1].keys():
                char_data[lang[0]] = lang[1][char_data["id"]]["name"]

#Update recruitment
def cleanlist(recruit_list:str) -> str:
    return recruit_list.replace("\\n","\n").replace("/"," / ").replace("  "," ").replace("< / ","</")

gacha_CN_list   =   cleanlist(json_gacha["recruitDetail"]).split("\n")
gacha_EN_list   =   cleanlist(json_gachaEN["recruitDetail"]).split("\n")

bypass          =   {
                        "THRM-EX"               :   "Thermal-EX",
                        "\'Justice Knight\'"    :   "\"Justice Knight\"",
                        "Justice Knight"        :   "\"Justice Knight\"",
                        "Shirayuki"             :   "ShiraYuki"
                    }

for i in range(6):
    ##CN
    for ops in gacha_CN_list[gacha_CN_list.index("★"*(i+1))+1].split(" / "):
        op = (re.search(r"<@rc.eml>(.+?)</>",ops).group(1) if re.search(r"<@rc.eml>(.+?)</>",ops) else ops).replace("\r","")
        json_akhr[[index for index,d in enumerate(json_akhr) if d["name_cn"] == op][0]]["hidden"] = False
    ##EN
    for ops in gacha_EN_list[gacha_EN_list.index("★"*(i+1))+1].split(" / "):
        op = re.search(r"<@rc.eml>(.+?)</>",ops).group(1) if re.search(r"<@rc.eml>(.+?)</>",ops) else ops
        json_akhr[[index for index,d in enumerate(json_akhr) if name_check(d["name_en"]) == bypass.get(op,op)][0]]["globalHidden"] = False

with open("json/tl-akhr.json", "w", encoding="utf-8") as filepath :
    json.dump(json_akhr,filepath,indent = 4, ensure_ascii = False)
    
with open("update/tl-talent.json", "w", encoding="utf-8") as filepath :
    json.dump(talent_tl,filepath,indent = 4, ensure_ascii = False)

with open("update/tl-skill.json", "w", encoding="utf-8") as filepath :
    json.dump(skill_tl,filepath,indent = 4, ensure_ascii = False)

#########################################################################################################
# Mats
#########################################################################################################
#akmatuses.html
mat_button = []
for new_mat in NEW_MATS:
    mat_button.append(f'<button type="button" onclick="clickBtnTag(this)" class="btn btn-sm btn-secondary ak-btn btn-tag my-1 button-tag" data-toggle="tooltip" data-placement="top" title="{json_item["items"][new_mat]["name"]}" mat-id="{new_mat}"></button>')

mat_button.sort(reverse = False,key = lambda new_mat : new_mat.split("\"")[-2][0:-1]) #sort mat id
mat_button.sort(reverse = True, key = lambda new_mat : new_mat.split("\"")[-2][-1]) #sort rarity

with open("update/akmatuses.txt", "w", encoding="utf-8") as writer:
    writer.write("\n\n".join(mat_button))

drop_parse = {
                "ALWAYS"    : "Always",
                "ALMOST"    : "Common",
                "USUAL"     : "Medium",
                "OFTEN"     : "Rare",
                "SOMETIMES" : "Very Rare"}

for new_mat in NEW_MATS:
    if new_mat not in MAT_LIST:
        mat_source = {
                        json_stage["stages"][stage["stageId"]]["code"]  : drop_parse[stage["occPer"]] 
                            for stage in json_item["items"][new_mat]["stageDropList"]
                    }
        mat_craft = {
                        json_item["items"][mat_cost["id"]]["name"]  : mat_cost["count"]
                            for mat_recipe in json_building["workshopFormulas"]
                                if json_building["workshopFormulas"][mat_recipe]["itemId"] == new_mat
                                    for mat_cost in json_building["workshopFormulas"][mat_recipe]["costs"]
                    }
        #json/akmaterial.json
        json_akmaterial.append({
                                    "id"        : len(json_akmaterial),
                                    "itemId"    : new_mat,
                                    "IconID"    : json_item["items"][new_mat]["iconId"],
                                    "name_cn"   : json_item["items"][new_mat]["name"],
                                    "name_en"   : "",
                                    "name_jp"   : "",
                                    "name_kr"   : "",
                                    "name_tw"   : "",
                                    "level"     : int(json_item["items"][new_mat]["rarity"][-1]),
                                    "source"    : mat_source,
                                    "madeof"    : mat_craft
                                })
        #json/tl-item.json
        json_tl_item.append({
                                "itemId"    : new_mat,
                                "name_cn"   : json_item["items"][new_mat]["name"],
                                "name_en"   : "",
                                "name_jp"   : "",
                                "name_kr"   : "",
                                "name_tw"   : ""
                            })

#Update Old item localization
##akmaterial.json
temp = ""
for mat_data in json_akmaterial:
    for lang in [["name_en",json_itemEN],["name_jp",json_itemJP],["name_kr",json_itemKR]]:
        if mat_data[lang[0]] == "":
            if mat_data["itemId"] in lang[1]["items"]:
                mat_data[lang[0]] = lang[1]["items"][mat_data["itemId"]]["name"]
    mat_data["IconID"] = json_item["items"][mat_data["itemId"]]["iconId"]
    for key in ["id", "itemId", "IconID", "name_cn", "name_en", "name_jp", "name_kr", "name_tw", "level", "source", "madeof"]:
        temp = mat_data[key]
        mat_data.pop(key)
        mat_data[key] = temp

with open("json/akmaterial.json", "w", encoding="utf-8") as filepath :
    json.dump(json_akmaterial,filepath,indent = 4, ensure_ascii = False)

##tl-item.json
for mat_data in json_tl_item:
    for lang in [["name_en",json_itemEN],["name_jp",json_itemJP],["name_kr",json_itemKR]]:
        if mat_data[lang[0]] == "":
            if mat_data["itemId"] in lang[1]["items"].keys():
                mat_data[lang[0]] = lang[1]["items"][mat_data["itemId"]]["name"]

with open("json/tl-item.json", "w", encoding="utf-8") as filepath :
    json.dump(json_tl_item,filepath,indent = 4, ensure_ascii = False)

#########################################################################################################
# Mod
#########################################################################################################   
newmods = json_mod_table["equipTrackDict"][-1]["trackList"]
NEW_MODS = [[newmods[i]["charId"],newmods[i]["equipId"]] for i in range(len(newmods)) if not re.search("_001_",newmods[i]["equipId"])]
skip_mod = ""
mod_tl = {}

for new_mod_list in NEW_MODS:
    if new_mod_list[1] in json_temp_mod.keys():
            #skip_mod += f'\n\t{new_mod_list[0]} --- {new_mod_list[1]}'
            pass
    try:
        char_key = new_mod_list[0]
        new_mod_id = new_mod_list[1]
        mod_trait_candidate = json_mod_battle[new_mod_id]["phases"][0]["parts"][0]["overrideTraitDataBundle"]["candidates"][0]
        if mod_trait_candidate["additionalDescription"]:
            new_trait[mod_trait_candidate["additionalDescription"]] = update_new_trait("mod",new_mod_id,new_mod_list[0],json_mod_table["equipDict"][new_mod_id]["typeIcon"])
        else :
            new_trait[mod_trait_candidate["overrideDescripton"]]    = update_new_trait("mod",new_mod_id,new_mod_list[0],json_mod_table["equipDict"][new_mod_id]["typeIcon"])
        temp_phase = []
        for phase in [1,2]:
            for part in json_mod_battle[new_mod_id]["phases"][phase]["parts"]:
                temp_part = []
                if part["target"] in ["TALENT_DATA_ONLY","TALENT"] and not part["isToken"] and part["addOrOverrideTalentDataBundle"]["candidates"][0]["upgradeDescription"] != "":
                    for pot in range(len(part["addOrOverrideTalentDataBundle"]["candidates"])):
                        candidate = part["addOrOverrideTalentDataBundle"]["candidates"][pot]
                        talent_candidate_CN = json_char[char_key]["talents"][candidate["talentIndex"]]["candidates"][pot-len(part["addOrOverrideTalentDataBundle"]["candidates"])]
                        talent_candidate_EN = json_charEN[char_key]["talents"][candidate["talentIndex"]]["candidates"][pot-len(part["addOrOverrideTalentDataBundle"]["candidates"])] if char_key in json_charEN.keys() else None
                        if char_key in json_charEN and candidate["talentIndex"] != -1:
                            temp_part.append({
                                                "name"                  :   talent_candidate_EN["name"],
                                                "EN"                    :   talent_candidate_EN["description"],
                                                "CN"                    :   talent_candidate_CN["description"],
                                                "mod"                   :   candidate["upgradeDescription"],
                                                "upgradeDescription"    :   ""
                                            })
                        else:
                            temp_part.append({
                                                "name"                  :   candidate["name"],
                                                "CN"                    :   talent_candidate_CN["description"],
                                                "mod"                   :   candidate["upgradeDescription"],
                                                "upgradeDescription"    :   ""
                                            })
                if len(temp_part) :temp_phase.append(temp_part)
        mod_tl[new_mod_id] = temp_phase
    except:
        skip_mod += f'\n\t{new_mod_list[0]} --- {new_mod_list[1]}'

with open("update/tl-module.json", "w", encoding="utf-8") as filepath :
    json.dump(mod_tl,filepath,indent = 4, ensure_ascii = False)

poplist = []
for mod in json_temp_mod.keys():
    if mod in json_mod_battleEN.keys():
        poplist.append(mod)
for mod in poplist:
    json_temp_mod.pop(mod)

with open("json/tl-module.json", "w", encoding="utf-8") as filepath :
    json.dump(json_temp_mod,filepath,indent = 4, ensure_ascii = False)

#########################################################################################################
# Trait
#########################################################################################################
pop = []
for key in new_trait.keys():
    if key in json_trait["full"].keys():
        pop.append(key)
for key in pop:
    new_trait.pop(key)

with open("update/tl-attacktype.json", "w", encoding="utf-8") as filepath :
    json.dump(new_trait,filepath,indent = 4, ensure_ascii = False)

#########################################################################################################
# Termology Update
#########################################################################################################

for term in json_construct["termDescriptionDict"]:
    if term not in json_term["termDescriptionDict"].keys():
        json_term["termDescriptionDict"][term] = json_construct["termDescriptionDict"][term]

for term in json_term["termDescriptionDict"].keys():
    if term in json_constructEN["termDescriptionDict"].keys() and 'cc.' not in term :
        json_term["termDescriptionDict"][term] = json_constructEN["termDescriptionDict"][term]
        
with open("json/named_effects.json", "w", encoding="utf-8") as filepath :
    json.dump(json_term,filepath,indent = 4, ensure_ascii = False)

#########################################################################################################
# RIIC EN Update
#########################################################################################################
for riic in json_building["buffs"].keys():
    if riic not in json_riicTL.keys():
        json_riicTL[riic]=  {
                                "name"          :   json_building["buffs"][riic]["buffName"],
                                "desc"          :   json_building["buffs"][riic]["description"],
                                "descformat"    :   json_building["buffs"][riic]["description"]
                            }

for riic in json_buildingEN["buffs"].keys():
    json_riicTL[riic]=  {
                            "name"          :   json_buildingEN["buffs"][riic]["buffName"],
                            "desc"          :   json_riicTL[riic]["desc"],
                            "descformat"    :   json_buildingEN["buffs"][riic]["description"]
                        }
    
with open("json/ace/riic.json", "w", encoding="utf-8") as filepath :
    json.dump(json_riicTL,filepath,indent = 4, ensure_ascii = False)

Akenemy()

if skip_char:
    print(f'\nNEW CHAR skip list = {skip_char}')
if skip_mod:
    print(f'NEW MOD skip list = {skip_mod}')
    
print("pyUpdate Completed !!!\n")