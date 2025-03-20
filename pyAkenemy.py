################################################################################################################################################################################################################################################
# IMPORT
################################################################################################################################################################################################################################################

import json
import re
import glob
from datetime import datetime
from pyfunction import print_header

################################################################################################################################################################################################################################################
# Global Variable
################################################################################################################################################################################################################################################
stage_total = 0
stage_collection = {"stages":{}, "zones":{}, "activity":{}, "enemy":{}}
activity_collection = {"Dict":{}}
akenemy = {
            "gamemode":{
                        "main"      : {"name" : "Main Theme", "activity" : {}},                         # Mode : Main Theme     -> Activity : Episode XX                                -> Stage : XX-YY
                        "sidestory" : {"name" : "Side Story", "activity" : {}},                         # Mode : Side Story     -> Activity : AB : XYZ      -> Zone : FGHIJ             -> Stage : AB-XX
                        "supply"    : {"name" : "Supplies Operations", "activity" : {}},                # Mode : Supplies Op    -> Activity : AB : XYZ (MM)                             -> Stage : AB-CD-X
                        "campaign"  : {"name" : "Annihilation Mission", "activity" : {}},               # Mode : Annihilation   -> Activity : camp_XX
                        "coop"      : {"name" : "CO-OP", "activity" : {}},                              # Mode : Coop           -> Activity : XYZ                                       -> Stage : AB-XX
                        "cc"        : {"name" : "CC : Contingency Contract", "activity" : {}},          # Mode : CC             -> Activity : CC#XX         -> Zone : Main/Rotation     -> Stage : XYZ
                        "is"        : {"name" : "IS : Integrated Strategies", "activity" : {}},         # Mode : IS             -> Activity : IS#XX         -> Zone : Floor XX          -> Stage : XYZ
                        "exp"       : {"name" : "Experimental Gamemode", "activity" : {}},
                        "tn"        : {"name" : "TN : Trials for Navigator", "activity" : {}},          # Mode : TN             -> Activity : TN#XX                                     -> Stage : TN-XX
                        "sss"       : {"name" : "SSS : Stationary Security Service", "activity" : {}},  # Mode : SSS            -> Activity : Tower                                     -> Stage : LT-XX
                        "ra"        : {"name" : "RA : Reclamation Algorithm", "activity" : {}},         # Mode : RA             -> Activity : RA#XX         -> Zone : Fight/Rush/Zone   -> Stage : XYZ
                        "pending"   : []
            },
            "events":{
                
            },
            "enemies":{
                
            }
        }

################################################################################################################################################################################################################################################
# JSON
################################################################################################################################################################################################################################################
def json_load(filepath : str) -> dict :
    if filepath.find("_easy_sub_")  != -1     : filepath=filepath.replace("_easy_sub_","_sub_")
    elif filepath.find("_easy_")    != -1     : filepath=filepath.replace("_easy_","_main_")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_json(data) -> dict :
    match data:
        case "json_Database" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/enemydata/enemy_database.json")
        case "json_DatabaseEN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/levels/enemydata/enemy_database.json")
        case "json_Handbook" : 
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/enemy_handbook_table.json")
        case "json_HandbookEN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/enemy_handbook_table.json")

        case "json_activity" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/activity_table.json")
        case "json_activityEN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/activity_table.json")

        case "json_stage" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/stage_table.json")
        case "json_stageEN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/stage_table.json")

        case "json_zone" : 
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/zone_table.json")
        case "json_zoneEN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/zone_table.json")

        case "json_campaign" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/campaign_table.json")

        case "json_SSS" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/climb_tower_table.json")
        case "json_SSSEN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/climb_tower_table.json")

        case "json_CC" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/crisis_table.json")
        case "json_CC2" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/crisis_v2_table.json")
        case "json_CCEN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/crisis_table.json")
        case "json_CC2EN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/crisis_v2_table.json")

        #case "json_IS0" :
            #return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/roguelike_table.json")
        case "json_IS" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/roguelike_topic_table.json")
        case "json_ISEN0" :
            return json_load("json/gamedata/en_US(Old)/gamedata/excel/roguelike_table.json")
        case "json_ISEN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/roguelike_topic_table.json")

        case "json_RA1" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/sandbox_table.json")
        case "json_RA2" :
            return json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/sandbox_perm_table.json")
        case "json_RA1EN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/sandbox_table.json")
        case "json_RA2EN" :
            return json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/sandbox_perm_table.json")

        case "Fillerjson" :
            return json_load("json/Filler.json")
        case "Activityjson" :
            return json_load("json/activity.json")
        case "EnemyAbility" :
            return json_load("json/enemy_abilities.json")
        
        case _ :
            return json_load(data)

################################################################################################################################################################################################################################################
# Enemy Ability Lister
################################################################################################################################################################################################################################################

def get_stat_grade() :
    ################################################################################################################################################################################################################################################
    # STAT GRADER
    ################################################################################################################################################################################################################################################
    #   
    #   statgrade={"attack":{},"def":{},"magicRes":{},"maxHP":{},"moveSpeed":{},"attackSpeed":{},"enemyDamageRes":{},"enemyRes":{}}
    #
    #   for statclass in json_HandbookEN["levelInfoList"]:
    #       for stat in statclass.keys():
    #           if stat != "classLevel":
    #               statgrade[stat][statclass["classLevel"]]=statclass[stat]["max"] if stat == "attackSpeed" else statclass[stat]["min"]
    #
    #   print(statgrade)
    #
    STAT = {
                'attack'            : {'SS': 5000.0, 'S+': 3000.0, 'S': 2000.0, 'A+': 1500.0, 'A': 1000.0, 'B+': 700.0, 'B': 500.0, 'C': 300.0, 'D': 200.0, 'E': 0.0}, 
                'def'               : {'SS': 5000.0, 'S+': 3000.0, 'S': 2000.0, 'A+': 1200.0, 'A': 1000.0, 'B+': 800.0, 'B': 500.0, 'C': 200.0, 'D': 100.0, 'E': 0.0}, 
                'magicRes'          : {'SS': 90.0, 'S+': 80.0, 'S': 70.0, 'A+': 60.0, 'A': 50.0, 'B+': 30.0, 'B': 20.0, 'C': 10.0, 'D': 1.0, 'E': 0.0}, 
                'maxHP'             : {'SS': 500000.0, 'S+': 250000.0, 'S': 100000.0, 'A+': 25000.0, 'A': 12000.0, 'B+': 8000.0, 'B': 5000.0, 'C': 3500.0, 'D': 1000.0, 'E': 0.0}, 
                'moveSpeed'         : {'SS': 2.0, 'S+': 1.8, 'S': 1.5, 'A+': 1.2, 'A': 1.0, 'B+': 0.9, 'B': 0.7, 'C': 0.5, 'D': 0.3, 'E': 0.0}, 
                'attackSpeed'       : {'SS': 0.5, 'S+': 0.8, 'S': 1.0, 'A+': 1.2, 'A': 1.7, 'B+': 2.6, 'B': 3.5, 'C': 5.0, 'D': 6.9, 'E': -1.0}, 
                'enemyDamageRes'    : {'SS': 90.0, 'S+': 80.0, 'S': 70.0, 'A+': 60.0, 'A': 50.0, 'B+': 30.0, 'B': 20.0, 'C': 10.0, 'D': 1.0, 'E': 0.0}, 
                'enemyRes'          : {'SS': 90.0, 'S+': 80.0, 'S': 70.0, 'A+': 60.0, 'A': 50.0, 'B+': 30.0, 'B': 20.0, 'C': 10.0, 'D': 1.0, 'E': 0.0}
                }

