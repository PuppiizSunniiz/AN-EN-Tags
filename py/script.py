import json
import glob
import re
import subprocess
import os
import inspect
from typing import Any

R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
B = '\033[34m'
RE = '\033[0m'


################################################################################################################################################################################################################################################
# JSON
################################################################################################################################################################################################################################################
def json_load(filepath) -> dict:
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_json() -> dict :
    return {
                "json_activity" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/activity_table.json"),
                "json_audio" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/audio_data.json"),
                "json_battle_equip" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/battle_equip_table.json"),
                "json_building" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/building_data.json"),
                "json_campaign" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/campaign_table.json"),
                "json_chapter" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/chapter_table.json"),
                "json_character" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/character_table.json"),
                "json_charm" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/charm_table.json"),
                "json_charword" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/charword_table.json"),
                "json_char_meta" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/char_meta_table.json"),
                "json_char_patch" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/char_patch_table.json"),
                "json_checkin" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/checkin_table.json"),
                "json_climb_tower" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/climb_tower_table.json"),
                "json_clue" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/clue_data.json"),
                "json_crisis" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/crisis_table.json"),
                "json_crisis_v2" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/crisis_v2_table.json"),
                "json_display_meta" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/display_meta_table.json"),
                "json_enemy_handbook" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/enemy_handbook_table.json"),
                "json_favor" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/favor_table.json"),
                "json_gacha" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/gacha_table.json"),
                "json_gamedata" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/gamedata_const.json"),
                "json_handbook_info" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_info_table.json"),
                "json_handbook" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_table.json"),
                "json_handbook_team" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_team_table.json"),
                "json_item" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/item_table.json"),
                "json_medal" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/medal_table.json"),
                "json_mission" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/mission_table.json"),
                "json_open_server" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/open_server_table.json"),
                "json_player_avatar" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/player_avatar_table.json"),
                "json_range" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/range_table.json"),
                "json_replicate" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/replicate_table.json"),
                "json_retro" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/retro_table.json"),
                "json_roguelike" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/roguelike_table.json"),
                "json_roguelike_topic" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/roguelike_topic_table.json"),
                "json_sandbox_perm" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/sandbox_perm_table.json"),
                "json_sandbox" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/sandbox_table.json"),
                "json_shop_client" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/shop_client_table.json"),
                "json_skill" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/skill_table.json"),
                "json_skin" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/skin_table.json"),
                "json_stage" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/stage_table.json"),
                "json_story_review_meta" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/story_review_meta_table.json"),
                "json_story_review" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/story_review_table.json"),
                "json_story" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/story_table.json"),
                "json_tech_buff" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/tech_buff_table.json"),
                "json_tip" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/tip_table.json"),
                "json_token" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/token_table.json"),
                "json_uniequip" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/uniequip_table.json"),
                "json_zone" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/zone_table.json"),
                "json_enemy_database" : json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/enemydata/enemy_database.json"),
                
                "json_activityEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/activity_table.json"),
                "json_audioEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/audio_data.json"),
                "json_battle_equipEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/battle_equip_table.json"),
                "json_buildingEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/building_data.json"),
                "json_campaignEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/campaign_table.json"),
                "json_chapterEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/chapter_table.json"),
                "json_characterEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/character_table.json"),
                "json_charmEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/charm_table.json"),
                "json_charwordEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/charword_table.json"),
                "json_char_metaEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/char_meta_table.json"),
                "json_char_patchEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/char_patch_table.json"),
                "json_checkinEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/checkin_table.json"),
                "json_climb_towerEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/climb_tower_table.json"),
                "json_clueEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/clue_data.json"),
                "json_crisisEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/crisis_table.json"),
                "json_crisis_v2EN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/crisis_v2_table.json"),
                "json_display_metaEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/display_meta_table.json"),
                "json_enemy_handbookEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/enemy_handbook_table.json"),
                "json_favorEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/favor_table.json"),
                "json_gachaEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/gacha_table.json"),
                "json_gamedataEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/gamedata_const.json"),
                "json_handbook_infoEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/handbook_info_table.json"),
                "json_handbookEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/handbook_table.json"),
                "json_handbook_teamEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/handbook_team_table.json"),
                "json_itemEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/item_table.json"),
                "json_medalEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/medal_table.json"),
                "json_missionEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/mission_table.json"),
                "json_open_serverEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/open_server_table.json"),
                "json_player_avatarEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/player_avatar_table.json"),
                "json_rangeEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/range_table.json"),
                "json_replicateEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/replicate_table.json"),
                "json_retroEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/retro_table.json"),
                "json_roguelikeEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/roguelike_table.json"),
                "json_roguelike_topicEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/roguelike_topic_table.json"),
                "json_sandbox_permEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/sandbox_perm_table.json"),
                "json_sandboxEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/sandbox_table.json"),
                "json_shop_clientEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/shop_client_table.json"),
                "json_skillEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/skill_table.json"),
                "json_skinEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/skin_table.json"),
                "json_stageEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/stage_table.json"),
                "json_story_review_metaEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/story_review_meta_table.json"),
                "json_story_reviewEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/story_review_table.json"),
                "json_storyEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/story_table.json"),
                "json_tech_buffEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/tech_buff_table.json"),
                "json_tipEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/tip_table.json"),
                "json_tokenEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/token_table.json"),
                "json_uniequipEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/uniequip_table.json"),
                "json_zoneEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/zone_table.json"),
                "json_enemy_databaseEN" : json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/levels/enemydata/enemy_database.json"),
                
                "json_named_effect" : json_load("json/named_effects.json"),
                "json_dict" : json_load("py/dict.json")
        }

DB = load_json()

################################################################################################################################################################################################################################################
# Util
################################################################################################################################################################################################################################################
def script_result(text : str | list | dict, show : bool = False):
    '''
        Output result
            STR, LIST   >   TXT
            DICT        >   JSON
    '''
    if isinstance(text,str):
        with open("py/script.txt", "w", encoding = "utf-8") as filepath:
            filepath.write(text)
    elif isinstance(text,list):
        with open("py/script.txt", "w", encoding = "utf-8") as filepath:
            filepath.write("\n".join(text))
    elif isinstance(text,dict):
        with open("py/script.json", "w", encoding = "utf-8") as filepath:
            json.dump(text, filepath, indent = 4, ensure_ascii = False) # ensure_ascii = False
    
    file = f'py/script.{f"txt" if isinstance(text,str) or isinstance(text,list) else f"json"}'
    print(f'\n{Y}Script Completed{RE} -> {R}{file}{RE}')
    if show:
        subprocess.run(f'code --reuse-window -g "{os.path.abspath(file)}"', shell=True)

def list_to_array(LIST : list) -> list :
    return [elem for elem in LIST if elem not in [f'\n{"-"*80}\n', ""]]

def printr(*arg):
    print(f'{R}[:{inspect.currentframe().f_back.f_lineno}]{RE}', *arg, RE)

def printc(*arg):
    all_arg = [*arg]
    print(f'{R}[:{inspect.currentframe().f_back.f_lineno}]{RE}', " ".join([f'{G}{all_arg[i]}' if i % 2 == 1 else f'{B}{all_arg[i]}' for i in range(len(all_arg))]), RE) # type: ignore

def printt(*arg, mode = ""):
    file = __file__
    print(f'[{R}{file}:{inspect.currentframe().f_back.f_lineno}{RE}]')
    if mode == "c":
        all_arg = [*arg]
        print(" ".join([f'{G}{all_arg[i]}' if i % 2 == 1 else f'{B}{all_arg[i]}' for i in range(len(all_arg))]), RE)
    else:
        print(*arg)

def join_and(text_list : list | set) -> str :
    return_text = " and ".join(text_list)
    if len(text_list) >= 3:
        return_text = return_text.replace(" and ", ", ", len(text_list) - 2)
    return return_text

def falsy_compare(a, b) -> bool:
    return not bool(a) and not bool(b) or a == b

def decimal_format(dec : float) -> str:
    if int(dec) != dec and len(str(dec).split(".")[-1]) > 1:
        return f'{dec:.2f}'
    elif int(dec) != dec and len(str(dec).split(".")[-1]) == 1:
        return f'{dec:.1f}'
    else:
        return f'{dec:.0f}'

def wiki_trim(text : str) -> str:
    return text.replace("'", "").replace('"', "").replace("?", "")

################################################################################################################################################################################################################################################
# Old Script
################################################################################################################################################################################################################################################
def skin_lister(show : bool = False) :
    '''
        list all skin name
    '''
    skin_list = []

    for skin in DB["json_skin"]["charSkins"]:
        if skin.find("char_") == 0 : 
            if skin.find("@") != -1:
                new_skin = skin.replace("@","_")
            else:
                new_skin = skin.replace("#","_")
            #print(new_skin)
            skin_list.append(new_skin)

    skin_list.sort(key = lambda skin : (int(skin.split("_")[1]) , skin.split("_")[3]))

    script_result("\n".join(skin_list))

def skill_icon_lister(show : bool = False):
    '''
        list all skill id
    '''
    skill_list = []

    for skill in DB["json_skill"]:
        if skill.find("sktok") != 0:
            if DB["json_skill"][skill]["iconId"]:
                skill_icon = f'skill_icon_{DB["json_skill"][skill]["iconId"]}.png'
            else : skill_icon = f'skill_icon_{skill}.png'
        
            skill_list.append(skill_icon)   

    skill_list = sorted(list(set(skill_list)))

    with open("py/script compare.txt","r") as filepath:
        for text in filepath:
            if text.strip() in skill_list :
                print(text)
                skill_list.remove(text.strip())

    script_result("\n".join(skill_list))

def ops_e2_talent(show : bool = False):
    '''
        fetch e2 talent both p1 and talent potential
    '''
    new_mod = [["Ines"]]

    #print(DB["json_character"].keys())
    #DB["json_character"][char]["appellation"]
    char_dict = {char:(DB["json_characterEN"][char]["talents"] if char in DB["json_characterEN"] else DB["json_character"][char]["talents"]) for char in DB["json_character"] if DB["json_character"][char]["appellation"] in [mod[0] for mod in new_mod]}

    for char,talents in char_dict.items():
        char_dict[char] = [[{("upgradeDescription" if x == "description" else x):talent["candidates"][i][x] for x in ["name", "description", "blackboard"]} for i in ([-1] if talent["candidates"][-1]["requiredPotentialRank"] == 0 else [-2,-1])] for talent in talents]
    script_result(char_dict)

def term_kw(show : bool = False):
    term_list = []
    for term in DB["json_named_effect"]["termDescriptionDict"]:
        if term[0:2] == "ba":
            term_detail = DB["json_named_effect"]["termDescriptionDict"][term]
            term_list.append(term_detail["termId"]+"\t"+term_detail["termName"]+"\t"+term_detail["description"])
    
    script_result("\n".join(term_list))

def recruit_update(show : bool = False):
    '''
        fetch recruit ops details from recruitment instruction straight from "gacha_table.json"
    '''
    def cleanlist(recruit_list:str) -> str:
        return recruit_list.replace("\\n","\n").replace("/"," / ").replace("  "," ").replace("< / ","</")
    gacha_CN_list   =   cleanlist(DB["json_gacha"]["recruitDetail"]).split("\n")
    gacha_EN_list   =   cleanlist(DB["json_gachaEN"]["recruitDetail"]).split("\n")
    char_list       =   DB["json_dict"]["Char"]
    recruitCN       =   []
    recruitEN       =   []
    bypass          =   {
                            "THRM-EX"           :   "Thermal-EX",
                            "\'Justice Knight\'"    :   "\"Justice Knight\"",
                            "Shirayuki"         :   "ShiraYuki"
                        }
    #print(gacha_EN_list)
    for i in range(6):
        for ops in gacha_CN_list[gacha_CN_list.index("★"*(i+1))+1].split(" / "):
            op = re.search(r"<@rc.eml>(.+?)</>",ops).group(1) if re.search(r"<@rc.eml>(.+?)</>",ops) else ops
            recruitCN.append(char_list["CN2Code"][op.replace("\r","")])
        for ops in gacha_EN_list[gacha_EN_list.index("★"*(i+1))+1].split(" / "):
            op = re.search(r"<@rc.eml>(.+?)</>",ops).group(1) if re.search(r"<@rc.eml>(.+?)</>",ops) else ops
            
            op = bypass.get(op,op)
            
            recruitEN.append(char_list["Name2Code"][op])
            
    
    script_result("\n".join(recruitCN+recruitEN))
    
def boss_stage_regex(show : bool = False):
    '''
        regex for boss stage variant
    '''
    stage = ("ro4_b_2_b")

    test = re.search(r'(ro[0-9]{0,2}_._[0-9]{1,2})(_[a-z]{1}|)',stage)

    print(test.group(1))

def skin_artist(show : bool = False):
    for skin in DB["json_skin"]["charSkins"].keys():
        if skin in DB["json_skinEN"]["charSkins"].keys():
        #print(skin)
            if DB["json_skin"]["charSkins"][skin]["displaySkin"]["drawerList"]:
                CN_skin_artist = (" & ").join([x.strip() for x in DB["json_skin"]["charSkins"][skin]["displaySkin"]["drawerList"]])
                EN_skin_artist = (" & ").join([x.strip() for x in DB["json_skinEN"]["charSkins"][skin]["displaySkin"]["drawerList"]])
                if CN_skin_artist != EN_skin_artist:
                    print(f'{skin}\t{CN_skin_artist}\t{EN_skin_artist}')

def va_artist(show : bool = False):
    va = []
    va_dict = {}
    
    for op in DB["json_charword"]["voiceLangDict"].keys():
        if op in DB["json_charwordEN"]["voiceLangDict"].keys():
            for lang in DB["json_charword"]["voiceLangDict"][op]["dict"].keys():
                if lang in DB["json_charwordEN"]["voiceLangDict"][op]["dict"].keys():
                    VA_CN = DB["json_charword"]["voiceLangDict"][op]["dict"][lang]["cvName"][0].strip()
                    VA_EN = DB["json_charwordEN"]["voiceLangDict"][op]["dict"][lang]["cvName"][0].strip()
                    if VA_CN != VA_EN :
                        va.append(f'{op},{lang},{VA_CN},{VA_EN}')
                        if VA_CN in va_dict.keys() and va_dict[VA_CN] != VA_EN:
                            print(f'{op}\t{VA_CN}\t{va_dict[VA_CN]}\t{VA_EN}')
                        else :
                            va_dict[VA_CN] = VA_EN
                    
    if va : script_result(("\n").join(va))

def subpower_list(show : bool = False):
    temp = []
    for char in DB["json_character"]:
        if DB["json_character"][char]["subPower"]:
            temp.append(DB["json_character"][char]["appellation"])

    print (temp)

