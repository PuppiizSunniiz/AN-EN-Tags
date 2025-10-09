import json
import glob
import re
import subprocess
import os
import inspect
from typing import Any, Callable

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
                "json_dict" : json_load("py/dict.json"),
                "json_activity_json" : json_load("json/activity.json"),
        }

DB = load_json()

################################################################################################################################################################################################################################################
# Util
################################################################################################################################################################################################################################################
def script_result(text : str | list | set | dict ,
                    show : bool = False,
                    indent : int | None = 4,
                    key_sort : bool = False,
                    sort_keys : Callable = lambda x : x,
                    forced_txt : bool = False,
                    txt_nokey : bool = False,
                    no_tab : bool = False,
                    ) -> None:
    '''
        Output result
            STR, LIST, SET  >   TXT
            DICT            >   JSON
    '''
    def dict_to_txt(text : dict, tab : int = 0) -> str:
        to_txt = []
        keys = sorted(text.keys(), key = sort_keys) if key_sort else text.keys()
        for key in keys:
            if isinstance(text[key], dict):
                to_txt.append(f'{"" if tab else "\n"}{"\t" * tab}{key}')
                to_txt += dict_to_txt(text[key], 0 if no_tab else tab + 1)
            else:
                value_text = (f'\n{text[key]}').replace("\n", f'\n{"\t" * (tab + (len(key) + 3) // 4 + 1)}') if text[key] and "\n" in text[key] else text[key]
                to_txt += [f'{"\t" * tab}{value_text}'] if txt_nokey else [f'{"\t" * tab}{key} : {value_text}']
        return to_txt
    
    if isinstance(text, str):
        with open("py/script.txt", "w", encoding = "utf-8") as filepath:
            filepath.write(text)
    elif isinstance(text, list) or isinstance(text, set):
        with open("py/script.txt", "w", encoding = "utf-8") as filepath:
            filepath.write("\n".join(text))
    elif isinstance(text, dict) and indent:
        if forced_txt:
            with open("py/script.txt", "w", encoding = "utf-8") as filepath:
                filepath.write("\n".join(dict_to_txt(text)))
        else :
            with open("py/script.json", "w", encoding = "utf-8") as filepath:
                json.dump(text, filepath, indent = indent, ensure_ascii = False, sort_keys = key_sort)
    else:
        with open("py/script.json", "w", encoding = "utf-8") as filepath:
            json.dump(text, filepath, separators = (",", ":"), ensure_ascii = False, sort_keys = key_sort)
    
    file = f'py/script.{"json" if isinstance(text, dict) and not forced_txt else "txt"}'
    print(f'\n{Y}Script Completed{RE} -> {R}{file}{RE}')
    if show:
        subprocess.run(f'code --reuse-window -g "{os.path.abspath(file)}"', shell = True)

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

################################################################################################################################################################################################################################################
# DB Keys
################################################################################################################################################################################################################################################

#'json_activity', 'json_audio', 'json_battle_equip', 'json_building', 'json_campaign', 'json_chapter', 'json_character', 'json_charm',
#'json_charword', 'json_char_meta', 'json_char_patch', 'json_checkin', 'json_climb_tower', 'json_clue', 'json_crisis', 'json_crisis_v2',
#'json_display_meta', 'json_enemy_handbook', 'json_favor', 'json_gacha', 'json_gamedata', 'json_handbook_info', 'json_handbook', 'json_handbook_team',
#'json_item', 'json_medal', 'json_mission', 'json_open_server', 'json_player_avatar', 'json_range', 'json_replicate', 'json_retro', 'json_roguelike',
#'json_roguelike_topic', 'json_sandbox_perm', 'json_sandbox', 'json_shop_client', 'json_skill', 'json_skin', 'json_stage', 'json_story_review_meta',
#'json_story_review', 'json_story', 'json_tech_buff', 'json_tip', 'json_token', 'json_uniequip', 'json_zone', 'json_enemy_database'

#'json_named_effect', 'json_dict'

# EN

################################################################################################################################################################################################################################################
# Script Playground
################################################################################################################################################################################################################################################

def token_id():
    for token in DB["json_character"].keys():
        if token.startswith("token_"):
            printr(f'{token} | {Y}{token.split("_")[2]}{RE} | {G}{DB["json_character"][token]["appellation"]}{RE} | {B}{DB["json_character"][token]["name"]}')
#token_id()

def story_review_color():
    for event_id in DB["json_story_review_meta"]["miniActTrialData"]["miniActTrialDataMap"].keys():
        printr(f'{event_id:<10} : {DB["json_activity_json"]["Dict"][event_id]["nameEN"]:<30} #{DB["json_story_review_meta"]["miniActTrialData"]["miniActTrialDataMap"][event_id]["themeColor"]}')