def enemy_ability_list(json_Database : dict, json_DatabaseEN : dict, json_Handbook : dict, json_HandbookEN : dict, json_enemy_ablilies : dict) -> None :
    enemy_database_CN = {}
    enemy_database_EN = {}

    for enemy_key in json_Database["enemies"]:
        enemy_database_CN[enemy_key["Key"]] = enemy_key["Value"]
    for enemy_key in json_DatabaseEN["enemies"]:
        enemy_database_EN[enemy_key["Key"]] = enemy_key["Value"]
        
    enemy_database              = {}
    enemy_abilities_database    = {}
    errortest = 0

    enemy_damageType    = []
    enemy_Tag           = []
    enemy_motion        = []
    enemy_applyWay      = []
    
    for enemy_key in json_Handbook["enemyData"]:
        ## Handbook Test
        if json_Handbook["enemyData"][enemy_key]["hideInHandbook"] or enemy_key == "enemy_1265_durcar":
            continue
        else :
            isEN = enemy_key in enemy_database_EN
            database = enemy_database_EN if isEN else enemy_database_CN
            handbook = json_HandbookEN["enemyData"] if isEN else json_Handbook["enemyData"]

        abilitiescheck = {
                            "abilityList"         : len(handbook[enemy_key]["abilityList"]),
                            "talentBlackboard"    : database[enemy_key][0]["enemyData"]["talentBlackboard"],
                            "skills"              : database[enemy_key][0]["enemyData"]["skills"],
                            "spData"              : database[enemy_key][0]["enemyData"]["spData"],
                            "all"                 : len(handbook[enemy_key]["abilityList"]) or database[enemy_key][0]["enemyData"]["talentBlackboard"] or database[enemy_key][0]["enemyData"]["skills"] or database[enemy_key][0]["enemyData"]["spData"]
                        }
        
        ## Data Test
        if (" & ").join(handbook[enemy_key]["damageType"]) not in enemy_damageType          : enemy_damageType.append((" & ").join(handbook[enemy_key]["damageType"]))
        if str(handbook[enemy_key]["enemyTags"]) not in enemy_Tag                           : enemy_Tag.append(str(handbook[enemy_key]["enemyTags"]))
        if database[enemy_key][0]["enemyData"]["motion"]["m_value"] not in enemy_motion     : enemy_motion.append(database[enemy_key][0]["enemyData"]["motion"]["m_value"])
        if database[enemy_key][0]["enemyData"]["applyWay"]["m_value"] not in enemy_applyWay : enemy_applyWay.append(database[enemy_key][0]["enemyData"]["applyWay"]["m_value"])

        ## Data Handle
        enemy_database[enemy_key] = {
                                    "enemyId"           : handbook[enemy_key]["enemyId"],
                                    "name"              : handbook[enemy_key]["name"],
                                    "enemyIndex"        : handbook[enemy_key]["enemyIndex"],
                                    "sortId"            : handbook[enemy_key]["sortId"],
                                    "enemyLevel"        : handbook[enemy_key]["enemyLevel"],
                                    "description"       : handbook[enemy_key]["description"],
                                    "abilityList"       : handbook[enemy_key]["abilityList"],
                                    "linkEnemies"       : handbook[enemy_key]["linkEnemies"],
                                    "damageType"        : handbook[enemy_key]["damageType"],
                                    
                                    "applyWay"          : database[enemy_key][0]["enemyData"]["applyWay"]["m_value"],
                                    "motion"            : database[enemy_key][0]["enemyData"]["motion"]["m_value"],
                                    "enemyTags"         : database[enemy_key][0]["enemyData"]["enemyTags"]["m_value"],
                                    "lifePointReduce"   : database[enemy_key][0]["enemyData"]["lifePointReduce"]["m_value"],
                                    "rangeRadius"       : database[enemy_key][0]["enemyData"]["rangeRadius"]["m_value"],
                                    "attributes"        : []
                                }

        if abilitiescheck["all"] :
            enemy_abilities_database[enemy_key] = {
                                                    "abilityList"       : handbook[enemy_key]["abilityList"],
                                                    "talentBlackboard"  : [] if abilitiescheck["talentBlackboard"] else None ,
                                                    "skills"            : [] if abilitiescheck["skills"] else None,
                                                    "spData"            : [] if abilitiescheck["spData"] else None,
                                                    "isEN"              : isEN,
                                                    "isCompleted"       : False
                                                }

        for level in range(len(database[enemy_key])):
            level_attributes = {}
            for stat in database[enemy_key][level]["enemyData"]["attributes"] :
                if database[enemy_key][level]["enemyData"]["attributes"][stat]["m_defined"] and database[enemy_key][level]["enemyData"]["attributes"][stat]["m_value"]!=database[enemy_key][0]["enemyData"]["attributes"][stat]["m_value"]:
                    level_attributes[stat]=database[enemy_key][level]["enemyData"]["attributes"][stat]["m_value"]
                else :
                    level_attributes[stat]=database[enemy_key][0]["enemyData"]["attributes"][stat]["m_value"]
            enemy_database[enemy_key]["attributes"].append(level_attributes)
            
            if abilitiescheck["talentBlackboard"]   : enemy_abilities_database[enemy_key]["talentBlackboard"].append(database[enemy_key][level]["enemyData"]["talentBlackboard"] if database[enemy_key][level]["enemyData"]["talentBlackboard"] else database[enemy_key][0]["enemyData"]["talentBlackboard"])
            if abilitiescheck["skills"]             : enemy_abilities_database[enemy_key]["skills"].append(database[enemy_key][level]["enemyData"]["skills"] if database[enemy_key][level]["enemyData"]["skills"] else database[enemy_key][0]["enemyData"]["skills"])
            if abilitiescheck["spData"]             : enemy_abilities_database[enemy_key]["spData"].append(database[enemy_key][level]["enemyData"]["spData"] if database[enemy_key][level]["enemyData"]["spData"] else database[enemy_key][0]["enemyData"]["spData"])

        # Update CN > EN
        #if isEN and not json_enemy_ablilies[enemy_key]["isEN"]:
            #json_enemy_ablilies[enemy_key] = enemy_abilities_database[enemy_key]
        
        ## New Error Check
        if len(database[enemy_key]) > 1 :
            for key in ["applyWay","motion","enemyTags","lifePointReduce","rangeRadius"] :
                if database[enemy_key][1]["enemyData"][key]["m_defined"] and database[enemy_key][0]["enemyData"][key]["m_value"] != database[enemy_key][1]["enemyData"][key]["m_value"] :
                    print(f'{enemy_key} has {key} Level Conflict')
                    errortest += 1
                    if errortest == 1 : print(print_header("Error Test"))
                
        if len(database[enemy_key]) > 1 and abilitiescheck["all"]:
            if database[enemy_key][0]["enemyData"]["spData"] != database[enemy_key][1]["enemyData"]["spData"] and database[enemy_key][0]["enemyData"]["spData"] and database[enemy_key][1]["enemyData"]["spData"]:
                print(f'{enemy_key} has spData Level Conflict')
                errortest += 1
                if errortest == 1 :  print(print_header("Error Test"))

        if len(handbook[enemy_key]["linkEnemies"]):
            linkenemies=[]
            for link in handbook[enemy_key]["linkEnemies"]:
                if link in handbook.keys(): linkenemies.append(link)
            #print(enemy_key,len(linkenemies),linkenemies)
            
    ### print Data test

    print(print_header("Data Test"))
    print(f'\nDamage Type = {enemy_damageType}')
    print(f'Enemy Tags (Handbook "enemyTags") = {enemy_Tag}')
    print(f'Enemy Motion = {enemy_motion}')
    print(f'Enemy Attack Type = {enemy_applyWay}\n')
    
    with open("test/enemy_database_stat.json", "w", encoding="utf-8") as JSON :
        json.dump(enemy_database,JSON,indent = 4, ensure_ascii = False)

    with open("test/enemy_database_abilities.json", "w", encoding="utf-8") as JSON :
        json.dump(enemy_abilities_database, JSON, indent = 4, ensure_ascii = False)
        
    with open("json/enemy_abilities.json", "w", encoding="utf-8") as JSON :
        json.dump(json_enemy_ablilies, JSON, indent = 4, ensure_ascii = False)

