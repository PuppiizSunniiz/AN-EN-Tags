import json
import re
from pyfunction import json_load, printr, script_result

def special_op():
    json_special = json_load(r"json\gamedata\ArknightsGameData\zh_CN\gamedata\excel\special_operator_table.json")

    sp_op : dict = {}

    for char in json_special["nodeUnlockMissionGroup"].keys():
        char_dict : dict = {}
        
        mission_list : list[str] = json_special["nodeUnlockMissionGroup"][char]["missionIds"]
        
        for mission in mission_list:
            mission_data    : dict  = json_special["nodeUnlockMissionData"][mission]
            mission_desc    : str   = mission_data["description"]
            mission_to      : str   = mission.split("_")[2]
            mission_type    : str   = mission.split("_")[1]
            
            if mission_type == "evolve":
                char_dict.setdefault(mission_type, {}).setdefault("unlock", ["" for _ in range(2)])
                elite_phase = int(mission_to[-1]) - 1
                char_dict[mission_type]["unlock"][elite_phase] = mission_desc
            elif mission_type == "skill" :
                char_dict.setdefault(mission_type, {}).setdefault("unlock", ["" for _ in range(7)])
                skill_end = int(mission_to[-1])
                skill_start = skill_end - 3
                char_dict[mission_type]["unlock"] = [mission_desc if skill_start <= lv < skill_end else char_dict[mission_type]["unlock"][lv] for lv in range(7)]
            elif re.match(r'master[\d]', mission_type) :
                char_dict.setdefault(mission_type, {}).setdefault("unlock", ["" for _ in range(3)])
                master_phase = int(mission_to[-1]) - 1
                char_dict[mission_type]["unlock"][master_phase] = mission_desc
            elif re.match(r'skill[\d]', mission_type) :
                char_dict.setdefault(mission_type, {}).setdefault("unlock", ["" for _ in range(3)])
                skill_lv = int(re.search(r'^(?:\D*|)([\d]*)$', mission_to).group(1)) - 7 - 1
                char_dict[mission_type]["unlock"][skill_lv] = mission_desc
            elif re.match(r'uniequip[\d]', mission_type) :
                char_dict.setdefault(mission_type, {}).setdefault("unlock", ["" for _ in range(3)])
                mod_lv = int(mission_to) - 1
                char_dict[mission_type]["unlock"][mod_lv] = mission_desc
            else:
                printr(f'Mission type new case !!! : {mission_type} ({char})')
            
        sp_op[char] = char_dict
    
    return sp_op

if __name__ == "__main__":
    script_result(special_op(), True)
else:
    with open(r"json\puppiiz\special_operator.json", "w", encoding = "utf-8") as filepath :
        json.dump(special_op(), filepath, indent = 4, ensure_ascii = False)