#story_review_color()

def all_char_name():
    def get_name(char_data : dict) -> list:
        names = []
        for key in ["name", "appellation"]:
            value = char_data[key]
            if value and value != " ": names.append(value)
        return names
    
    DB["json_characterJP"] = json_load("json/gamedata/ArknightsGameData_YoStar/ja_JP/gamedata/excel/character_table.json")
    DB["json_characterKR"] = json_load("json/gamedata/ArknightsGameData_YoStar/ko_KR/gamedata/excel/character_table.json")
    printr(DB["json_characterKR"].keys())
    char_names = {}
    for char_id in DB["json_character"].keys():
        if not char_id.startswith("char_") : continue
        char_name = get_name(DB["json_character"][char_id])
        for other_lang in [DB["json_characterEN"], DB["json_characterJP"], DB["json_characterKR"]]:
            if char_id in other_lang.keys():
                char_name += get_name(other_lang[char_id])
        char_names[char_id] = list(set(char_name))
    script_result(char_names, True, forced_txt = True)

#all_char_name()

def asciiing():
    ascii_list = [
        [112, 97, 108, 97, 99, 101, 115, 0, 127, 255],
        [79, 114, 105, 103, 105, 110, 105, 117, 109, 32, 109, 117, 116, 101, 666, 404],
        [99, 111, 110, 115, 116, 101, 108, 108, 97, 116, 105, 111, 110, "0xGA"],
        [111, 99, 101, 97, 110, 115, 32, 114, 97, 118, 101, "0xZZ"],
        [115, 112, 101, 99, 116, 101, 114, 115, 32, 99, 108, 97, 105, 109, 0, 255],
    ]
    ascii_result = []
    #printr("".join([chr(c) if isinstance(c, int) and 65 <= c <= 122 else f'[{c}]'for c in ascii_list ]))
    #printr("".join([chr(c) if isinstance(c, int) else f'[{c}]'for c in ascii_list ]))
    for ascii in ascii_list:
        ascii_result.append("".join([chr(c) if isinstance(c, int) and (65 <= c <= 122 or c == 32) else f'[{c}]'for c in ascii]))
    script_result(ascii_result, True)
#asciiing()

#printr(ord("z"), ord("A"))

#print(bytes.fromhex("0x5053"))

#0x4F6D
#0x3252
#0x5343
#0x4344
#0x5053