################################################################################################################################################################################################################################################
# Stage Lister
################################################################################################################################################################################################################################################

def Stage_Lister(stage_event : str, stage_code : str, stage_name : str, stage_id : str, level_id : str, stage_zone : str, stage_filepath : str, extra = "") -> int :
    '''
    
    Collects stage, enemy, and akenemy data for a given stage event.
    
    Parameters:
    - stage_event: event/activity stage in.
    - stage_code: Code Abbrevation.
    - stage_name: Name of the stage.
    - stage_id: Unique ID for the stage.
    - level_id: File path or identifier for the stage's level.
    - stage_zone: Zone identifier where the stage is located.
    - stage_filepath: File path to retrieve stage-related data.
    - extra: Optional parameter, potentially for additional data (default is empty string).
    
    Returns:
    - Always returns 1.
    
    "act26side_01" : {
        "stageId"   : "act26side_01",                               # ID for call
        "levelId"   : "Activities/act26side/level_act26side_01",    # File path
        "zoneId"    : "act26sre_zone1",                             # Stage Zone
        "code"      : "HE-1",                                       # Stage Code for Display
        "name"      : "Home Sweet Home",                            # Stage Name for Display
        "Event"     : "act26side"                                   # Stage Activity
    },
    '''
    ### Prep Variable
    level_id        = level_id.split("gamedata/levels/")[-1]
    stage_name      = f'{stage_name} (Boss)' if re.search(r"rogue[0-9]{0,2}_[b]-", stage_id) else stage_name
    stage_event     = "1stact" if stage_event == "a001" else stage_event
    stage_zone      = main_zone(stage_id,stage_zone) if stage_event.find("main")!=-1 else (stage_event if stage_zone == "act2vmulti_zone1" else stage_zone)
    
    def Stage_Lister_stage() :
    ### Stage Collect
        if stage_event not in stage_collection["activity"] :
            stage_collection["activity"][stage_event] = []
        if stage_zone not in stage_collection["activity"][stage_event] : 
            stage_collection["activity"][stage_event].append(stage_zone)
            stage_collection["zones"][stage_zone]=[]
        if stage_id not in stage_collection["zones"][stage_zone] :
            stage_collection["zones"][stage_zone].append(stage_id)
        if stage_id not in stage_collection["stages"]:
            stage_collection["stages"][stage_id] = {
                                                    "stageId"   :   stage_id,
                                                    "levelId"   :   level_id,
                                                    "zoneId"    :   stage_zone,
                                                    "code"      :   stage_code,
                                                    "name"      :   stage_name,
                                                    "Event"     :   stage_event
                                                }
        #else : print("DUPE stage ID : ",stage_event,stage_id,stage_name)

    def Stage_Lister_enemy() :
    ### Enemy Collect
        stageforenemylist = json_load(stage_filepath)
        for enemy in stageforenemylist["enemyDbRefs"]:
            enemy_id = enemy["id"]
            if enemy["overwrittenData"]: 
                enemy_id = enemy["overwrittenData"]["prefabKey"]["m_value"] if enemy["overwrittenData"]["prefabKey"]["m_defined"] else enemy["id"]
            stage_collection["enemy"].setdefault(enemy_id,{}).setdefault(get_stage_gamemode(stage_event),{}).setdefault(stage_event,{}).setdefault(stage_zone,[]).append(stage_id)

    
    def Stage_Lister_Akenemy():
    ### Akenemy collect
        stage_gamemode = get_stage_gamemode(stage_event)
        akenemy_activity = akenemy["gamemode"][stage_gamemode]["activity"]
            
        akenemy_activity.setdefault(stage_event,{"name":"","date":0,"zone":{}})
        akenemy_activity[stage_event]["zone"].setdefault(stage_zone, {"name":"","stage":{}})
            
        if stage_id not in akenemy_activity[stage_event]["zone"][stage_zone]["stage"] :
            if stage_event in ["act17d1"] or (stage_gamemode in ["cc","is","ra","campaign"] and stage_event != "act42d0"):
                display_name = stage_name
            elif stage_id.find("tough") != -1 or stage_id.find("easy") != -1:
                display_name = f'{stage_code} : {stage_name} <b>({stage_zone.split(" ")[2]})</b>'
            elif stage_id.find("#f#") != -1:
                display_name = f'{stage_code} : {stage_name} <b>(Challenge)</b>'
            else: display_name = f'{stage_code} : {stage_name}'
            akenemy_activity[stage_event]["zone"][stage_zone]["stage"][stage_id] = display_name
            
    Stage_Lister_stage()
    Stage_Lister_enemy()
    Stage_Lister_Akenemy()
    
    return 1

def RA_rush_Lister(Rushgroup_config : dict, stage_event : str) -> int :
    '''
    stage_event  = RA#??
    
    rush_group = NORMAL | ELITE | etc
    
    => RA#??_GROUP_rushparty
    '''
    stage_counter = 0
    for Rushgroup in Rushgroup_config :
        for Rushparty in range(len(Rushgroup_config[Rushgroup])) :
            enemyGroupKey   = Rushgroup_config[Rushgroup][Rushparty]["enemyGroupKey"]
            stage_code      = f'{stage_event}_{enemyGroupKey}'
            stage_id        = f'{stage_event}_{enemyGroupKey}'
            level_id        = f'{stage_event}/rushparty/{Rushgroup}/{enemyGroupKey}'
            stage_name      = (" ").join(stage_code.split("_")[1:]).capitalize()
            stage_zone      = f'{stage_event} {Rushgroup.capitalize()} Rushparty'
            
            if stage_zone   not in stage_collection["zones"]             : stage_collection["zones"][stage_zone] = []
            if stage_code   not in stage_collection["zones"][stage_zone] : stage_collection["zones"][stage_zone].append(stage_code)
            
            if stage_code not in stage_collection["stages"]:
                stage_collection["stages"][stage_id] ={
                                                        "stageId"   :   stage_id,
                                                        "levelId"   :   level_id,
                                                        "zoneId"    :   stage_zone,
                                                        "code"      :   stage_code,
                                                        "name"      :   stage_name,
                                                        "Event"     :   stage_event
                                                    }
            
            for enemy in Rushgroup_config[Rushgroup][Rushparty]["enemy"]:
                enemy_id = enemy["enemyKey"]
                stage_collection["enemy"].setdefault(enemy_id,{}).setdefault(get_stage_gamemode(stage_event),{}).setdefault(stage_event,{}).setdefault(stage_zone,[]).append(stage_id)
                    
            ### Akenemy collect
            stage_gamemode = get_stage_gamemode(stage_event)
            akenemy_activity = akenemy["gamemode"][stage_gamemode]["activity"]
                
            akenemy_activity.setdefault(stage_event,{"name":"","zone":{}})
            akenemy_activity[stage_event]["zone"].setdefault(stage_zone, {"name":"","stage":{}})
                
            if stage_id not in akenemy_activity[stage_event]["zone"][stage_zone]["stage"] :
                akenemy_activity[stage_event]["zone"][stage_zone]["stage"][stage_id] = stage_name
                
            stage_counter += 1
            
    return stage_counter

