################################################################################################################################################################################################################################################
# IMPORT
################################################################################################################################################################################################################################################

import json
import re
import glob
from datetime import datetime
from pyfunction import print_header, time_to_str

time_start = datetime.now()
lap_time = []
################################################################################################################################################################################################################################################
# JSON
################################################################################################################################################################################################################################################
def json_load(filepath : str) -> dict :
    if filepath.find("_easy_sub_")  != -1     : filepath = filepath.replace("_easy_sub_","_sub_")
    elif filepath.find("_easy_")    != -1     : filepath = filepath.replace("_easy_","_main_")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

JSON = {
        "json_Database"     : "json/gamedata/zh_CN/gamedata/levels/enemydata/enemy_database.json",
        "json_DatabaseEN"   : "json/gamedata/en_US/gamedata/levels/enemydata/enemy_database.json",
        "json_Handbook"     :  "json/gamedata/zh_CN/gamedata/excel/enemy_handbook_table.json",
        "json_HandbookEN"   : "json/gamedata/en_US/gamedata/excel/enemy_handbook_table.json",

        "json_activity"     : "json/gamedata/zh_CN/gamedata/excel/activity_table.json",
        "json_activityEN"   : "json/gamedata/en_US/gamedata/excel/activity_table.json",

        "json_stage"        : "json/gamedata/zh_CN/gamedata/excel/stage_table.json",
        "json_stageEN"      : "json/gamedata/en_US/gamedata/excel/stage_table.json",

        "json_zone"         :  "json/gamedata/zh_CN/gamedata/excel/zone_table.json",
        "json_zoneEN"       : "json/gamedata/en_US/gamedata/excel/zone_table.json",

        "json_campaign"     : "json/gamedata/zh_CN/gamedata/excel/campaign_table.json",

        "json_SSS"          : "json/gamedata/zh_CN/gamedata/excel/climb_tower_table.json",
        "json_SSSEN"        : "json/gamedata/en_US/gamedata/excel/climb_tower_table.json",

        "json_CC"           : "json/gamedata/zh_CN/gamedata/excel/crisis_table.json",
        "json_CC2"          : "json/gamedata/zh_CN/gamedata/excel/crisis_v2_table.json",
        "json_CCEN"         : "json/gamedata/en_US/gamedata/excel/crisis_table.json",
        "json_CC2EN"        : "json/gamedata/en_US/gamedata/excel/crisis_v2_table.json",

        #"json_IS0"         : "json/gamedata/zh_CN/gamedata/excel/roguelike_table.json",
        "json_IS"           : "json/gamedata/zh_CN/gamedata/excel/roguelike_topic_table.json",
        "json_ISEN0"        : "json/gamedata/en_US(Old)/gamedata/excel/roguelike_table.json",
        "json_ISEN"         : "json/gamedata/en_US/gamedata/excel/roguelike_topic_table.json",

        "json_RA1"          : "json/gamedata/zh_CN/gamedata/excel/sandbox_table.json",
        "json_RA2"          : "json/gamedata/zh_CN/gamedata/excel/sandbox_perm_table.json",
        "json_RA1EN"        : "json/gamedata/en_US/gamedata/excel/sandbox_table.json",
        #"json_RA2EN"       : "json/gamedata/en_US/gamedata/excel/sandbox_perm_table.json",

        "Fillerjson"        : "json/Filler.json",
        "Activityjson"      : "test/activity.json",
        "EnemyAbility"      : "json/enemy_abilities.json"
}
################################################################################################################################################################################################################################################
# JSON Dumpling
################################################################################################################################################################################################################################################
def json_dumps():
    with open("test/activity.json",'w') as JSON :
        json.dump(activity_collection, JSON, indent = 4, ensure_ascii = False)

    with open("test/stage.json",'w') as JSON :
        json.dump(stage_collection,  JSON, indent = 4, ensure_ascii = False)
    
    with open("json/akenemy.json",'w') as JSON :
        json.dump(akenemy, JSON, indent = 4, ensure_ascii = False)

    print(f'\n>>Stage Collected Total : {stage_total} stages')
    print(f'>> Akenemy Completed\n\n\t{datetime.now().strftime("%d %b %Y %H:%M:%S")}\n')