def stage_kill_test(show : bool = False):
    IGNORED = {"enemy_10082_mpweak","enemy_10072_mpprhd"}
    test = {"all":{}, "filtered_start":{},"filtered_end":{}, "enemies":{"KILL":0, "NORMAL":[], "ELITE":[], "BOSS":[], "Extra":[]}}
    times = 0
    enemies = {"KILL":{}, "Extra":{}}
    count = [0,0]
    stage_path = r'json\gamedata\ArknightsGameData\zh_CN\gamedata\levels\obt\training\level_training_26.json'
    stage_key = stage_path.split("\\")[-1].replace("level_", "").replace(".json", "").replace("training","tr")
    script_json = json_load(stage_path)

    stages_json = json_load(r'test\stage.json')

    def enemy_motion_search(key):
        for data in DB["json_enemy_database"]["enemies"]:
            if data["Key"] == key:
                return data["Value"][0]["enemyData"]["motion"]["m_value"]

    def enemy_ref():
        temp = {}
        for enemy_data in script_json.get("enemyDbRefs", []):
            if enemy_data["overwrittenData"] and enemy_data["overwrittenData"]["prefabKey"]["m_defined"]:
                temp[enemy_data["id"]] = enemy_data["overwrittenData"]["prefabKey"]["m_value"]
            else :
                temp[enemy_data["id"]] = enemy_data["id"]
        return temp

    enemy_ref_json = enemy_ref()
    print(enemy_ref_json)

    height = len(script_json["mapData"]["map"])
    width = len(script_json["mapData"]["map"][0])
    for wave in script_json.get("waves",[]):
        times += wave["preDelay"] + wave["postDelay"]
        for fragment in wave.get("fragments",[]):
            times += fragment["preDelay"]
            for action in fragment.get("actions",[]):
                times += action["preDelay"]
                routes = script_json["routes"][action["routeIndex"]]
                currroute = {
                                "actionType"        : action["actionType"],
                                "key"               : action["key"],
                                "count"             : action["count"],
                                "startPosition"     : routes["startPosition"],
                                "TEST_start"        : script_json["mapData"]["map"][-routes["startPosition"]["row"]-1][routes["startPosition"]["col"]],
                                "TEST_tile_start"   : script_json["mapData"]["tiles"][script_json["mapData"]["map"][-routes["startPosition"]["row"]-1][routes["startPosition"]["col"]]]["tileKey"],
                                "endPosition"       : routes["endPosition"],
                                "TEST_end"          : script_json["mapData"]["map"][-routes["endPosition"]["row"]-1][routes["endPosition"]["col"]],
                                "TEST_tile_end"     : script_json["mapData"]["tiles"][script_json["mapData"]["map"][-routes["endPosition"]["row"]-1][routes["endPosition"]["col"]]]["tileKey"],
                                "checkpoints"       : routes["checkpoints"]
                            }
                test["all"][action["routeIndex"]] = currroute
                # Is enemy // Spawning // not mechanic enemy
                if action["key"].split("_")[0] == "enemy" and action["actionType"] == "SPAWN" and action["key"] not in IGNORED:
                    #from Red box // or // prespawn
                    if script_json["mapData"]["tiles"][script_json["mapData"]["map"][-routes["startPosition"]["row"]-1][routes["startPosition"]["col"]]]["tileKey"] == "tile_start" or times == 0: 
                        test["filtered_start"][action["routeIndex"]] = currroute
                        enemies["KILL"][enemy_ref_json[action["key"]]] = enemies["KILL"].get(enemy_ref_json[action["key"]], 0) + action["count"]
                        count[0] += action["count"]
                    #Go to Red box // #legal spawn movement
                    elif script_json["mapData"]["tiles"][script_json["mapData"]["map"][-routes["endPosition"]["row"]-1][routes["endPosition"]["col"]]]["tileKey"] == "tile_end":# and enemy_motion_search(action["key"]) == routes["motionMode"]:
                        test["filtered_end"][action["routeIndex"]] = currroute
                        enemies["Extra"][enemy_ref_json[action["key"]]] = enemies["Extra"].get(enemy_ref_json[action["key"]], 0) + action["count"]
                        count[1] += action["count"]

    for enemy in enemies["KILL"].keys():
        test["enemies"]["KILL"] += enemies["KILL"][enemy]
        test["enemies"][DB["json_enemy_handbook"]["enemyData"][enemy]["enemyLevel"]].append([enemy, DB["json_enemy_handbook"]["enemyData"][enemy]["name"], DB["json_enemy_handbookEN"]["enemyData"][enemy]["name"] if enemy in DB["json_enemy_handbookEN"]["enemyData"].keys() else "" , enemies["KILL"][enemy]])

    for enemy in enemies["Extra"].keys():
        test["enemies"]["Extra"].append([enemy, DB["json_enemy_handbook"]["enemyData"][enemy]["name"], DB["json_enemy_handbookEN"]["enemyData"][enemy]["name"] if enemy in DB["json_enemy_handbookEN"]["enemyData"].keys() else "" , enemies["Extra"][enemy]])

    print(f'\n# {stage_key} ({stages_json["stages"][stage_key]["code"]})\nMAP Height : {height}, MAP Width : {width}')
    print("Enemy count = ", count[0], "### More suspect = ", count[1])
    script_result(test)

def stage_kills(stage_paths = [], show : bool = False): #need check for drop in like kevin
    IGNORED = {"enemy_10082_mpweak", "enemy_10072_mpprhd", "enemy_3009_mpprss"} # square / Hand / EYESOFPRIESTESS
    result_json = {}
    result_text = []
    for stage_path in stage_paths if stage_paths else [r'json\gamedata\ArknightsGameData_YoStar\en_US\gamedata\levels\obt\campaign\level_camp_03.json']: #[rf'json\gamedata\ArknightsGameData\zh_CN\gamedata\levels\obt\main\level_main_15-{i+1:02}.json' for i in range(18)] + [r'json\gamedata\ArknightsGameData\zh_CN\gamedata\levels\obt\training\level_training_26.json'] + [rf'json\gamedata\ArknightsGameData\zh_CN\gamedata\levels\obt\hard\level_hard_15-{i+1:02}.json' for i in range(4)]:
        temp = {"KILL":0, "NORMAL":[], "ELITE":[], "BOSS":[], "Extra":[], "Extra_details":[]}
        times = 0
        enemies = {"KILL":{}, "Extra":{}}
        count = [0,0]
        stage_key = stage_path.split("\\")[-1].replace("level_", "").replace(".json", "").replace("training","tr")
        script_json = json_load(stage_path)

        stages_json = json_load(r'test\stage.json')

        def enemy_count(key):
            for data in DB["json_enemy_database"]["enemies"]:
                if data["Key"] == key:
                    return data["Value"][0]["enemyData"]["notCountInTotal"]["m_value"]

        def enemy_ref():
            temp = {}
            for enemy_data in script_json.get("enemyDbRefs", []):
                if enemy_data["overwrittenData"] and enemy_data["overwrittenData"]["prefabKey"]["m_defined"]:
                    temp[enemy_data["id"]] = enemy_data["overwrittenData"]["prefabKey"]["m_value"]
                else :
                    temp[enemy_data["id"]] = enemy_data["id"]
            return temp

        enemy_ref_json = enemy_ref()

        height = len(script_json["mapData"]["map"])
        width = len(script_json["mapData"]["map"][0])
        for wave in script_json.get("waves",[]):
            times += wave["preDelay"] + wave["postDelay"]
            for fragment in wave.get("fragments",[]):
                times += fragment["preDelay"]
                for action in fragment.get("actions",[]):
                    if action["hiddenGroup"] and action["hiddenGroup"] != "group1": continue
                    if action["actionType"] == "SPAWN": times += action["preDelay"]
                    routes = script_json["routes"][action["routeIndex"]]
                    currroute = {
                                                                    "actionType"        : action["actionType"],
                                                                    "key"               : action["key"],
                                                                    "count"             : action["count"],
                                                                    "hiddenGroup"       : action["hiddenGroup"],
                                                                    "routeIndex"        : action["routeIndex"],
                                                                    "startPosition"     : routes["startPosition"],
                                                                    "TEST_start"        : script_json["mapData"]["map"][-routes["startPosition"]["row"]-1][routes["startPosition"]["col"]],
                                                                    "TEST_tile_start"   : script_json["mapData"]["tiles"][script_json["mapData"]["map"][-routes["startPosition"]["row"]-1][routes["startPosition"]["col"]]]["tileKey"],
                                                                    "endPosition"       : routes["endPosition"],
                                                                    "TEST_end"          : script_json["mapData"]["map"][-routes["endPosition"]["row"]-1][routes["endPosition"]["col"]],
                                                                    "TEST_tile_end"     : script_json["mapData"]["tiles"][script_json["mapData"]["map"][-routes["endPosition"]["row"]-1][routes["endPosition"]["col"]]]["tileKey"],
                                                                    "checkpoints"       : routes["checkpoints"]
                                                                }
                    # Is enemy // Spawning // not mechanic enemy
                    if action["key"].split("_")[0] == "enemy" and action["actionType"] == "SPAWN" and action["key"] not in IGNORED:
                        #from Red box // or // prespawn
                        if script_json["mapData"]["tiles"][script_json["mapData"]["map"][-routes["startPosition"]["row"]-1][routes["startPosition"]["col"]]]["tileKey"] in ["tile_start", "tile_flystart"] or times == 0: 
                            enemies["KILL"][enemy_ref_json[action["key"]]] = enemies["KILL"].get(enemy_ref_json[action["key"]], 0) + action["count"]
                            count[0] += action["count"]
                        #Go to Red box // #legal spawn movement
                        elif script_json["mapData"]["tiles"][script_json["mapData"]["map"][-routes["endPosition"]["row"]-1][routes["endPosition"]["col"]]]["tileKey"] == "tile_end":# and enemy_motion_search(action["key"]) == routes["motionMode"]:
                            temp["Extra_details"].append(currroute)
                            enemies["Extra"][enemy_ref_json[action["key"]]] = enemies["Extra"].get(enemy_ref_json[action["key"]], 0) + action["count"]
                            count[1] += action["count"]

        for enemy in enemies["KILL"].keys():
            temp["KILL"] += enemies["KILL"][enemy]
            temp[DB["json_enemy_handbook"]["enemyData"][enemy]["enemyLevel"]].append([enemy, DB["json_enemy_handbook"]["enemyData"][enemy]["name"], DB["json_enemy_handbookEN"]["enemyData"][enemy]["name"] if enemy in DB["json_enemy_handbookEN"]["enemyData"].keys() else "" , enemies["KILL"][enemy]])

        for enemy in enemies["Extra"].keys():
            temp["Extra"].append([enemy, DB["json_enemy_handbook"]["enemyData"][enemy]["name"], DB["json_enemy_handbookEN"]["enemyData"][enemy]["name"] if enemy in DB["json_enemy_handbookEN"]["enemyData"].keys() else "" , enemies["Extra"][enemy]])

        print(f'\n# {stage_key} ({stages_json["stages"][stage_key]["code"]})\nMAP Height : {height}, MAP Width : {width}')
        print("Enemy count = ", count[0], "### More suspect = ", count[1])
        result_json[f'{stage_key} ({stages_json["stages"][stage_key]["code"]})'] = temp
    
    #script_result(result_json)
    
    for stage in result_json.keys():
        result_text.append(f'\n{"-"*80}\n\n# {stage}\n')
        result_text.append(f'\tKill counter : {result_json[stage]["KILL"]}\n')
        for level in ["NORMAL", "ELITE", "BOSS"]:
            if result_json[stage][level]:
                result_text.append(f'\t{level}')
                for enemy in result_json[stage][level]:
                    result_text.append(f'\t{enemy[3]:3} X {enemy[0]:25}\t{enemy[1]:30}\t{enemy[2]}')
        if result_json[stage]["Extra"]:
            result_text.append("\n\tExtra")
            for enemy in result_json[stage]["Extra"]:
                result_text.append(f'\t{enemy[3]:3} X {enemy[0]:25}\t{enemy[1]:30}\t{enemy[2]}')
        
    #script_result(("\n").join(result_text), show)
    
    if stage_paths:
        return result_json

def infinity_skill(show : bool = False):
    infinity = []
    exclude = ["skchr_typhon_2", "skchr_thorns_3", "skchr_buildr_2"]
    bypass = ["skchr_swire2_1", "skchr_swire2_2", "skchr_marcil_2"]
    skill_CN = DB["json_skill"]
    skill_EN = DB["json_skillEN"]
    text_to_find = ["Can switch between the default state and the following state", 
                    "Can switch between the original state and the following state",
                    "Can switch between the initial state and the following state",
                    "Can switch between initial state and the following state:",
                    "Unlimited duration, can manually deactivate skill",
                    "Unlimited duration", 
                    "Infinite duration",
                    "Manually Bypass",
                    "持续时间无限"]
    
    i_range = range(len(text_to_find))
    temp = [[] for i in i_range]
    
    for skill in skill_EN:
        if skill.find("skchr") == -1 and skill.find("skcom") == -1 or skill in exclude:
            continue
        #print(skill, skill.find("skchar") != -1, skill_EN[skill]["levels"][0]["description"])
        if skill in bypass:
            temp[len(text_to_find) - 2].append(skill)
            infinity.append(skill)
            continue
        if skill_EN[skill]["levels"][0]["description"]:
            for txt in range(len(text_to_find) - 2):
                if skill_EN[skill]["levels"][0]["description"].find(text_to_find[txt]) != -1:
                    temp[txt].append(skill)
                    infinity.append(skill)
                    break
    
    infinity.append(f'\n{"-" * 80}\n')
    
    for skill in skill_CN:
        if skill.find("skchr") == -1 and skill.find("skcom") == -1:
            continue
        #print(skill, skill.find("skchar") != -1, skill_CN[skill]["levels"][0]["description"])
        if skill in infinity + exclude:
            #print(skill,"DUPE key")
            continue
        if skill_CN[skill]["levels"][0]["description"] and skill_CN[skill]["levels"][0]["description"].find("持续时间无限") != -1:
            temp[len(text_to_find) - 1].append(skill)
            infinity.append(skill)
    
    print("\nSkills :\n", list_to_array(infinity))
    print("\nOperators :\n", sorted(set([skill.split("_")[1] for skill in list_to_array(infinity)])))
    for i in i_range:
        if temp[i]:
            print("\n# ", text_to_find[i],"\n",temp[i])
    
    script_result(infinity)

################################################################################################################################################################################################################################################
# DB Keys
################################################################################################################################################################################################################################################

#'json_activity', 'json_audio', 'json_battle_equip', 'json_building', 'json_campaign', 'json_chapter', 'json_character', 'json_charm',
#'json_charword', 'json_char_meta', 'json_char_patch', 'json_checkin', 'json_climb_tower', 'json_clue', 'json_crisis', 'json_crisis_v2',
#'json_display_meta', 'json_enemy_handbook', 'json_favor', 'json_gacha', 'json_gamedata', 'json_handbook_info', 'json_handbook', 'json_handbook_team',
#'json_item', 'json_medal', 'json_mission', 'json_open_server', 'json_player_avatar', 'json_range', 'json_replicate', 'json_retro', 'json_roguelike',
#'json_roguelike_topic', 'json_sandbox_perm', 'json_sandbox', 'json_shop_client', 'json_skill', 'json_skin', 'json_stage', 'json_story_review_meta',
#'json_story_review', 'json_story', 'json_tech_buff', 'json_tip', 'json_token', 'json_uniequip', 'json_zone', 'json_enemy_database'

# EN

################################################################################################################################################################################################################################################
# Script Playground
################################################################################################################################################################################################################################################

def char_name(show : bool = False):
    temp = {}
    DB_EN = DB["json_characterEN"]
    DB_JP = json_load("json/gamedata/ArknightsGameData_YoStar/ja_JP/gamedata/excel/character_table.json")
    DB_KR = json_load("json/gamedata/ArknightsGameData_YoStar/ko_KR/gamedata/excel/character_table.json")
    
    for key in DB_EN.keys():
        if "trap_" in key:
            continue
        if key in temp.keys():
            temp[f'{DB_EN[key]["name"]} ({key})']
        else :
            temp[DB_EN[key]["name"]] = {
                                            "key" :   key,
                                            "JP"  :   DB_JP[key]["name"],
                                            "KR"  :   DB_KR[key]["name"]
                                        }
        
    script_result(temp, show)