def main_zone(stage_id : str,event_id : str) -> str :
    if event_id.split("_")[-1] == "0" :
        zone_prefix = "Prologue : "
    else:
        zone_prefix = f'EP{event_id.split("_")[-1]} : '
    
    if stage_id.find("tr") != -1:
        return f'{zone_prefix}Training'
    elif stage_id.find("easy") != -1:
        return f'{zone_prefix}Story Environment'
    elif stage_id.find("#f#") != -1:
        return f'{zone_prefix}Challenge'
    elif stage_id.find("tough") != -1:
        return f'{zone_prefix}Adverse Environment'
    elif stage_id.find("hard") != -1:
        if int(event_id.split("_")[-1]) > 9:
            return f'{zone_prefix}Adverse Environment'
        elif int(event_id.split("_")[-1]) == 9:
            return f'{zone_prefix}Standard Environment'
        else :
            return f'{zone_prefix}Normal'
    else:
        if int(event_id.split("_")[-1]) > 8:
            return f'{zone_prefix}Standard Environment'
        else:
            return f'{zone_prefix}Normal'

def IS_zone(stage_id : str, IS : str) -> str:
    '''IS = IS#??'''
    match stage_id.split("_")[1].split("-")[0]:
        case "n":
            return f'Floor {stage_id.split("_")[2]}'
        case "b":
            return f'{"Floor" if isinstance(IS_boss(stage_id,IS),int) else ""} {IS_boss(stage_id,IS)}'
        case "t":
            return "Treasure"
        case "ev":
            return "Event"
        case "duel":
            return "Duel"
    return stage_id

def IS_boss(stage_id : str, IS : str) -> str:
    IS_boss_dict = {
                        "IS#1":{
                                    "ro_b_1": 3,
                                    "ro_b_2": 3,
                                    "ro_b_3": 3,
                                    "ro_b_4": 5,
                                    "ro_b_5": 5,
                                    "ro_b_6": 6,
                                },
                        "IS#2":{
                                    "ro1_b_1": 3,
                                    "ro1_b_2": 3,
                                    "ro1_b_3": 3,
                                    "ro1_b_4": 3,
                                    "ro1_b_5": 3,
                                    "ro1_b_6": 5,
                                    "ro1_b_7": 5,
                                    "ro1_b_8": 6,
                                    "ro1_b_9": 6 
                                },
                        "IS#3":{
                                    "ro2_b_1"   : 3,
                                    "ro2_b_2"   : 3,
                                    "ro2_b_3"   : 3,
                                    "ro2_b_4"   : 5,
                                    "ro2_b_5"   : 5,
                                    "ro2_b_6"   : 6,
                                    "ro2_b_7"   : 6,
                                    "ro2_b_8"   : "Wonderland",
                                    "ro2_b_9"   : "Wonderland",
                                    "ro2_b_10"  : "Wonderland"
                                },
                        "IS#4":{
                                    "ro3_b_1"   : 3,
                                    "ro3_b_2"   : 3,
                                    "ro3_b_3"   : 3,
                                    "ro3_b_4"   : 5,
                                    "ro3_b_5"   : 5,
                                    "ro3_b_6"   : 6,
                                    "ro3_b_7"   : 6,
                                },
                        "IS#5":{
                                    "ro4_b_1"    : 3,
                                    "ro4_b_2"    : 3,
                                    "ro4_b_3"    : 3,
                                    "ro4_b_4"    : 5,
                                    "ro4_b_5"    : 5,
                                    "ro4_b_6"    : 6,
                                    "ro4_b_7"    : 6
                                }
                    }
    return IS_boss_dict[IS].get(re.search(r'(ro[0-9]{0,2}_._[0-9]{1,2})(_[a-z]{1}|)',stage_id).group(1),"???") # cut variant _b _c

def get_stage_gamemode(stage_event : str) -> str :
        if stage_event.find("main_") != -1 :
            return "main"
        elif stage_event.find("weekly_") != -1 :
            return "supply"
        elif stage_event.find("camp_") != -1 :
            return "campaign"
        
        elif stage_event == "act17d1" or re.search(r"act[0-9]{1,2}(vmulti|multi)",stage_event):
            return "coop"
        elif stage_event == "PinchOut" or re.search(r"CC(|BP)#",stage_event) : 
            return "cc"
        elif stage_event.find("IS#") != -1 :
            return "is"
        
        elif re.search(r"act[0-9]{1,2}(lock|vecb|vautochess|arcade)",stage_event) or stage_event in ["act42d0"]: # act42d0 = DOS
            return "exp"
        
        elif stage_event.find("bossrush") != -1 :
            return "tn"
        elif stage_event.find("tower_") == 0 :
            return "sss"
        elif stage_event.find("RA#") != -1:
            return "ra"

        elif re.search(r"act[0-9]{1,2}(side|mini|d0|d3|d5)",stage_event) or stage_event == "1stact": # 1stact = Grani
            return "sidestory"
        else:
            return "pending"

################################################################################################################################################################################################################################################
# Stage collection
################################################################################################################################################################################################################################################
def decorator(collector) :
    def decorate(*args): 
        global stage_total       
        count_stage(args[0])

        collection_result = collector(*args)

        stage_total += count_total_stage(collection_result)
    
    return decorate

def count_stage(*args):
    stage_count = sum([len(arg.keys()) if isinstance(arg, dict) else len(arg) for arg in args])
    print(f'\nStage to Check : {stage_count} stages')

def count_total_stage(collection_result : list):
    print(f'Stage Listed : {collection_result[0]} stages')
    print(f'>> {collection_result[1]} Stage Completed')
    
    return collection_result[0]

