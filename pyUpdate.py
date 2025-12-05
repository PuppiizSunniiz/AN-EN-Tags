import re
import json
from types import NoneType
from pyAudio import audio_json
from pyRIIC import riic_tl_json
from pyfunction import URSUS, char_ready, name_check, json_load, printr, R, G, B, Y, RE
from pyAkenemy import Akenemy
from py import Ready
from typing import Any
Ready()
#########################################################################################################
# JSON
#########################################################################################################
json_building       =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/building_data.json")
json_buildingEN     =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/building_data.json")

json_char_patch     =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/char_patch_table.json")
json_char_patchEN   =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/char_patch_table.json")
json_char_patchJP   =   json_load("json/gamedata/ArknightsGameData_YoStar/ja_JP/gamedata/excel/char_patch_table.json")
json_char_patchKR   =   json_load("json/gamedata/ArknightsGameData_YoStar/ko_KR/gamedata/excel/char_patch_table.json")

json_char           =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/character_table.json")
json_charEN         =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/character_table.json")
json_charJP         =   json_load("json/gamedata/ArknightsGameData_YoStar/ja_JP/gamedata/excel/character_table.json")
json_charKR         =   json_load("json/gamedata/ArknightsGameData_YoStar/ko_KR/gamedata/excel/character_table.json")

json_item           =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/item_table.json")
json_itemEN         =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/item_table.json")
json_itemJP         =   json_load("json/gamedata/ArknightsGameData_YoStar/ja_JP/gamedata/excel/item_table.json")
json_itemKR         =   json_load("json/gamedata/ArknightsGameData_YoStar/ko_KR/gamedata/excel/item_table.json")

json_gacha          =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/gacha_table.json")
json_gachaEN        =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/gacha_table.json")

json_skill          =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/skill_table.json")
json_skillEN        =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/skill_table.json")

json_skin           =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/skin_table.json")
json_skinEN         =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/skin_table.json")

json_charword       =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/charword_table.json")
json_charwordEN     =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/charword_table.json")

json_handbook       =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_info_table.json")
json_handbookEN     =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/handbook_info_table.json")

json_mod_battle     =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/battle_equip_table.json")
json_mod_battleEN   =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/battle_equip_table.json")

json_construct      =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/gamedata_const.json")
json_constructEN    =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/gamedata_const.json")

json_enemy          =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/enemy_handbook_table.json")
json_enemyEN        =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/enemy_handbook_table.json")

json_mod_table      =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/uniequip_table.json")
json_stage          =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/stage_table.json")

json_dict           =   json_load("py/dict.json")
json_akmaterial     =   json_load("json/akmaterial.json")
json_term           =   json_load("json/named_effects.json")

json_trait          =   json_load("json/tl-attacktype.json")
json_akhr           =   json_load("json/tl-akhr.json")
json_tl_item        =   json_load("json/tl-item.json")
json_temp_mod       =   json_load("json/tl-module.json")

json_skillTL        =   json_load("json/ace/tl-skills.json")
json_talentTL       =   json_load("json/ace/tl-talents.json")

#########################################################################################################
# New
#########################################################################################################
#["OpsName#1","OpsName#2", ...]
NEW_CHARS : list[str] = ["Nasti", "Cairn", "Skybox",] # "", 

#["ItemID#1","ItemID#2", ...]
NEW_MATS : list[str] = [] # "",

Rechecked : bool = True # True False

#########################################################################################################
# Prep
#########################################################################################################
new_trait : dict = {}

CLASS_PARSE_EN : dict[str, str] = {
                                    "MEDIC"   : "Medic",          "WARRIOR"   : "Guard",
                                    "SPECIAL" : "Specialist",     "SNIPER"    : "Sniper",
                                    "PIONEER" : "Vanguard",       "CASTER"    : "Caster",
                                    "SUPPORT" : "Supporter",      "TANK"      : "Defender"
                                }