def enemy_wave_csv():
    all_stage_dict = {}
    all_stage = glob.glob(r'json\gamedata\ArknightsGameData_YoStar\en_US\gamedata\levels\activities\act1multi\*')
    for stage in all_stage:
        stage_id = stage.split("\\")[-1].split(".json")[0]
        stage_json = json_load(stage)
        all_stage_dict[stage_id] = {
                                        "options"       : stage_json["options"],
                                        "runes"         : stage_json["runes"],
                                        "globalBuffs"   : stage_json["globalBuffs"],
                                    }
        stage_waves = []
        for wave in stage_json["waves"]:
            curr_wave = {"advancedWaveTag" : wave["advancedWaveTag"]}
            curr_fragment = []
            for fragment in wave["fragments"]:
                curr_action = []
                spawn_key = ""
                for action in fragment["actions"]:
                    if action["randomSpawnGroupKey"] and action["randomSpawnGroupPackKey"]:
                        spawn_key = action["randomSpawnGroupKey"]
                    elif not action["randomSpawnGroupKey"] and not action["randomSpawnGroupPackKey"]:
                        spawn_key = ""
                    action_detail = {
                                    "actionType"                : action["actionType"],
                                    "key"                       : action["key"],
                                    "count"                     : action["count"],
                                    "preDelay"                  : action["preDelay"],
                                    "interval"                  : action["interval"],
                                    "hiddenGroup"               : action["hiddenGroup"],
                                    "randomSpawnGroupKey"       : spawn_key if spawn_key else action["randomSpawnGroupKey"],
                                    "randomSpawnGroupPackKey"   : action["randomSpawnGroupPackKey"],
                                    "weight"                    : action["weight"],
                                }
                    curr_action.append(action_detail)
                curr_fragment.append(curr_action)
            curr_wave["fragments"] = curr_fragment
            stage_waves.append(curr_wave)
        all_stage_dict[stage_id]["waves"] = stage_waves
    
    script_result(all_stage_dict)
    
    # txt
    script_txt = []
    for stage in all_stage_dict:
        script_txt.append(f'\n{stage}')
        script_txt.append(f'{"wave":>5}{"frag":>5}{"action":>10}{"group":^8}{"GroupKey":<10}{"GroupPack":<10}{"key":^20}{"count":<6}{"preDelay":>10}{"interval":>10}{"weight":<6}')
        for i in range(len(all_stage_dict[stage]["waves"])):
            for j in range(len(all_stage_dict[stage]["waves"][i]["fragments"])):
                for action in all_stage_dict[stage]["waves"][i]["fragments"][j]:
                    hiddenGroup             = action["hiddenGroup"] or ""
                    randomSpawnGroupKey     = action["randomSpawnGroupKey"] or ""
                    randomSpawnGroupPackKey = action["randomSpawnGroupPackKey"] or ""
                    script_txt.append(f'{i:^5}{j:^5}{action["actionType"].split("_")[0]:<10}{hiddenGroup:<8}{randomSpawnGroupKey:^10}{randomSpawnGroupPackKey:^10}{action["key"]:<20}{action["count"]:>6}{action["preDelay"]:^10}{action["interval"]:^10}{action["weight"]:>6}')
    #script_result(script_txt, True)
    
    #csv
    script_txt = []
    script_txt.append("stage|wave|frag|action|group|GroupKey|GroupPack|key|name|ID|Class|count|preDelay|interval|weight")
    for stage in all_stage_dict:
        for i in range(len(all_stage_dict[stage]["waves"])):
            for j in range(len(all_stage_dict[stage]["waves"][i]["fragments"])):
                for action in all_stage_dict[stage]["waves"][i]["fragments"][j]:
                    hiddenGroup             = action["hiddenGroup"] or "-"
                    randomSpawnGroupKey     = action["randomSpawnGroupKey"] or "-"
                    randomSpawnGroupPackKey = action["randomSpawnGroupPackKey"] or "-"
                    try :
                        key_name    = DB["json_enemy_handbookEN"]["enemyData"][action["key"]]["name"] if action["key"].startswith("enemy") else DB["json_characterEN"][action["key"].split("#")[0]]["name"]
                        key_id      = DB["json_enemy_handbookEN"]["enemyData"][action["key"]]["enemyIndex"] if action["key"].startswith("enemy") else "-"
                        key_class   = DB["json_enemy_handbookEN"]["enemyData"][action["key"]]["enemyLevel"] if action["key"].startswith("enemy") else "-"
                    except KeyError:
                        key_name    = action["key"]
                        key_id      = "-"
                        key_class   = "-"
                    script_txt.append(f'{stage}|{i}|{j}|{action["actionType"].split("_")[0]}|{hiddenGroup}|{randomSpawnGroupKey}|{randomSpawnGroupPackKey}|{action["key"]}|{key_name}|{key_id}|{key_class}|{action["count"]}|{action["preDelay"]}|{action["interval"]}|{action["weight"]}')
    script_result(script_txt, True)
    
#enemy_wave_csv()

def dumpling():
    dump_dump = []
    dump_dict = {}
    '''
    #EXP & Skill
    for i in range(9):
        dump_txt = ""
        for j in range(4):
            if dump_txt:
                dump_txt += "|"
            dump_data = DB["json_activity"]["activity"]["HALFIDLE_VERIFY1"]["act1vhalfidle"]["charSkillRankData"][f'TIER_{j + 3}']["skillRankData"]
            if i < len(dump_data):
                dump_txt += str(dump_data[i]["cost"])
            else:
                dump_txt += "-"
        dump_dump.append(dump_txt)
    
    # Enemy drop pool
    dump_data = DB["json_activity"]["activity"]["HALFIDLE_VERIFY1"]["act1vhalfidle"]["enemyItemDropPoolDict"]
    for enemy in dump_data.keys():
        dump_dump.append(f'{enemy}|{dump_data[enemy]["exp"]}|{dump_data[enemy]["mileStoneCnt"]}|{dump_data[enemy]["battleItemDropPool"]}|{dump_data[enemy]["resourceItemDropPool"]}')
    '''
    
    # Equipment
    dump_data = DB["json_activity"]["activity"]["HALFIDLE_VERIFY1"]["act1vhalfidle"]["equipItemData"]
    for equip_type_variant in dump_data.keys():
        for lv in dump_data[equip_type_variant].keys():
            for equip_variant in dump_data[equip_type_variant][lv]:
                bb_runes = []
                for rune in equip_variant["runeData"]["runes"]:
                    for bb in rune["blackboard"]:
                        bb_runes.append(bb)
                dump_dict[equip_variant["alias"]] = {
                                                        "name"          : equip_variant["name"],
                                                        "description"   : equip_variant["runeData"]["description"],
                                                        "runes"         : bb_runes,
                }
    
    script_result(dump_dict, True, key_sort=True)
    #script_result(dump_dump, True)
dumpling()