def stage_json_stage_collect(json_stage, json_stageEN):
    ## stage_table || All - Main Theme / Side Story / Weekly stage / Annihilation
    @decorator
    def stage_main(json_stage, json_stageEN):
        stage_counter = 0
        for stage in json_stage:
        # ignore Challenge and Story -> [tutorial, challenge, story, story2, easy mode, emperor fun mode, ???] & ??? & SSS_EX_stage & TN_stage (only normal accept)
            if not [stage for prohibit in ["guide_","st_","_st","act4d0","act17d7"] if stage.find(prohibit) != -1] and json_stage[stage]["levelId"].find("Activities/ACT21side/Mission/")==-1 and not re.search(r"lt_.+_ex", stage) and not re.search(r"bossrush_(tm|ex|fin)", stage):
                if json_stage[stage]["levelId"].find("/") !=- 1:
                    if json_stage[stage]["levelId"].split("/")[1] in ["Campaign"]:
                        stage_event = json_stage[stage]["stageId"].lower()
                    elif json_stage[stage]["levelId"].split("/")[1] in ["Main","Training","Hard","Weekly","Promote","Legion"]:
                        stage_event = json_stage[stage]["zoneId"].lower()
                    else:
                        stage_event = json_stage[stage]["levelId"].split("/")[1].lower()
                elif json_stage[stage]["levelId"].split("\\")[1]:
                    stage_event = json_stage[stage]["levelId"].split("\\")[1].lower()

            # add Stagezone
                stage_code       = json_stage[stage]["stageId"] if json_stage[stage]["stageType"] == "CAMPAIGN" else json_stage[stage]["code"]
                stage_name       = json_stageEN[stage]["name"] if stage in json_stageEN.keys() else json_stage[stage]["name"]
                stage_id         = json_stage[stage]["stageId"]
                level_id         = json_stage[stage]["levelId"]
                stage_zone       = json_stage[stage]["stageId"] if json_stage[stage]["stageType"] == "CAMPAIGN" else (f'{stage_event}' if stage_event in ["act7d5","act6d5","act4d0"] else json_stage[stage]["zoneId"])
                stage_filepath   = f'json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/{level_id.lower()}.json'
                
                stage_counter += Stage_Lister(stage_event, stage_code, stage_name, stage_id, level_id, stage_zone, stage_filepath)
        
        return [stage_counter, "Main & Activity"]
    
    stage_main(json_stage["stages"], json_stageEN["stages"])

def COOP_stage_collect(Fillerjson) :
## COOP1 : Defense Protocols (罗德岛防御协议) "act17d1"
    COOP = glob.glob("json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/activities/act17d1/*")
    
    @decorator
    def COOP_main(COOP):
        stage_counter = 0
        for stagepath in COOP:
            stage_name   = Fillerjson["stage_name"][stagepath.split("\\")[-1]]
            stage_id     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
            
            stage_counter += Stage_Lister("act17d1",stage_id,stage_name,stage_id,stagepath,"act17d1",stagepath)
            
        return [stage_counter, "COOP"]

    COOP_main(COOP)

def CC_stage_collect(Fillerjson, json_CC, json_CC2, json_activityEN) :
## CC : Contingency Contract (危机合约)

    CC1 = glob.glob("json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/obt/rune/*")
    CC2 = glob.glob("json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/obt/crisis/v2/*")
    POT = glob.glob("json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/activities/act38rune/*")

### CC Beta (act5d1) & CC Season 1 (crisis_table)
    
    @decorator
    def CC_main(CC1):
        stage_counter = 0
        for CC in range(len(json_CC["seasonInfo"])+1):
            CC_num   = str(CC - 1) if CC - 1 >= 10 else "0" + str(CC - 1)
            CC_Zone  = f'CC#{CC_num}' if CC > 0 else "CC#Beta"
            stage_num = str(CC + 1) if CC + 1 >= 10 else "0" + str(CC + 1)
            CC_Stage = [stage for stage in CC1 if re.search(rf'{stage_num}-.+\.json',stage)]+([f'json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/obt/rune\\{rotatestage}' for rotatestage in Fillerjson["CCRotate"][CC_Zone]] if CC_Zone in Fillerjson["CCRotate"] else [])
            
            for stagepath in CC_Stage:
                stage_name   = Fillerjson["stage_name"][stagepath.split("\\")[-1]] if re.search(rf'{stage_num}-.+\.json',stagepath) else Fillerjson["stage_name"][stagepath.split("\\")[-1]].split(" (Main)")[0]
                stage_id     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
                
                stage_counter += Stage_Lister(CC_Zone,stage_id,stage_name,stage_id,stagepath,CC_Zone,stagepath)
        
        return [stage_counter, "CC Operation"]
    
    CC_main(CC1)

### POT (act38rune)
    @decorator
    def POT_main(POT):
        stage_counter = 0
        for stagepath in POT:
            stage_name   = Fillerjson["stage_name"][stagepath.split("\\")[-1]]
            stage_id     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
            
            stage_counter += Stage_Lister("PinchOut",stage_id,stage_name,stage_id,stagepath,"PinchOut",stagepath)
            
        return [stage_counter, "PinchOut"]
    
    POT_main(POT)

## DOS "act42d0"
    DOS = json_activityEN["activity"]["TYPE_ACT42D0"]["act42d0"]
    
    @decorator
    def DOS_main(main_stage, challenge_stage):
        stage_counter = 0
        for stage in main_stage.keys():
            stage_code       = main_stage[stage]["code"]
            stage_name       = main_stage[stage]["name"]
            stage_id         = main_stage[stage]["stageId"]
            level_id         = main_stage[stage]["levelId"]
            stage_zone       = main_stage[stage]["areaId"]
            stage_filepath   = "json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/"+level_id.lower()+".json"
            
            stage_counter += Stage_Lister("act42d0",stage_code,stage_name,stage_id,level_id,stage_zone,stage_filepath)
            
        for stage in challenge_stage.keys():
            stage_code       = challenge_stage[stage]["code"]
            stage_name       = challenge_stage[stage]["name"]
            stage_id         = challenge_stage[stage]["stageId"]
            level_id         = challenge_stage[stage]["levelId"]
            stage_filepath   = "json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/"+level_id.lower()+".json"
            
            stage_counter += Stage_Lister("act42d0",stage_code,stage_name,stage_id,level_id,"challenge",stage_filepath)
            
        return [stage_counter, "DOS"]
    
    DOS_main(DOS["stageInfoData"], DOS["challengeInfoData"])
    
### CC Season 2 (crisis_v2_table)
    @decorator
    def CC2_main(CC2):
        stage_counter = 0
        for CC in range(len(json_CC2["seasonInfoDataMap"].keys())):
            CC_num = str(CC+1) if CC+1 >= 10 else "0"+str(CC+1)
            CC_Zone = f'CCBP#{CC_num}'
            stage_num = str(CC+1) if CC+1 >= 10 else "0"+str(CC+1)
            CC_Stage = [stage for stage in CC2 if re.search(rf'{stage_num}-.+\.json',stage)]+(["json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/obt/crisis/v2\\"+rotatestage for rotatestage in Fillerjson["CCRotate"][CC_Zone]] if CC_Zone in Fillerjson["CCRotate"].keys() else [])
            if CC == 0 : CC_Stage = list(filter(lambda x : re.search(rf'v2_01-0[^46]',x),CC_Stage))
            for stagepath in CC_Stage:
                stage_name   = Fillerjson["stage_name"][stagepath.split("\\")[-1]] if re.search(rf'{stage_num}-.+\.json',stagepath) else Fillerjson["stage_name"][stagepath.split("\\")[-1]].split(" (Main)")[0]
                stage_id     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]

                stage_counter += Stage_Lister(CC_Zone,stage_id,stage_name,stage_id,stagepath,CC_Zone,stagepath)

        return [stage_counter, "CC Battleplan"]
    
    CC2_main(CC2)

def IS_stage_collect(json_ISEN0, json_IS, json_ISEN):
## IS
### IS 1
    @decorator
    def IS0_main(IS0_Stage):
        stage_counter = 0
        for ISstage in IS0_Stage.keys():
            if ISstage.split("_")[1]!="e":
                stage_name  = IS0_Stage[ISstage]["name"]
                stagepath   = f'json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/{IS0_Stage[ISstage]["levelId"].lower()}.json'
                stage_id    = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
                stage_zone  = f'IS#1 {IS_zone(ISstage,"IS#1")}'

                stage_counter += Stage_Lister("IS#1",stage_id,stage_name,stage_id,stagepath,stage_zone,stagepath,"IS#1")

        return [stage_counter, "IS#1"]
    
    IS0_main(json_ISEN0["stages"])

