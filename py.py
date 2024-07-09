import json
import re
from pyfunction import epoch,json_load

#########################################################################################################
# JSON
#########################################################################################################
json_char       =   json_load("json/gamedata/zh_CN/gamedata/excel/character_table.json")
json_char_patch =   json_load("json/gamedata/zh_CN/gamedata/excel/char_patch_table.json")
json_mod        =   json_load("json/gamedata/zh_CN/gamedata/excel/uniequip_table.json")
json_range      =   json_load("json/gamedata/zh_CN/gamedata/excel/range_table.json")

#########################################################################################################
# Function
#########################################################################################################
def msgbox(msg) -> str:
    if isinstance(msg,str):
        repeat = len(msg) + 8
        return f'{"#" * repeat}\n#   {msg}   #\n{"#" * repeat}'
    elif isinstance(msg,list):
        repeat = max(map(len,msg)) + 15
        return f'{"#" * repeat}'+"\n#    ".join(msg)+f' \n{"#" * repeat}'

def continue_check(menu_msg="") -> bool:
    print(msgbox(f'Continue {menu_msg}? (Y/N) | 0 : Exit'))
    answer=input().strip()
    match answer.lower():
        case "n":
            return False
        case "y":
            return True
        case "0":
            exit()
        case _:
            return continue_check(menu_msg)

def get_char_name(char_key) -> str:
    '''
        Get char_key as Char key
        
        Check if appellation in Russian
        
        Return as Eng name
    '''
    Russian = {'Гум': 'Gummy', 'Зима': 'Zima', 'Истина': 'Istina', 'Позёмка': 'Pozëmka', 'Роса': 'Rosa','Лето':'Leto'}
    appellation = json_char[char_key]["appellation"]    
    return Russian.get(appellation,appellation)

def char_check():
    def Charout(text,mode):
        print(msgbox(f'What "{text}" to check ?'))
        char_input=input().strip()
        
        if re.search(r'".+"',char_input):
            char_input=char_input[1:-1]
        
        char_result=[[char_key,DB["Char"][mode][char_key]] for char_key in DB["Char"][mode].keys() if char_input.lower() in char_key.lower()]
        if char_result:
            print("Result :")
            for char in char_result:
                print(f'\t{char}')
            print(f'\n\tSearch result : {len(char_result)}')
        else:
            print(f'\nNo Char Code with "{char_input}" exist')
        
        if continue_check(mode):
            Charout(text,mode)
        
    print(msgbox(["\n#  Select Mode",
                        "1 : Char Name from Char Code",
                        "2 : Char Code from Char Name",
                        "0 : Exit"
                ]))
    
    char_input=input().strip()
    match char_input:
        case "0":
            return False
        case "1":
            Charout("Char Code","Code2Name")
        case "2":
            Charout("Char Name","Name2Code")
        case _:
            return char_check()
        
    return continue_check("Character Name/Code check")

def mod_check():
    print(msgbox('What Module Num to check ? (1/2/3 or 0 : Exit)'))
    mod_num=input().strip()
    
    if mod_num == "0" :
        return False
    elif mod_num not in ["1","2","3"]:
        mod_check()
        
    mod_num = int(mod_num)
    
    mod_result = [f'{get_char_name(mod_key)} -- {mod_key}' for mod_key, mod_value in json_mod["charEquip"].items() if len(mod_value)>mod_num]

    mod_result.sort()
    mod_result.append("Search result :"+str(len(mod_result)))
    print("\n".join(mod_result))
    return continue_check("Module check")

def range_check():
    print(msgbox("What Range to check ? (S: Show All Range | 0 : Exit)"))
    range_id=input().strip().lower()
    
    if range_id == "0":
        return False
    elif range_id == "s":
        print(list(DB["Range"].keys()))
        return True
    elif range_id not in DB["Range"].keys():
        print(f'{range_id} is not a valid Range ID')
        return continue_check("Range check")
    else :
        print("\n".join(DB["Range"][range_id]))
        return continue_check("Range check")
    
def time_check():
    print(msgbox("What Epoch time to check ? (0 : Exit)"))
    time = int(input())
    
    if time == "0":
        return False
    else :
        try :
            print(f'\nEpoch time = {epoch(time)}')
        except :
            print("Invalid epoch times")
        return continue_check("Epoch time check")

'''
    def Tagcheck():
        print(msgbox("What Tag(s) to check ? (up to 5 tags | 0 : Exit)"))
        tags=input().strip()
    
        if tags=="0":
            return False
        else :
            tagscheck(tags)
    
        def tagscheck(tags):
            tags = tags.split(" ")
            for i in range(len(tags)):
                match tags[i]:
					case "guard":
					    tags[i] = 近卫干员		#Guard
					case "sni":
					    tags[i] = 狙击干员		#Sniper
					case "defender":
					    tags[i] = 重装干员		#Defender
					case "medic":
					    tags[i] = 医疗干员		#Medic
					case "sup":
					    tags[i] = 辅助干员		#Supporter
					case "caster":
					    tags[i] = 术师干员		#Caster
					case "spec":
					    tags[i] = 特种干员		#Specialist
					case "van":
					    tags[i] = 先锋干员		#Vanguard
					case "melee":
					    tags[i] = 近战位		#Melee
					case "range":
					    tags[i] = 远程位		#Ranged
					case "top":
					    tags[i] = 高级资深干员	#Top Operator
					case "cc":
					    tags[i] = 控场			#Crowd-Control
					case "nuker":
					    tags[i] = 爆发			#Nuker
					case "senior":
					    tags[i] = 资深干员		#Senior Operator
					case "heal":
					    tags[i] = 治疗			#Healing
					case "support":
					    tags[i] = 支援			#Support
					case "starter":
					    tags[i] = 新手			#Starter
					case "dp":
					    tags[i] = 费用回复		#DP-Recovery
					case "dps":
					    tags[i] = 输出			#DPS
					case "survival":
					    tags[i] = 生存			#Survival
					case "aoe":
					    tags[i] = 群攻			#AoE
					case "defense":
					    tags[i] = 防护			#Defense
					case "slow":
					    tags[i] = 减速			#Slow
					case "debuff":
					    tags[i] = 削弱			#Debuff
					case "frd":
					    tags[i] = 快速复活		#Fast-Redeploy
					case "shift":
					    tags[i] = 位移			#Shift
					case "summon":
					    tags[i] = 召唤			#Summon
					case "robot":
					    tags[i] = 支援机械		#Robot
					case "male":
					    tags[i] = 男性干员		#Male
					case "female":
					    tags[i] = 女性干员		#Female
            recruitment()
'''
#########################################################################################################
# Ready
#########################################################################################################
DB={}

