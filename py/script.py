import json
import glob
import re
import subprocess
import os

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
# Old Script
################################################################################################################################################################################################################################################
def script_result(text):
    '''
        output result
            str     >   text
            dict    >   json
    '''
    if isinstance(text,str):
        with open("py/script.txt", "w", encoding = "utf-8") as filepath:
            filepath.write(text)
    elif isinstance(text,dict):
        with open("py/script.json", "w") as filepath:
            json.dump(text,filepath,indent = 4, ensure_ascii = False)
    
    file = f'py/script.{"txt" if isinstance(text,str) else "json"}'
    print(f'Script Completed -> {file}')
    subprocess.run(f'code --reuse-window -g "{os.path.abspath(file)}"', shell=True)

def skin_lister() :
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

def skill_icon_lister():
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

def ops_e2_talent():
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

def term_kw():
    term_list = []
    for term in DB["json_named_effect"]["termDescriptionDict"]:
        if term[0:2] == "ba":
            term_detail = DB["json_named_effect"]["termDescriptionDict"][term]
            term_list.append(term_detail["termId"]+"\t"+term_detail["termName"]+"\t"+term_detail["description"])
    
    script_result("\n".join(term_list))

def recruit_update():
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
    
def boss_stage_regex():
    '''
        regex for boss stage variant
    '''
    stage = ("ro4_b_2_b")

    test = re.search(r'(ro[0-9]{0,2}_._[0-9]{1,2})(_[a-z]{1}|)',stage)

    print(test.group(1))

def skin_artist():
    for skin in DB["json_skin"]["charSkins"].keys():
        if skin in DB["json_skinEN"]["charSkins"].keys():
        #print(skin)
            if DB["json_skin"]["charSkins"][skin]["displaySkin"]["drawerList"]:
                CN_skin_artist = (" & ").join([x.strip() for x in DB["json_skin"]["charSkins"][skin]["displaySkin"]["drawerList"]])
                EN_skin_artist = (" & ").join([x.strip() for x in DB["json_skinEN"]["charSkins"][skin]["displaySkin"]["drawerList"]])
                if CN_skin_artist != EN_skin_artist:
                    print(f'{skin}\t{CN_skin_artist}\t{EN_skin_artist}')

def va_artist():
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
temp = []
for char in DB["json_character"]:
    if DB["json_character"][char]["subPower"]:
        temp.append(DB["json_character"][char]["appellation"])

print (temp)
