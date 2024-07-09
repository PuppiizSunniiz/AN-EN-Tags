################################################################################################################################################################################################################################################
# IMPORT
################################################################################################################################################################################################################################################

import json
import re
import glob
from datetime import datetime
from pyfunction import json_load

################################################################################################################################################################################################################################################
# JSON
################################################################################################################################################################################################################################################
def Akenemy() -> None :
    json_Database       =   json_load("json/gamedata/zh_CN/gamedata/levels/enemydata/enemy_database.json")
    json_DatabaseEN     =   json_load("json/gamedata/en_US/gamedata/levels/enemydata/enemy_database.json")

    json_Handbook       =   json_load("json/gamedata/zh_CN/gamedata/excel/enemy_handbook_table.json")
    json_HandbookEN     =   json_load("json/gamedata/en_US/gamedata/excel/enemy_handbook_table.json")

    json_activity       =   json_load("json/gamedata/zh_CN/gamedata/excel/activity_table.json")
    json_activityEN     =   json_load("json/gamedata/en_US/gamedata/excel/activity_table.json")

    json_stage          =   json_load("json/gamedata/zh_CN/gamedata/excel/stage_table.json")
    json_stageEN        =   json_load("json/gamedata/en_US/gamedata/excel/stage_table.json")

    json_zone           =   json_load("json/gamedata/zh_CN/gamedata/excel/zone_table.json")
    json_zoneEN         =   json_load("json/gamedata/en_US/gamedata/excel/zone_table.json")

    json_campaign       =   json_load("json/gamedata/zh_CN/gamedata/excel/campaign_table.json")

    json_SSS            =   json_load("json/gamedata/zh_CN/gamedata/excel/climb_tower_table.json")
    json_SSSEN          =   json_load("json/gamedata/en_US/gamedata/excel/climb_tower_table.json")

    json_CC             =   json_load("json/gamedata/zh_CN/gamedata/excel/crisis_table.json")
    json_CC2            =   json_load("json/gamedata/zh_CN/gamedata/excel/crisis_v2_table.json")
    json_CCEN           =   json_load("json/gamedata/en_US/gamedata/excel/crisis_table.json")
    json_CC2EN          =   json_load("json/gamedata/en_US/gamedata/excel/crisis_v2_table.json")

    #json_IS0            =   json_load("json/gamedata/zh_CN/gamedata/excel/roguelike_table.json")
    json_IS             =   json_load("json/gamedata/zh_CN/gamedata/excel/roguelike_topic_table.json")
    json_ISEN0          =   json_load("json/gamedata/en_US(Old)/gamedata/excel/roguelike_table.json")
    json_ISEN           =   json_load("json/gamedata/en_US/gamedata/excel/roguelike_topic_table.json")

    json_RA1            =   json_load("json/gamedata/zh_CN/gamedata/excel/sandbox_table.json")
    json_RA2            =   json_load("json/gamedata/zh_CN/gamedata/excel/sandbox_perm_table.json")
    json_RA1EN          =   json_load("json/gamedata/en_US/gamedata/excel/sandbox_table.json")
    #json_RA2EN          =   json_load("json/gamedata/en_US/gamedata/excel/sandbox_perm_table.json")

    Fillerjson          =   json_load("json/Filler.json")
    Activityjson        =   json_load("test/activity.json")

################################################################################################################################################################################################################################################
# STAT GRADER
################################################################################################################################################################################################################################################
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
################################################################################################################################################################################################################################################
# Enemies Database Query ??
################################################################################################################################################################################################################################################
    querydatabase={}
    querydatabaseEN={}

    for enemy in json_Database["enemies"]:
        querydatabase[enemy["Key"]]=enemy["Value"]
    for enemy in json_DatabaseEN["enemies"]:
        querydatabaseEN[enemy["Key"]]=enemy["Value"]