def event_tag(show : bool = False):
    tags = {}
    events = []
    SStag = DB["json_stage"]["storylineTags"]
    SSset = DB["json_stage"]["storylineStorySets"]
    for tag in SStag:
        tags[tag] = SStag[tag]["tagDesc"]
    
    events.append(f'Tags : {[tags[tag] for tag in tags]}\n')
        
    for event in SSset:
        if SSset[event]["ssData"]:
            print(" ".join(SSset[event]["titleImageId"].split("_")[1:]))
            events.append(f'{" ".join(SSset[event]["titleImageId"].split("_")[1:])} = {[tags[tag] for tag in SSset[event]["ssData"]["tags"]]}')
            
    script_result(events, show)

def event_desc(show : bool = False):
    events = []
    SSset = DB["json_stage"]["storylineStorySets"]
    
    for event in SSset:
        if SSset[event]["collectData"] and SSset[event]["storySetType"] == "COLLECT":
            events.append(f'\n{" ".join(SSset[event]["collectData"]["backgroundId"].split("_")[1:])}\n{SSset[event]["collectData"]["desc"]}')
            
    script_result(events, show)

def event_sypnosis(show : bool = False):
    events = {}
    SSset = DB["json_stage"]["storylineStorySets"]
    retro = json_load(r'temp\temp.json')

    for event in SSset:
        if SSset[event]["ssData"]:
            events["_".join(SSset[event]["ssData"]["backgroundId"].split("_")[1:])] = {"desc" : SSset[event]["ssData"]["desc"], "retro" : SSset[event]["ssData"]["retroActivityId"]}
        elif SSset[event]["collectData"]:
            events["_".join(SSset[event]["collectData"]["backgroundId"].split("_")[1:])] = {"desc" : SSset[event]["collectData"]["desc"], "retro" : None}
            
    for event in retro["retroActList"]:
        event_detail = retro["retroActList"][event]["detail"]
        for SSevent in [key for key in events.keys()]:
            if events[SSevent]["retro"] == event and events[SSevent]["desc"] == event_detail:
                events.pop(SSevent)
        
    script_result(events, show)

def EN_cv(show : bool = False):
    result = {}
    for char in DB["json_charword"]["voiceLangDict"]:
        if "EN" in DB["json_charword"]["voiceLangDict"][char]["dict"].keys():
            result[char] = {"CN":DB["json_charword"]["voiceLangDict"][char]["dict"]["EN"]["cvName"][0]}
    
    for char in DB["json_charwordEN"]["voiceLangDict"]:
        if "EN" in DB["json_charwordEN"]["voiceLangDict"][char]["dict"].keys():
            en_va = DB["json_charwordEN"]["voiceLangDict"][char]["dict"]["EN"]["cvName"][0]
            if char in result:
                result[char]["EN"] = en_va
            else:
                result[char] = {"EN":en_va}
    script_result(result, True)
    
    for char in result:
        if sorted(list(result[char].keys())) == ["CN", "EN"] and result[char]["CN"] != result[char]["EN"]:
            printr(f'char : {Y}{char}{RE}\nCN : {G}{result[char]["CN"]}{RE}\nEN : {B}{result[char]["EN"]}{RE}')
    
    printr("EN_cv completed")
    exit()

def wiki_enemies(event = "", show : bool = False) -> dict :
    def enemy_lv_data(enemy_data : dict, lv : int) -> dict:
        return enemy_data["Value"][lv]["enemyData"]
        
    data = {"zone" : {}, "stage" : {}, "enemies" : {}, "enemy_type" : {}}
    ACT = event if event else "act43side" # "act43side" = Act or Die
    ZonetoAct = DB["json_activity"]["zoneToActivity"]
    actzone = [zone for zone in ZonetoAct.keys() if ZonetoAct[zone] == ACT]
    if not actzone:
        printr(f'There no zone in this activity : {ACT}')
        exit()
    for zone in actzone:
        data["zone"].setdefault(zone, {})["name"] = DB["json_zone"]["zones"][zone]["zoneNameSecond"]
    
    allstage = DB["json_stage"]["stages"]
    stages = {}
    for stage in allstage.keys():
        if allstage[stage]["zoneId"] in actzone:
            stages[stage] = allstage[stage]

            if stage.find("#f#") == -1: data["zone"][allstage[stage]["zoneId"]].setdefault("stages", []).append(allstage[stage]["code"])
    
    data["stage_data"] = stages
    
    for stage in stages.keys():
        if stage.find("easy_") != -1: continue
        #printr(stage)
        if stage.find("#f#") == -1 and stages[stage]["levelId"]:
            stage_json = json_load(rf'json\gamedata\ArknightsGameData\zh_CN\gamedata\levels\{stages[stage]["levelId"].lower()}.json')
            if not isinstance(stage_json, dict):
                printr(f'\n{R}File path error {G}"{stage}" : {B}{stages[stage]["levelId"].lower()}{RE}')
                exit()
            
            for key in ["options", "mapData", "runes", "globalBuffs", "enemyDbRefs", "predefines", "hardPredefines", "routes", "waves"]:
                data["stage"].setdefault(stage, {})[key] = stage_json[key]
                if key == "enemyDbRefs":
                    for enemy in stage_json[key]:
                        if enemy["overwrittenData"] and enemy["overwrittenData"]["prefabKey"]["m_defined"]:
                            data["enemies"][enemy["overwrittenData"]["prefabKey"]["m_value"]] = {}
                        else :
                            data["enemies"][enemy["id"]] ={}
    # json_enemy_database
    act_enemies = data["enemies"].keys()
    for enemy_data in DB["json_enemy_database"]["enemies"]:
        if enemy_data["Key"] in act_enemies:
            enemy_code = enemy_data["Key"]
            # ['name', 'description', 'prefabKey', 'attributes', 'applyWay', 'motion', 'enemyTags', 'lifePointReduce', 'levelType', 'rangeRadius', 'numOfExtraDrops', 'viewRadius', 'notCountInTotal', 'talentBlackboard', 'skills', 'spData']
            enemy_data_key = ['name', 'description', 'prefabKey', 'applyWay', 'motion', 'enemyTags', 'lifePointReduce', 'levelType', 'rangeRadius', 'numOfExtraDrops', 'viewRadius', 'notCountInTotal']
            enemy_data_dict = {0 : enemy_lv_data(enemy_data, 0)}
            data["enemies"][enemy_code] = {"data" : {key : enemy_data_dict[0][key]["m_value"] for key in enemy_data_key}, "lv" : {}}
            for enemy_level_data in enemy_data["Value"]:
                if enemy_level_data["level"] != 0:
                    enemy_data_dict[enemy_level_data["level"]] = enemy_lv_data(enemy_data, enemy_level_data["level"])
                # ['maxHp', 'atk', 'def', 'magicResistance', 'cost', 'blockCnt', 'moveSpeed', 'attackSpeed', 'baseAttackTime', 'respawnTime', 'hpRecoveryPerSec', 'spRecoveryPerSec', 'maxDeployCount', 'massLevel', 'baseForceLevel', 'tauntLevel', 'epDamageResistance', 'epResistance', 'damageHitratePhysical', 'damageHitrateMagical', 'epBreakRecoverSpeed', 'stunImmune', 'silenceImmune', 'sleepImmune', 'frozenImmune', 'levitateImmune', 'disarmedCombatImmune', 'fearedImmune', 'palsyImmune', 'attractImmune']
                enemy_attr_key = ['maxHp', 'atk', 'def', 'magicResistance', 'moveSpeed', 'attackSpeed', 'baseAttackTime', 'respawnTime', 'hpRecoveryPerSec', 'spRecoveryPerSec', 'massLevel', 'baseForceLevel', 'tauntLevel', 'epDamageResistance', 'epResistance', 'damageHitratePhysical', 'damageHitrateMagical', 'epBreakRecoverSpeed', 'stunImmune', 'silenceImmune', 'sleepImmune', 'frozenImmune', 'levitateImmune', 'disarmedCombatImmune', 'fearedImmune', 'palsyImmune', 'attractImmune']
                enemy_attr_data = {}
                for key in enemy_attr_key:
                    if enemy_data_dict[enemy_level_data["level"]]["attributes"][key]["m_defined"]:
                        enemy_attr_data[key] = enemy_data_dict[enemy_level_data["level"]]["attributes"][key]["m_value"]
                    else:
                        enemy_attr_data[key] = enemy_data_dict[0]["attributes"][key]["m_value"]
                    # lv skill/trait/talents
                    for key in ['talentBlackboard', 'skills', 'spData']:
                        if enemy_data_dict[enemy_level_data["level"]][key]:
                            enemy_attr_data[key] = enemy_data_dict[enemy_level_data["level"]][key]
                        else:
                            enemy_attr_data[key] = enemy_data_dict[0][key]
                    data["enemies"][enemy_code]["lv"][enemy_level_data["level"]] = enemy_attr_data
    
    act_enemies = [[key, data["enemies"][key]["data"]["name"]] for key in data["enemies"].keys()]
    # json_enemy_handbook
    for enemy in act_enemies:
        if enemy[0] in DB["json_enemy_handbook"]["enemyData"]:
            enemy_handbook_data = DB["json_enemy_handbook"]["enemyData"][enemy[0]]
        else: 
            for enemy_handbook_key in DB["json_enemy_handbook"]["enemyData"]:
                if DB["json_enemy_handbook"]["enemyData"][enemy_handbook_key]["name"] == enemy[1]:
                    enemy_handbook_data = DB["json_enemy_handbook"]["enemyData"][enemy_handbook_key]
        data["enemies"][enemy[0]]["handbook"] = enemy_handbook_data
        #print(data["enemies"][enemy[0]])
    # Enemy type dict
    ## CN
    for enemy_type in DB["json_enemy_handbook"]["raceData"]:
        data["enemy_type"][enemy_type] = DB["json_enemy_handbookEN"]["raceData"].get(enemy_type, DB["json_enemy_handbook"]["raceData"][enemy_type])["raceName"]
    
    #script_result(data, show)
    return data
    