def test_dumps(dump_collection):
    with open("test/test-dump.json",'w') as JSON :
        json.dump(dump_collection, JSON, indent = 4, ensure_ascii = False)
    #if error_test > 0 : print(error_enemy)
    print(f'\n\tScipt Completed : {time_to_str(datetime.now() - time_start)} {{{datetime.now() - time_start}}}\n')
    exit()

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

def time_lap():
    lap = time_start
    length = max(map(len,[time[0] for time in lap_time]))
    for time in lap_time:
        print(f'Function {time[0]:<{length}} time : {time_to_str(time[1] - lap)} {{{time[1] - lap}}}')
        lap = time[1]
    print(f'\tScript Completed : {time_to_str(datetime.now() - time_start)} {{{datetime.now() - time_start}}}\n')

def time_attack(func):
    def timed(*arg):
        global lap_time
        func(*arg)
        lap_time.append([func.__name__,datetime.now()])
    return timed

def dump_trash(trash):
    if isinstance(trash, list):
        print(f'Length = {len(set(trash))} : {sorted(set(trash), key = lambda dump : dump[0] if isinstance(dump,list) else dump)})')
    elif isinstance(trash, dict):
        dumpster = {}
        for k in trash :
            dumpster.update({k:list(set(trash[k]))})
        test_dumps(dumpster)