CLASS_PARSE_CN : dict[str, str] = {
                                    'SNIPER' :"狙击", 'PIONEER':"先锋", 'TANK'   :"重装",  'MEDIC'   :"医疗",
                                    'SUPPORT':"辅助", 'SPECIAL':"特种", 'WARRIOR':"近卫",  'CASTER'  :"术师"
                                }

for char_key in json_char_patch["patchChars"].keys():
    json_char_patch["patchChars"][char_key]["appellation"] += f' ({CLASS_PARSE_EN[json_char_patch["patchChars"][char_key]["profession"]]})'

json_char.update(json_char_patch["patchChars"])
json_charJP.update(json_char_patchJP["patchChars"])
json_charKR.update(json_char_patchKR["patchChars"])

char_ready  = char_ready(json_char)

char_list : list[str] = [char_data["name_en"] for char_data in json_akhr]
MAT_LIST : list[str] = [mat_data["itemId"] for mat_data in json_akmaterial]

#########################################################################################################
# Def function
#########################################################################################################
def get_new_akhr(new_char_id : str, new_char_name : str) -> dict[str, Any]:
    gender : str = ''.join(json_handbook["handbookDict"][new_char_id]["storyTextAudio"][0]["stories"][0]["storyText"].split("\n")[1].split("】")[1].split()) if new_char_id in json_handbook["handbookDict"] else "temp"
    sex : dict[str, str] = {"女士" : "女"}
    return  {
                                    "id"            :   new_char_id,
                                    "name_cn"       :   json_char[new_char_id]["name"],
                                    "name_en"       :   new_char_name if not new_char_name in URSUS.values() else [k for k, v in URSUS.items() if new_char_name == v][0],
                                    "name_jp"       :   "",
                                    "name_kr"       :   "",
                                    "nationId"      :   json_char[new_char_id]["nationId"],
                                    "groupId"       :   json_char[new_char_id]["groupId"],
                                    "teamId"        :   json_char[new_char_id]["teamId"],
                                    "subPower"      :   json_char[new_char_id]["subPower"],
                                    "type"          :   CLASS_PARSE_CN[json_char[new_char_id]["profession"]],
                                    "level"         :   int(json_char[new_char_id]["rarity"][-1]),
                                    "sex"           :   sex.get(gender, gender),
                                    "tags"          :   (["高级资深干员"] if json_char[new_char_id]["rarity"][-1] == "6" else []) + \
                                                        (["资深干员"] if json_char[new_char_id]["rarity"][-1] == "5" else []) + \
                                                        (["近战位"] if json_char[new_char_id]["position"] == "MELEE" else []) + \
                                                        (["远程位"] if json_char[new_char_id]["position"] == "RANGED" else []) + \
                                                        json_char[new_char_id]["tagList"],
                                    "hidden"        :   True,
                                    "globalHidden"  :   True,
                                    "gamemode"      :   "BASE"
            }

def update_new_trait(mode : str, new_id : str, new_char_name : str, extra : str = "") -> dict[str, str] | None:
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
        case _ :
            printr(f'Invalid mode !!! : {mode}')
            return