def wiki_article(event_code : str, event_type = "", event_name = "") -> list:
    '''
        event_type = episode/ intermezzo/ sidestory/ storycollection
                    vb/ ig
        
        page_footer = 
        
            "Side Story operations" - intermezzo/ sidestory/ storycollection
        
            "Seasonal game modes" - vb/ ig
            
            "Other event operations" - ig
        
    '''
    enemy_rune = ["enemy_attribute_mul", "char_attribute_mul", "level_enemy_replace"]
    non_enemy_rune = ["env_system_new", "global_cost_recovery_mul", "global_lifepoint", "map_tile_blackb_assign"]
    
    enemy_buffs = []
    non_enemy_buffs = ["periodic_damage"]
    skip_buffs = ["strife_mode_feature", "cooperate_fortress_global_buff", "act27sisde_enemy_global_buff"]
    
    def stage_level(level : str) -> str:
            if level == "-" or not level:
                return ""
            elif level.find("精英") != -1:
                return f'Elite {level.split("精英")[-1].split("LV.")[0].strip()} Level {level.split("LV.")[-1]}'.replace("二", "2")
            else:
                return f'Level {level.split("LV.")[-1]}'
    
    def desc_cond_writer(desc_cond : str) -> str:
        def desc_tl(desc):
            desc_tl_dict = {
                "'''<[[涨潮]]>'''被淹没的地块无法部署，水中的我方单位攻击速度降低，持续受到侵蚀损伤" : "'''<[[High Tide]]>''' Unable to deploy on flooded tiles. Allied units and enemies in the water will be affected by \"Erosion\"",
                "'''<[[岩浆喷射处]]>'''每隔一定时间会喷出岩浆，对周围8格内的我方单位造成大量伤害且融化障碍物" : "'''<[[Lava Crack]]>''' spray out lava periodically, dealing massive damage to friendly units on the surrounding 8 tiles and melting down Roadblocks",
                "'''<[[热泵通道]]>'''每隔一段时间便会对其上的我军和敌军造成大量伤害" : "'''<[[Heat Pump Passage]]>''' that periodically inflict damage to units standing on them are present on the field",
                "部分敌人的基础属性提升" : "Increases some enemies' base stats.",
                "'''<[[毒性雾霾]]>'''我方单位会持续失去生命" : "'''<[[Poison Haze]]>''' Operators lose HP constantly",
                "'''<[[沼泽地段]]>'''置于其中的干员攻击速度逐渐降低，经过的敌人攻击速度和移动速度逐渐降低" : "'''<[[Mire]]>'''Gradually reduces the ASPD of Operators within, and the ASPD and Movement Speed of enemies within",
                "'''<[[芦苇丛]]>'''置于其中的干员获得\"迷彩\"" : "'''<[[Reed Beds]]>''' Operators within gain Camouflage.",
                "'''<[[玉门天灾工事]]>'''置于其中的单位对地面单位造成的伤害提升，受到来自地面单位的伤害降低" : "'''<[[Yumen Catastrophe Defense]]>''' Units placed here deal more damage to ground units and take less damage from ground units.",
                "\\n\\n<color=#FFA300>'''<[[危险区域]]>'''</color>危险区域内的干员会在波次转换时撤退" : "",
                "\\n\\n<color=#FFA300>'''<[[实体程式]]>'''</color>已完成波次再次挑战时可以激活，激活后本波次内我方干员获得大幅强化" : "",
                "\\n\\n<color=#FFA300>'''<[[定向试炼]]>'''</color>定向试炼提供3名预选干员组成的小队": "",
                "<color=#EC1F1FFF>附加条件：</color>" : ""
            }
            for k,v in desc_tl_dict.items():
                desc = desc.replace(k,v)
            return desc
        # stage mechanic
        desc = re.sub(r'<@[A-Za-z.1-9_]*?><(.*?)><\/>', r"'''<[[\1]]>'''", desc_cond)
        # challenge condition
        if re.search(r'<@lv.fs>附加条件：<\/>\\n', desc):
            desc = re.sub(r'<@lv.fs>附加条件：<\/>\\n', "", desc)
            desc = re.sub(r'<[^[](.*?)[^]\/]>', r"'''<[[\1]]>'''", desc)
        else:
            desc = re.sub(r'<([^[c/].*?[^]\/])>', r"'''<[[\1]]>'''", desc)
        return desc_tl(desc).replace("\\n", "<br/>").replace("\n", "<br/>").replace("<br/><br/>", "<br/>")
    
    def stage_kill_lister(data : dict, stage_key : str) -> dict:
        def enemy_ref_dict(enemyDbRefs : list) -> dict:
            temp = {}
            for enemy in enemyDbRefs:
                if enemy["overwrittenData"] and enemy["overwrittenData"]["prefabKey"]["m_defined"]:
                    temp[enemy["id"]] = enemy["overwrittenData"]["prefabKey"]["m_value"]
                else :
                    temp[enemy["id"]] = enemy["id"]
            return temp
        def spawner_finder(mapData : dict):
            spawner_index = ""
            for tile in mapData["tiles"]:
                if tile["tileKey"] == "tile_mpprts_enemy_born":
                    spawner_index = mapData["tiles"].index(tile)
                
            if spawner_index:
                x_max = len(mapData["map"][0])
                y_max = len(mapData["map"])
                
        
        stage_kill_data = {}
        IGNORED = {"enemy_10082_mpweak", "enemy_10072_mpprhd", "enemy_3009_mpprss"} # square / Hand / EYESOFPRIESTESS
        #stage_data = data["stage"][stage_key]
        stage_enemy_ref = enemy_ref_dict(data["stage"][stage]["enemyDbRefs"])
        # ie. Ep15 za hand spawner
        extra_spawner_int = ""
        enemy_counter : dict[str, Any] = {"KILL" : {}, "Suspect" : {}, "Extra" : {}}
        counter = [0, 0, 0]
        # data prep
        mapData = data["stage"][stage_key]["mapData"]
        stage_height = len(mapData["map"])
        stage_width = len(mapData["map"][0])
        times = 0
        if event_type == "tn":
            tn_kill_lister = []
            tn_wave_kill = {"KILL" : {}, "Suspect" : {}, "Extra" : {}}
            tn_wave = 0
            
        isSuiXiang = False
        waves = data["stage"][stage]["waves"]
        for wave in waves:
            times += wave["preDelay"] + wave["postDelay"]
            if event_type == "tn":
                if wave["fragments"][0]["actions"][0]["key"].find("trap_091_brctrl") != -1 and wave["fragments"][0]["actions"][0]["key"].find("empty") != -1:
                    tn_kill_lister.append(tn_wave_kill)
                    tn_wave_kill = {"KILL" : {}, "Suspect" : {}, "Extra" : {}}
                    tn_wave += 1
                    continue
            for fragment in wave["fragments"]:
                #printr("fragment", "")
                times += fragment["preDelay"]
                last_enemy = ""
                for action in fragment["actions"]:
                    #printr("action", action)
                    routes = data["stage"][stage]["routes"][action["routeIndex"]]
                    
                    if action["hiddenGroup"] and action["hiddenGroup"] != "group1": continue
                    
                    if action["key"].split("_")[0] == "enemy" and action["actionType"] == "SPAWN" and action["key"] not in IGNORED:
                            #from Red box // or                                                                                                                                     // prespawn                             // Sui wisp
                            if mapData["tiles"][mapData["map"][-routes["startPosition"]["row"] - 1][routes["startPosition"]["col"]]]["tileKey"] in ["tile_start", "tile_flystart"] or times + action["preDelay"] == 0 or (isSuiXiang and action["key"].find("enemy_1211_msfsui") != -1): 
                                enemy_counter["KILL"][stage_enemy_ref[action["key"]]] = enemy_counter["KILL"].get(stage_enemy_ref[action["key"]], 0) + action["count"]
                                counter[0] += action["count"]
                                if event_type == "tn":
                                    tn_wave_kill["KILL"][stage_enemy_ref[action["key"]]] = tn_wave_kill["KILL"].get(stage_enemy_ref[action["key"]], 0) + action["count"]
                            #Go to Blue box //                                                                                                               #legal spawn movement
                            elif mapData["tiles"][mapData["map"][-routes["endPosition"]["row"] - 1][routes["endPosition"]["col"]]]["tileKey"] == "tile_end":# and enemy_motion_search(action["key"]) == routes["motionMode"]:
                                if last_enemy != "enemy_10072_mpprhd":
                                    enemy_counter["Suspect"][stage_enemy_ref[action["key"]]] = enemy_counter["Suspect"].get(stage_enemy_ref[action["key"]], 0) + action["count"]
                                    counter[1] += action["count"]
                                    if event_type == "tn":
                                        tn_wave_kill["Suspect"][stage_enemy_ref[action["key"]]] = tn_wave_kill["Suspect"].get(stage_enemy_ref[action["key"]], 0) + action["count"]
                                else:
                                    enemy_counter["Extra"][stage_enemy_ref[action["key"]]] = enemy_counter["Extra"].get(stage_enemy_ref[action["key"]], 0) + action["count"]
                                    counter[2] += action["count"]
                                    if event_type == "tn":
                                        tn_wave_kill["Extra"][stage_enemy_ref[action["key"]]] = tn_wave_kill["Extra"].get(stage_enemy_ref[action["key"]], 0) + action["count"]
                    
                    if action["actionType"] == "SPAWN":
                        last_enemy = stage_enemy_ref[action["key"]]
                    if action["key"].find("enemy_1526_sfsui") != -1:
                        isSuiXiang = True
                
        if event_type == "tn":
            tn_kill_lister.append(tn_wave_kill)
        enemy_counter["counter"] = counter
        if event_type == "tn": enemy_counter["tn_counter"] = tn_kill_lister
        return enemy_counter
    
    def enemies_lister(def_data : dict) -> dict:
        def enemy_trim(enemy_name, e_class = ""):
            trim_result = re.sub(r"(.+?|)'(.+?)'(.+?|)",r'\1"\2"\3', enemy_name)
            if event_type == "tn" and e_class == "BOSS":
                return trim_result.replace(",", "")
            else:
                return trim_result.replace('"', "")
        
        enemy_classes = ["NORMAL", "ELITE", "BOSS"]
        enemy_list = {k:{} for k in enemy_classes}
        for kill_type in ["KILL", "Suspect"]:
            for enemy in def_data[kill_type]:
                enemy_class = big_data["enemies"][enemy]["data"]["levelType"]
                enemy_list[enemy_class][enemy] = enemy_list[enemy_class].get(enemy, 0) + def_data[kill_type][enemy]
        enemies_output = {k:[] for k in enemy_classes}
        #printr(stage)
        for enemy_class in enemy_classes:
            for enemy in sorted(enemy_list[enemy_class].keys(), key = lambda enemy_key : big_data["enemies"][enemy_key]["handbook"]["enemyIndex"]):
                enemy_code = big_data["enemies"][enemy]["handbook"]["enemyId"]
                enemy_names = DB["json_enemy_handbookEN"]["enemyData"][enemy_code]["name"] if enemy_code in DB["json_enemy_handbookEN"]["enemyData"] else enemy_names_tl.get(enemy, f'{big_data["enemies"][enemy]["handbook"]["name"]}({enemy})')
                enemy_count = enemy_list[enemy_class][enemy]
                if enemy_class == "BOSS":
                    if event_type == "tn":
                        enemies_output[enemy_class].append(enemy_trim(enemy_names, enemy_class))
                    else:
                        enemies_output[enemy_class].append(f'{{{{E|{f'{enemy_trim(enemy_names)}|{enemy_count}' if enemy_count > 1 else enemy_trim(enemy_names)}}}}}')
                else:
                    enemies_output[enemy_class].append(f'{{{{E|{enemy_trim(enemy_names)}|{enemy_count}}}}}')
        return {k:", ".join(v) for k,v in enemies_output.items()}
    
    def tn_enemies_lister(def_data):
        enemy_classes = ["NORMAL", "ELITE", "BOSS"]
        wave_count = 1
        tn_enemies_output = []
        for wave in def_data:
            tn_enemies = enemies_lister(wave)
            for enemy_class in enemy_classes:
                tn_enemies_output.append(f'|{enemy_class.lower()} {wave_count} = {tn_enemies.get(enemy_class, "")}')
            wave_count += 1
        return "\n".join(tn_enemies_output)
    
    def token_lister(def_data : list) -> str:
        token_list = {}
        token_output = []
        token_skip = ["trap_162_lrctrl", "trap_042_tidectrl", "trap_091_brctrl", "trap_054_dancdol", "trap_090_recodr"] # EP14 Controller / Tide Controller / TN Controller / Mouthpiece Doll / Entitative Program (TN Buff)
        for token in def_data:
            token_code = token["inst"].get("characterKey", token["alias"])
            if token_code in token_skip:
                continue
            else:
                token_list[token_code] = token_list.get(token_code, 0) + 1
        for token in token_list:
            token_name = DB["json_characterEN"][token]["name"] if token in DB["json_characterEN"] else token_names_tl.get(token, f'{DB["json_character"][token]["name"]}({token})')
            token_output.append(f'{{{{D|{wiki_trim(token_name)}|{token_list[token]}}}}}')
            #printr(token_name)
        return ", ".join(token_output)
            
    def tile_lister(def_data : list) -> list:
        tile_output = []
        tile_skip = ["tile_forbidden", "tile_wall", "tile_road", "tile_floor", "tile_toxichill", "tile_toxicroad", "tile_toxicwall", "tile_toxic", "tile_reed", "tile_reedw", "tile_mire", "tile_yinyang_wall", "tile_yinyang_road", "tile_stairs", "tile_passable_wall"]
        tlle_full_skip = ["tile_start", "tile_end", "tile_telin", "tile_telout", "tile_hole", "tile_fence_bound", "tile_flystart", "tile_smog", "tile_start_cooperate", "tile_end_cooperate", "tile_allygoal", "tile_football", "tile_enemygoal", "tile_green"]
        for tile in def_data:
            if (tile["tileKey"] in tile_skip and not tile["blackboard"] and not tile["effects"]) or tile["tileKey"] in tlle_full_skip:
                continue
            tile_data = {tile["tileKey"] : {"blackboard" : tile["blackboard"], "effects" : tile["effects"]}}
            if tile_data not in tile_output:
                tile_output.append(tile_data)
        #if tile_output: printc("tile_output", stage, tile_output)
        return tile_output
    
    def tile_writer(def_data : list) -> str:
        if not def_data: return ""
        tile_result = []
        for tile in def_data:
            #printr(tile)
            tile_id = list(tile.keys())[0]
            match tile_id:
                case "tile_healing":
                    heal = 0
                    for blackboard in tile[tile_id]["blackboard"]:
                        if blackboard["key"] == "HP_RECOVERY_PER_SEC_BY_MAX_HP_RATIO":
                            heal = blackboard["value"]
                    if not heal:
                        printr(f'{R}Medical Rune{RE} key is invalid : {Y}{blackboard["key"]}{RE}')
                        exit()
                    tile_result.append(f'The [[Medical Rune]] restores {heal:{".0%" if len(str(heal).split(".")[-1]) < 2 else ".1%"}} of maximum HP every second to the friendly unit on it.')
                case "tile_bigforce":
                    force = 0
                    for blackboard in tile[tile_id]["blackboard"]:
                        if blackboard["key"] == "base_force_level":
                            force = blackboard["value"]
                    if not force:
                        printr(f'{R}Specialist Tactical Point{RE} key is invalid : {Y}{blackboard["key"]}{RE}')
                        exit()
                    tile_result.append(f'The [[Specialist Tactical Point]] increases the [[shift]] force of the friendly unit on it by {force:.0f} level.')
                case "tile_toxic":
                    if tile[tile_id] == {'blackboard': [{'key': 'dynamic', 'value': 1.0, 'valueStr': None}], 'effects': None}:
                        continue
                    else:
                        printr(f'new {Y}"tile_toxic"{RE} stat just drop\n{tile[tile_id]}')
                        exit()
                case "tile_volspread":
                    damage = 0
                    cd_max = 0
                    cd_min = 0
                    for blackboard in tile[tile_id]["blackboard"]:
                        match blackboard["key"]:
                            case "damage":
                                damage = decimal_format(blackboard["value"])
                            case "cd_min":
                                cd_min = decimal_format(blackboard["value"])
                            case "cd_max":
                                cd_max = decimal_format(blackboard["value"])
                            case _ :
                                printr(f'new {Y}"tile_volspread" : Lava Crack{RE} stat just drop\n{tile[tile_id]}')
                                exit()
                    tile_result.append(f'The [[Lava Crack]]s erupt every {f'{cd_min}-{cd_max} seconds' if cd_min != cd_max else f'{cd_max} seconds'} and deals {damage} True damage to friendly units in the surrounding tiles.')
                case "tile_volcano":
                    damage = 0
                    cd_max = 0
                    cd_min = 0
                    for blackboard in tile[tile_id]["blackboard"]:
                        match blackboard["key"]:
                            case "damage":
                                damage = decimal_format(blackboard["value"])
                            case "cd_min":
                                cd_min = decimal_format(blackboard["value"])
                            case "cd_max":
                                cd_max = decimal_format(blackboard["value"])
                            case _ :
                                printr(f'new {Y}"tile_volcano" : Heat Pump Passage{RE} stat just drop\n{tile[tile_id]}')
                                exit()
                    tile_result.append(f'The [[Heat Pump Passage]] erupt every {f'{cd_min} ~ {cd_max} seconds' if cd_min !=cd_max else f'{cd_max} seconds'} and deals {damage} True damage.')
                case "tile_floor" | "tile_road":
                    if len(tile[tile_id]["blackboard"]) == 1 and tile[tile_id]["blackboard"][0]["key"] == "gems_type":
                        continue
                    else :
                        printc(f'New tile_floor / tile_road case just frop : {tile[tile_id]}')
                case "tile_defup":
                    if len(tile[tile_id]["blackboard"]) == 1 and tile[tile_id]["blackboard"][0]["key"] == "def":
                        defense = tile[tile_id]["blackboard"][0]["value"]
                        tile_result.append(f'The [[Defense Rune]] increases the DEF of the friendly unit on it by {defense:.0f}.')
                    else :
                        printc(f'New tile_defup case just drop : {tile[tile_id]}')
                case "tile_infection":
                    damage = 0
                    atk = 0
                    aspd = 0
                    duration = 0
                    for blackboard in tile[tile_id]["blackboard"]:
                        match blackboard["key"]:
                            case "damage":
                                damage = blackboard["value"]
                            case "atk":
                                atk = blackboard["value"]
                            case "attack_speed":
                                aspd = blackboard["value"]
                            case "duration":
                                duration = blackboard["value"]
                            case _:
                                printc(f'New {Y}tile_infection{RE} case just drop : {B}{tile[tile_id]}{RE}')
                    if damage and atk and aspd and duration:
                        tile_result.append(f'The [[Active Originium]] effect deals {damage:.0f} True damage every second, increases ATK and ASPD by {atk:{".0%" if len(str(atk).split(".")[-1]) < 2 else ".1%"}} and {aspd:.0f}, respectively, and lasts for {duration:.0f} seconds. ')
                    else:
                        printr(f'Active Originium effect value if {R}not{RE} completed : {R}{stage} {B}{tile}')
                        exit()
                case "tile_yinyang_wall" | "tile_yinyang_road":
                    default_effect = [
                                        [{'key': 'dynamic', 'value': 1.0, 'valueStr': None}, {'key': 'buff_yinyang[same].atk_scale', 'value': 0.6, 'valueStr': None}, {'key': 'buff_yinyang[diff].atk_scale', 'value': 1.4, 'valueStr': None}],
                                        [{'key': 'dynamic', 'value': 0.0, 'valueStr': None}, {'key': 'buff_yinyang[same].atk_scale', 'value': 0.6, 'valueStr': None}, {'key': 'buff_yinyang[diff].atk_scale', 'value': 1.4, 'valueStr': None}]
                                    ]
                    if tile[tile_id]["blackboard"] in default_effect and not tile[tile_id]["effects"]:
                        continue
                    else :
                        printc(f'New {Y}tile_yinyang{RE} case just drop : {B}{tile[tile_id]}{RE}')
                case "tile_defbreak":
                    if tile[tile_id] == {'blackboard': [{'key': 'def', 'value': 0.5, 'valueStr': None}], 'effects': None}:
                        continue
                    else:
                        printc(f'New {Y}tile_defbreak{RE} case just drop : {B}{tile[tile_id]}{RE}')
                case _ :
                    printr(f'new Terrain to add : {Y}{tile_id}\n\t{G}{tile[tile_id]["blackboard"]}\n\t{B}{tile[tile_id]["effects"]}{RE}')
        
        if tile_result:
            #printr(f'{B}tile_writer {G}{stage} {Y}{tile_result}{RE}')
            if len(tile_result) > 1:
                return f'\n*{"\n*".join(tile_result)}'
            else:
                return f'\n{"\n".join(tile_result)}'
        else:
            return ""
    
    def addendum_writer(runes = [], buffs = [], DP = 1, diff = "", head = "", foot = ""):
        norm_env = [
                        {'key': 'env_017_act35side', 'attack_speed': -60.0, 'max_hp': 0.1, 'atk': 0.1}
                    ]

        env_name = {
                        "env_017_act35side" : ""
                    }
        buff_writer = []
        if buffs:
            for buff in buffs:
                if buff["prefabKey"] in enemy_buffs:
                    continue
                elif buff["prefabKey"] in non_enemy_buffs:
                    temp = {k:v for k,v in buff.items()}
                    printr(temp["blackboard"])
                    match buff["prefabKey"]:
                        case "periodic_damage":
                            damage = temp["blackboard"].pop("damage")
                            interval = temp["blackboard"].pop("interval")
                            if temp["blackboard"]:
                                printc(f'There new blackboard key in {Y}{buff["prefabKey"]}{RE} : {B}{temp["blackboard"]}{RE}')
                            else:
                                buff_writer.append(f'\nThe [[Poison Haze]] deals {damage:.0f} True damage every {decimal_format(interval)} seconds to all friendly units on the map.')
                        case _:
                            printc(f'There new case in addendum Towns : {buff["prefabKey"]}')
                else:
                    printc(f'New buff in town !!! {buff["prefabKey"]}')
        
        addendum = f'{"\n".join(buff_writer)}\n{head}'
        if DP != 1: addendum += f'DP regeneration rate is reduced by 100%. '
        rune_writer = []
        for rune in runes:
            temp = {k:v for k,v in rune.items()}
            if rune["key"] in enemy_rune:
                continue
            if rune["key"] not in non_enemy_rune:
                printc(f'{Y}{rune["key"]}{RE} is not in {G}non_enemy_rune{RE} : {B}{non_enemy_rune}{RE}')
                
            if rune["difficultyMask"] == "ALL" or rune["difficultyMask"] == diff:
                match rune["key"]:
                    case "env_system_new":
                        if rune["blackboard"] in norm_env:
                            continue
                        else :
                            printc(f'New Environment just drop : {rune["blackboard"]}')
                    case "global_cost_recovery_mul":
                            scale = temp["blackboard"].pop("scale")
                            if temp["blackboard"]:
                                printc(f'There new blackboard key in {Y}{rune["prefabKey"]}{RE} : {B}{temp["blackboard"]}{RE}')
                            else:
                                rune_writer.append(f'\nThe automatic DP generation rate is reduced to 1 DP every {decimal_format(scale)} seconds.')
                    case "global_lifepoint":
                        # global_lifepoint()
                        continue
                    case "map_tile_blackb_assign":
                        printc(f'New map_tile_blackb_assign just drop : {rune["blackboard"]}')
                    case _:
                        printc(f'New case just drop : {rune["key"]}')
        addendum += f'{"\n".join(rune_writer)}\n{foot}'
        return addendum

    def eaddendum_lister(stage_key : str):
        eaddendum = []
        # Individual Enemy
        enemies_data_key = ["applyWay", "motion", "enemyTags", "lifePointReduce", "levelType", "rangeRadius", "numOfExtraDrops", "notCountInTotal"]
        #printr(stage)
        for enemy_ref in big_data["stage"][stage_key]["enemyDbRefs"]:
            enemy_id = enemy_ref["id"]
            enemy_lv = enemy_ref["level"]
            enemy_overwrittenData = {}
            if enemy_ref["overwrittenData"]:
                for key in enemy_ref["overwrittenData"]:
                    #printr(key, enemy_id)
                    if key == "attributes":
                        for attribute in enemy_ref["overwrittenData"][key]:
                            if enemy_ref["overwrittenData"][key][attribute]["m_defined"] and (enemy_ref["overwrittenData"][key][attribute]["m_value"] != big_data["enemies"][enemy_id]["lv"][enemy_lv][attribute]):
                                enemy_overwrittenData[attribute] = enemy_ref["overwrittenData"][key][attribute]["m_value"]
                    elif key == "prefabKey" and enemy_ref["overwrittenData"][key]["m_defined"]:
                        enemy_id = enemy_ref["overwrittenData"][key]["m_value"]
                    elif key in ["talentBlackboard", "skills", "spData"]:
                        if enemy_ref["overwrittenData"][key] and enemy_ref["overwrittenData"][key] != big_data["enemies"][enemy_id]["lv"][enemy_lv][key]:
                            match key:
                                case "talentBlackboard":
                                    blackboard_list = []
                                    dupe_value = False
                                    for blackboard in enemy_ref["overwrittenData"][key]:
                                        for talent_blackboard in big_data["enemies"][enemy_id]["lv"][enemy_lv][key]:
                                            if blackboard["key"] != talent_blackboard["key"]:
                                                continue
                                            else:
                                                if blackboard["value"] == talent_blackboard["value"] and blackboard["valueStr"] == talent_blackboard["valueStr"]:
                                                    dupe_value = True
                                                    break
                                                elif blackboard["value"] != talent_blackboard["value"]:
                                                    blackboard_list.append(blackboard)
                                                    break
                                                elif blackboard["valueStr"] != talent_blackboard["valueStr"]:
                                                    blackboard_list.append(blackboard)
                                                    break
                                                printr(f'ermmmmm blackboard not new or wat plz check this\n{G}{blackboard}\n{B}{talent_blackboard}{RE}')
                                        if not blackboard_list and not dupe_value:
                                            printr(f'new blackboard key {Y}{blackboard["key"]}{RE} for : {Y}{enemy_id}{R}({stage_key}){RE}')
                                    if blackboard_list:
                                        enemy_overwrittenData[key] = blackboard_list
                                case _:
                                    printr(f'Update other case soon !!! {Y}(skills, spData){RE}')
                            
                    elif key not in ["name", "description", "viewRadius"]:
                        if enemy_ref["overwrittenData"][key]["m_defined"] and not falsy_compare(enemy_ref["overwrittenData"][key]["m_value"], (big_data["enemies"][enemy_id]["lv"][enemy_lv][key] if key not in enemies_data_key else big_data["enemies"][enemy_id]["data"][key])):
                            #printc(key, (data["enemies"][enemy_id]["lv"][enemy_lv][key] if key not in enemies_data_key else data["enemies"][enemy_id]["data"][key]), enemy_ref["overwrittenData"][key]["m_value"], (data["enemies"][enemy_id]["lv"][enemy_lv][key] if key not in enemies_data_key else data["enemies"][enemy_id]["data"][key]) == enemy_ref["overwrittenData"][key]["m_value"])
                            enemy_overwrittenData[key] = enemy_ref["overwrittenData"][key]["m_value"]
            if enemy_overwrittenData: 
                eaddendum.append({enemy_id:enemy_overwrittenData})
        
        #if eaddendum: printc("eaddendum", stage, eaddendum)
        return eaddendum
    
    def eaddendum_writer(eaddendum, runes = [], buffs = [], diff = "", mul = False):
        def eaddendum_stat_writer(key, value):
            match key:
                case "rangeRadius":
                    return f'an attack range of {decimal_format(value)} tiles'
                case "lifePointReduce":
                    if value == 0:
                        return "Does not deduct [[Life Point|Life Points]]"
                    elif value < 0:
                        printr(f'There {Y}Negative value{RE} case to investigate {R}({stage}, {Y}{enemy_code}{R}){RE}')
                    else:
                        return f'deduct {int(value)} [[Life Point|Life Points]] upon entering a [[Protection Objective]]'
                case "massLevel":
                    return f'weight {value}'
                case _ :
                    return f'{value:.0f} {eaddendum_dict[key]}'
        buff_writer = []        
        if buffs:
            for buff in buffs:
                if buff["prefabKey"] in non_enemy_buffs:
                    continue
                elif buff["prefabKey"] in enemy_buffs:
                    temp = {k:v for k,v in buff.items()}
                    match buff["prefabKey"]:
                        case _:
                            printc(f'There new case in eaddendum buff Towns : {buff["prefabKey"]}')
                else:
                    printc(f'New buff in town !!! {buff["prefabKey"]}')
                    
        #attribute_key = ['maxHp', 'atk', 'def', 'magicResistance', 'moveSpeed', 'attackSpeed', 'baseAttackTime', 'respawnTime', 'hpRecoveryPerSec', 'spRecoveryPerSec', 'massLevel', 'baseForceLevel', 'tauntLevel', 'epDamageResistance', 'epResistance', 'damageHitratePhysical', 'damageHitrateMagical', 'epBreakRecoverSpeed', 'stunImmune', 'silenceImmune', 'sleepImmune', 'frozenImmune', 'levitateImmune', 'disarmedCombatImmune', 'fearedImmune', 'palsyImmune', 'attractImmune']
        eaddendum_dict = {"max_hp": "HP", "maxHp": "HP", "atk": "ATK", "def": "DEF", "magicResistance": "RES", "moveSpeed": "MSPD", "move_speed": "MSPD", "rangeRadius": "Attack Range", "lifePointReduce" : "Life Points", "massLevel": "weight", "baseAttackTime": "BAT"}
        eaddendum_skip = ["name", "description", "spRecoveryPerSec", "talentBlackboard", "spData", "skills"]
        eaddendum_hard_skip = ["name", "description"]
        eaddendum_result = buff_writer
        if runes:
            for rune in runes:
                if rune["key"] in non_enemy_rune:
                    continue
                if rune["key"] not in enemy_rune:
                    printc(f'{Y}{rune["key"]}{RE} is {R}not{RE} in {G}enemy_rune{RE} : {R}{stage} {B}{enemy_rune}{RE}')
                if rune["difficultyMask"] == "ALL" or rune["difficultyMask"] == diff:
                    #printr(stage, "im here")
                    match rune["key"]:
                        case "char_attribute_mul":
                            temp_stat = []
                            temp_value = []
                            char_name = ""
                            for key in rune["blackboard"]:
                                if key in eaddendum_skip:
                                    continue
                                elif key == "char" and rune["blackboard"][key].find("enemy") != -1:
                                    char_name = big_data["enemies"][rune["blackboard"][key]]["data"]["name"]
                                elif key == "char" and rune["blackboard"][key].find("enemy") == -1:
                                    char_name = DB["json_characterEN"][rune["blackboard"][key]]["name"] if rune["blackboard"][key] in DB["json_characterEN"] else token_names_tl.get(rune["blackboard"][key], DB["json_character"][rune["blackboard"][key]]["name"])
                                elif key in eaddendum_dict.keys():
                                    temp_stat.append(eaddendum_dict[key])
                                    temp_value.append(f'{rune["blackboard"][key] - 1:.0%}')
                                else:
                                    printr(f'{Y}{key}{RE} is {R}not{RE} in {Y}eaddendum_dict !!! {R}({stage}){RE}')
                                    exit()
                            if temp_stat and temp_value:
                                eaddendum_result.append(f'\n{char_name} have {join_and(temp_stat)} increased by {join_and(set(temp_value) if len(set(temp_value)) == 1 else temp_value)}.')
                        case "enemy_attribute_mul":
                            temp_stat = []
                            temp_value = []
                            all_enemy = []
                            enemy_name = ""
                            for key in rune["blackboard"]:
                                if key in eaddendum_skip or rune["blackboard"][key] == 0:
                                    continue
                                elif key in eaddendum_dict.keys():
                                    temp_stat.append(eaddendum_dict[key])
                                    temp_value.append(f'{rune["blackboard"][key] - 1:.0%}')
                                elif key == "enemy":
                                    all_enemy = rune["blackboard"][key].split("|")
                                    enemy_name = join_and([big_data["enemies"][enemy]["data"]["name"] for enemy in all_enemy])
                                else:
                                    printr(f'{Y}{key}{RE} is {R}not{RE} in {Y}eaddendum_dict !!! {R}({stage}){RE}')
                                    exit()
                            if temp_stat and temp_value:
                                eaddendum_result.append(f'\n{enemy_name if enemy_name else "All enemies"} have their {join_and(temp_stat)} increased by {join_and(set(temp_value) if len(set(temp_value)) == 1 else temp_value)}.')
                        case "level_enemy_replace":
                            enemy_base = ""
                            enemy_replace = "" 
                            for key in rune["blackboard"]:
                                if key == "key":
                                    base_enemy = rune["blackboard"][key].split("|")
                                    enemy_base = join_and([big_data["enemies"][enemy]["data"]["name"] for enemy in base_enemy])
                                elif key == "value":
                                    replace_enemy = rune["blackboard"][key].split("|")
                                    enemy_replace = join_and([big_data["enemies"][enemy]["data"]["name"] for enemy in replace_enemy])
                                else :
                                    printr(f'new key for {Y}level_enemy_replace{RE} just drop : {B}{key}{R} ({stage}){RE}')
                                    exit()
                            if enemy_base and enemy_replace:
                                eaddendum_result.append(f'\nAll {enemy_base} are replaced with {enemy_replace}.')
                        case _:
                            printr(f'{Y}{stage}{RE} New enemy rune key just drop : {B}{rune["key"]}{RE}')
                else: printr(f'New Difficulty to add : {Y}{rune["difficultyMask"]}{RE}')
        
        # Individual enemies
        for enemy in eaddendum:
            eaddendum_parse = []
            enemy_key = list(enemy.keys())[0]
            enemy_code = big_data["enemies"][enemy_key]["handbook"]["enemyId"]
            enemy_name = DB["json_enemy_handbookEN"]["enemyData"][enemy_code]["name"] if enemy_code in DB["json_enemy_handbookEN"]["enemyData"] else enemy_names_tl.get(enemy_key, f'{big_data["enemies"][enemy_key]["data"]["name"]}({enemy_key})')
            for ref_stat in list(enemy.values()):
                for k,v in ref_stat.items():
                    if k in eaddendum_skip or (k == "attackSpeed" and v == 100):
                        continue
                    if k not in eaddendum_dict:
                        printr(f'{Y}{k}{RE} is {R}not{RE} in {G}eaddendum_dict !!!{RE} {R}({stage}, {Y}{enemy_key}{R}){RE}')
                        exit()
                    if k == "rangeRadius" and v in [0, -1]:
                        continue
                    eaddendum_parse.append(eaddendum_stat_writer(k, v))
                if eaddendum_parse:
                    eaddendum_result.append(f'\n*{enemy_name} have {join_and(eaddendum_parse)}.')
        return "".join(eaddendum_result)
    
    def rune_lister(def_data : list) -> list:
        rune_list = []
        rune_skip = ["env_035_act1break_boss[hud]"]
        for rune in def_data:
            temp = {k:v for k,v in rune.items()}
            temp["blackboard"] = {}
            for blackboard in rune["blackboard"]:
                if blackboard["valueStr"] and blackboard["valueStr"] in rune_skip:
                    temp["blackboard"] = {}
                    break
                else :
                    temp["blackboard"].update({blackboard["key"]:(blackboard["valueStr"] if blackboard["valueStr"] else blackboard["value"])})
            if temp["blackboard"]:
                rune_list.append(temp)
        
        new_rune_list = [new_rune for new_rune in[rune["key"] for rune in rune_list] if new_rune not in (enemy_rune + non_enemy_rune)]
        if new_rune_list != []:
            printr(f'{Y}{stage}{RE} There new rune(s) in town !!! : {B}{new_rune_list}{RE}')
        return rune_list
    
    def global_buff_lister(def_data : list) -> list:
        global_buff = []
        if sorted([buff["prefabKey"] for buff in def_data]) != sorted(list(set([buff["prefabKey"] for buff in def_data]))):
            printc(sorted([buff["prefabKey"] for buff in def_data]), sorted(list(set([buff["prefabKey"] for buff in def_data]))), sorted([buff["prefabKey"] for buff in def_data]) != sorted(list(set([buff["prefabKey"] for buff in def_data]))))
            printc(f'There dupe buff key need fix {[buff["prefabKey"] for buff in def_data]}')
            exit()
        for buff in def_data:
            if buff["prefabKey"] in skip_buffs:
                continue
            elif buff["prefabKey"] not in (non_enemy_buffs + enemy_buffs):
                printr(f'{Y}{stage}{RE} New global buff just drop !!! : {B}{buff["prefabKey"]}{RE}')
            else:
                temp = {k:v for k,v in buff.items()}
                temp["blackboard"] = {}
                for blackboard in buff["blackboard"]:
                    temp["blackboard"][blackboard["key"]] = blackboard["valueStr"] if blackboard["valueStr"] else blackboard["value"]
                global_buff.append(temp)
        return global_buff

    def global_lifepoint(def_data, default = 3, diff = "ALL"):
        if def_data:
            for rune in def_data:
                if rune["key"] == "global_lifepoint" and diff == rune["difficultyMask"]:
                    for blackboard in rune["blackboard"]:
                        if blackboard["key"] == "value":
                            return int(blackboard["value"])
        return default

    def operators_predefine_writer(def_comp_data, def_preauto_data, def_auto_data, fixed):
        #printt("stage, fixed, def_comp_data, def_preauto_data, def_auto_data\n", stage, fixed, def_comp_data, def_preauto_data, def_auto_data ,mode="c")
        def elite_parse(elite):
            if elite.find("PHASE") != -1:
                return elite[-1]
            else:
                printr(f'There is no "PHASE" !!! : {elite}')
                exit()
        
        def op_lister(op, group):
            op_id = op["inst"].get("characterKey", op["alias"])
            op_name = DB["json_characterEN"][op_id]["name"] if op_id in DB["json_characterEN"] else DB["json_characterEN"][op_id]["appellation"]
            op_elite = elite_parse(op["inst"].get("phase", 0))
            op_level = op["inst"].get("level", 1)
            op_skill = op["skillIndex"]
            op_sklv = op["mainSkillLvl"]
            op_trust = op["inst"].get("favorPoint", 0) * 2
            op_mod = op["uniEquipIds"]
            
            group[op_id] = {
                                "name" : op_name, 
                                "elite" : op_elite, 
                                "level" : op_level, 
                                "skill" : op_skill, 
                                "skilllv" : op_sklv, 
                                "trust" : op_trust, 
                                "mod" : op_mod
                            }
            return
        
        def op_writer(text, lister, mod_count):
            def skill_mastery(skill_lv):
                if skill_lv > 7:
                    return f'Spec. Level {skill_lv - 7}'
                else:
                    return f'Level {skill_lv}'
                
            writer = [f'\n{text} = ']
            sorted_lister = lister.keys() if text[1:] == "comp" else sorted(lister.keys(), key = lambda k : lister[k]["name"])
            for op_id in sorted_lister:
                op_name = lister[op_id]["name"]
                if op_name not in all_op:
                    all_op.append(op_name)
                else:
                    redeploy_op.append(op_name)
                op_elite = lister[op_id]["elite"]
                op_level = lister[op_id]["level"]
                skill_id = DB["json_character"][op_id]["skills"][lister[op_id]["skill"]]["skillId"]
                skill_name = DB["json_skillEN"][skill_id]["levels"][0]["name"] if skill_id in DB["json_skillEN"] else skill_names_tl.get(skill_name, f'{DB["json_skill"][skill_id]["levels"][0]["name"]}({skill_id})')
                skill_lv = skill_mastery(lister[op_id]["skilllv"])
                
                trust = lister[op_id]["trust"]
                if trust not in all_trust:
                    all_trust.append(trust)

                if lister[op_id]["mod"]:
                    mod_key = lister[op_id]["mod"][0]["key"]
                    mod_lv = lister[op_id]["mod"][0]["level"]
                    mod_abb = f'{DB["json_uniequip"]["equipDict"][mod_key]["typeIcon"].upper()}'.replace("-D", "-Δ").replace("-A", "-α")
                    
                    all_mod.append([op_name, f'uses {mod_abb} {'[[Operator Module]]' if mod_count == 0 else 'Operator Module'} at Stage {mod_lv}.'])
                    mod_count += 1
                
                writer.append(f'*{{{{C|{op_name}}}}} (Elite {op_elite} Level {op_level}, {{{{Skill|{skill_name}}}}} {skill_lv})')
            
            return "\n".join(writer)
        
        predefine_result = "|fixed = "
        comp = {}
        pre = {}
        auto = {}
        all_op = []
        redeploy_op = []
        all_trust = []
        all_mod = []
        mod_count = 0
        if fixed:
            predefine_result += "true"
            if def_comp_data:
                for op in def_comp_data:
                    op_lister(op, comp)
                predefine_result += op_writer("|comp", comp, mod_count)
            else:
                predefine_result += "\n|comp = None"
            
            if def_preauto_data:
                for op in def_preauto_data:
                    if op["hidden"]:
                        op_lister(op, auto)
                        predefine_result += op_writer("|auto", auto, mod_count)
                    else:
                        op_lister(op, pre)
                        predefine_result += op_writer("|pre", pre, mod_count)
            
            predefine_result += "\n|saddendum = \n"
            
            if len(all_op) > 1:
                if len(all_trust) == 1:
                    predefine_result += f'All Operators have {all_trust[0]}% [[Trust]].'
                else:
                    printr(f'There multiple trusts !!! : {Y}{all_trust}')
                    exit()

                if all_mod:
                    for mod in all_mod:
                        predefine_result += f'\n*{mod[0]} {mod[1]}'
            elif len(all_op) == 1:
                predefine_result += f'{all_op[0]} has {all_trust[0]}% [[Trust]]{f' and {all_mod[0][1]}' if all_mod else ""}.'
            
        return predefine_result
    
    def stage_article_data(data : dict, stage : str, mode : str, diff = "") -> dict:
        #printr(stage)
            
        def drop_lister(def_data : list) -> dict:
            drop_types = ["COMPLETE", "NORMAL", "ADDITIONAL", "SPECIAL"]
            drop_list = {k:{} for k in drop_types}
            drop_rates = {"ALWAYS": 1, "ALMOST": 2, "USUAL": 3, "OFTEN": 4, "SOMETIMES": 5}
            for drop in def_data:
                if drop["dropType"] == "COMPLETE":
                    drop_list["COMPLETE"][drop["id"]] = drop
                else:
                    drop_list["NORMAL"][drop["id"]] = drop
            drop_output = {k:[] for k in drop_types}
            for drop_type in drop_types:
                for drop in sorted(drop_list[drop_type].keys(), key = lambda k : -100000000000 if k == "4002" else DB["json_item"]["items"][k]["sortId"]):
                    drop_name = DB["json_itemEN"]["items"][drop]["name"] if drop in DB["json_itemEN"]["items"] else item_names_tl.get(drop, f'{DB["json_item"]["items"][drop]["name"]}({drop})')
                    drop_rate = 0 if drop_type == "COMPLETE" else drop_rates[drop_list[drop_type][drop]["occPercent"]]
                    if drop_type == "ADDITIONAL":
                        drop_output[drop_type].append(f'{{{{I|{drop_name}}}}}')
                    else:
                        drop_output[drop_type].append(f'{{{{I|{drop_name}|rate={drop_rate}}}}}')
            
            return {k:" ".join(v) for k,v in drop_output.items()}
            
        def auto_deploy_lister(waves):
            ops = []
            for wave in waves:
                for fragment in wave["fragments"]:
                    for action in fragment["actions"]:
                        if action["actionType"] == "ACTIVATE_PREDEFINED" and action["key"].split("_") == "char":
                            ops.append(action["key"])
            #printr(ops)
            
        match mode :
            case "info":
                code = data["stage_data"][stage]["code"]
                part = data["stage_data"][stage]["zoneId"]
                return {
                            "code" : code,
                            "name" : data["stage_data"][stage]["name"],
                            "part" : data["zone"][part]["name"],
                            "prev" : data["zone"][part]["stages"][data["zone"][part]["stages"].index(code) - 1] if data["zone"][part]["stages"].index(code) - 1 in range(len(data["zone"][part]["stages"])) else "",
                            "next" : data["zone"][part]["stages"][data["zone"][part]["stages"].index(code) + 1] if data["zone"][part]["stages"].index(code) + 1 in range(len(data["zone"][part]["stages"])) else "",
                            "desc" : data["stage_data"][stage]["description"],
                            "note" : "",
                            "map name" : "",
                            "type" : data["stage_data"][stage],
                            "adverse" : ""
                    }
            case "data":
                enemies_data = enemies_lister(data["enemies_stage"][stage])
                drop_data = drop_lister(data["stage_data"][stage]["stageDropInfo"]["displayDetailRewards"])
                if diff:
                    stage_code = stage + "#f#"
                    diff_type = data["stage_data"][stage_code]["diffGroup"]
                else:
                    stage_code = stage
                    diff_type = data["stage_data"][stage_code]["diffGroup"]
                    
                return {
                            "cond" : data["stage_data"][stage_code]["description"] if diff == "hard" else "",
                            "level" : stage_level(data["stage_data"][stage_code]["dangerLevel"]),
                            "sanity" : data["stage_data"][stage_code]["apCost"],
                            "drill" : data["stage_data"][stage_code]["practiceTicketCost"] if isinstance(data["stage_data"][stage_code]["practiceTicketCost"], int) and data["stage_data"][stage_code]["practiceTicketCost"] > 0 else "",
                            "unit_limit" : data["stage"][stage]["options"]["characterLimit"],
                            "enemies" : sum(data["enemies_stage"][stage]["counter"][0:2]),
                            "lp" : global_lifepoint(data["stage"][stage]["runes"], data["stage"][stage]["options"]["maxLifePoint"], diff),
                            "dp" : data["stage"][stage]["options"]["initialCost"],
                            "deployable" : token_lister(data["stage"][stage]["predefines"]["tokenCards"]) if data["stage"][stage]["predefines"] else "",
                            "static" : token_lister(data["stage"][stage]["predefines"]["tokenInsts"]) if data["stage"][stage]["predefines"] else "",
                            "terrain" : tile_lister(data["stage"][stage]["mapData"]["tiles"]),
                            "addendum" : "",
                            "firstdrop" : drop_data.get("COMPLETE", ""),
                            "regdrops" : drop_data.get("NORMAL", ""),
                            "specdrops" : drop_data.get("SPECIAL", ""),
                            "extradrops" : drop_data.get("ADDITIONAL", ""),
                            "normal" : enemies_data.get("NORMAL", ""),
                            "elite" : enemies_data.get("ELITE", ""),
                            "boss" : enemies_data.get("BOSS", ""),
                            "eaddendum" : eaddendum_lister(stage_code),
                            "fixed" : data["stage_data"][stage_code]["isPredefined"] if data["stage_data"][stage_code]["isPredefined"] else "",
                            "comp" : data["stage"][stage]["predefines"]["characterCards"] if data["stage"][stage]["predefines"] else "",
                            "pre_auto" : data["stage"][stage]["predefines"]["characterInsts"] if data["stage"][stage]["predefines"] else "",
                            "auto" : auto_deploy_lister(data["stage"][stage]["waves"]),
                            "saddendum" : "",
                            "rune" : rune_lister(data["stage"][stage]["runes"]) if data["stage"][stage]["runes"] else "",
                            "globalBuffs" : global_buff_lister(data["stage"][stage]["globalBuffs"]) if data["stage"][stage]["globalBuffs"] else ""
                        }
            case _ :
                printr(f'Invalid mode {mode}')
                exit()
                return {}
    
    def stage_article_writer(data, mode):
        
        def event_type_writer():
            event_return = (event_name if event_name else event_code) if event_code else ""
            if event_type and event_return:
                return f'|{event_type} = {event_name}'
            else:
                return f'''|episode = {event_return}
                        |intermezzo = {event_return}
                        |sidestory = {event_return}
                        |storycollection = {event_return}
                        '''
        
        def stage_type_writer():
            ######################################################################################################################################################################################
            ## stage > "appearanceStyle"                                ## Wiki stage TYPE
            ######################################################################################################################################################################################
            ## 'MAIN_NORMAL'            Normal Looking                  ## standard         Normal stage                    ||  default
            ## 'TRAINING'               Training Stage                  ## sub              Sub stage                       ||  appearanceStyle = SUB
            ## 'MAIN_PREDEFINED'        Fixed squad - Main stage        ## fixed            Fixed / Training non Cinematic  ||  isPredefined = True
            ## 'SUB'                    Sub yes sub the S one           ## cinematic        Story battle stage              ||  performanceStageFlag = PERFORMANCE_STAGE
            ## 'SPECIAL_STORY'          Hidden story stage / EG         ## hard             hard/boss stage red stage       ||  hilightMark = True
            ## 'HIGH_DIFFICULTY'        H Stage / Extreme               ## extreme          Extreme stage                   ||  appearanceStyle = HIGH_DIFFICULTY
            ## 'MIST_OPS'               MO stage / Mini annihilation    ##
            ######################################################################################################################################################################################
            if data["type"]["performanceStageFlag"] == "PERFORMANCE_STAGE":
                return f'|type = cinematic'
            elif data["type"]["appearanceStyle"] == "HIGH_DIFFICULTY":
                return f'|type = extreme'
            elif data["type"]["appearanceStyle"] == "SUB":
                return f'|type = sub'
            elif data["type"]["hilightMark"] == True:
                return f'|type = hard'
            elif data["type"]["isPredefined"] == True:
                return f'|type = fixed'
            else:
                return f'|type = standard'

        # https://arknights.wiki.gg/wiki/Template:Operation_info/doc
        match mode:
            case "info":
                return f'''
                            ### {data["code"]}
                            {{{{construction}}}}
                            {{{{Spoiler notice|article}}}}
                            {{{{Translation|article}}}}
                            {{{{Operation info
                            |code = {data["code"]}
                            |name = {data["name"]}
                            {event_type_writer()}
                            |part = {data["part"]}
                            |prev = {data["prev"]}
                            |next = {data["next"]}
                            |desc = {desc_cond_writer(data["desc"])}
                            |note = {data["note"]}
                            {stage_type_writer()}
                            }}}}'''.replace("                        ", "").replace("\n\n","\n")
            
            # https://arknights.wiki.gg/wiki/Template:Operation_data/doc
            case "data":
                return f'''{{{{Operation data
                            |cond = {desc_cond_writer(data["cond"])}
                            |level = {data["level"]}
                            |sanity = {data["sanity"]}
                            |drill = {data["drill"]}
                            |unit limit = {data["unit_limit"]}
                            |enemies = {data["enemies"]}
                            |lp = {data["lp"]}
                            |dp = {data["dp"]}
                            |deployable = {data["deployable"]}
                            |static = {data["static"] if data["static"] else ""}
                            |terrain = {tile_writer(data["terrain"])}
                            |addendum = {eaddendum_writer(data["addendum"], data["rune"], data["globalBuffs"])}
                            |firstdrop = {data["firstdrop"]}
                            |regdrops = {data["regdrops"]}
                            |specdrops = {data["specdrops"]}
                            |extradrops = {data["extradrops"]}
                            |normal = {data["normal"]}
                            |elite = {data["elite"]}
                            |boss = {data["boss"]}
                            |eaddendum = {eaddendum_writer(data["eaddendum"], data["rune"], data["globalBuffs"])}
                            {operators_predefine_writer(data["comp"], data["pre_auto"], data["auto"], data["fixed"])}
                            }}}}'''.replace("                        ", "").replace("\n\n","\n")

    def ig_article_data(data, stage_key):
        # https://arknights.wiki.gg/wiki/Template:IG_operation_info
        enemies_data = enemies_lister(data["enemies_stage"][stage_key])
        ig_season = re.search(r'act([0-9]){1,2}multi', event_code)
        return {
                    "code" : data["stage_data"][stage_key]["code"],
                    "name" : data["stage_data"][stage_key]["name"],
                    "nomap" : "", 
                    "map" : "", 
                    "season" : ig_season.group(1) if ig_season else "", 
                    "group" : "", 
                    "desc" : data["stage_data"][stage_key]["description"],
                    "level" : stage_level(data["stage_data"][stage_key]["dangerLevel"]), 
                    "unit limit" : data["stage"][stage_key]["options"]["characterLimit"], 
                    "enemies" : "", 
                    "lp" : global_lifepoint(data["stage"][stage]["runes"], data["stage"][stage]["options"]["maxLifePoint"]),
                    "dp" : data["stage"][stage]["options"]["initialCost"], 
                    "deployable" : token_lister(data["stage"][stage]["predefines"]["tokenCards"]) if data["stage"][stage]["predefines"] else "",
                    "static" : token_lister(data["stage"][stage]["predefines"]["tokenInsts"]) if data["stage"][stage]["predefines"] else "",
                    "terrain" : tile_lister(data["stage"][stage]["mapData"]["tiles"]),
                    "addendum" : "", 
                    "obj1" : "", 
                    "obj2" : "", 
                    "obj2+" : "", 
                    "normal" : enemies_data.get("NORMAL", ""),
                    "elite" : enemies_data.get("ELITE", ""),
                    "boss" : enemies_data.get("BOSS", ""),
                    "eaddendum" : eaddendum_lister(stage_key),
                    "comp" : "",
                    "pre" : "",
                    "auto" : "",
                    "saddendum" : "",
                    "rune" : rune_lister(data["stage"][stage]["runes"]) if data["stage"][stage]["runes"] else "",
                    "globalBuffs" : global_buff_lister(data["stage"][stage]["globalBuffs"]) if data["stage"][stage]["globalBuffs"] else ""
        }
    
    def ig_article_writer(ig_data):
        return f'''{{{{IG operation info
                |code = {ig_data["code"]}
                |name = {ig_data["name"]} 
                |nomap = 
                |map = 
                |season = {ig_data["season"]} 
                |group = 
                |desc = {desc_cond_writer(ig_data["desc"])}
                |level = {ig_data["level"]}
                |unit limit = {ig_data["unit limit"]} 
                |enemies = 
                |lp = {ig_data["lp"]} 
                |dp = {ig_data["dp"]} 
                |deployable = {ig_data["deployable"]} 
                |static = {ig_data["static"]} 
                |terrain = {tile_writer(ig_data["terrain"])}
                |addendum = {addendum_writer(ig_data["rune"], ig_data["globalBuffs"])}
                |obj1 = {ig_data["obj1"]} 
                |obj2 = {ig_data["obj2"]} 
                |obj2+ = {ig_data["obj2+"]} 
                |normal = {ig_data["normal"]}
                |elite = {ig_data["elite"]}
                |boss = {ig_data["boss"]}
                |eaddendum = {eaddendum_writer(ig_data["eaddendum"], ig_data["rune"], ig_data["globalBuffs"])}
                |comp =
                |pre =
                |auto =
                |saddendum =
                }}}}
                {{{{Other event operations}}}}
                [[Category:Rhodes Island Icebreaker Games operations]]
                '''.replace("                ", "").replace("\n\n","\n")

    def tn_article_data(data, stage_key):
        tn_season = re.search(r'act([0-9]){1,2}bossrush', event_code)
        return {
                    "code" : data["stage_data"][stage_key]["code"],
                    "name" : data["stage_data"][stage_key]["name"],
                    "season" : tn_season.group(1) if tn_season else "",
                    "desc" : data["stage_data"][stage_key]["description"],
                    "entitative" : "true" if int(stage_key[-1]) > 1 else "",
                    "orientation" : "true" if stage_key.find("tm") != -1 else "",
                    "cond" : data["stage_data"][stage_key]["description"] if data["stage_data"][stage_key]["description"].find("附加条件：") != -1 else "",
                    "unit limit" : data["stage"][stage_key]["options"]["characterLimit"], 
                    "dp" : data["stage"][stage_key]["options"]["initialCost"], 
                    "lp" : global_lifepoint(data["stage"][stage_key]["runes"], data["stage"][stage_key]["options"]["maxLifePoint"]),
                    "enemies" : sum(data["enemies_stage"][stage_key]["counter"][0:2]),
                    "deployable" : token_lister(data["stage"][stage_key]["predefines"]["tokenCards"]) if data["stage"][stage_key]["predefines"] else "",
                    "static" : token_lister(data["stage"][stage_key]["predefines"]["tokenInsts"]) if data["stage"][stage_key]["predefines"] else "",
                    "terrain" : tile_lister(data["stage"][stage_key]["mapData"]["tiles"]),
                    "addendum" : "",
                    "tn enemies" : data["enemies_stage"][stage_key]["tn_counter"] ,
                    "eaddendum" : eaddendum_lister(stage_key),
                    "ultimate" : "true" if stage_key.find("04") != -1 else "",
                    "comp" : DB["json_activityEN"]["activity"]["BOSS_RUSH"][event_code]["stageAdditionDataMap"][stage_key]["teamIdList"] if event_code in DB["json_activityEN"]["basicInfo"] else DB["json_activity"]["activity"]["BOSS_RUSH"][event_code]["stageAdditionDataMap"][stage_key]["teamIdList"],
                    "rewards" : DB["json_activity"]["activity"]["BOSS_RUSH"][event_code]["stageDropDataMap"][stage_key],
                    "rune" : rune_lister(data["stage"][stage_key]["runes"]) if data["stage"][stage_key]["runes"] else "",
                    "globalBuffs" : global_buff_lister(data["stage"][stage_key]["globalBuffs"]) if data["stage"][stage_key]["globalBuffs"] else ""
        }
    
    def tn_article_writer(tn_data, mode, ext = 0):
        '''
        mode = info/ data/ squad/ rewards
        '''
        def tn_comp_writer(tn_comp_data) -> str:
            tn_comp_result = []
            tn_decode_result = []
            tn_comp_DB = DB["json_activityEN"]["activity"]["BOSS_RUSH"][event_code] if event_code in DB["json_activityEN"]["basicInfo"] else DB["json_activity"]["activity"]["BOSS_RUSH"][event_code]
            ultimate = tn_data["ultimate"]
            tn_comp_txt = ""
            for team in tn_comp_data:
                if team == "free":
                    continue
                tn_comp_result.append(f'{"*" if ultimate else ""}\'\'\'{tn_comp_DB["teamDataMap"][team]["teamName"]}\'\'\'')
                tn_comp_result.append("\n".join(sorted([f'{'**' if ultimate else "*"}[[{DB["json_characterEN"][char]["name"] if char in DB["json_characterEN"] else DB["json_character"][char]["appellation"]}]]' for char in tn_comp_DB["teamDataMap"][team]["charIdList"]])))
                tn_decode_result.append(f'{{{{Decoder|{tn_comp_DB["teamDataMap"][team]["teamBuffName"]}|{tn_comp_DB["teamDataMap"][team]["teamBuffDes"]}}}}}')
                
            if ultimate:
                tn_comp_txt = f'|comp = \n{"\n".join(tn_comp_result)}\n*7 other additional [[Operator|Operators]] (including the [[Support Unit]])'
            else:
                tn_comp_txt = f'|comp = \n{"One of the following and up to 7 additional [[Operator|Operators]] (including the [[Support Unit]]): "}\n{"\n".join(tn_comp_result)}'
            
            tn_comp_txt += f'\n|decoder = {"".join(tn_decode_result)}'
            
            return tn_comp_txt
        
        def tn_reward_writer(tn_rewards_data) -> str:
            rewards_result = ""
            for stage_reward in tn_rewards_data:
                rewards = []
                for key in sorted(stage_reward.keys()):
                    for reward in stage_reward[key]["displayDetailRewards"]:
                        if stage_reward[key]["clearWaveCount"] and reward["dropCount"]:
                            rewards.append(str(reward["dropCount"]))
                rewards_result += f'\n|{", ".join(rewards)}'
            return rewards_result
        
        match mode:
            case "info":
                return f'''{{{{construction}}}}
                            {{{{Spoiler notice|article}}}}
                            {{{{Translation|article}}}}
                            {{{{TN operation info
                            |code = {tn_data["code"]}
                            |name = {tn_data["name"]}
                            |season = {tn_data["season"]}
                            |desc = {desc_cond_writer(tn_data["desc"])}
                            |entitative = {tn_data["entitative"]}
                            }}}}'''.replace("                            ","").replace("\n\n","\n")
            case "data":
                return f'''{{{{TN operation data
                            {f'|orientation = {tn_data["orientation"]}' if tn_data["orientation"] else ""}
                            {f'|cond = {desc_cond_writer(tn_data["cond"])}' if tn_data["cond"] else ""}
                            |unit limit = {tn_data["unit limit"]}
                            |dp = {tn_data["dp"]}
                            |lp = {tn_data["lp"]}
                            |enemies = {tn_data["enemies"]}
                            |deployable = {tn_data["deployable"]}
                            |static = {tn_data["static"]}
                            |terrain = {tile_writer(tn_data["terrain"])}
                            |addendum = {addendum_writer(tn_data["rune"], tn_data["globalBuffs"])}
                            {tn_enemies_lister(tn_data["tn enemies"])}
                            |eaddendum = {eaddendum_writer(tn_data["eaddendum"], tn_data["rune"], tn_data["globalBuffs"])}
                            }}}}'''.replace("                            ","").replace("\n\n","\n").replace("\n\n","\n")
            case "squad":
                return f'''{{{{TN squad
                            |ultimate = {tn_data["ultimate"]}
                            {tn_comp_writer(tn_data["comp"])}
                            }}}}
                            '''.replace("                            ","").replace("\n\n","\n")
            case "rewards":
                return f'''{{{{TN rewards
                            {tn_reward_writer(tn_data)}
                            }}}}
                            {{{{TN operations}}}}
                            '''.replace("                            ","").replace("\n\n","\n")
            case _:
                printr(f'Seem you forgor {Y}mode{RE} : {R}"tn_article_writer"{RE}')

    def vb_article_data(data, stage_key, mode):
        def group_search(groupId, prev_next):
            match prev_next:
                case "prev": 
                    prev_stage = DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["defenseGroupDict"][groupId]["orderedStageList"][0]
                    if stage_key != prev_stage:
                        return data["stage_data"][prev_stage]["code"]
                    else:
                        return ""
                case "next":
                    next_stage = DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["defenseGroupDict"][groupId]["orderedStageList"][1]
                    if stage_key != next_stage:
                        return data["stage_data"][next_stage]["code"]
                    else:
                        return ""
                case _:
                    printr(f'VB group_search mode invalid : {prev_next}')
                    exit()
            
        vb_tl = {
                    "核心突破" : "Kernel Breakthrough",
                    "特别战线" : "Special Front"
                }

        enemies_data = enemies_lister(data["enemies_stage"][stage_key])
        code = data["stage_data"][stage_key]["code"]
        zoneId = data["stage_data"][stage_key]["zoneId"]
        
        match mode:
            case "core":
                prev_in_zone = data["zone"][zoneId]["stages"][data["zone"][zoneId]["stages"].index(code) - 1] if data["zone"][zoneId]["stages"].index(code) - 1 in range(len(data["zone"][zoneId]["stages"])) else ""
                next_in_zone = data["zone"][zoneId]["stages"][data["zone"][zoneId]["stages"].index(code) + 1] if data["zone"][zoneId]["stages"].index(code) + 1 in range(len(data["zone"][zoneId]["stages"])) else ""
                story_desc = DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["offenseStageDict"][stage_key]["storyDesc"]
                boss_info = DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["offenseStageDict"][stage_key]["bossData"]["desc"] if DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["offenseStageDict"][stage_key]["bossData"] else ""
            case "sp":
                group_id = DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["defenseBasicDict"][stage_key]["groupId"]
                prev_in_zone = group_search(group_id, "prev") if group_id else ""
                next_in_zone = group_search(group_id, "next") if group_id else ""
            case "hard":
                story_desc = DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["hardStageDict"][stage_key]["storyDesc"]
                boss_info = DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["hardStageDict"][stage_key]["bossData"]["desc"] if DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["hardStageDict"][stage_key]["bossData"] else ""
            case _ :
                printr(f'VB mode invalid : {mode}')
                exit()
        
        return {
                    "code" : data["stage_data"][stage_key]["code"],
                    "title" : "",
                    "name" : data["stage_data"][stage_key]["name"],
                    "part" : vb_tl.get(data["zone"][zoneId]["name"], data["zone"][zoneId]["name"]),
                    "prev" : prev_in_zone if mode in ["core", "sp"] else "",
                    "next" : next_in_zone if mode in ["core", "sp"] else "",
                    "story" : story_desc if mode in ["core", "hard"] else "",
                    "desc" : data["stage_data"][stage_key]["description"],
                    "boss info" : boss_info if mode in ["core", "hard"] else "",
                    "unit limit" : data["stage"][stage_key]["options"]["characterLimit"],
                    "enemies" : sum(data["enemies_stage"][stage_key]["counter"][0:2]),
                    "dp" : data["stage"][stage_key]["options"]["initialCost"],
                    "deployable" : token_lister(data["stage"][stage]["predefines"]["tokenCards"]) if data["stage"][stage]["predefines"] else "",
                    "static" : token_lister(data["stage"][stage]["predefines"]["tokenInsts"]) if data["stage"][stage]["predefines"] else "",
                    "terrain" : tile_lister(data["stage"][stage]["mapData"]["tiles"]),
                    "addendum" : f'\n*Only {DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["defenseDetailDict"][stage_key]["defenseCharLimit"]} [[Operator]]s can be included to the squad.\n*The [[Support Unit]] cannot be used.' if mode == "sp" else "",
                    "firstreward" : DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["stageRewardDict"][stage_key]["completeRewardCnt"],
                    "regreward" : DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["stageRewardDict"][stage_key]["normalRewardCnt"],
                    "supply" : DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["defenseDetailDict"][stage_key]["buffId"] if mode == "sp" else "",
                    "normal" : enemies_data.get("NORMAL", ""),
                    "elite" : enemies_data.get("ELITE", ""),
                    "boss" : enemies_data.get("BOSS", ""),
                    "eaddendum" : eaddendum_lister(stage_key),
                    "rune" : rune_lister(data["stage"][stage]["runes"]) if data["stage"][stage]["runes"] else "",
                    "globalBuffs" : global_buff_lister(data["stage"][stage]["globalBuffs"]) if data["stage"][stage]["globalBuffs"] else ""
        }

    def vb_article_writer(vb_data, mode):
        def vb_supply(vb_supply_id):
            vb_supply_data = DB["json_activity"]["activity"]["VEC_BREAK_V2"][event_code]["battleBuffDict"][vb_supply_id]
            return f'''|supply = {vb_supply_data["name"]}
                        |supplyno = {int(vb_supply_id.split("_rune")[-1])}
                        |supplydesc = {vb_supply_data["desc"]}'''.replace("                        ","")
        
        return f'''{{{{construction}}}}
                    {{{{Spoiler notice|article}}}}
                    {{{{Translation|article}}}}
                    {{{{VB operation info
                    |code = {vb_data["code"]}
                    |name = {vb_data["name"]}
                    |part = {vb_data["part"]}
                    |prev = {vb_data["prev"]}
                    |next = {vb_data["next"]}
                    |desc = {(f'\'\'{desc_cond_writer(vb_data["story"])}\'\'\n' if vb_data["story"] else "") + desc_cond_writer(vb_data["desc"])}
                    |boss info = {desc_cond_writer(vb_data["boss info"]) if vb_data["boss info"] else ""}
                    |unit limit = {vb_data["unit limit"]}
                    |enemies = {vb_data["enemies"]}
                    |dp = {vb_data["dp"]}
                    |deployable = {vb_data["deployable"]}
                    |static = {vb_data["static"]}
                    |terrain = {tile_writer(vb_data["terrain"])}
                    |addendum = {addendum_writer(vb_data["rune"], vb_data["globalBuffs"], foot = vb_data["addendum"]) if mode == "sp" else addendum_writer(vb_data["rune"], vb_data["globalBuffs"])}
                    |firstreward = {vb_data["firstreward"]}
                    {f'|regreward = {vb_data["regreward"]}' if mode != "sp" else ""}
                    {vb_supply(vb_data["supply"]) if mode == "sp" else ""}
                    |normal = {vb_data["normal"]}
                    |elite = {vb_data["elite"]}
                    |boss = {vb_data["boss"]}
                    |eaddendum = {eaddendum_writer(vb_data["eaddendum"], vb_data["rune"], vb_data["globalBuffs"])}
                    }}}}
                    '''.replace("                    ","").replace("\n\n","\n")

    def enemy_article_writer(data : dict, mode : str):
        def damage_type(damageType : str) -> str:
            match damageType:
                case "PHYSIC":
                    return "Physical"
                case "MAGIC":
                    return "Arts"
                case "NO_DAMAGE":
                    return "None"
                case "HEAL":
                    return "Healing"
                case _ :
                    printr(f'New enemy damage type detected !!!')
                    exit()

        def enemy_trait(traits : list) -> str:
            form = 0
            enemy_traits = "|trait = "
            for trait in traits:
                if trait["textFormat"] == "TITLE":
                    form += 1
                    enemy_traits += f'|form{form} name = {trait["text"]}\n|form{form} =\n'
                else :
                    enemy_traits += f'*{trait["text"]}\n'
            
            return enemy_traits
        
        def enemy_stats(stats : dict) -> str:
            enemy_stat = ""
            for lv in sorted(stats.keys()):
                enemy_stat += f'|lv{lv} hp = {stats[lv]["maxHp"]}\n|lv{lv} atk = {stats[lv]["atk"]}\n|lv{lv} def = {stats[lv]["def"]}\n|lv{lv} res = {stats[lv]["magicResistance"]:0}\n|lv{lv} eres = {stats[lv]["epDamageResistance"]:0}\n|lv{lv} erst = {stats[lv]["epResistance"]:0}\n'
            return enemy_stat
            
        def base_upgrade_key(enemy_key : str, mode : str) -> str:
            '''
                Mode
                    - base
                    - upgrade
            '''
            base_key = ""
            upgrade_key = ""
            
            if len(enemy_key.split("_")) == 3:
                upgrade_key = enemy_key + "_2"
            else:
                upgrade_key = enemy_key[:-1] + str(int(enemy_key[-1]) + 1)
                if len(enemy_key.split("_")[-1]) == "2":
                    base_key = "_".join(enemy_key.split("_")[:-1])
                else:
                    base_key = enemy_key[:-1] + str(int(enemy_key[-1]) - 1)
            
            if mode == "base":
                return base_key
            elif mode == "upgrade":
                return upgrade_key
            else:
                printr(f'{Y}Wrong Mode BAKA !!!{RE} (Mode = {R}"{mode}"{RE} : Key = {R}{enemy_key}){RE}')
                exit()
            
        # https://arknights.wiki.gg/wiki/Template:Enemy_infobox
        data_name = data["data"]["name"] if data["data"]["name"] else ""
        enemy_name = enemy_names_tl.get(data_name, data_name)
        if mode == "info":
            data_prefabKey = data["data"]["prefabKey"] if data["data"]["prefabKey"] else ""
            
            return f'''{{{{construction}}}}
                        {{{{Spoiler notice|article}}}}
                        {{{{Enemy notice|}}}}
                        {{{{Enemy infobox
                        |name = {enemy_name.replace('"',"")}
                        |title = {enemy_name if enemy_name.find('"') != -1 else ""}
                        |image = {enemy_name.replace('"',"") if enemy_name.find('"') != -1 else ""}
                        |code = {data["handbook"]["enemyIndex"]}
                        |cnname = {data["data"]["name"]}
                        |jpname = 
                        |krname = 
                        |type = {data["enemy_type"](data["data"]["enemyTags"])}
                        |grade = {data["data"]["levelType"].capitalize()}
                        |attack = {"Melee/Ranged" if data["data"]["applyWay"] == "ALL" else data["data"]["applyWay"].lower()}
                        |damage = {"/".join([damage_type(damageType) for damageType in data["handbook"]["damageType"]])}
                        |target = {"Aerial" if data["data"]["motion"] == "FLY" else "Ground"}
                        {enemy_trait(data["handbook"]["abilityList"])}
                        |intro = {event_name}
                        |base = {enemy_names_tl[base_upgrade_key(data_prefabKey, "base")] if base_upgrade_key(data_prefabKey, "base")in DB["json_enemy_handbook"]["enemyData"].keys() else ""}
                        |upgrade = {enemy_names_tl[base_upgrade_key(data_prefabKey, "base")] if base_upgrade_key(data_prefabKey, "base") in DB["json_enemy_handbook"]["enemyData"].keys() else ""}
                        }}}}'''.replace("                        ", "")
        if mode == "header":
            return f"The '''{enemy_name if enemy_name.find('"') != -1 else ""}''' is a [[{R} enemy]|{R}] in ''[[Arknights]]''."
        if mode == "enemy desc":
            return f'{{{{Enemy description|{data["handbook"]["description"]}}}}}'
        if mode == "Overview":
            return '''==Overview==
                        {{{{Enemy ability head}}}}
                        {{{{Enemy ability cell|info=|type=|initcd=|cd=}}}}
                        {{{{Table end}}}}'''.replace("                        ", "")
                        
        if mode == "Appearances":
            return '''==Appearances==
                        {{{{Appearances |side stories = [[EP-8]] &bull; [[EP-EX-8]]}}}}'''
        if mode == "stat":
            return f'''==Stats==
                        {{{{Enemy stats
                        {enemy_stats(data["lv"])}
                        |speed = {data["lv"]["0"]["moveSpeed"]}
                        |interval = {data["lv"]["0"]["baseAttackTime"]}
                        |range = {data["data"]["rangeRadius"] if data["data"]["rangeRadius"] != -1 else 0}
                        |range note = 
                        |regen = {data["lv"]["0"]["hpRecoveryPerSec"]}
                        |regen note = 
                        |weight = {data["lv"]["0"]["massLevel"]}
                        |weight note = 
                        |lp = {data["data"]["lifePointReduce"]}
                        |lp note = 
                        |silence = {0 if data["lv"]["0"]["silenceImmune"] else ""}
                        |stun = {0 if data["lv"]["0"]["stunImmune"] else ""}
                        |sleep = {0 if data["lv"]["0"]["sleepImmune"] else ""}
                        |freeze = {0 if data["lv"]["0"]["frozenImmune"] else ""}
                        |levitate = {0 if data["lv"]["0"]["levitateImmune"] else ""}
                        |frighten = {0 if data["lv"]["0"]["disarmedCombatImmune"] else ""}
                        |fear = {0 if data["lv"]["0"]["fearedImmune"] else ""}
                        |addendum = 
                        }}}}
                        '''.replace("                        ", "")
        if mode == "year":
            return f'{{{{Y{R} enemies}}}}'
        
    article_data = []
    ishard = False
    is6star = False
    big_data = wiki_enemies(event_code)
    big_data["enemies_stage"] = {}
    for stage in big_data["stage"]:
        big_data["enemies_stage"][stage] = stage_kill_lister(big_data, stage)
        
    #script_result(big_data)
    #exit()
    # Stage article
    # - https://arknights.wiki.gg/wiki/Template:Operation_info/doc
    # - https://arknights.wiki.gg/wiki/Template:Operation_data/doc
    if event_type in ["vb", "ig", "tn"]:
        mode_info = event_type
        page_footer = "Seasonal game modes"
    else:
        mode_info = "sidestory"
        page_footer = "Side Story operations"
        
    for stage in big_data["stage"].keys():
        if mode_info == "sidestory":
            stage_info = stage_article_data(big_data, stage, "info")
            stage_data = stage_article_data(big_data, stage, "data")
            if big_data["stage_data"][stage]["hardStagedId"]:
                ishard = True
                stage_data_hard = stage_article_data(big_data, stage, "data", "hard")
            
            if big_data["stage_data"][stage]["sixStarStageId"]:
                is6star = True
                stage_data_hard = stage_article_data(big_data, stage, "data", "hard")
            
            if ishard or is6star:
                stage_article = [stage_article_writer(stage_info, "info"), "<tabber>", "Normal Mode=", stage_article_writer(stage_data, "data"), "|-|Challenge Mode=", stage_article_writer(stage_data_hard, "data"), "</tabber>", f'{{{{{page_footer}}}}}']
            else:
                stage_article = [stage_article_writer(stage_info, "info"), stage_article_writer(stage_data, "data"), f'{{{{{page_footer}}}}}']
            article_data += stage_article
        
        elif mode_info == "ig":
            stage_info = ig_article_data(big_data, stage)
            stage_article = [f'### {stage}', ig_article_writer(stage_info), f'{{{{{page_footer}}}}}']
            article_data += stage_article
        
        elif mode_info == "tn":
            tn_diff = ["Basic Trial", "Orientation Trial", "Spectacular Trial", "Ultimate Trial"]
            tn_stage_code_template = [f'{event_code}_0', f'{event_code}_tm0', f'{event_code}_ex0', f'{event_code}_fin0']
            tn_stage_count = len(list(set(big_data["zone"][f'{event_code}_zone1']["stages"])))
            for i in range(1, 1 + tn_stage_count):
                tn_wave_count = big_data["zone"][f'{event_code}_zone1']["stages"].count(f'TN-{i}')
                tn_reward = []
                for j in range(tn_wave_count):
                    tn_stage_code = f'{tn_stage_code_template[j]}{i}'
                    tn_article_data_dict = tn_article_data(big_data, tn_stage_code)
                    tn_reward.append(tn_article_data_dict["rewards"])
                    if j == 0 :
                        article_data += [f'TN-{i}', tn_article_writer(tn_article_data_dict, "info"), "<tabber> Basic Trial="]
                    else:
                        article_data += [f'|-|{tn_diff[j]}=']
                    
                    article_data += [tn_article_writer(tn_article_data_dict, "data")]
                
                article_data += ["</tabber>\n", tn_article_writer(tn_article_data(big_data, f'{tn_stage_code_template[1]}{i}'), "squad"), tn_article_writer(tn_reward, "rewards")]
            break
        
        elif mode_info == "vb":
            if stage.find("sp") != -1 :
                mode = "sp"
                #continue
            elif stage.find("_h") != -1 :
                mode = "hard"
                #continue
            else:
                mode = "core"
                #continue
            stage_info = vb_article_data(big_data, stage, mode)
            stage_article = [f'### {stage}', vb_article_writer(stage_info, mode), f'{{{{{page_footer}}}}}']
            article_data += stage_article

    # Enemies articles
    # - https://arknights.wiki.gg/wiki/Template:Enemy_infobox
    # - https://arknights.wiki.gg/wiki/Template:Appearances
    for enemy in big_data["enemies"]:
        #print(enemy)
        break
        enemy_article_writer(big_data["enemies"][enemy])
    #printc(sorted(data["enemies"].keys()))
    script_result(big_data)
    return article_data