################################################################################################################################################################################################################################################
# Test Area
################################################################################################################################################################################################################################################
    enemy_database={}
    enemy_abilitiesdatabase={}
    errortest=0

    enemy_damageType=[]
    enemyTag=[]
    enemymotion=[]
    enemyapplyWay=[]
    '''
    for enemy in json_Handbook["enemyData"]:
        ## Handbook Test
        if json_Handbook["enemyData"][enemy]["hideInHandbook"] :
            continue
        else :
            database = querydatabaseEN if enemy in querydatabaseEN.keys() else querydatabase
            handbook = json_HandbookEN["enemyData"] if enemy in json_HandbookEN["enemyData"].keys() else json_Handbook["enemyData"]

        abilitiescheck = {
                            "abilityList"         : len(handbook[enemy]["abilityList"]),
                            "talentBlackboard"    : database[enemy][0]["enemyData"]["talentBlackboard"],
                            "skills"              : database[enemy][0]["enemyData"]["skills"],
                            "spData"              : database[enemy][0]["enemyData"]["spData"],
                            "all"                 : len(handbook[enemy]["abilityList"]) or database[enemy][0]["enemyData"]["talentBlackboard"] or database[enemy][0]["enemyData"]["skills"] or database[enemy][0]["enemyData"]["spData"]
                        }
        
        ## Data Test
        if (" & ").join(handbook[enemy]["damageType"]) not in enemy_damageType :enemy_damageType.append((" & ").join(handbook[enemy]["damageType"]))
        if str(handbook[enemy]["enemyTags"]) not in enemyTag :enemyTag.append(str(handbook[enemy]["enemyTags"]))
        if database[enemy][0]["enemyData"]["motion"]["m_value"] not in enemymotion : enemymotion.append(database[enemy][0]["enemyData"]["motion"]["m_value"])
        if database[enemy][0]["enemyData"]["applyWay"]["m_value"] not in enemyapplyWay : enemyapplyWay.append(database[enemy][0]["enemyData"]["applyWay"]["m_value"])

        ## Data Handle
        enemy_database[enemy]=  {
                                    "enemyId"           : handbook[enemy]["enemyId"],
                                    "name"              : handbook[enemy]["name"],
                                    "enemyIndex"        : handbook[enemy]["enemyIndex"],
                                    "sortId"            : handbook[enemy]["sortId"],
                                    "enemyLevel"        : handbook[enemy]["enemyLevel"],
                                    "description"       : handbook[enemy]["description" ],
                                    "abilityList"       : handbook[enemy]["abilityList"],
                                    "linkEnemies"       : handbook[enemy]["linkEnemies"],
                                    "damageType"        : handbook[enemy]["damageType"],
                                    
                                    "applyWay"          : database[enemy][0]["enemyData"]["applyWay"]["m_value"],
                                    "motion"            : database[enemy][0]["enemyData"]["motion"]["m_value"],
                                    "enemyTags"         : database[enemy][0]["enemyData"]["enemyTags"]["m_value"],
                                    "lifePointReduce"   : database[enemy][0]["enemyData"]["lifePointReduce"]["m_value"],
                                    "rangeRadius"       : database[enemy][0]["enemyData"]["rangeRadius"]["m_value"],
                                    "attributes"        : []
                                }

        if abilitiescheck["all"] :
            enemy_abilitiesdatabase[enemy]={
                                                "abilityList"       : handbook[enemy]["abilityList"],
                                                "talentBlackboard"  : [] if abilitiescheck["talentBlackboard"] else None ,
                                                "skills"            : [] if abilitiescheck["skills"] else None,
                                                "spData"            : [] if abilitiescheck["spData"] else None
                                            }

        for level in range(len(database[enemy])):
            levelattributes={}
            for stat in database[enemy][level]["enemyData"]["attributes"].keys():
                if database[enemy][level]["enemyData"]["attributes"][stat]["m_defined"] and database[enemy][level]["enemyData"]["attributes"][stat]["m_value"]!=database[enemy][0]["enemyData"]["attributes"][stat]["m_value"]:
                    levelattributes[stat]=database[enemy][level]["enemyData"]["attributes"][stat]["m_value"]
                else:
                    levelattributes[stat]=database[enemy][0]["enemyData"]["attributes"][stat]["m_value"]
            enemy_database[enemy]["attributes"].append(levelattributes)
            
            if abilitiescheck["talentBlackboard"]   : enemy_abilitiesdatabase[enemy]["talentBlackboard"].append(database[enemy][level]["enemyData"]["talentBlackboard"] if database[enemy][level]["enemyData"]["talentBlackboard"] else database[enemy][0]["enemyData"]["talentBlackboard"])
            if abilitiescheck["skills"]             : enemy_abilitiesdatabase[enemy]["skills"].append(database[enemy][level]["enemyData"]["skills"] if database[enemy][level]["enemyData"]["skills"] else database[enemy][0]["enemyData"]["skills"])
            if abilitiescheck["spData"]             : enemy_abilitiesdatabase[enemy]["spData"].append(database[enemy][level]["enemyData"]["spData"] if database[enemy][level]["enemyData"]["spData"] else database[enemy][0]["enemyData"]["spData"])

        ## New Error Check
        if len(database[enemy]) >1:
            for key in ["applyWay","motion","enemyTags","lifePointReduce","rangeRadius"]:
                if database[enemy][1]["enemyData"][key]["m_defined"] and database[enemy][0]["enemyData"][key]["m_value"] != database[enemy][1]["enemyData"][key]["m_value"]:
                    print(enemy,"has {key} Level Conflict")
                    errortest+=1
                    if errortest==1 : print("\n#########################################################\n###################     Error Test    ###################\n#########################################################")
                
        if len(database[enemy]) >1 and abilitiescheck["all"]:
            if database[enemy][0]["enemyData"]["spData"] != database[enemy][1]["enemyData"]["spData"] and database[enemy][0]["enemyData"]["spData"] and database[enemy][1]["enemyData"]["spData"]:
                print(enemy,"has spData Level Conflict")
                errortest+=1
                if errortest==1 : print("\n#########################################################\n###################     Error Test    ###################\n#########################################################")

        if len(handbook[enemy]["linkEnemies"]):
            linkenemies=[]
            for link in handbook[enemy]["linkEnemies"]:
                if link in handbook.keys(): linkenemies.append(link)
            #print(enemy,len(linkenemies),linkenemies)
            
    ### print Data test

    print("\n#########################################################\n###################     Data Test     ###################\n#########################################################")
    print("\nDamage Type = ",enemy_damageType)
    print("Enemy Tags (Handbook \"enemyTags\") = ",enemyTag)
    print("Enemy Motion = ",enemymotion)
    print("Enemy Attack Type = ",enemyapplyWay)
    print("\n")

    dumpling=json.dumps(enemy_database,indent=4, ensure_ascii=False)
    with open("test/enemy_database_stat.json",'w') as JSON :
        JSON.write(dumpling)

    dumpling=json.dumps(enemy_abilitiesdatabase,indent=4, ensure_ascii=False)
    with open("test/enemy_database_abilities.json",'w') as JSON :
        JSON.write(dumpling)'''

    '''
    ##########################################
    ##############   HANDBOOK   ##############
    ##########################################
        "abilityList"       : List          //  [
                                                    {
                                                        "text": "Does not deduct Life Points when ...",
                                                        "textFormat": "NORMAL"  ==> ["NORMAL","TITLE",SILENCE]
                                                    }
                                                ]
        
    ##########################################
    #### DATABASE  [Level0, Level1, ...]  ####
    ##########################################
        note : "talentBlackboard", "skills", "spData" below Have to write date by hand (new json) with "abilityList" in HANDBOOK
        "talentBlackboard"  : List of Dict  //  [
                                                    {
                                                        "key": "selfbuff.attack_speed",
                                                        "value": 40.0,
                                                        "valueStr": null
                                                    }
                                                ]
        "skills"            : List of Dict  //  [
                                                    {
                                                        "prefabKey": "BringDown",
                                                        "priority": 0,
                                                        "cooldown": 10000.0,
                                                        "initCooldown": 7.0,
                                                        "spCost": 0,
                                                        "blackboard": [
                                                            {
                                                                "key": "def",
                                                                "value": -0.5,
                                                                "valueStr": null
                                                            },
                                                            {
                                                                "key": "magic_resistance",
                                                                "value": -0.5,
                                                                "valueStr": null
                                                            }
                                                        ]
                                                    }
                                                ]
        "spData":           : Dict          //  {
                                                    "spType": "INCREASE_WHEN_ATTACK",
                                                    "maxSp": 3,
                                                    "initSp": 0,
                                                    "increment": 1.0
                                                }
    '''