def update_char_TraitSkillTalent(new_char_name : str) :
    new_char_id = char_ready["Name2Code"][new_char_name]
    ## AKHR
    if new_char_id not in [char["id"] for char in json_akhr]:
        json_akhr.append(get_new_akhr(new_char_id, new_char_name))
    ## Trait
    new_trait[json_char[new_char_id]["description"]] = update_new_trait("char", new_char_id, new_char_name, json_char[new_char_id]["subProfessionId"])
    ## Talent
    if new_char_id not in json_talentTL:
        talent_tl[new_char_id] = [
                                    [
                                        {
                                            "name"  : candidate["name"],
                                            "descCN": parentheses(candidate["description"]),
                                            "desc"  : ""
                                        } for candidate in talent["candidates"] if not candidate["isHideTalent"]
                                    ]  for talent in json_char[new_char_id]["talents"] if not talent["candidates"][0]["isHideTalent"]
                                ]
    ## Skill
    for skill in json_char[new_char_id]["skills"]:
        skill_id = skill["skillId"]
        if skill_id not in json_skillTL.keys():
            skill_tl[skill_id] = {
                                    "name"  : json_skill[skill_id]["levels"][0]["name"],
                                    "desc"  : [parentheses(json_skill[skill_id]["levels"][x]["description"]) for x in range(len(json_skill[skill_id]["levels"]))]
                                }
    ## Token Find
    if json_char[new_char_id]["displayTokenDict"] :
        for new_token_key in json_char[new_char_id]["displayTokenDict"]:
        #### Token trait
            if new_token_key not in json_char: continue
            new_trait[json_char[new_token_key]["description"]] = update_new_trait("token", new_char_id, new_char_name, new_token_key)
        #### Token talent
            if new_token_key not in json_talentTL:
                talent_tl[new_token_key] = [
                                            [
                                                {
                                                    "name"  : candidate["name"],
                                                    "descCN": parentheses(candidate["description"]),
                                                    "desc"  : ""
                                                } for candidate in talent["candidates"]
                                            ]  for talent in json_char[new_token_key]["talents"]
                                        ]
        #### Token Skill
            for skill in json_char[new_token_key]["skills"]:
                if skill["skillId"] and skill_id not in json_skillTL.keys():
                    skill_id = skill["skillId"]
                    skill_tl[skill_id] = {
                                            "name"  : json_skill[skill_id]["levels"][0]["name"],
                                            "desc"  : [parentheses(json_skill[skill_id]["levels"][x]["description"]) if len(json_skill[skill_id]["levels"]) == 10 else json_skill[skill_id]["levels"][0]["description"] for x in range(10)]
                                        }

def parentheses(desc : str) -> str :
    clean_dict = {
                    r'(’)'              : "'",
                    r'(。)'             : ". ",
                    r'(…)'              : "...",
                    r'(，|、| +, )'     : ", ",
                    r'(“|”)'            : "\"",
                    r'【'               : " [",
                    r'】'               : "] ",
                    r'（'               : " (",
                    r'）'               : ") ",
                    r'；'	            : "; ",
                    r'？'               : "? ",
                    r'！'               : "! ",
                    r'[  ]+'            : " ",
                    r'％'              	: "%",
                }
    
    if isinstance(desc, NoneType):
        return None
    else:
        for k,v in clean_dict.items():
            desc = re.sub(k, v, desc)
        return desc

#########################################################################################################
# Chars
#########################################################################################################
skip_char   = []
talent_tl   = {}
skill_tl    = {}
for new_char_name in NEW_CHARS:
    if new_char_name not in char_list:
        try:
            update_char_TraitSkillTalent(new_char_name)
        except:
            skip_char.append(new_char_name)

    if Rechecked and new_char_name in char_list:
        update_char_TraitSkillTalent(new_char_name)

#Update old char
for char_data in json_akhr:
    char_data["nationId"]   = json_char[char_data["id"]]["nationId"]
    char_data["groupId"]    = json_char[char_data["id"]]["groupId"]
    char_data["teamId"]     = json_char[char_data["id"]]["teamId"]
    char_data["subPower"]   = json_char[char_data["id"]]["subPower"]
    for lang in [["name_en", json_charEN],["name_jp", json_charJP], ["name_kr", json_charKR]]:
        if char_data["id"] in lang[1].keys():
            char_data[lang[0]] = lang[1][char_data["id"]]["name"]

#Update recruitment
def cleanlist(recruit_list:str) -> str:
    return recruit_list.replace("\\n", "\n").replace("/", " / ").replace("  ", " ").replace("< / ", "</")

gacha_CN_list   =   cleanlist(json_gacha["recruitDetail"]).split("\n")
gacha_EN_list   =   cleanlist(json_gachaEN["recruitDetail"]).split("\n")

bypass          =   {
                        #"THRM-EX"               :   "Thermal-EX",
                        #"\'Justice Knight\'"    :   "\"Justice Knight\"",
                        "Justice Knight"        :   "\'Justice Knight\'",
                        #"Shirayuki"             :   "ShiraYuki",
                        "Mr.Nothing"            :   "Mr. Nothing",
                    }

