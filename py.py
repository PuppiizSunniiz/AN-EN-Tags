import json
import re
from pyfunction import epoch,json_load

#########################################################################################################
# JSON
#########################################################################################################
json_char       =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/character_table.json")
json_char_patch =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/char_patch_table.json")
json_mod        =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/uniequip_table.json")
json_range      =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/range_table.json")
json_dict       =   json_load("py/dict.json")

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
        
        char_result = [[char_key,DB["Char"][mode][char_key]] for char_key in DB["Char"][mode].keys() if char_input.lower() in char_key.lower()]
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
                        "1 : Char Code for Char Name",
                        "2 : Char Name for Char Code",
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
    elif range_id == "a":
        for key in DB["Range"].keys():
            range_img = "\n".join(DB["Range"][key])
            print(f'{key}\n{range_img}')
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

#########################################################################################################
# Ready
#########################################################################################################
def Ready(update = ""):
    DB = {}
    oldchar = list(json_dict["Char"]["Code2Name"].keys())

    ClassParse = {
                    "MEDIC"     : "Medic",         "WARRIOR"    : "Guard",
                    "SPECIAL"   : "Specialist",    "SNIPER"     : "Sniper",
                    "PIONEER"   : "Vanguard",      "CASTER"     : "Caster",
                    "SUPPORT"   : "Supporter",     "TANK"       : "Defender"
                }

    for char_key in json_char_patch["patchChars"].keys():
        json_char_patch["patchChars"][char_key]["appellation"] += f' ({ClassParse[json_char_patch["patchChars"][char_key]["profession"]]})'
    json_char.update(json_char_patch["patchChars"])

    char_ready = {
                    "Code2Name" :   {},
                    "Name2Code" :   {},
                    "CN2Code"   :   {}
                }
    ops_exclude = [] # "isNotObtainable": true
    for char_key in json_char.keys():
        if "char_" in char_key:

            char_ready["Code2Name"][char_key] = get_char_name(char_key)
            #char_ready["Code2Name"].setdefault(char_key,[]).append(get_char_name(char_key))
            char_ready["Name2Code"].setdefault(get_char_name(char_key),[]).append(char_key)
            char_ready["CN2Code"].setdefault(json_char[char_key]["name"],[]).append(char_key)
            if json_char[char_key]["isNotObtainable"]:
                ops_exclude.append(char_key)
    DB["Char"] = char_ready

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
        
    DB["Range"] = range_ready

    with open('py/dict.json', 'w', encoding='utf-8') as file:
        json.dump(DB, file, indent=4, ensure_ascii=False)
    
    if __name__ == "__main__" :
        return DB
    else:
        print("Ready !!!")
    
    if update:
        return list(DB["Char"]["Code2Name"].keys()) - oldchar
#########################################################################################################
# Go !!!
#########################################################################################################
def LetsGo():
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

if __name__ == "__main__" :
    DB = Ready()
    LetsGo()