################################################################################################################################################################################################################################################
# Stage Lister
################################################################################################################################################################################################################################################

    def StageLister(stageevent:str,stagecode:str,stagename:str,stageId:str,levelId:str,zoneId:str,jsonpath:str,extra="") -> None :
        '''
        "act26side_01" : {
            "stageId"   : "act26side_01",
            "levelId"   : "Activities/act26side/level_act26side_01",
            "zoneId"    : "act26sre_zone1",
            "code"      : "HE-1",
            "name"      : "Home Sweet Home",
            "Event"     : "act26side"
        },
        '''
        stagename   = f'{stagename} (Boss)' if extra and re.search(r"rogue[0-9]{0,2}_[b]-", stageId) else stagename
        stageevent  = "1stact" if stageevent == "a001" else stageevent
        
        if extra:
            if stageevent   not in stage_collection["zone"].keys()              : stage_collection["zone"][stageevent]={}
            if zoneId       not in stage_collection["zone"][stageevent].keys()  : stage_collection["zone"][stageevent][zoneId]=[]
            if stagecode    not in stage_collection["zone"][stageevent][zoneId] : stage_collection["zone"][stageevent][zoneId].append(stagecode)
        else:
            if stageevent   not in stage_collection["zone"].keys()              : stage_collection["zone"][stageevent]=[]
            if stagecode    not in stage_collection["zone"][stageevent]         : stage_collection["zone"][stageevent].append(stagecode)
        
        if stageId not in stage_collection["stage"].keys():
            stage_collection["stage"][stageId] ={
                                                    "stageId"   :   stageId,
                                                    "levelId"   :   levelId.split("gamedata/levels/")[-1],
                                                    "zoneId"    :   zoneId,
                                                    "code"      :   stagecode,
                                                    "name"      :   stagename,
                                                    "Event"     :   stageevent
        }
        
        if stageevent.find("Campaign")!=-1 or stageevent.find("IS#")!=-1 or stageevent.find("CC")!=-1 or stageevent.find("PinchOut")!=-1:
            stagecode=stagename
        
        stageforenemylist=json.loads(open(jsonpath).read())
        for enemy in stageforenemylist["enemyDbRefs"]:
            enemyid = enemy["id"]
            if enemy["overwrittenData"]: enemyid = enemy["overwrittenData"]["prefabKey"]["m_value"] if enemy["overwrittenData"]["prefabKey"]["m_defined"] else enemy["id"]
            if enemyid not in stage_collection["enemy"].keys() : stage_collection["enemy"][enemyid]={"Filtered":[],"Appearance":{}}
            if extra:
                if stageevent not in stage_collection["enemy"][enemyid]["Filtered"]:
                    stage_collection["enemy"][enemyid]["Filtered"].append(stageevent)
                    stage_collection["enemy"][enemyid]["Appearance"][stageevent]={}
                if zoneId not in stage_collection["enemy"][enemyid]["Appearance"][stageevent] : 
                    stage_collection["enemy"][enemyid]["Appearance"][stageevent][zoneId]=[]
                if stagecode not in stage_collection["enemy"][enemyid]["Appearance"][stageevent][zoneId] : 
                    stage_collection["enemy"][enemyid]["Appearance"][stageevent][zoneId].append(stagecode)
            else:
                if stageevent not in stage_collection["enemy"][enemyid]["Filtered"] : 
                    stage_collection["enemy"][enemyid]["Filtered"].append(stageevent)
                    stage_collection["enemy"][enemyid]["Appearance"][stageevent]=[]
                if stagecode not in stage_collection["enemy"][enemyid]["Appearance"][stageevent] : 
                    stage_collection["enemy"][enemyid]["Appearance"][stageevent].append(stagecode)

    def RArushLister(stageevent:str,rushgroup:str) -> None :
        '''
        stageevent = RA#??
        
        rushgroup = NORMAL | ELITE | etc
        
        => RA#??_GROUP_rushparty
        '''
        stagename   = "rushparty"
        stageId     = f'{stageevent}_{rushgroup}_{stagename}'
        
        if stageevent   not in stage_collection["zone"].keys()      : stage_collection["zone"][stageevent]=[]
        if stageId    not in stage_collection["zone"][stageevent] : stage_collection["zone"][stageevent].append(stageId)
        
        if stageId not in stage_collection["stage"].keys():
            stage_collection["stage"][stageId] ={
                                                    "stageId"   :   stageId,
                                                    "levelId"   :   stageId,
                                                    "zoneId"    :   stageevent,
                                                    "code"      :   stageId,
                                                    "name"      :   stagename,
                                                    "Event"     :   stageevent
                                                }
    
    def ISzone(stageId:str,IS:str) -> str:
        '''IS = IS#??'''
        match stageId.split("_")[1]:
            case "n":
                return f'Floor {stageId.split("_")[2]}'
            case "b":
                return f'Floor {ISboss(stageId,IS)}'
            case "t":
                return "Treasure"
            case "ev":
                return "Event"
        return stageId

    def ISboss(stageId:str,IS:str) -> str:
        ISbossdict={"IS#1":{
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
                                "ro2_b_1_b" : 3,
                                "ro2_b_2"   : 3,
                                "ro2_b_2_b" : 3,
                                "ro2_b_3"   : 3,
                                "ro2_b_3_b" : 3,
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
                                "ro3_b_1_b" : 3 ,
                                "ro3_b_2"   : 3,
                                "ro3_b_2_b" : 3 ,
                                "ro3_b_3"   : 3,
                                "ro3_b_3_b" : 3 ,
                                "ro3_b_4"   : 5,
                                "ro3_b_4_b" : 5 ,
                                "ro3_b_5"   : 5,
                                "ro3_b_5_b" : 5 ,
                                "ro3_b_6"   : 6,
                                "ro3_b_6_b" : 6 ,
                                "ro3_b_7"   : 6,
                                "ro3_b_7_b" : 6 
                            },
                    "IS#5":{
                                "ro3_b_1"   : 3,
                                "ro3_b_1_b" : 3 ,
                                "ro3_b_2"   : 3,
                                "ro3_b_2_b" : 3 ,
                                "ro3_b_3"   : 3,
                                "ro3_b_3_b" : 3 ,
                                "ro3_b_4"   : 5,
                                "ro3_b_4_b" : 5 ,
                                "ro3_b_5"   : 5,
                                "ro3_b_5_b" : 5 ,
                                "ro3_b_6"   : 6,
                                "ro3_b_6_b" : 6 ,
                                "ro3_b_7"   : 6,
                                "ro3_b_7_b" : 6 
                            }
                    }
        return str(ISbossdict[IS][stageId])