enemy_names_tl = {
                    "enemy_10094_crstf" : "Freelance Sound Technician",
                    "enemy_10094_crstf_2" : "Stubborn Sound Technician", 
                    "enemy_10095_crgst" : "Overacting Extra", 
                    "enemy_10095_crgst_2" : "Art-Immersed Extra", 
                    "enemy_10096_crprp" : "Exhausted Prop Master", 
                    "enemy_10096_crprp_2" : "Attention-Seeking Prop Master", 
                    "enemy_10097_crshd" : "Guilt-Ridden Designer", 
                    "enemy_10097_crshd_2" : "Heart-Submissive Designer", 
                    "enemy_10098_crhro" : "Fated Protagonist", 
                    "enemy_10098_crhro_2" : "Destined Hero", 
                    "enemy_10099_crvln" : "Fated Antagonist", 
                    "enemy_10099_crvln_2" : "Destined Villain", 
                    "enemy_10100_crrol" : "Agile Mannequin", 
                    "enemy_10100_crrol_2" : "Free-Willed Mannequin", 
                    "enemy_10101_crgun" : "Disgruntled Cameraman", 
                    "enemy_10101_crgun_2" : "Short-Tempered Cameraman", 
                    "enemy_10102_crblt" : "", 
                    "enemy_10102_crblt_2" : "", 
                    "enemy_1568_dirctr" : "'Tragodia'",
                    
                    "enemy_8012_mcnd" : "Document",
                    "enemy_8013_mcnrsh" : "Leafmat",
                    "enemy_8014_mcnelp" : "Stopwatch",
                    "enemy_8015_mcnrhd" : "Loudvoice",
                    "enemy_8010_mcnist" : "Mechanist, Heart of Machinery",
                    "enemy_8010_mcnist_2" : "Mechanist, Heart of Machinery",
                    "enemy_8010_mcnist_3" : "Mechanist, Heart of Machinery",
                    "enemy_8011_mcndog" : "Structural Principle",
                    "enemy_8011_mcndog_2" : "Structural Principle",
                    "enemy_8011_mcndog_3" : "Structural Principle"
                }
