import json
import re
from pyfunction import char_ready, name_check, json_load
from pyUpdate import update_new_trait

#########################################################################################################
# JSON
#########################################################################################################
json_char           =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/character_table.json")
json_charEN         =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/character_table.json")
json_charJP         =   json_load("json/gamedata/ArknightsGameData_YoStar/ja_JP/gamedata/excel/character_table.json")
json_charKR         =   json_load("json/gamedata/ArknightsGameData_YoStar/ko_KR/gamedata/excel/character_table.json")

json_skill          =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/skill_table.json")
json_skillEN        =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/skill_table.json")

json_mod_battle     =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/battle_equip_table.json")

json_mod_table      =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/uniequip_table.json")

json_handbook       =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_info_table.json")

json_team_handbook  =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/handbook_team_table.json")

json_akhr           =   json_load("json/tl-akhr.json")
json_temp_mod       =   json_load("json/tl-module.json")

#########################################################################################################
# Prep
#########################################################################################################
Classparse= {'SNIPER':"狙击", 'PIONEER':"先锋", 'TANK':"重装",  'MEDIC':"医疗", 'SUPPORT':"辅助", 'SPECIAL':"特种", 'WARRIOR':"近卫",  'CASTER':"术师"}

#########################################################################################################
# Test Area
#########################################################################################################
newmods = json_mod_table["equipTrackDict"][-1]["trackList"]
NEW_MODS = [[newmods[i]["charId"],newmods[i]["equipId"]] for i in range(len(newmods)) if not re.search("_001_",newmods[i]["equipId"])]

skip_mod = []
mod_tl = {}
new_trait ={}
for new_mod_list in NEW_MODS:
    
    try:
        char_key = new_mod_list[0]
        new_mod_id = new_mod_list[1]
        if new_mod_id in json_temp_mod.keys():
            print(char_key,new_mod_id,"Already in so skip")
            pass
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
        skip_mod.append(new_mod_list)
        

json_test = {
                "skip_mod"  : skip_mod,
                "mod_tl"    : mod_tl,
                "new_trait" : new_trait
             }

with open("test/test.json", "w", encoding="utf-8") as filepath :
    json.dump(json_test,filepath,indent = 4, ensure_ascii = False)