import json
from pyfunction import NameCheck

#########################################################################################################
# JSON
#########################################################################################################
json_char           =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/character_table.json").read())
json_charEN         =   json.loads(open("json/gamedata/en_US/gamedata/excel/character_table.json").read())
json_charJP         =   json.loads(open("json/gamedata/ja_JP/gamedata/excel/character_table.json").read())
json_charKR         =   json.loads(open("json/gamedata/ko_KR/gamedata/excel/character_table.json").read())

json_handbook       =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/handbook_info_table.json").read())

json_akhr           =   json.loads(open("test/tl-akhr.json").read())

#########################################################################################################
# Prep
#########################################################################################################
Classparse= {'SNIPER':"狙击", 'PIONEER':"先锋", 'TANK':"重装",  'MEDIC':"医疗", 'SUPPORT':"辅助", 'SPECIAL':"特种", 'WARRIOR':"近卫",  'CASTER':"术师"}

#########################################################################################################
# Test Area
#########################################################################################################
testhr=[]
for char in json_akhr:
    testhr.append({
                        "id":                   char["id"],
                        "name_cn":              json_char[char["id"]]["name"],
                        "name_en":              json_char[char["id"]]["appellation"],
                        "name_jp":              json_charJP[char["id"]]["name"] if char["id"] in json_charJP.keys() else "",
                        "name_kr":              json_charKR[char["id"]]["name"] if char["id"] in json_charKR.keys() else "",
                        "characteristic_cn":    char["characteristic_cn"],
                        "characteristic_en":    char["characteristic_en"],
                        "characteristic_jp":    char["characteristic_jp"],
                        "characteristic_kr":    char["characteristic_kr"],
                        "camp":                 char["camp"],
                        "type":                 Classparse[json_char[char["id"]]["profession"]],
                        "level":                int(json_char[char["id"]]["rarity"][-1]),
                        "sex":                  ''.join((json_handbook["handbookDict"][char["id"]]["storyTextAudio"][0]["stories"][0]["storyText"].split("\n")[1].split("】")[1]).split()) if char["id"] in json_handbook["handbookDict"] else "",
                        "tags":                 ["高级资深干员" for x in range(1) if json_char[char["id"]]["rarity"][-1]=="6"]+ \
                                                ["资深干员" for x in range(1) if json_char[char["id"]]["rarity"][-1]=="5"]+ \
                                                ###["新手" for x in range(1) if json_char[char["id"]]["rarity"][-1]=="2"]+ \
                                                ["近战位" for x in range(1) if json_char[char["id"]]["position"]=="MELEE"]+ \
                                                ["远程位" for x in range(1) if json_char[char["id"]]["position"]=="RANGED"]+ \
                                                json_char[char["id"]]["tagList"],
                        "hidden":               char["hidden"],
                        "globalHidden":         char["globalHidden"]
    })
#########################################################################################################
# Dumb
#########################################################################################################
modDict={}

dumpling=json.dumps(testhr,indent=4, ensure_ascii=False)
with open("test/test-akhr.json",'w') as JSON :
    JSON.write(dumpling)