################################################################################################################################################################################################################################################
# Stage collection
################################################################################################################################################################################################################################################
    stage_collection={"stage":{},"zone":{},"enemy":{}} #,"ignore":{}
    akenemy={
                "gamemode":{
                            "main":[],
                            "sidestory":[],
                            "supply":[],
                            "campaign":[],
                            "coop":[],
                            "cc":[],
                            "is":[],
                            "tn":[],
                            "sss":[],
                            "ra":[],
                            "pending":[]
                },
                "events":{
                    
                },
                "enemies":{
                    
                }
            }

## stage_table || All Event / Weekly stage / Annihilation
    for stage in json_stage["stages"]:
        
    # ignore Challenge and Story
        if stage.find("guide_")==-1 and stage.find("#f#")==-1 and stage.find("st_")==-1 and stage.find("_st")==-1 and stage.find("easy")==-1 and json_stage["stages"][stage]["levelId"].find("Activities/ACT21side/Mission/")==-1 and stage.find("act4d0")==-1 and stage.find("act17d7")==-1 and not re.search(r"lt_.+_ex", stage) and not re.search(r"bossrush_(tm|ex|fin)", stage):
            if json_stage["stages"][stage]["levelId"].find("/")!=-1:
                if json_stage["stages"][stage]["levelId"].split("/")[1] in ["Main","Training","Hard","Weekly","Promote"]:
                    stagezone = json_stage["stages"][stage]["zoneId"]
                elif json_stage["stages"][stage]["levelId"].split("/")[1] in ["Campaign"]:
                    stagezone = json_stage["stages"][stage]["stageId"]
                elif json_stage["stages"][stage]["levelId"].split("/")[1] in ["Legion"]:
                    stagezone = json_stage["stages"][stage]["levelId"].split("/")[2]
                else:
                    stagezone = json_stage["stages"][stage]["levelId"].split("/")[1].lower()
            elif json_stage["stages"][stage]["levelId"].split("\\")[1]:
                stagezone = json_stage["stages"][stage]["levelId"].split("\\")[1]

        # add Stagezone
            stagecode       = json_stage["stages"][stage]["stageId"] if json_stage["stages"][stage]["stageType"] == "CAMPAIGN" else json_stage["stages"][stage]["code"]
            stagename       = json_stageEN["stages"][stage]["name"] if stage in json_stageEN["stages"].keys() else json_stage["stages"][stage]["name"]
            stageId         = json_stage["stages"][stage]["stageId"]
            levelId         = json_stage["stages"][stage]["levelId"]
            zoneId          = json_stage["stages"][stage]["zoneId"]
            jsonforlister   = "json/gamedata/zh_CN/gamedata/levels/"+levelId.lower()+".json"
            
            StageLister(stagezone.lower(),stagecode,stagename,stageId,levelId,zoneId,jsonforlister)

    print("\n>> Activity Stage Completed")
    