################################################################################################################################################################################################################################################
# Global Variable
################################################################################################################################################################################################################################################
stage_total = 0
stage_collection = {"stages":{}, "zones":{}, "activity":{}, "enemy":{}}
activity_collection = {"Dict":{}}
akenemy = {
            "gamemode":{
                        "tutorial"  : {"name" : "Tutorial", "activity" : {}}, 
                        "main"      : {"name" : "Main Theme", "activity" : {}},                         # Mode : Main Theme     -> Activity : Episode XX                                -> Stage : XX-YY
                        "sidestory" : {"name" : "Side Story", "activity" : {}},                         # Mode : Side Story     -> Activity : AB : XYZ      -> Zone : FGHIJ             -> Stage : AB-XX
                        "supply"    : {"name" : "Supplies Operations", "activity" : {}},                # Mode : Supplies Op    -> Activity : AB : XYZ (MM)                             -> Stage : AB-CD-X
                        "campaign"  : {"name" : "Annihilation Mission", "activity" : {}},               # Mode : Annihilation   -> Activity : camp_XX
                        "coop"      : {"name" : "CO-OP", "activity" : {}},                              # Mode : Coop           -> Activity : XYZ                                       -> Stage : AB-XX
                        "cc"        : {"name" : "CC : Contingency Contract", "activity" : {}},          # Mode : CC             -> Activity : CC#XX         -> Zone : Main/Rotation     -> Stage : XYZ
                        "is"        : {"name" : "IS : Integrated Strategies", "activity" : {}},         # Mode : IS             -> Activity : IS#XX         -> Zone : Floor XX          -> Stage : XYZ
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
IMMUNITY = ["stunImmune", "silenceImmune", "sleepImmune", "frozenImmune", "levitateImmune", "disarmedCombatImmune", "fearedImmune"]
DB = {k:json_load(v) for k,v in JSON.items()}

act_zone_collector = []
dump_collector = []
dict_collector = {}


################################################################################################################################################################################################################################################
# Error Handling
################################################################################################################################################################################################################################################
error_test = 0
error_enemy = {
                "immune" : []
            }
error_stage = {
    
}
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

@time_attack
def enemy_lister(json_Database : dict, json_DatabaseEN : dict, json_Handbook : dict, json_HandbookEN : dict, json_enemy_ablilies : dict, output_control : bool) -> None :
    global error_test
    
    def enemy_json(JSON) :
        return {data["Key"]:data["Value"] for data in JSON["enemies"]}
    
    def talentblackboard_transform(blackboards) :
        if blackboards[0] :
            transformer = [{b["key"]:(b["valueStr"] if b["valueStr"] else b["value"]) for b in blackboard} for blackboard in blackboards]
            to_return = [{k:transformer[i].get(k,transformer[0][k]) for k in transformer[0].keys()} for i in range(len(transformer))] 
            return to_return
        else :
            return blackboards
    
    def skills_transform(skills):
        if skills[0] :
            to_return = [[{skill["prefabKey"]:{k:(talentblackboard_transform([skill[k]])[0] if k == "blackboard" and skill[k] else skill[k]) for k in skill.keys() if k != "prefabKey"}} for skill in level] for level in skills]
            return to_return
        else:
            return skills
    
    def enemy_output(json_enemy_ablilies, database, abilities_database):
        with open("test/NEW_enemy_database.json",'w') as JSON :
            json.dump(database,JSON,indent = 4, ensure_ascii = False)
        
        for enemy in json_enemy_ablilies:
            if json_enemy_ablilies[enemy]["isCompleted"]:
                abilities_database.pop(enemy)
        json_enemy_ablilies.update(abilities_database)
        with open("json/enemy_abilities.json",'w') as JSON :
            json.dump(json_enemy_ablilies, JSON, indent = 4, ensure_ascii = False)
    
    def enemy_error(database):
        # Error & Data Test
        # Data Prep
        global error_test
        enemy_damageType    = []
        enemy_motion        = []
        enemy_applyWay      = []
        for enemy in database:
            # Error Test
            # Only test on 2 or more levels
            if len(database[enemy]["stats"].keys()) >= 2:
                # Immune Error Test
                for x in IMMUNITY :
                    if len(set([database[enemy]["stats"][i]["attributes"][x] for i in range(len(database[enemy]["stats"].keys()))])) == 2 :
                            error_enemy["immune"].append(enemy)
                            error_test += 1
                            

            # Data Test
            if database[enemy]["details"]["damageType"] : enemy_damageType.append((" & ").join(database[enemy]["details"]["damageType"]))
            enemy_motion += [database[enemy]["stats"][level]["motion"] for level in database[enemy]["stats"]]
            enemy_applyWay += [database[enemy]["stats"][level]["applyWay"] for level in database[enemy]["stats"]]

                
        ### print Data test
        if error_test > 0: print(print_header("Error Test"))
        if error_enemy["immune"] : print(error_enemy["immune"])
        print(print_header("Data Test"))
        print(f'\nDamage Type = {list(set(enemy_damageType))}')
        print(f'Enemy Motion = {list(set(enemy_motion))}')
        print(f'Enemy Attack Type = {list(set(enemy_applyWay))}\n')
    
    enemy_database_CN   = enemy_json(json_Database)
    enemy_database_EN   = enemy_json(json_DatabaseEN)
    difftabase_list     = enemy_database_CN.keys() - enemy_database_EN.keys()
    database            = {}
    abilities_prebuild  = {}
    abilities_database  = {}
    # Build Enemy Database
    for enemy in enemy_database_CN :
        database[enemy] = {"details" : {}, "stats" : {}}
        for level in enemy_database_CN[enemy] :
            database[enemy]["stats"][level["level"]] = {k : (bool(v) if k in ["talentBlackboard", "skills", "spData"] else (v["m_value"] if v["m_defined"] else enemy_database_CN[enemy][0]["enemyData"][k]["m_value"])) for k,v in level["enemyData"].items() if k not in ["attributes"]}
            database[enemy]["stats"][level["level"]].update({"attributes":{k:(v["m_value"] if v["m_defined"] else enemy_database_CN[enemy][0]["enemyData"]["attributes"][k]["m_value"]) for k,v in level["enemyData"]["attributes"].items()}})
            # Update CN to EN
            if enemy not in difftabase_list:
                database[enemy]["stats"][level["level"]].update({"name" : enemy_database_EN[enemy][0]["enemyData"]["name"]["m_value"], "description" : enemy_database_EN[enemy][0]["enemyData"]["description"]["m_value"]})
            # Prebuild Ablities Database
            if enemy in abilities_prebuild :
                for k in ["talentBlackboard", "skills", "spData"]:
                    abilities_prebuild[enemy][k].append(enemy_database_CN[enemy][level["level"]]["enemyData"][k] if enemy_database_CN[enemy][level["level"]]["enemyData"][k] else enemy_database_CN[enemy][0]["enemyData"][k])
            if sum([bool(database[enemy]["stats"][level["level"]][k]) for k in ["talentBlackboard", "skills", "spData"]]) and enemy not in abilities_prebuild:
                abilities_prebuild[enemy] = {k:[v] for k,v in level["enemyData"].items() if k in ["talentBlackboard", "skills", "spData"]}
        # Update Handbook to database
        database[enemy]["details"] = {x:(json_Handbook["enemyData"][enemy][x] if (enemy in json_Handbook["enemyData"] and x in json_Handbook["enemyData"][enemy]) else None) for x in ["enemyId","name","nameEN","enemyIndex","sortId","enemyLevel","description","abilityList","linkEnemies","damageType"]}
        database[enemy]["details"].update({"nameEN" : json_HandbookEN["enemyData"][enemy]["name"], "description" : json_HandbookEN["enemyData"][enemy]["description"], "abilityList" : json_HandbookEN["enemyData"][enemy]["abilityList"]} if enemy in json_HandbookEN["enemyData"] else {})
        # Update Hidden unit
        if enemy not in json_Handbook["enemyData"]:
            database[enemy]["details"]["name"]          = enemy_database_CN[enemy][0]["enemyData"]["name"]["m_value"]
            database[enemy]["details"]["damageType"]    = []
            if enemy in enemy_database_EN:
                database[enemy]["details"]["nameEN"]    = enemy_database_EN[enemy][0]["enemyData"]["name"]["m_value"]
        # Build Abilities Database
        for enemy in abilities_prebuild :
            abilities_database[enemy] = {
                                            "abilityList"       : database[enemy]["details"]["abilityList"],
                                            "talentBlackboard"  : talentblackboard_transform(abilities_prebuild[enemy]["talentBlackboard"]) ,
                                            "skills"            : skills_transform(abilities_prebuild[enemy]["skills"]),
                                            "spData"            : abilities_prebuild[enemy]["spData"],
                                            "isEN"              : bool(database[enemy]["details"]["nameEN"]),
                                            "isCompleted"       : False
                                    }

    if output_control : 
        enemy_error(database)
        enemy_output(json_enemy_ablilies, database, abilities_database)

################################################################################################################################################################################################################################################
# Stage
################################################################################################################################################################################################################################################
@time_attack
def stage_lister(json_stage : dict) :
    def stage_stage_lister (stage):
        def stage_type_handler(stage_type, act):
            match stage_type:
                case "GUIDE" :
                    return "GUIDE"
                case "MAIN" | "SUB":
                    return "main"
                case "DAILY":
                    return "DAILY"
                case "CAMPAIGN" :
                    return "CAMPAIGN"
                case "ACTIVITY":
                    if re.search(r'act[0-9]{1,2}vmulti', act):
                        return "COOP"
                    else:
                        return "ACTIVITY"
                case "CLIMB_TOWER":
                    return "CLIMB_TOWER"
                case _:
                    #dump_collector.append(stage_type)
                    return stage_type
        def zone_id_handler(stage_type, zone_id, stage_id):
            match stage_type:
                case "MAIN" | "SUB":
                    if stage_id.find('#f#') != -1 :
                        return f'{zone_id}_hard'
                    elif stage_id.find('tr') != -1 :
                        return f'{zone_id}_training'
                    elif stage_id.find('easy') != -1 :
                        return f'{zone_id}_easy'
                    elif stage_id.find('tough') != -1 :
                        return f'{zone_id}_tough'
                    else :
                        return f'{zone_id}_normal'
                case "CLIMB_TOWER":
                    if zone_id.find('_n_') != -1 :
                        if stage_id.find('ex') != -1 :
                            return f'{zone_id}_ex'
                        else :
                            return f'{zone_id}_normal'
                    else :
                        return zone_id
                case "CAMPAIGN" :
                    return "CAMPAIGN".lower()
                case "DAILY" :
                    return f'{stage_id.split("_")[1]}'
                case "GUIDE" :
                    return zone_id
                case "ACTIVITY" :
                    if zone_id.find("main") != -1 : 
                        if stage_id.find("#f#") != -1 :
                            return f'{stage_id.split("_")[0]}_hard'
                        else :
                            return f'{stage_id.split("_")[0]}_normal'
                    act_zone_collector.append(zone_id)
                    return zone_id
                case _ :
                    dict_collector.setdefault("zone_id_handler",[]).append(stage_type)
                    return zone_id
        def act_id_handler(stage_type, act_id, zone_id):
            #dump_collector.append(stage_type)
            match stage_type:
                case "SUB" | "MAIN" :
                    #dump_collector.append(f'main_{int(zone_id.split("_")[1]):02}')
                    return f'main_{int(zone_id.split("_")[1]):02}'
                case "CLIMB_TOWER":
                    #dump_collector.append(zone_id)
                    return zone_id
                case "DAILY" | "ACTIVITY" | "GUIDE" | "CAMPAIGN" : #
                    #dump_collector.append(act_id)
                    return act_id
                case _ :
                    dict_collector.setdefault("act_id_handler",[]).append(stage_type)
                    #dump_collector.append(stage_type)
                    return act_id
        
        stage_path = stage["levelId"].replace("\\","/").lower()
        act_path = stage_path.split("/")[1]
        stage_detail = {
                            "stage_id"   : stage["stageId"],
                            "stage_type" : stage_type_handler(stage["stageType"], act_path),
                            "level_id"   : stage_path,
                            "zone_id"    : zone_id_handler(stage["stageType"], stage["zoneId"], stage["stageId"]),
                            "act_id"     : act_id_handler(stage["stageType"], act_path, stage["zoneId"])
                    }
        return stage_detail
    
    stage_dict = {"stage":{},"ignore":[]}

    for stage in json_stage["stages"]:
        if stage.find("st") != -1:
            stage_dict["ignore"].append(stage)
        else:
            stage_dict["stage"][stage] = stage_stage_lister(json_stage["stages"][stage])

@time_attack
def act_lister(json_activity : dict, json_activityEN : dict, json_zone :dict, json_zoneEN : dict) :
    def zone_lister():
        return
    for zone in act_zone_collector :
        if zone not in json_zone["zones"]:
            dump_collector.append(zone)
    print(dump_collector)
    print(sorted(list(set(act_zone_collector))))

@time_attack
def act_naming() :
    pass

@time_attack
def akenenmy() :
    pass

################################################################################################################################################################################################################################################
# Application
################################################################################################################################################################################################################################################
if __name__ == "__main__":
    #print(JSON.keys())
    #enemy_lister(DB["json_Database"],DB["json_DatabaseEN"],DB["json_Handbook"], DB["json_HandbookEN"], DB["EnemyAbility"], False)
    stage_lister(DB["json_stage"])
    act_lister(DB["json_activity"], DB["json_activityEN"], DB["json_zone"], DB["json_zoneEN"])
    if dump_collector : 
        dump_trash(dump_collector)
    if dict_collector : 
        dump_trash(dict_collector)
    time_lap()

# DB["json_Database"], DB["json_DatabaseEN"], DB["json_Handbook"], DB["json_HandbookEN"], DB["json_activity"], DB["json_activityEN"], DB["json_stage"], DB["json_stageEN"],
# DB["json_zone"], DB["json_zoneEN"], DB["json_campaign"], DB["json_SSS"], DB["json_SSSEN"], DB["json_CC"], DB["json_CC2"], DB["json_CCEN"], DB["json_CC2EN"],
# DB["json_IS"], DB["json_ISEN0"], DB["json_ISEN"], DB["json_RA1"], DB["json_RA2"], DB["json_RA1EN"], 
# DB["Fillerjson"], DB["Activityjson"], DB["EnemyAbility"]