### IS 2+
    for ISseason in json_IS["details"].keys():
        @decorator
        def IS_main(IS_season_stage):
            stage_counter = 0
            for ISstage in IS_season_stage.keys():
                if ISstage.split("_")[1]!="e":
                    try:
                        stage_name =  json_ISEN["details"][ISseason]["stages"][ISstage]["name"]
                    except:
                        stage_name =  IS_season_stage[ISstage]["name"]
                    
                    stagepath   = f'json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/{IS_season_stage[ISstage]["levelId"].lower()}.json'
                    stage_event = f'IS#{int(ISseason[-1])+1}'
                    stage_id    = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
                    stage_zone  = f'{stage_event} {IS_zone(ISstage,stage_event)}'
                    
                    stage_counter += Stage_Lister(stage_event, stage_id, stage_name, stage_id, stagepath, stage_zone, stagepath, stage_event)
            
            return [stage_counter, stage_event]
    
        IS_main(json_IS["details"][ISseason]["stages"])

def RA_stage_collect(json_RA1EN, json_RA2, json_RA2EN): #
### RA#1
    @decorator
    def RA0_main(RA0_stages):
        #### Map Stage
        stage_counter = 0
        stage_preview = json_RA1EN["sandboxActTables"]["act1sandbox"]["rewardConfigDatas"]["stageDefaultPreviewRewardDict"]
        for RAstage in RA0_stages.keys():
            stagepath   = f'json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/{RA0_stages[RAstage]["levelId"].lower()}.json'
            stage_name  = RA0_stages[RAstage]["name"]
            if RAstage in stage_preview:
                match stage_preview[RAstage]["rewardList"][0]["rewardType"]:
                    case "BUILDINGMAT" :
                        stage_zone = 'RA#1 Field : Building Material'
                    case "FOODMAT":
                        stage_zone = 'RA#1 Field : Food Material'
                    case _ :
                        print(RAstage)
                        stage_zone = 'RA#1 Field : ???'
            else :
                stage_zone = "RA#1 Field : Battle"
            
            stage_counter += Stage_Lister("RA#1",RAstage,stage_name,RAstage,stagepath,stage_zone,stagepath)
        return [stage_counter, "RA#1 Map"]
    
    @decorator
    def RA0_rush(_):
        #### Rush Parties
        stage_counter = 0
        stage_counter += RA_rush_Lister(Rushgroup_config, "RA#1")
                        
        return [stage_counter, "RA#1 Rush Party"]
    
    Rushgroup_config = json_RA1EN["sandboxActTables"]["act1sandbox"]["rushEnemyGroup"]["rushEnemyGroupConfigs"]
    
    RA0_main(json_RA1EN["sandboxActTables"]["act1sandbox"]["stageDatas"])
    RA0_rush([rushparty for rushgroup in Rushgroup_config for rushparty in Rushgroup_config[rushgroup]])
    
### RA#2 and maybe more ???
    for RAseason in json_RA2["detail"]["SANDBOX_V2"].keys():
        stage_event = f'RA#{int(RAseason[-1])+1}'
        @decorator
        def RA_main(RA_stages):
        #### Map Stage
            stage_counter = 0
            for RAstage in RA_stages.keys():
                #stage_name = RA_stages[RAstage]["name"]
                try:
                    stage_name = json_RA2EN["detail"]["SANDBOX_V2"][RAseason]["stageData"][RAstage]["name"]
                except:
                    stage_name = RA_stages[RAstage]["name"]
                
                stage_preview = json_RA2["detail"]["SANDBOX_V2"][RAseason]["rewardConfigData"]["stageMapPreviewRewardDict"]
                
                stagepath = f'json/gamedata/ArknightsGameData/zh_CN/gamedata/levels/{RA_stages[RAstage]["levelId"].lower()}.json'
                
                if RAstage in stage_preview:
                    match stage_preview[RAstage]["rewardList"][0]["rewardType"]:
                        case "BUILDINGMAT" :
                            stage_zone = f'{stage_event} Field : Building Material'
                        case "FOODMAT":
                            stage_zone = f'{stage_event} Field : Food Material'
                        case _ :
                            print(RAstage)
                            stage_zone = f'{stage_event} Field : ???'
                else :
                    stage_zone = f'{stage_event} Field : Battle'
                
                stage_counter += Stage_Lister(stage_event, RAstage, stage_name, RAstage, stagepath, stage_zone, stagepath)
            return [stage_counter, f'{stage_event} Map']
        
        @decorator
        def RA_rush(_):
            #### Rush Parties
            stage_counter = 0
            stage_counter += RA_rush_Lister(Rushgroup_config, stage_event)
            return [stage_counter, f'{stage_event} Rush Party']
        
        Rushgroup_config = json_RA2["detail"]["SANDBOX_V2"][RAseason]["rushEnemyData"]["rushEnemyGroupConfigs"]
        
        RA_main(json_RA2["detail"]["SANDBOX_V2"][RAseason]["stageData"])
        RA_rush([rushparty for rushgroup in Rushgroup_config for rushparty in Rushgroup_config[rushgroup]])

################################################################################################################################################################################################################################################
# Activity
################################################################################################################################################################################################################################################
def get_activity_DB() -> dict :
    return  {
                "activity"      : load_json("json_activity"),
                "activityEN"    : load_json("json_activityEN"),
                "zone"          : load_json("json_zone"),
                "zoneEN"        : load_json("json_zoneEN"),
                "stage"         : load_json("json_stage"),
                "campaign"      : load_json("json_campaign"),
                "SSS"           : load_json("json_SSS"),
                "SSSEN"         : load_json("json_SSSEN"),
                "CC"            : load_json("json_CC"),
                "CCEN"          : load_json("json_CCEN"),
                "CC2"           : load_json("json_CC2"),
                "CC2EN"         : load_json("json_CC2EN"),
                "IS"            : load_json("json_IS"),
                "ISEN"          : load_json("json_ISEN"),
                "RA2"           : load_json("json_RA2")
    }

def activity_collect(Activityjson):
    DB = get_activity_DB()
    timeline = []

## Activity
    for act in DB["activity"]["basicInfo"].keys():
        if DB["activity"]["basicInfo"][act]["hasStage"]:
            activity_collection["Dict"][act] = {
                    "nameCN"    : DB["activity"]["basicInfo"][act]["name"],
                    "nameEN"    : ("DOS : " if act == "act42d0" else "") + (DB["activityEN"]["basicInfo"][act]["name"] if act in DB["activityEN"]["basicInfo"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else "")) + (f' #{act.split("act")[-1].split("bossrush")[0]}' if act.find("bossrush")!= -1 and act in DB["activityEN"]["basicInfo"].keys() else ""),
                    "startCN"   : DB["activity"]["basicInfo"][act]["startTime"]
            }
            if activity_collection["Dict"][act]["startCN"] > 0 : timeline.append([act,activity_collection["Dict"][act]["nameEN"] if activity_collection["Dict"][act]["nameEN"] else activity_collection["Dict"][act]["nameCN"],activity_collection["Dict"][act]["startCN"]])

