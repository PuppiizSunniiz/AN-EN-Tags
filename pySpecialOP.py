import json
import re
from pyfunction import json_load, printr, script_result

json_special        = json_load(r"json\gamedata\ArknightsGameData\zh_CN\gamedata\excel\special_operator_table.json")
json_specialEN      = json_load(r"json\gamedata\ArknightsGameData_YoStar\en_US\gamedata\excel\special_operator_table.json")

json_char_meta      = json_load(r"json\gamedata\ArknightsGameData\zh_CN\gamedata\excel\char_meta_table.json")
json_char_metaEN    = json_load(r"json\gamedata\ArknightsGameData_YoStar\en_US\gamedata\excel\char_meta_table.json")

json_rogue          = json_load(r"json\gamedata\ArknightsGameData\zh_CN\gamedata\excel\roguelike_topic_table.json")
json_rogueEN        = json_load(r"json\gamedata\ArknightsGameData_YoStar\en_US\gamedata\excel\roguelike_topic_table.json")

json_activity_dict  = json_load(r"json\activity.json")
json_dict           = json_load(r"py/dict.json")

def TL_mission(UnlockMissionData : dict = {}):  #   f'<@ba.kw>{}</>'
    def IS_name(season):
        return json_rogueEN["topics"][season]["name"] if season in json_rogueEN["topics"] else json_activity_dict["Dict"][f'IS#{int(season[-1])+1}']["nameEN"].split(":")[-1].strip()
    def IS_zone(zone):
        return f'<@ba.kw>{json_rogueEN["details"][season]["zones"][zone]["name"] if season in json_rogueEN["details"] and zone in json_rogueEN["details"][season]["zones"] else f'Floor {int(zone[-1])+1}'}</>'
    def IS_mode(mode):
        return " (Regular Operations)" if mode == "NORMAL" else ""
    def IS_diff(diff, season):
        return "" if diff in ["0", 0] else f' on <@ba.kw>{json_rogueEN["details"][season]["difficulties"][int(diff)]["name"] if season in json_rogueEN["details"] else "Difficulty"} {diff}</> or above'
    def IS_band_count(band_count):
        return "" if band_count in ["1", 1] else f' with <@ba.kw>{band_count}</> different Squads'
    def IS_node(node, season):
        node_dict = {
                        "INCIDENT"                                  :   "Encounter",
                        "BATTLE_NORMAL,BATTLE_ELITE,BATTLE_BOSS"    :   "Combat",
                        "BATTLE,BATTLE_HARD"                        :   "'Turmoil'",
                        "DUEL"                                      :   "Face-Off",
                        "PORTAL"                                    :   "Wander into Wonderland",
        }
        return f'<@ba.kw>{node_dict.get(node, json_rogueEN["details"][season]["nodeTypeData"][node]["name"] if season in json_rogueEN["details"] and node in json_rogueEN["details"][season]["nodeTypeData"] else json_rogue["details"][season]["nodeTypeData"][node]["name"] if node not in node_dict else f'[PH] {node}')}</>'
    def IS_band_name(band, season):
        return f'<@ba.kw>{json_rogueEN["details"][season]["items"][band.split(",")[0]]["name"] if season in json_rogueEN["details"] and band in json_rogueEN["details"][season]["items"] else f'{json_rogue["details"][season]["items"][band.split(",")[0]]["name"]} Squad'}</>'
    def IS_char(char):
        return f'<@ba.kw>{json_dict["Char"]["Code2Name"][char]}</>'
        
    auto_tl = f'{UnlockMissionData["description"]}</br></br>(Auto-translated)</br>'
    
    match UnlockMissionData["template"]:
        case "Rlv2PassZoneSpec":
            _, season, mode, diff, _, zone = UnlockMissionData["param"]
            return f'{auto_tl}Reach {IS_zone(zone)} in Integrated Strategies: {IS_name(season)}{IS_mode(mode)}{IS_diff(diff, season)}'
        case "Rlv2BandGradeCnt":
            _, season, diff, band_count = UnlockMissionData["param"]
            return f'{auto_tl}Clear any ending{IS_band_count(band_count)} in Integrated Strategies: {IS_name(season)}{IS_diff(diff, season)}'
        case "Rlv2PassNodeSpec":
            _, season, mode, diff, node, nodes = UnlockMissionData["param"]
            return f'{auto_tl}Clear <@ba.kw>{nodes}</> {IS_node(node, season)} nodes in Integrated Strategies: {IS_name(season)}{IS_mode(mode)}{IS_diff(diff, season)}'
        case "Rlv2EndingWithBandChar":
            _, season, mode, diff, band, char = UnlockMissionData["param"]
            return f'{auto_tl}Clear any ending with the {IS_band_name(band, season)} with {IS_char(char)} recruited in Integrated Strategies: {IS_name(season)}{IS_mode(mode)}{IS_diff(diff, season)}'
        case "Rlv2RecruitSpecificChar":
            _, season, char, times = UnlockMissionData["param"]
            return f'{auto_tl}Recruit {IS_char(char)} in Integrated Strategies: {IS_name(season)}{f' <@ba.kw>{times}</> times' if int(times) > 1 else ""}'
        case "Rlv2UpgradeSpecificChar":
            _, season, char, times = UnlockMissionData["param"]
            return f'{auto_tl}Promote {IS_char(char)} in Integrated Strategies: {IS_name(season)}{f' <@ba.kw>{times}</> times' if int(times) > 1 else ""}'
        case "Rlv2MeetBandit":
            _, season, mode, _, times = UnlockMissionData["param"]
            return f'{auto_tl}Clear node occupied by “居民” in Integrated Strategies: {IS_name(season)}{IS_mode(mode)}{f' <@ba.kw>{times}</> times' if int(times) > 1 else ""}'
        case "Rlv2EliteBattleWithChar":
            _, season, mode, diff, char = UnlockMissionData["param"]
            return f'{auto_tl}Recruit {IS_char(char)} and clear any Emergency Ops node in Integrated Strategies: {IS_name(season)}{IS_mode(mode)}{IS_diff(diff, season)}'
        case "Rlv2GainItem":
            _, count, item = UnlockMissionData["param"]
            return f'{auto_tl}Obtain <@ba.kw>{count}</> <@ba.kw>{item}</> in Integrated Strategies: {IS_name(json_special["operatorBasicData"][UnlockMissionData["missionGroup"]]["targetId"])}'
        case "Rlv2MoveCostAp":
            _, season, mode, _, count = UnlockMissionData["param"]
            return f'{auto_tl}Spend <@ba.kw>{count}</> Action in Integrated Strategies: {IS_name(season)}{IS_mode(mode)}'
        case "Rlv2ShopRecycle":
            _, item, count = UnlockMissionData["param"]
            return f'{auto_tl}Sell <@ba.kw>{count}</> <@ba.kw>{item}</> in Integrated Strategies: {IS_name(json_special["operatorBasicData"][UnlockMissionData["missionGroup"]]["targetId"])}'
        case _:
            return UnlockMissionData["description"]
            _, _, _, _, _, _ = UnlockMissionData["param"]
            return f'{auto_tl}'