item_names_tl = {"act43side_token_phantom" : "Mysterious Black Shadow"}
token_names_tl = {}
skill_names_tl = {}

# Trials for Navigator #04
#script_result(wiki_article("act4bossrush", "tn", "Trials for Navigator #04"))

# Rhodes Island Icebreaker Games #1
#script_result(wiki_article("act1multi", "ig", "Rhodes Island Icebreaker Games #1"))

# Vector Breakthrough Mechanist
#script_result(wiki_article("act1break", "vb", "Vector Breakthrough Mechanist"))

'''
temp = [[],[]]
for stage in DB["json_stage"]["stages"]:
    if DB["json_stage"]["stages"][stage]["performanceStageFlag"] not in temp[0]:
        temp[0].append(DB["json_stage"]["stages"][stage]["performanceStageFlag"])
        temp[1].append(stage)
    if DB["json_stage"]["stages"][stage]["performanceStageFlag"] == "PERFORMANCE_STAGE":
        temp[1].append(stage)
printr(temp)
'''
# stage > appearanceStyle = ['MAIN_NORMAL', 'TRAINING', 'MAIN_PREDEFINED', 'SUB', 'SPECIAL_STORY', 'HIGH_DIFFICULTY', 'MIST_OPS']
#                            ['main_00-01', 'tr_01', 'main_01-02', 'sub_02-01', 'spst_08-01', 'hard_05-01', 'act40side_mo01']]

# stage > stageType = [['MAIN', 'SUB', 'GUIDE', 'SPECIAL_STORY', 'DAILY', 'ACTIVITY', 'CAMPAIGN', 'CLIMB_TOWER'],
#                       ['main_00-01', 'sub_03-1-1', 'guide_01', 'spst_08-01', 'wk_melee_1', 'act43side_st01', 'camp_01', 'lt_tr_01']]

# stage > performanceStageFlag = [['NORMAL_STAGE', 'PERFORMANCE_STAGE'], 
#                                  ['main_00-01', 'main_06-15']]