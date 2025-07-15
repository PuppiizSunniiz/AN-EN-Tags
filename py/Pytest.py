import json
import re
from pyfunction import char_ready, name_check, json_load
#from pyUpdate import update_new_trait

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
ops = {}
json_test = []
for op in json_akhr:
    ops[op["id"]] = op

with open("temp/txt.txt", "r", encoding="utf-8") as starter :
    for i in list(starter):
        op = i.replace("\n","")
        json_test.append(ops[op])

with open("test/test.json", "w", encoding="utf-8") as filepath :
    json.dump(json_test,filepath,indent = 4, ensure_ascii = False)