for i in range(6):
    ##CN
    for ops in gacha_CN_list[gacha_CN_list.index("★" * (i + 1)) + 1].split(" / "):
        op_search = re.search(r"<@rc.eml>(.+?)</>", ops)
        op = (op_search.group(1) if op_search else ops).replace("\r", "")
        json_akhr[[index for index, data in enumerate(json_akhr) if data["name_cn"] == op][0]]["hidden"] = False
    ##EN
    for ops in gacha_EN_list[gacha_EN_list.index("★" * (i + 1)) + 1].split(" / "):
        op_search = re.search(r"<@rc.eml>(.+?)</>", ops)
        op = op_search.group(1) if op_search else ops
        json_akhr[[index for index, data in enumerate(json_akhr) if name_check(data["name_en"]) == bypass.get(op, op)][0]]["globalHidden"] = False

with open("json/tl-akhr.json", "w", encoding = "utf-8") as filepath :
    json.dump(json_akhr, filepath, indent = 4, ensure_ascii = False)
    
with open("update/tl-talent.json", "w", encoding = "utf-8") as filepath :
    json.dump(talent_tl, filepath, indent = 4, ensure_ascii = False)

with open("update/tl-skill.json", "w", encoding = "utf-8") as filepath :
    json.dump(skill_tl, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# Mats
#########################################################################################################
#akmatuses.html
mat_button : list[str] = []
for new_mat in NEW_MATS:
    mat_button.append(f'<button type="button" onclick="clickBtnTag(this)" class="btn btn-sm btn-secondary ak-btn btn-tag my-1 button-tag" data-toggle="tooltip" data-placement="top" title="{json_item["items"][new_mat]["name"]}" mat-id="{new_mat}"></button>')

mat_button.sort(reverse = False,key = lambda new_mat : new_mat.split("\"")[-2][0:-1]) #sort mat id
mat_button.sort(reverse = True, key = lambda new_mat : new_mat.split("\"")[-2][-1]) #sort rarity

with open("update/akmatuses.txt", "w", encoding = "utf-8") as writer:
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
    mat_id = mat_data["itemId"]
    for lang in [["name_en", json_itemEN], ["name_jp", json_itemJP], ["name_kr", json_itemKR]]:
        key = lang[0]
        item_json = lang[1]
        if mat_data[key] == "":
            if mat_id in item_json["items"]:
                mat_data[key] = item_json["items"][mat_id]["name"]
    mat_data["IconID"] = json_item["items"][mat_id]["iconId"]
    for key in ["id", "itemId", "IconID", "name_cn", "name_en", "name_jp", "name_kr", "name_tw", "level", "source", "madeof"]:
        temp = mat_data[key]
        mat_data.pop(key)
        mat_data[key] = temp

with open("json/akmaterial.json", "w", encoding = "utf-8") as filepath :
    json.dump(json_akmaterial, filepath, indent = 4, ensure_ascii = False)

##tl-item.json
for mat_data in json_tl_item:
    mat_id = mat_data["itemId"]
    mat_data["iconId"] = json_item["items"][mat_id]["iconId"]
    mat_data["rarity"] = json_item["items"][mat_id]["rarity"]
    for lang in [["name_en", json_itemEN], ["name_jp", json_itemJP], ["name_kr", json_itemKR]]:
        key = lang[0]
        item_json = lang[1]
        if mat_data[key] == "":
            if mat_id in item_json["items"].keys():
                mat_data[key] = item_json["items"][mat_id]["name"]
    for key in ["itemId", "iconId", "rarity", "name_cn", "name_en", "name_jp", "name_kr", "name_tw"]:
        if not key in mat_data : continue
        temp = mat_data[key]
        mat_data.pop(key)
        mat_data[key] = temp
    

with open("json/tl-item.json", "w", encoding = "utf-8") as filepath :
    json.dump(json_tl_item, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# Mod
#########################################################################################################   
newmods = json_mod_table["equipTrackDict"][-1]["trackList"]
NEW_MODS = [[newmods[i]["charId"], newmods[i]["equipId"]] for i in range(len(newmods)) if not re.search("_001_", newmods[i]["equipId"])]
skip_mod = ""
mod_tl = {}

for new_mod_list in NEW_MODS:
    if new_mod_list[1] in json_temp_mod.keys():
        continue
    try:
        char_key = new_mod_list[0]
        new_mod_id = new_mod_list[1]
        mod_trait_candidate = json_mod_battle[new_mod_id]["phases"][0]["parts"][0]["overrideTraitDataBundle"]["candidates"][0]
        if mod_trait_candidate["additionalDescription"]:
            new_trait[mod_trait_candidate["additionalDescription"]] = update_new_trait("mod", new_mod_id, new_mod_list[0], json_mod_table["equipDict"][new_mod_id]["typeIcon"])
        else :
            new_trait[mod_trait_candidate["overrideDescripton"]]    = update_new_trait("mod", new_mod_id, new_mod_list[0], json_mod_table["equipDict"][new_mod_id]["typeIcon"])
        temp_phase = []
        for phase in [1, 2]:
            for part in json_mod_battle[new_mod_id]["phases"][phase]["parts"]:
                temp_part = []
                if part["target"] in ["TALENT_DATA_ONLY","TALENT"] and not part["isToken"] and part["addOrOverrideTalentDataBundle"]["candidates"][0]["upgradeDescription"] != "":
                    for pot in range(len(part["addOrOverrideTalentDataBundle"]["candidates"])):
                        candidate = part["addOrOverrideTalentDataBundle"]["candidates"][pot]
                        talent_candidate_CN = json_char[char_key]["talents"][candidate["talentIndex"]]["candidates"][pot-len(part["addOrOverrideTalentDataBundle"]["candidates"])]
                        talent_candidate_EN = json_charEN[char_key]["talents"][candidate["talentIndex"]]["candidates"][pot-len(part["addOrOverrideTalentDataBundle"]["candidates"])] if char_key in json_charEN.keys() else {}
                        if char_key in json_charEN and candidate["talentIndex"] != -1:
                            temp_part.append({
                                                "name"                  :   talent_candidate_EN["name"],
                                                "EN"                    :   talent_candidate_EN["description"],
                                                "CN"                    :   parentheses(talent_candidate_CN["description"]),
                                                "mod"                   :   parentheses(candidate["upgradeDescription"]),
                                                "upgradeDescription"    :   ""
                                            })
                        else:
                            temp_part.append({
                                                "name"                  :   candidate["name"],
                                                "CN"                    :   parentheses(talent_candidate_CN["description"]),
                                                "mod"                   :   parentheses(candidate["upgradeDescription"]),
                                                "upgradeDescription"    :   ""
                                            })
                if len(temp_part) :temp_phase.append(temp_part)
        mod_tl[new_mod_id] = temp_phase
    except:
        skip_mod += f'\n\t{new_mod_list[0]} --- {new_mod_list[1]}'

with open("update/tl-module.json", "w", encoding = "utf-8") as filepath :
    json.dump(mod_tl, filepath, indent = 4, ensure_ascii = False)

poplist = []
for mod in json_temp_mod.keys():
    if mod in json_mod_battleEN.keys():
        poplist.append(mod)
for mod in poplist:
    json_temp_mod.pop(mod)

with open("json/tl-module.json", "w", encoding = "utf-8") as filepath :
    json.dump(json_temp_mod, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# Trait
#########################################################################################################
pop = []
for key in new_trait.keys():
    if key in json_trait["full"].keys():
        pop.append(key)
for key in pop:
    new_trait.pop(key)

with open("update/tl-attacktype.json", "w", encoding = "utf-8") as filepath :
    json.dump(new_trait, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# Termology Update
#########################################################################################################
for term in json_construct["termDescriptionDict"]:
    if term not in json_term["termDescriptionDict"].keys():
        json_term["termDescriptionDict"][term] = {k:parentheses(json_construct["termDescriptionDict"][term][k]) for k in json_construct["termDescriptionDict"][term].keys()}

for term in json_term["termDescriptionDict"].keys():
    if term in json_constructEN["termDescriptionDict"].keys() :
        json_term["termDescriptionDict"][term] = json_constructEN["termDescriptionDict"][term]
        
with open("json/named_effects.json", "w", encoding = "utf-8") as filepath :
    json.dump(json_term, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# TL Artist CN -> EN (JSON Compare)
#########################################################################################################
json_artist = {"Illustrator" : {}, "VA" : {}}
artist_dupe_catch : list[str] = []

# Illustrator
## Skin_table
for skin in json_skin["charSkins"].keys():
    if skin in json_skinEN["charSkins"].keys():
        for dlist in ["drawerList", "designerList"]:
            if json_skin["charSkins"][skin]["displaySkin"][dlist]:
                if len(json_skin["charSkins"][skin]["displaySkin"][dlist]) > 1: printr("NEW Illustrator Dlist JUST DROP !!!")
                CN_skin_artist = json_skin["charSkins"][skin]["displaySkin"][dlist][0].strip()
                EN_skin_artist = json_skinEN["charSkins"][skin]["displaySkin"][dlist][0].strip()
                if CN_skin_artist != EN_skin_artist:
                    if CN_skin_artist in json_artist["Illustrator"].keys() and json_artist["Illustrator"][CN_skin_artist] != EN_skin_artist:
                        artist_dupe_catch.append(f'\n\t{CN_skin_artist} {json_artist["Illustrator"][CN_skin_artist]} {EN_skin_artist}')
                    else :
                        json_artist["Illustrator"][CN_skin_artist] = EN_skin_artist
## npcDict
for npc in json_handbook["npcDict"].keys():
    if npc in json_handbookEN["npcDict"].keys():
        for dlist in ["illustList", "designerList"]:
            if json_handbook["npcDict"][npc][dlist]:
                if len(json_handbook["npcDict"][npc][dlist]) > 1: printr("NEW Illustrator Dlist JUST DROP !!!")
                CN_skin_artist = json_handbook["npcDict"][npc][dlist][0].strip()
                EN_skin_artist = json_handbookEN["npcDict"][npc][dlist][0].strip()
                if CN_skin_artist != EN_skin_artist:
                    if CN_skin_artist in json_artist["Illustrator"].keys() and json_artist["Illustrator"][CN_skin_artist] != EN_skin_artist:
                        artist_dupe_catch.append(f'\n\t{CN_skin_artist} {json_artist["Illustrator"][CN_skin_artist]} {EN_skin_artist}')
                    else :
                        json_artist["Illustrator"][CN_skin_artist] = EN_skin_artist

# Voice Actor
    for op in json_charword["voiceLangDict"].keys():
        if op in json_charwordEN["voiceLangDict"].keys():
            for lang in json_charword["voiceLangDict"][op]["dict"].keys():
                if lang in json_charwordEN["voiceLangDict"][op]["dict"].keys():
                    VA_CN = json_charword["voiceLangDict"][op]["dict"][lang]["cvName"][0].strip()
                    VA_EN = json_charwordEN["voiceLangDict"][op]["dict"][lang]["cvName"][0].strip()
                    if VA_CN != VA_EN :
                        if VA_CN in json_artist["VA"].keys() and json_artist["VA"][VA_CN] != VA_EN:
                            artist_dupe_catch.append(f'\n\t{op} {VA_CN} {json_artist["VA"][VA_CN]} {VA_EN}')
                        else :
                            json_artist["VA"][VA_CN] = VA_EN

with open("json/tl-artist.json", "w", encoding = "utf-8") as filepath :
    json.dump(json_artist, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# Stage_table
#########################################################################################################
stage_json = {}

for stage in json_stage["stages"].keys():
    def skip_stage(stage : str):
        for skip in ["bossrush_", "_st", "_tr", "break_", "enemyduel_", "multi_", "arcade_", "autochess_", "vecb_", "_mo", "multi-", "lock_"]:
            if stage.find(skip) != -1:
                return True
        return False
        
    if stage.startswith(("tr_", "lt_", "camp_", "st_", "spst_", "easy_", "tough_", "wk_", "pro_", "guide_")) or stage.endswith(("#f#","#s")) or skip_stage(stage):
        continue
    stage_json[stage] = json_stage["stages"][stage]["code"]

with open("json/puppiiz/stage_code.json", "w", encoding = "utf-8") as filepath :
    json.dump(stage_json, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# enemy_table
#########################################################################################################
enemy_json = {}

for enemy in json_enemy["enemyData"].keys():
    if enemy in json_enemyEN["enemyData"].keys():
        enemy_json[enemy] = json_enemyEN["enemyData"][enemy]["name"]
    else :
        enemy_json[enemy] = json_enemy["enemyData"][enemy]["name"]

with open("json/puppiiz/enemy_name.json", "w", encoding = "utf-8") as filepath :
    json.dump(enemy_json, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# potential_token
#########################################################################################################
potential_token = {}

for char in json_char.keys():
    token_id = json_char[char]["potentialItemId"] or json_char[char]["activityPotentialItemId"]
    
    if not token_id or not char.startswith("char") or json_char[char]["isNotObtainable"]:
        continue
    
    item_json = json_itemEN if token_id in json_itemEN["items"].keys() else json_item
    
    potential_token[token_id] = {
                                    "description"   : item_json["items"][token_id]["description"],
                                    "usage"         : item_json["items"][token_id]["usage"]
                                }

with open("json/puppiiz/potential_token.json", "w", encoding = "utf-8") as filepath :
    json.dump(potential_token, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# char_names
#########################################################################################################
sp_char_dict = {
                    "ë" : "e",  # Pozëmka
                    "ł" : "l",  # Młynar
                    "í" : "i",  # Eyjafjalla the Hvít Aska
                    "š" : "s",  # Wiš'adel
                    "ū" : "u",  # Yūtenji Nyamu
                }

def simple_name(char_name : str) -> str:
    for sp_char in sp_char_dict.keys():
        if char_name.find(sp_char) != -1:
            return False
    return True

def get_name(char_data : dict) -> list:
    names : list[str] = []
    for key in ["name", "appellation"]:
        value : str = char_data[key]
        if value and value != " ":
            names.append(value)
            if not simple_name(value) :
                names += [value.replace(k, v) for k, v in sp_char_dict.items() if value.find(k) != -1]
    return names + [name.replace("'", "") for name in names if name.find("'") != -1]

char_names = {}
for char_id in json_char.keys():
    if not char_id.startswith("char_") : continue
    char_name = get_name(json_char[char_id]) + [URSUS.get(json_char[char_id]["appellation"], json_char[char_id]["appellation"])]
    for other_lang in [json_charEN, json_charJP, json_charKR]:
        if char_id in other_lang.keys():
            char_name += get_name(other_lang[char_id])
    char_names[char_id] = sorted(list(set(char_name)))

with open("json/puppiiz/char_names.json", "w", encoding = "utf-8") as filepath :
    json.dump(char_names, filepath, indent = 4, ensure_ascii = False)

#########################################################################################################
# The Rest
#########################################################################################################
Akenemy()
riic_tl_json()
audio_json()

if skip_char:
    printr(f'{Y}NEW CHAR{RE} skip list = {", ".join([f'{G}{skip_char[i]}{RE}' if i % 2 == 0 else f'{B}{skip_char[i]}{RE}' for i in range(len(skip_char))])}')
if skip_mod:
    printr(f'NEW MOD skip list = {skip_mod}')
if artist_dupe_catch :
    printr(f'Artist Conflict list -> {artist_dupe_catch}')

printr("pyUpdate Completed !!!\n")