## Main
    for act in DB["zone"]["mainlineAdditionInfo"].keys():
        activity_collection["Dict"][act] = {
                    "nameCN"    : f'{DB["zone"]["zones"][act]["zoneNameFirst"]} : {DB["zone"]["zones"][act]["zoneNameSecond"]}',
                    "nameEN"    : f'{DB["zoneEN"]["zones"][act]["zoneNameFirst"]} : {DB["zoneEN"]["zones"][act]["zoneNameSecond"]}' if act in DB["zoneEN"]["zones"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else f'{DB["zone"]["zones"][act]["zoneNameFirst"]} : {DB["zone"]["zones"][act]["zoneNameSecond"]}'),
                    "startCN"   : DB["zone"]["mainlineAdditionInfo"][act]["zoneOpenTime"]
        }
        if activity_collection["Dict"][act]["startCN"] > 0 : timeline.append([act,activity_collection["Dict"][act]["nameEN"] if activity_collection["Dict"][act]["nameEN"] else activity_collection["Dict"][act]["nameCN"],activity_collection["Dict"][act]["startCN"]])

# Other act
## Weekly
    for act in stage_collection["activity"].keys():
        if act.find("weekly_") == 0 :
            activity_collection["Dict"][act] = {
                "nameCN"    : f'{DB["zone"]["zones"][act]["zoneNameSecond"]} ({stage_collection["zones"][act][0][:-2]})',
                "nameEN"    : Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else (f'{stage_collection["zones"][act][0][:-2]} : {DB["zoneEN"]["zones"][act]["zoneNameSecond"]}' if act in DB["zoneEN"]["zones"].keys() else f'{stage_collection["zones"][act][0][:-2]} : {DB["zone"]["zones"][act]["zoneNameSecond"]}'),
                "startCN"   : -1
        }
## Annihilation
        elif act.find("camp") == 0 :
            activity_collection["Dict"][act] = {
                "nameCN"    : DB["stage"]["stages"][act]["name"],
                "nameEN"    : stage_collection["stages"][act]["name"],
                "startCN"   : DB["campaign"]["campaignRotateStageOpenTimes"][int(act[-2:])-1]["startTs"] if act.find("_r_")!= -1 else -1
        }
## SSS (lt)
        elif act.find("tower_") == 0 :
            activity_collection["Dict"][act] = {
                "nameCN"    : DB["SSS"]["towers"][act]["name"] if act in DB["SSS"]["towers"].keys() else (Activityjson["Dict"][act]["nameCN"] if act in Activityjson["Dict"].keys() else None),
                "nameEN"    : DB["SSSEN"]["towers"][act]["name"] if act in DB["SSSEN"]["towers"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else (DB["SSS"]["towers"][act]["name"] if act in DB["SSS"]["towers"].keys() else None)),
                "startCN"   : -1
        }
## CC#Beta (act5d1)
        elif act == "CC#Beta" :
            activity_collection["Dict"][act] = {
                "nameCN"    : activity_collection["Dict"]["act5d1"]["nameCN"],
                "nameEN"    : f'{act} : {activity_collection["Dict"]["act5d1"]["nameEN"]}',
                "startCN"   : activity_collection["Dict"]["act5d1"]["startCN"]
        }
## CC Operation
        elif act.find("CC#") == 0 :
            activity_collection["Dict"][act] = {
                "nameCN"    : DB["CC"]["seasonInfo"][int(act.split("CC#")[-1])]["name"],
                "nameEN"    : f'{act} : {DB["CCEN"]["seasonInfo"][int(act.split("CC#")[-1])]["name"]}',
                "startCN"   : DB["CC"]["seasonInfo"][int(act.split("CC#")[-1])]["startTs"]
        }
## Pinch out (act38d1)
        elif act == "PinchOut" :
            activity_collection["Dict"][act] = {
                "nameCN"    : activity_collection["Dict"]["act38d1"]["nameCN"],
                "nameEN"    : activity_collection["Dict"]["act38d1"]["nameEN"],
                "startCN"   : activity_collection["Dict"]["act38d1"]["startCN"]
        }
## CC Battleplan
        elif act.find("CCBP#") == 0 :
            activity_collection["Dict"][act] = {
                "nameCN"    : DB["CC2"]["seasonInfoDataMap"][f'crisis_v2_season_{int(act.split("CCBP#")[-1])}_1']["name"],
                "nameEN"    : f'{act} : {DB["CC2EN"]["seasonInfoDataMap"]["crisis_v2_season_"+str(int(act.split("CCBP#")[-1]))+"_1"]["name"]}' if f'crisis_v2_season_{int(act.split("CCBP#")[-1])}_1' in DB["CC2EN"]["seasonInfoDataMap"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else None),
                "startCN"   : DB["CC2"]["seasonInfoDataMap"][f'crisis_v2_season_{int(act.split("CCBP#")[-1])}_1']["startTs"]
        }
## IS#1 ("act12d6")
        elif act == "IS#1":
            activity_collection["Dict"][act] = {
                "nameCN"    : activity_collection["Dict"]["act12d6"]["nameCN"],
                "nameEN"    : f'{act} : {activity_collection["Dict"]["act12d6"]["nameEN"]}',
                "startCN"   : activity_collection["Dict"]["act12d6"]["startCN"]
        }
## IS#2 and later
        elif act.find("IS#") != -1:
            activity_collection["Dict"][act] = {
                "nameCN"    : DB["IS"]["topics"][f'rogue_{int(act.split("#")[-1])-1}']["name"],
                "nameEN"    : act+" : "+DB["ISEN"]["topics"][f'rogue_{int(act.split("#")[-1])-1}']["name"] if f'rogue_{int(act.split("#")[-1])-1}' in DB["ISEN"]["topics"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else None),
                "startCN"   : DB["IS"]["topics"][f'rogue_{int(act.split("#")[-1])-1}']["startTime"]
        }
## RA#1 "act1sandbox"
        elif act == "RA#1":
            activity_collection["Dict"][act] = {
                "nameCN"    : activity_collection["Dict"]["act1sandbox"]["nameCN"],
                "nameEN"    : f'{act} : {activity_collection["Dict"]["act1sandbox"]["nameEN"]}',
                "startCN"   : activity_collection["Dict"]["act1sandbox"]["startCN"]
        }
## RA#2 and maybe later
        elif act.find("RA#") != -1:
            activity_collection["Dict"][act] = {
                    "nameCN"    : DB["RA2"]["basicInfo"][f'sandbox_{int(act.split("#")[-1])-1}']["topicName"],
                    "nameEN"    : Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else None, #f'{act} : {json_RA2EN["basicInfo"][f'sandbox_{int(act.split("#")[-1])-1}']["topicName"]}'
                    "startCN"   : DB["RA2"]["basicInfo"][f'sandbox_{int(act.split("#")[-1])-1}']["topicStartTime"]
            }
            
        if act in activity_collection["Dict"]:
            if activity_collection["Dict"][act]["startCN"] != -1 :
                new_timeline = [act,activity_collection["Dict"][act]["nameEN"] if activity_collection["Dict"][act]["nameEN"] else activity_collection["Dict"][act]["nameCN"],activity_collection["Dict"][act]["startCN"]]
                if new_timeline not in timeline : timeline.append(new_timeline)
        else:
            #Bandage
            new_timeline = [act,"[PH] New Act", 9999999999]
            if new_timeline not in timeline : 
                timeline.append(new_timeline)
                activity_collection["Dict"][act] = {
                                                        "nameCN": "[PH] New Act",
                                                        "nameEN": "New Act",
                                                        "startCN": 9999999999
                                                    }

    timeline.sort(reverse = False, key = lambda event : event[2])
    activity_collection["Timeline"] = timeline