## COOP1 : Defense Protocols (罗德岛防御协议) "act17d1"
    COOP = glob.glob("json/gamedata/zh_CN/gamedata/levels/activities/act17d1/*")
    for stagepath in COOP:
        stagename   = Fillerjson["stages"][stagepath.split("\\")[-1]]
        stageId     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
        
        StageLister("act17d1",stageId,stagename,stageId,stagepath,"act17d1",stagepath)

    print(">> COOP Stage Completed")

## CC : Contingency Contract (危机合约)

    CC1 = glob.glob("json/gamedata/zh_CN/gamedata/levels/obt/rune/*")
    CC2 = glob.glob("json/gamedata/zh_CN/gamedata/levels/obt/crisis/v2/*")
    POT = glob.glob("json/gamedata/zh_CN/gamedata/levels/activities/act38rune/*")

### CC Beta (act5d1) & CC Season 1 (crisis_table)
    for cc in range(len(json_CC["seasonInfo"])+1):
        ccnum = str(cc-1) if cc-1 >= 10 else "0"+str(cc-1)
        CCZone = f'CC#{ccnum}' if cc>0 else "CC#Beta"
        stagenum = str(cc+1) if cc+1 >= 10 else "0"+str(cc+1)
        CCStage = [stage for stage in CC1 if re.search(rf'{stagenum}-.+\.json',stage)]+(["json/gamedata/zh_CN/gamedata/levels/obt/rune\\"+rotatestage for rotatestage in Fillerjson["CCRotate"][CCZone]] if CCZone in Fillerjson["CCRotate"].keys() else [])
        stage_collection["zone"][CCZone]=[]
        for stagepath in CCStage:
            stagename   = Fillerjson["stages"][stagepath.split("\\")[-1]] if re.search(rf'{stagenum}-.+\.json',stagepath) else Fillerjson["stages"][stagepath.split("\\")[-1]].split(" (Main)")[0]
            stageId     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
            
            StageLister(CCZone,stageId,stagename,stageId,stagepath,CCZone,stagepath)

    print(">> CC Operation Stage Completed")

### POT (act38rune)
    stage_collection["zone"]["PinchOut"]=[]
    for stagepath in POT:
        stagename   = Fillerjson["stages"][stagepath.split("\\")[-1]]
        stageId     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
        
        StageLister("PinchOut",stageId,stagename,stageId,stagepath,"PinchOut",stagepath)
        
    print(">> Pinch-Out Stage Completed")

## DOS "act42d0"
    DOS = json_activityEN["activity"]["TYPE_ACT42D0"]["act42d0"]
    for stage in DOS["stageInfoData"].keys():
        stagecode       = DOS["stageInfoData"][stage]["code"]
        stagename       = DOS["stageInfoData"][stage]["name"]
        stageId         = DOS["stageInfoData"][stage]["stageId"]
        levelId         = DOS["stageInfoData"][stage]["levelId"]
        zoneId          = DOS["stageInfoData"][stage]["areaId"]
        jsonforlister   = "json/gamedata/zh_CN/gamedata/levels/"+levelId.lower()+".json"
        
        StageLister("act42d0",stagecode,stagename,stageId,levelId,zoneId,jsonforlister)
        
    for stage in DOS["challengeInfoData"].keys():
        stagecode       = DOS["challengeInfoData"][stage]["code"]
        stagename       = DOS["challengeInfoData"][stage]["name"]
        stageId         = DOS["challengeInfoData"][stage]["stageId"]
        levelId         = DOS["challengeInfoData"][stage]["levelId"]
        jsonforlister   = "json/gamedata/zh_CN/gamedata/levels/"+levelId.lower()+".json"
        
        StageLister("act42d0",stagecode,stagename,stageId,levelId,"challenge",jsonforlister)

### CC Season 2 (crisis_v2_table)
    for cc in range(len(json_CC2["seasonInfoDataMap"].keys())):
        ccnum = str(cc+1) if cc+1 >= 10 else "0"+str(cc+1)
        CCZone = f'CCBP#{ccnum}'
        stagenum = str(cc+1) if cc+1 >= 10 else "0"+str(cc+1)
        CCStage = [stage for stage in CC2 if re.search(rf'{stagenum}-.+\.json',stage)]+(["json/gamedata/zh_CN/gamedata/levels/obt/crisis/v2\\"+rotatestage for rotatestage in Fillerjson["CCRotate"][CCZone]] if CCZone in Fillerjson["CCRotate"].keys() else [])
        if cc == 0 : CCStage = list(filter(lambda x : re.search(rf'v2_01-0[^46]',x),CCStage))
        stage_collection["zone"][CCZone]=[]
        for stagepath in CCStage:
            stagename   = Fillerjson["stages"][stagepath.split("\\")[-1]] if re.search(rf'{stagenum}-.+\.json',stagepath) else Fillerjson["stages"][stagepath.split("\\")[-1]].split(" (Main)")[0]
            stageId     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]

            StageLister(CCZone,stageId,stagename,stageId,stagepath,CCZone,stagepath)

    print(">> CC Battleplan Completed")

## IS
### IS 1
    for ISstage in json_ISEN0["stages"].keys():
        if ISstage.split("_")[1]!="e":
            stagename   = json_ISEN0["stages"][ISstage]["name"]
            stagepath   = "json/gamedata/zh_CN/gamedata/levels/"+json_ISEN0["stages"][ISstage]["levelId"].lower()+".json"
            stageId     = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]

            StageLister("IS#1",stageId,stagename,stageId,stagepath,ISzone(ISstage,"IS#1"),stagepath,"IS#1")

    print(">> IS#1 Stage Completed")

