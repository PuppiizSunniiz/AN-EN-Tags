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

json_team_handbook  =   json.loads(open("json/gamedata/en_US/gamedata/excel/handbook_team_table.json").read())

json_akhr           =   json.loads(open("json/tl-akhr.json").read())

#########################################################################################################
# Prep
#########################################################################################################
Classparse= {'SNIPER':"狙击", 'PIONEER':"先锋", 'TANK':"重装",  'MEDIC':"医疗", 'SUPPORT':"辅助", 'SPECIAL':"特种", 'WARRIOR':"近卫",  'CASTER':"术师"}

#########################################################################################################
# Test Area
#########################################################################################################
testhr=[]

nation=[]
nationjson=[]
group=[]
groupjson=[]
team=[]
teamjson=[]
HTMLjson=[]

for char in json_akhr:
    #print(char["id"])
    testhr.append({
                        "id":                   char["id"],
                        "name_cn":              json_char[char["id"]]["name"],
                        "name_en":              json_char[char["id"]]["appellation"],
                        "name_jp":              json_charJP[char["id"]]["name"] if char["id"] in json_charJP.keys() else "",
                        "name_kr":              json_charKR[char["id"]]["name"] if char["id"] in json_charKR.keys() else "",
                        #"characteristic_cn":    char["characteristic_cn"],
                        #"characteristic_en":    char["characteristic_en"],
                        #"characteristic_jp":    char["characteristic_jp"],
                        #"characteristic_kr":    char["characteristic_kr"],
                        "nationId":             json_char[char["id"]]["nationId"],
                        "groupId":              json_char[char["id"]]["groupId"],
                        "teamId":               json_char[char["id"]]["teamId"],
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
                        "globalHidden":         char["globalHidden"] if "globalHidden" in char.keys() else False
    })
    if json_char[char["id"]]["nationId"] :
        nation.append(json_char[char["id"]]["nationId"])      
    if json_char[char["id"]]["groupId"] :
        group.append(json_char[char["id"]]["groupId"]) 
    if json_char[char["id"]]["teamId"] :
        team.append(json_char[char["id"]]["teamId"])   
        
        
print("nation =",set(nation))
print("group =",set(group))
print("team =",set(team))

#<div class="op-faction btn-secondary tooltip2" data-id="LOGO_BLACKSTEEL" onclick="toggleBtn(this)" section="faction"><img class='faction-img'  src='https://raw.githubusercontent.com/Aceship/Arknight-Images/main/factions/logo_blacksteel.png'><span class="tooltiptext tooltiptop tooltipstyle1 nohover">Blacksteel Worldwide</span></div>

for nationID in set(nation):
    nationjson.append({
                        "id" : nationID,
                        "order" : json_team_handbook[nationID]["orderNum"],
                        "Name": json_team_handbook[nationID]["powerName"],
                        "HTML" : "<div class=\"op-faction btn-secondary tooltip2\" data-id=\""+nationID+"\" onclick=\"toggleBtn(this)\" section=\"faction\"><img class='faction-img'  src='https://raw.githubusercontent.com/Aceship/Arknight-Images/main/factions/logo_"+nationID+".png'><span class=\"tooltiptext tooltiptop tooltipstyle1 nohover\">"+json_team_handbook[nationID]["powerName"]+"</span></div>"
    })
nationjson.sort(reverse=False,key=lambda x : x["order"])

for groupID in set(group):
    groupjson.append({
                        "id" : groupID,
                        "order" : json_team_handbook[groupID]["orderNum"],
                        "Name": json_team_handbook[groupID]["powerName"],
                        "HTML" : "<div class=\"op-faction btn-secondary tooltip2\" data-id=\""+groupID+"\" onclick=\"toggleBtn(this)\" section=\"faction\"><img class='faction-img'  src='https://raw.githubusercontent.com/Aceship/Arknight-Images/main/factions/logo_"+groupID+".png'><span class=\"tooltiptext tooltiptop tooltipstyle1 nohover\">"+json_team_handbook[groupID]["powerName"]+"</span></div>"
    })
groupjson.sort(reverse=False,key=lambda x : x["order"])

for teamID in set(team):
    teamjson.append({
                        "id" : teamID,
                        "order" : json_team_handbook[teamID]["orderNum"],
                        "Name": json_team_handbook[teamID]["powerName"],
                        "HTML" : "<div class=\"op-faction btn-secondary tooltip2\" data-id=\""+teamID+"\" onclick=\"toggleBtn(this)\" section=\"faction\"><img class='faction-img'  src='https://raw.githubusercontent.com/Aceship/Arknight-Images/main/factions/logo_"+teamID+".png'><span class=\"tooltiptext tooltiptop tooltipstyle1 nohover\">"+json_team_handbook[teamID]["powerName"]+"</span></div>"
    })
teamjson.sort(reverse=False,key=lambda x : x["order"])

for faction in nationjson+groupjson+teamjson:
    HTMLjson.append(faction["HTML"])



#########################################################################################################
# Dumb
#########################################################################################################
modDict={}

dumpling=json.dumps(testhr,indent=4, ensure_ascii=False)
with open("test/test-akhr.json",'w') as JSON :
    JSON.write(dumpling)
    
dumpling=json.dumps({"nation":nationjson,"group":groupjson,"team":teamjson,"HTML":("\n").join(HTMLjson)},indent=4, ensure_ascii=False)
with open("test/test-nationtag.json",'w') as JSON :
    JSON.write(dumpling)