def akenemy_collect(json_zone, json_zoneEN):
    ### Event Name
    for event in stage_collection["activity"].keys():
        if event in activity_collection["Dict"].keys():
            if event in akenemy["gamemode"]["sidestory"]["activity"] and event not in ["act42d0","act1lock"] :
                akenemy["events"][event] = f'[{last_of_nested(akenemy["gamemode"]["sidestory"]["activity"][event]["zone"])[-1].split("-")[0].upper()}] : {activity_collection["Dict"][event]["nameEN"] if activity_collection["Dict"][event]["nameEN"] else activity_collection["Dict"][event]["nameCN"]}'
            elif event.lower() == "act2vmulti" :
                akenemy["events"][event] = f'[{last_of_nested(akenemy["gamemode"]["coop"]["activity"][event]["zone"])[-1].split("-")[0].upper()}] : {activity_collection["Dict"][event]["nameEN"] if activity_collection["Dict"][event]["nameEN"] else activity_collection["Dict"][event]["nameCN"]}'
            else:
                akenemy["events"][event] = activity_collection["Dict"][event]["nameEN"]
        else:
            akenemy["events"][event] = None
    
    ### Event > Zone > stage Name
    for gamemode in akenemy["gamemode"].keys()-["pending"]:
        for activity in akenemy["gamemode"][gamemode]["activity"].keys() :
            akenemy["gamemode"][gamemode]["activity"][activity]["name"] = activity_collection["Dict"][activity]["nameEN"] if activity not in akenemy["events"] else akenemy["events"][activity]
            akenemy["gamemode"][gamemode]["activity"][activity]["date"] = activity_collection["Dict"][activity]["startCN"] if activity in akenemy["events"] else -1
            for zone in akenemy["gamemode"][gamemode]["activity"][activity]["zone"].keys() :
                try:
                    if zone in activity_collection["Dict"].keys() and zone == activity:
                        akenemy["gamemode"][gamemode]["activity"][activity]["zone"][zone]["name"] = akenemy["events"][zone] #activity_collection["Dict"][zone]["nameEN"] if activity_collection["Dict"][zone]["nameEN"] else activity_collection["Dict"][zone]["nameCN"]
                    elif zone in json_zoneEN["zones"]:
                        akenemy["gamemode"][gamemode]["activity"][activity]["zone"][zone]["name"] = json_zoneEN["zones"][zone]["zoneNameSecond"]
                    else :
                        akenemy["gamemode"][gamemode]["activity"][activity]["zone"][zone]["name"] = json_zone["zones"][zone]["zoneNameSecond"]
                except:
                    akenemy["gamemode"][gamemode]["activity"][activity]["zone"][zone]["name"] = zone
    
    ### Sort Event
    mainzone_sorter = {"Training":0,"Story Environment":1,"Normal":2,"Standard Environment":2,"Challenge":3,"Adverse Environment":3}
    for gamemode in akenemy["gamemode"].keys():
        if gamemode in ["sidestory","coop","tn","exp"]:
            sort_event = sorted(akenemy["gamemode"][gamemode]["activity"].items(), reverse = False, key = lambda event : activity_collection["Dict"][event[0].lower()]["startCN"])
            akenemy["gamemode"][gamemode]["activity"] = {x[0]:x[1] for x in sort_event}
        if gamemode in ["sss"]:
            sort_event = sorted(akenemy["gamemode"][gamemode]["activity"].items(), reverse = False, key = lambda event : (-100 + int(event[0].split("_")[-1])) if event[0].find("_tr_") != -1 else int(event[0].split("_")[-1]))
            akenemy["gamemode"][gamemode]["activity"] = {x[0]:x[1] for x in sort_event}
        if gamemode in ["supply"]:
            sort_event = sorted(akenemy["gamemode"][gamemode]["activity"].items(), reverse = False, key = lambda event : int(event[0].split("_")[-1]))
            akenemy["gamemode"][gamemode]["activity"] = {x[0]:x[1] for x in sort_event}
        if gamemode in ["main"]:
            for act in akenemy["gamemode"][gamemode]["activity"]:
                sort_zone = sorted(akenemy["gamemode"][gamemode]["activity"][act]["zone"].items(), reverse = False, key = lambda zone : mainzone_sorter[zone[0].split(" : ")[-1]])
                akenemy["gamemode"][gamemode]["activity"][act]["zone"] = {x[0]:x[1] for x in sort_zone}

    akenemy["enemies"] = stage_collection["enemy"]

################################################################################################################################################################################################################################################
# JSON Dumpling
################################################################################################################################################################################################################################################
def json_dumps():
    with open("json/activity.json", "w", encoding="utf-8") as JSON :
        json.dump(activity_collection, JSON, indent = 4, ensure_ascii = False)

    with open("test/stage.json", "w", encoding="utf-8") as JSON :
        json.dump(stage_collection,  JSON, indent = 4, ensure_ascii = False)
    
    with open("json/akenemy.json", "w", encoding="utf-8") as JSON :
        json.dump(akenemy, JSON, indent = 4, ensure_ascii = False)

    print(f'\n>>Stage Collected Total : {stage_total} stages')
    print(f'>> Akenemy Completed\n\n\t{datetime.now().strftime("%d %b %Y %H:%M:%S")}\n')

def test_dumps(dump_collection):
    with open("test/test-dump.json", "w", encoding="utf-8") as JSON :
        json.dump(dump_collection, JSON, indent = 4, ensure_ascii = False)

################################################################################################################################################################################################################################################
# Utilities
################################################################################################################################################################################################################################################
def last_of_nested(nested):
    all_val = []

    for val in nested.values():
        if isinstance(val, dict):
            all_val.extend(last_of_nested(val))

        elif isinstance(val, list):
            for i in val:
                if isinstance(i, dict):
                    val.extend(last_of_nested(i))
                else:
                    val.append(i)
        else:
            all_val.append(val)
    return all_val

################################################################################################################################################################################################################################################
# Application
################################################################################################################################################################################################################################################

def Akenemy() :
    # Stage & Zone collection
    stage_json_stage_collect(load_json("json_stage"),load_json("json_stageEN"))
    COOP_stage_collect(load_json("Fillerjson"))
    CC_stage_collect(load_json("Fillerjson"), load_json("json_CC"), load_json("json_CC2"), load_json("json_activityEN"))
    IS_stage_collect(load_json("json_ISEN0"), load_json("json_IS"), load_json("json_ISEN"))
    RA_stage_collect(load_json("json_RA1EN"), load_json("json_RA2"), load_json("json_RA2EN"))
    # Activity & Gamemode collection
    activity_collect(load_json("Activityjson"))
    akenemy_collect(load_json("json_zone"),load_json("json_zoneEN"))
    # JSON dump
    json_dumps()
    
def enemyList() :
    enemy_ability_list(load_json("json_Database"), load_json("json_DatabaseEN"), load_json("json_Handbook"), load_json("json_HandbookEN"), load_json("EnemyAbility"))

if __name__ == "__main__" :
    #enemyList()
    Akenemy()