### IS 2+
    for ISseason in json_IS["details"].keys():
        for ISstage in json_IS["details"][ISseason]["stages"].keys():
            if ISstage.split("_")[1]!="e":
                try:
                    stagename =  json_ISEN["details"][ISseason]["stages"][ISstage]["name"]
                except:
                    stagename =  json_IS["details"][ISseason]["stages"][ISstage]["name"]
                
                stagepath = "json/gamedata/zh_CN/gamedata/levels/"+json_IS["details"][ISseason]["stages"][ISstage]["levelId"].lower()+".json"
                stageId = stagepath.split("\\")[-1].split(".")[0].split("level_")[-1]
                StageLister(f'IS#{int(ISseason[-1])+1}',stageId,stagename,stageId,stagepath,ISzone(ISstage,f'IS#{int(ISseason[-1])+1}'),stagepath,f'IS#{int(ISseason[-1])+1}')
        
        print(f'>> IS#{int(ISseason[-1])+1} Stage Completed')

### RA#1
    for RAstage in json_RA1EN["sandboxActTables"]["act1sandbox"]["stageDatas"].keys():
        stagepath = "json/gamedata/zh_CN/gamedata/levels/"+json_RA1EN["sandboxActTables"]["act1sandbox"]["stageDatas"][RAstage]["levelId"].lower()+".json"
        stagename = json_RA1EN["sandboxActTables"]["act1sandbox"]["stageDatas"][RAstage]["name"]
            
        StageLister("RA#1",RAstage,stagename,RAstage,stagepath,"RA#1",stagepath)
    #### Rush Parties
    for Rushgroup in json_RA1EN["sandboxActTables"]["act1sandbox"]["rushEnemyGroup"]["rushEnemyGroupConfigs"].keys():
        RArushLister("RA#1",Rushgroup)
        for Rushparty in json_RA1EN["sandboxActTables"]["act1sandbox"]["rushEnemyGroup"]["rushEnemyGroupConfigs"][Rushgroup]:
            for enemy in Rushparty["enemy"]:
                enemyid = enemy["enemyKey"]
                if enemyid not in stage_collection["enemy"].keys() : stage_collection["enemy"][enemyid]={"Filtered":[],"Appearance":{}}

                if "RA#1" not in stage_collection["enemy"][enemyid]["Filtered"] : 
                    stage_collection["enemy"][enemyid]["Filtered"].append("RA#1")
                    stage_collection["enemy"][enemyid]["Appearance"]["RA#1"]=[]
                if "RA#1_rushparty" not in stage_collection["enemy"][enemyid]["Appearance"]["RA#1"] : 
                    stage_collection["enemy"][enemyid]["Appearance"]["RA#1"].append(f'RA#1_{Rushgroup}_rushparty')
                    
    print(">> RA#1 Stage Completed")

### RA#2
    for RAseason in json_RA2["detail"]["SANDBOX_V2"].keys():
        for RAstage in json_RA2["detail"]["SANDBOX_V2"][RAseason]["stageData"].keys():
            #try:
                #stagename = json_RA2EN["detail"]["SANDBOX_V2"][RAseason]["stageData"][RAstage]["name"]
            #except:
                #stagename = json_RA2["detail"]["SANDBOX_V2"][RAseason]["stageData"][RAstage]["name"]
            
            stagename = json_RA2["detail"]["SANDBOX_V2"][RAseason]["stageData"][RAstage]["name"]
            
            stagepath = "json/gamedata/zh_CN/gamedata/levels/"+json_RA2["detail"]["SANDBOX_V2"][RAseason]["stageData"][RAstage]["levelId"].lower()+".json"
            
            StageLister(f'RA#{int(RAseason[-1])+1}',RAstage,stagename,RAstage,stagepath,f'RA#{int(RAseason[-1])+1}',stagepath)
        
        for Rushgroup in json_RA2["detail"]["SANDBOX_V2"][RAseason]["rushEnemyData"]["rushEnemyGroupConfigs"].keys():
            RArushLister(f'RA#{int(RAseason[-1])+1}',Rushgroup)
            for Rushparty in json_RA2["detail"]["SANDBOX_V2"][RAseason]["rushEnemyData"]["rushEnemyGroupConfigs"][Rushgroup]:
                for enemy in Rushparty["enemy"]:
                    enemyid = enemy["enemyKey"]
                    if enemyid not in stage_collection["enemy"].keys() : stage_collection["enemy"][enemyid]={"Filtered":[],"Appearance":{}}

                    if f'RA#{int(RAseason[-1])+1}' not in stage_collection["enemy"][enemyid]["Filtered"] : 
                        stage_collection["enemy"][enemyid]["Filtered"].append(f'RA#{int(RAseason[-1])+1}')
                        stage_collection["enemy"][enemyid]["Appearance"][f'RA#{int(RAseason[-1])+1}']=[]
                    if f'RA#{int(RAseason[-1])+1}_rushparty' not in stage_collection["enemy"][enemyid]["Appearance"][f'RA#{int(RAseason[-1])+1}'] : 
                        stage_collection["enemy"][enemyid]["Appearance"][f'RA#{int(RAseason[-1])+1}'].append(f'RA#{int(RAseason[-1])+1}_{Rushgroup}_rushparty')

        print(f'>> RA#{int(RAseason[-1])+1} Stage Completed')