def special_op():
    sp_op : dict = {}

    for char in json_special["nodeUnlockMissionGroup"].keys():
        char_dict : dict = {"unlock": {}, "proficiency" : {}}
        
        mission_list : list[str] = json_special["nodeUnlockMissionGroup"][char]["missionIds"]
        
        for mission in mission_list:
            mission_desc    : str   = json_specialEN["nodeUnlockMissionData"][mission]["description"] if mission in json_specialEN["nodeUnlockMissionData"] else TL_mission(json_special["nodeUnlockMissionData"][mission])
            mission_to      : str   = mission.split("_")[-1]
            mission_type    : str   = mission.split("_")[-2]
            
            if mission_type == "evolve":
                char_dict["unlock"].setdefault(mission_type, ["" for _ in range(2)])
                elite_phase = int(mission_to[-1]) - 1
                char_dict["unlock"][mission_type][elite_phase] = mission_desc
            elif mission_type == "skill" :
                char_dict["unlock"].setdefault(mission_type, ["" for _ in range(7)])
                skill_end = int(mission_to[-1])
                skill_start = skill_end - 3
                char_dict["unlock"][mission_type] = [mission_desc if skill_start <= lv < skill_end else char_dict["unlock"][mission_type][lv] for lv in range(7)]
            elif re.match(r'master[\d]', mission_type) :
                char_dict["unlock"].setdefault(mission_type, ["" for _ in range(3)])
                master_phase = int(mission_to[-1]) - 1
                char_dict["unlock"][mission_type][master_phase] = mission_desc
            elif re.match(r'skill[\d]', mission_type) :
                char_dict["unlock"].setdefault(mission_type, ["" for _ in range(3)])
                skill_lv = int(re.search(r'^(?:\D*|)([\d]*)$', mission_to).group(1)) - 7 - 1
                char_dict["unlock"][mission_type][skill_lv] = mission_desc
            elif re.match(r'uniequip[\d]', mission_type) :
                char_dict["unlock"].setdefault(mission_type, ["" for _ in range(3)])
                mod_lv = int(mission_to) - 1
                char_dict["unlock"][mission_type][mod_lv] = mission_desc
            else:
                printr(f'Mission type new case !!! : {mission_type} ({char})')
        
        master_list : list[str] = json_char_meta["charIdMasterListMap"][char]
        conditionDesc_dict = {
                                "无需招募，培训至精英阶段一生效"    :   "Does not require recruitment, goes into effect after training to Elite 1",
                                "无需招募，培训至精英阶段二生效"    :   "Does not require recruitment, goes into effect after training to Elite 2",
        }
        
        for master in master_list: 
            master_lv_list = json_char_metaEN["charMasterDataMap"].get(master, json_char_meta["charMasterDataMap"][master])["levelList"]
            master_type = master.replace(f'_{char.split("_")[-1]}_', "")
            if master_type not in char_dict["unlock"].keys():
                char_dict["unlock"][master_type] = [conditionDesc_dict.get(lv["conditionDesc"], lv["conditionDesc"]) for lv in master_lv_list ]
        
            char_dict["proficiency"][master_type] = [{"name" : lv["name"], "description" : lv["description"]} for lv in master_lv_list ]
        
        # sort key
        char_dict["unlock"] = {k:char_dict["unlock"][k] for k in sorted(char_dict["unlock"].keys())}
        
        sort_master_key             = list(dict.fromkeys([list(node.values())[0].split("_")[-2] for node in json_special["operatorDetailData"][char]["nodeDiagramMap"]["MASTER"]["nodePointDataMap"].values()]))
        char_dict["proficiency"]    = {k:char_dict["proficiency"][k] for k in sort_master_key}
        
        sp_op[char] = char_dict
    
    return sp_op

if __name__ == "__main__":
    script_result(special_op(), True)
else:
    with open(r"json\puppiiz\special_operator.json", "w", encoding = "utf-8") as filepath :
        json.dump(special_op(), filepath, indent = 4, ensure_ascii = False)