ClassParse = {
                "MEDIC"     : "Medic",         "WARRIOR"    : "Guard",
                "SPECIAL"   : "Specialist",    "SNIPER"     : "Sniper",
                "PIONEER"   : "Vanguard",      "CASTER"     : "Caster",
                "SUPPORT"   : "Supporter",     "TANK"       : "Defender"
            }

for char_key in json_char_patch["patchChars"].keys():
    json_char_patch["patchChars"][char_key]["appellation"] += f' ({ClassParse[json_char_patch["patchChars"][char_key]["profession"]]})'
json_char.update(json_char_patch["patchChars"])

char_ready={"Code2Name":{},"Name2Code":{}}
ops_exclude=[] # "isNotObtainable": true
for char_key in json_char.keys():
    if "char_" in char_key:
        char_ready["Code2Name"][char_key]=get_char_name(char_key)
        char_ready["Name2Code"][get_char_name(char_key)]=char_key
        if json_char[char_key]["isNotObtainable"]:
            ops_exclude.append(char_key)
DB["Char"]=char_ready

range_ready={} # 🟥🟧🟨🟩🟦🟪🟫⬛⬜🔳
for range_id in json_range.keys():
    
    temp =[[grid["col"],grid["row"]] for grid in json_range[range_id]["grids"]]
    
    max_x=max([x[0] for x in temp])
    min_x=min([x[0] for x in temp]+[0])
    max_y=max([y[1] for y in temp])
    min_y=min([y[1] for y in temp]+[0])
    
    range_array=[["⬛" for x in range(max_x - min_x + 1)] for y in range(max_y - min_y + 1)]
    
    range_array[max_y][abs(min(0, min_x))]="🔳"

    for col, row in temp:
        if [col, row] == [0,0]:
            range_array[row + max_y][col + abs(min(0, min_x))]="🟨"
        else:
            range_array[row + max_y][col + abs(min(0, min_x))]="🟦"
    
    range_ready[range_id] = ["".join(row) for row in range_array] + [str(temp)]
    
DB["Range"]=range_ready

tag_ready={}
for char in char_ready["Code2Name"].keys():
    tag_ready[char_ready["Code2Name"][char]]=["高级资深干员" for x in range(1) if json_char[char]["rarity"][-1]=="6"]+ \
                                            ["资深干员" for x in range(1) if json_char[char]["rarity"][-1]=="5"]+ \
                                            ["新手" for x in range(1) if json_char[char]["rarity"][-1]=="2"]+ \
                                            ["近战位" for x in range(1) if json_char[char]["position"]=="MELEE"]+ \
                                            ["远程位" for x in range(1) if json_char[char]["position"]=="RANGED"]+ \
                                            json_char[char]["tagList"]
DB["Tag"]=tag_ready

with open('py/dict.json', 'w', encoding='utf-8') as file:
    json.dump(DB, file, indent=4, ensure_ascii=False)

tag_ready={}

'''
    json_gacha  =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/gacha_table.json").read())
    json_gachaEN  =   json.loads(open("json/gamedata/en_US/gamedata/excel/gacha_table.json").read())
    gachapon={}
    for tag in json_gacha["gachaTags"]:
        gachapon[tag["tagId"]]={"tagName":tag["tagName"]}
    for tag in json_gachaEN["gachaTags"]:
        gachapon[tag["tagId"]].update({"EN":tag["tagName"]})
    gacha=json.dumps(gachapon,indent=4, ensure_ascii=False)
    with open('temp/tag.json','w') as JSON:
        JSON.write(gacha)
        
    tagstr=[]
    for key in gachapon.keys():
        tagstr.append("\t"*5+"case \""+gachapon[key]["EN"].lower()+"\":\n"+"\t"*6+"tags[i] = "+gachapon[key]["tagName"]+"\t"*round(4-len(gachapon[key]["tagName"])/2)+"#"+gachapon[key]["EN"])
    gachastr=("\n").join(tagstr)
    with open('temp/tag.txt','w') as JSON:
        JSON.write(gachastr)
'''

#########################################################################################################
# Go !!!
#########################################################################################################
while True:
    menu_option = ["\n#  Select Function",
                    "1 : Char Name/Code Check",
                    "M : Mod Check",
                    "R : Range Check",
                    "T : Time Epoch",
                    "0 : Exit"
                    ]
    print(msgbox(menu_option))
    menu_input = input().strip()
    match menu_input.lower():
        case "0":
            exit()
        case "1":
            char_check()
        case "m":
            mod_check()
        case "r":
            range_check()
        case "t":
            time_check()
        case _:
            continue