################################################################################################################################################################################################################################################
# Activity
################################################################################################################################################################################################################################################
    activity={"Dict":{}}
    timeline=[]

## Activity
    for act in json_activity["basicInfo"].keys():
        if json_activity["basicInfo"][act]["hasStage"]:
            activity["Dict"][act] = {
                    "nameCN"    : json_activity["basicInfo"][act]["name"],
                    "nameEN"    : ("DOS : " if act == "act42d0" else "") + (json_activityEN["basicInfo"][act]["name"] if act in json_activityEN["basicInfo"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else "")) + (f' #{act.split("act")[-1].split("bossrush")[0]}' if act.find("bossrush")!= -1 and act in json_activityEN["basicInfo"].keys() else ""),
                    "startCN"   : json_activity["basicInfo"][act]["startTime"]
            }
            timeline.append([act,activity["Dict"][act]["nameEN"] if activity["Dict"][act]["nameEN"] else activity["Dict"][act]["nameCN"],json_activity["basicInfo"][act]["startTime"]])

## Main
    for act in json_zone["mainlineAdditionInfo"].keys():
        activity["Dict"][act] = {
                    "nameCN"    : f'{json_zone["zones"][act]["zoneNameFirst"]} : {json_zone["zones"][act]["zoneNameSecond"]}',
                    "nameEN"    : f'{json_zoneEN["zones"][act]["zoneNameFirst"]} : {json_zoneEN["zones"][act]["zoneNameSecond"]}' if act in json_zoneEN["zones"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else f'{json_zone["zones"][act]["zoneNameFirst"]} : {json_zone["zones"][act]["zoneNameSecond"]}'),
                    "startCN"   : json_zone["mainlineAdditionInfo"][act]["zoneOpenTime"]
        }

# Other act
## Weekly
    for act in stage_collection["zone"].keys():
        if act.find("weekly_") == 0 :
            activity["Dict"][act]={
                "nameCN"    : f'{json_zone["zones"][act]["zoneNameSecond"]} ({stage_collection["zone"][act][0][:-2]})',
                "nameEN"    : Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else (f'{stage_collection["zone"][act][0][:-2]} : {json_zoneEN["zones"][act]["zoneNameSecond"]}' if act in json_zoneEN["zones"].keys() else f'{stage_collection["zone"][act][0][:-2]} : {json_zone["zones"][act]["zoneNameSecond"]}'),
                "startCN"   : -1
        }
## Annihilation
        elif act.find("camp") == 0 :
            activity["Dict"][act]={
                "nameCN"    : json_stage["stages"][act]["name"],
                "nameEN"    : stage_collection["stage"][act]["name"],
                "startCN"   : json_campaign["campaignRotateStageOpenTimes"][int(act[-2:])-1]["startTs"] if act.find("_r_")!= -1 else -1
        }
## SSS (lt)
        elif act.find("lt") == 0 :
            activity["Dict"][act]={
                "nameCN"    : json_SSS["towers"]["tower_n_"+act[-2:]]["name"] if "tower_n_"+act[-2:] in json_SSS["towers"].keys() else (Activityjson["Dict"][act]["nameCN"] if act in Activityjson["Dict"].keys() else None),
                "nameEN"    : json_SSSEN["towers"]["tower_n_"+act[-2:]]["name"] if "tower_n_"+act[-2:] in json_SSSEN["towers"].keys() else (Activityjson["Dict"][act]["nameEN"] if Activityjson["Dict"][act]["nameEN"] else (json_SSS["towers"]["tower_n_"+act[-2:]]["name"] if "tower_n_"+act[-2:] in json_SSS["towers"].keys() else None)),
                "startCN"   : -1
        }
## CC#Beta (act5d1)
        elif act == "CC#Beta" :
            activity["Dict"][act]={
                "nameCN"    : activity["Dict"]["act5d1"]["nameCN"],
                "nameEN"    : f'{act} : {activity["Dict"]["act5d1"]["nameEN"]}',
                "startCN"   : activity["Dict"]["act5d1"]["startCN"]
        }
## CC Operation
        elif act.find("CC#") == 0 :
            activity["Dict"][act] = {
                "nameCN"    : json_CC["seasonInfo"][int(act.split("CC#")[-1])]["name"],
                "nameEN"    : f'{act} : {json_CCEN["seasonInfo"][int(act.split("CC#")[-1])]["name"]}',
                "startCN"   : json_CC["seasonInfo"][int(act.split("CC#")[-1])]["startTs"]
        }
## Pinch out (act38d1)
        elif act == "PinchOut" :
            activity["Dict"][act] = {
                "nameCN"    : activity["Dict"]["act38d1"]["nameCN"],
                "nameEN"    : activity["Dict"]["act38d1"]["nameEN"],
                "startCN"   : activity["Dict"]["act38d1"]["startCN"]
        }
## CC Battleplan
        elif act.find("CCBP#") == 0 :
            activity["Dict"][act] = {
                "nameCN"    : json_CC2["seasonInfoDataMap"][f'crisis_v2_season_{int(act.split("CCBP#")[-1])}_1']["name"],
                "nameEN"    : f'{act} : {json_CC2EN["seasonInfoDataMap"]["crisis_v2_season_"+str(int(act.split("CCBP#")[-1]))+"_1"]["name"]}' if f'crisis_v2_season_{int(act.split("CCBP#")[-1])}_1' in json_CC2EN["seasonInfoDataMap"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else None),
                "startCN"   : json_CC2["seasonInfoDataMap"][f'crisis_v2_season_{int(act.split("CCBP#")[-1])}_1']["startTs"]
        }
## IS#1 ("act12d6")
        elif act == "IS#1":
            activity["Dict"][act] = {
                "nameCN"    : activity["Dict"]["act12d6"]["nameCN"],
                "nameEN"    : f'{act} : {activity["Dict"]["act12d6"]["nameEN"]}',
                "startCN"   : activity["Dict"]["act12d6"]["startCN"]
        }
## IS#2 and later
        elif act.find("IS#") != -1:
            activity["Dict"][act] = {
                "nameCN"    : json_IS["topics"][f'rogue_{int(act.split("#")[-1])-1}']["name"],
                "nameEN"    : act+" : "+json_ISEN["topics"][f'rogue_{int(act.split("#")[-1])-1}']["name"] if f'rogue_{int(act.split("#")[-1])-1}' in json_ISEN["topics"].keys() else (Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else None),
                "startCN"   : json_IS["topics"][f'rogue_{int(act.split("#")[-1])-1}']["startTime"]
        }
## RA#1 "act1sandbox"
        elif act == "RA#1":
            activity["Dict"][act]={
                "nameCN"    : activity["Dict"]["act1sandbox"]["nameCN"],
                "nameEN"    : f'{act} : {activity["Dict"]["act1sandbox"]["nameEN"]}',
                "startCN"   : activity["Dict"]["act1sandbox"]["startCN"]
        }
## RA#2 and maybe later
        elif act.find("RA#") != -1:
            activity["Dict"][act]={
                    "nameCN"    : json_RA2["basicInfo"][f'sandbox_{int(act.split("#")[-1])-1}']["topicName"],
                    "nameEN"    : Activityjson["Dict"][act]["nameEN"] if act in Activityjson["Dict"].keys() else None, #f'{act} : {json_RA2EN["basicInfo"][f'sandbox_{int(act.split("#")[-1])-1}']["topicName"]}'
                    "startCN"   : json_RA2["basicInfo"][f'sandbox_{int(act.split("#")[-1])-1}']["topicStartTime"]
            }

    timeline.sort(reverse=False,key=lambda event : event[2])
    activity["Timeline"]=timeline
    
    for event in stage_collection["zone"].keys():
        ### Gamemode
        if event.find("main_")!=-1:
            akenemy["gamemode"]["main"].append(event)
        elif event.find("weekly_")!=-1:
            akenemy["gamemode"]["supply"].append(event)
        elif event.find("bossrush")!=-1:
            akenemy["gamemode"]["tn"].append(event)
        elif event.find("camp_")!=-1:
            akenemy["gamemode"]["campaign"].append(event)
        elif event.find("lt")==0:
            akenemy["gamemode"]["sss"].append(event)
        elif event == "PinchOut" or event == "act42d0" or re.search(r"CC(|BP)#",event): 
            akenemy["gamemode"]["cc"].append(event)
        elif event.find("IS#")!=-1:
            akenemy["gamemode"]["is"].append(event)
        elif event.find("RA#")!=-1:
            akenemy["gamemode"]["ra"].append(event)
        elif event=="act17d1" or re.search(r"act[0-9]{1,2}vmulti",event):
            akenemy["gamemode"]["coop"].append(event)
        elif re.search(r"act[0-9]{1,2}(side|lock|mini|d0|d3|d5)",event) or event == "1stact":
            akenemy["gamemode"]["sidestory"].append(event)
            
        else:
            akenemy["gamemode"]["pending"].append(event.lower())

        ### Event
        if event in activity["Dict"].keys():
            if (event in akenemy["gamemode"]["sidestory"] and event not in["act42d0","act1lock"]) or event == "act2vmulti" :
                akenemy["events"][event] = f'{stage_collection["zone"][event][0].split("-")[0].upper()} : {activity["Dict"][event]["nameEN"]}'
            else:
                akenemy["events"][event] = activity["Dict"][event]["nameEN"]
        else:
            akenemy["events"][event] = None

    for gamemode in akenemy["gamemode"].keys():
        gamemodelist=akenemy["gamemode"][gamemode]
        if gamemode in ["sidestory","coop","tn","pending"]:
            gamemodelist.sort(reverse=False,key=lambda event : activity["Dict"][event.lower()]["startCN"])
        if gamemode in ["sss"]:
            gamemodelist.sort(reverse=False,key=lambda event : 0 if event=="lttr" else int(event.split("lt")[-1]))
        akenemy["gamemode"][gamemode]=gamemodelist
        
    for enemy in stage_collection["enemy"].keys():
        akenemy["enemies"][enemy]=stage_collection["enemy"][enemy]["Filtered"]

################################################################################################################################################################################################################################################
# JSON Dumpling
################################################################################################################################################################################################################################################

    dumpling=json.dumps(activity,indent=4, ensure_ascii=False)
    with open("test/activity.json",'w') as JSON :
        JSON.write(dumpling)

    dumpling=json.dumps(stage_collection,indent=4, ensure_ascii=False)
    with open("test/stage.json",'w') as JSON :
        JSON.write(dumpling)

    dumpling=json.dumps(akenemy,indent=4, ensure_ascii=False)
    with open("json/akenemy.json",'w') as JSON :
        JSON.write(dumpling)
        
    print(f'>> Akenemy Completed\n\n\t{datetime.now().strftime("%d %b %Y %H:%M:%S")}\n')
    
if __name__ == '__main__':
    Akenemy()