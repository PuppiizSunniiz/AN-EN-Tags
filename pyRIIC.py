import json
import re
from pyfunction import printr, script_result, json_load, R, G, B, Y, RE

def riic_tl_json(show : bool = False):
    json_building   =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/building_data.json")
    json_buildingEN =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/building_data.json")
    
    json_character  =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/character_table.json")
    
    json_gamedataEN =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/gamedata_const.json")
    
    json_riicTL = {"buffs" : {}, "chars" : json_building["chars"]}
    
    def riic_en_dict() -> dict[str, str]:
        temp = {}
        
        for key in json_buildingEN["buffs"].keys():
            if json_building["buffs"][key]["description"] not in temp.keys():
                temp[json_building["buffs"][key]["description"]] = json_buildingEN["buffs"][key]["description"]

        return temp

    def riic_tl(desc : str, mode : str) -> str:
        def riic_mode_tl(desc : str, mode : str) -> str:
            desc_sub = desc
            class_parse = {
                            "先锋" : "Vanguard",    "近卫"  : "Guard",      "重装" : "Defender",    "狙击" : "Sniper",
                            "术师" : "Caster",      "医疗"  : "Medic",      "辅助" : "Supporter",   "特种" : "Specialist"
                        }

            match mode:
                case "control":
                    pass
                case "power":
                    # Speed faction
                    re_power_rec_spd_ext_faction = r'^进驻发电站时，如果其他<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员进驻在发电站，则无人机充能速度<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_power_rec_spd_ext_faction, desc_sub):
                        desc_match          = re.match(re_power_rec_spd_ext_faction, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_power         = desc_match.group(2)
                        return f'When this Operator is assigned to a Power Plant, if there are no <${match_faction_skill}><@cc.kw>{match_faction_name}</></> operators assigned to a Power Plant, increases the drone recovery rate by <@cc.vup>{match_power}</>'
                case "manu":
                    # Speed & Morale
                    re_manu_formula_spd_limit_cost = r'^进驻制造站时，<@cc\.kw>([^<]*)<\/>类配方的生产力<@cc\.vup>([\+0-9%]*)<\/>，心情每小时消耗<@cc\.vup>([\+\-\.0-9]*)<\/>$'
                    if re.match(re_manu_formula_spd_limit_cost, desc_sub):
                        desc_match          = re.match(re_manu_formula_spd_limit_cost, desc_sub)
                        match_mat           = riic_match_tl(desc_match.group(1), "item")
                        match_spd           = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        return f'When this Operator is assigned to a Factory, <@cc.kw>{match_mat}</> formula related productivity <@cc.vup>{match_spd}</> and Morale consumed per hour <@cc.vup>{match_morale}</>'
                    # Speed together with
                    re_manu_prod_spd_double = r'^进驻制造站时，当与<@cc.kw>([^<]*)</>在同一个制造站时，<@cc.kw>([^<]*)</>类配方的生产力<@cc.vup>([\+0-9%]*)</>$'
                    if re.match(re_manu_prod_spd_double, desc_sub):
                        desc_match          = re.match(re_manu_prod_spd_double, desc_sub)
                        match_op            = riic_match_tl(desc_match.group(1), "op")
                        match_mat           = riic_match_tl(desc_match.group(2), "item")
                        match_prod          = desc_match.group(3)
                        return f'When this Operator is assigned to a Factory together with <@cc.kw>{match_op}</>, <@cc.kw>{match_mat}</> productivity <@cc.vup>{match_prod}</>'
                    # Speed & Cap
                    re_manu_prod_spd_limit_cost_down = r'^进驻制造站时，生产力<@cc\.vup>([\+0-9%]*)</>，仓库容量上限<@cc\.(vdown|vup)>([\-\+0-9]*)</>$'
                    if re.match(re_manu_prod_spd_limit_cost_down, desc_sub):
                        desc_match          = re.match(re_manu_prod_spd_limit_cost_down, desc_sub)
                        match_prod          = desc_match.group(1)
                        match_cap_desc      = desc_match.group(2)
                        match_cap           = desc_match.group(3)
                        return f'When this Operator is assigned to a Factory, Productivity <@cc.vup>{match_prod}</>, capacity limit <@cc.{match_cap_desc}>{match_cap}</>'
                    # Speed by Power Plants Robot
                    re_manu_token_prod_spd = r'^进驻制造站时，每有<@cc\.vup>([0-9]*)<\/>台<\$(cc\.[\.A-Za-z0-9]*)><@cc\.kw>[^<]*<\/><\/>进驻发电站，<@cc\.kw>([^<]*)<\/>类配方的生产力<@cc\.vup>([\+0-9%]*)</>$'
                    if re.match(re_manu_token_prod_spd, desc_sub):
                        desc_match          = re.match(re_manu_token_prod_spd, desc_sub)
                        match_every         = desc_match.group(1)
                        match_skill_id      = desc_match.group(2)
                        match_skill_name    = riic_match_tl(match_skill_id)
                        match_mat           = riic_match_tl(desc_match.group(3), "item")
                        match_prod          = desc_match.group(4)
                        return f'When this Operator is assigned to a Factory, for every <@cc.kw>{match_every}</> <$cc.{match_skill_id}><@cc.kw>{match_skill_name}</></> assigned to <@cc.kw>Power Plants</>, <@cc.kw>{match_mat}</> productivity <@cc.vup>{match_prod}</>'
                case "trade":
                    # Trade together with (Exuter : trade_ord_spd&multiPar[100]) 
                    re_trade_ord_spd_multiPar = r'^进驻贸易站时，订单获取效率<@cc\.vup>([\+0-9%]*)<\/>；当与<@cc\.kw><\$(cc\.[\.A-Za-z0-9]*)>([^<]*)<\/><\/>在同一个贸易站时，订单获取效率额外<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_trade_ord_spd_multiPar, desc_sub):
                        desc_match          = re.match(re_trade_ord_spd_multiPar, desc_sub)
                        match_spd1          = desc_match.group(1)
                        match_term          = desc_match.group(2)
                        if match_term in json_gamedataEN["termDescriptionDict"].keys():
                            match_with      = json_gamedataEN["termDescriptionDict"][match_term]["termName"]
                        else :
                            match_op        = desc_match.group(3)
                            match_with      = riic_match_tl(match_op, "op")
                        match_spd2          = desc_match.group(4)
                        return f'When this Operator is assigned to a Trading Post, order acquisition efficiency <@cc.vup>{match_spd1}</>；when in the same Trading Post as <${match_term}><@cc.kw>{match_with}</></>, additional order acquisition efficiency <@cc.vup>{match_spd2}</>'
                    # Trade faction
                    re_trade_ord_spd_par = r'^进驻贸易站时，同个贸易站中每有([0-9]*)名<\$(cc\.[^>]*)><@cc\.kw>拉特兰<\/><\/>干员，当前贸易站订单获取效率<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_trade_ord_spd_par, desc_sub):
                        desc_match          = re.match(re_trade_ord_spd_par, desc_sub)
                        match_every         = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_spd         = desc_match.group(3)
                        return f'When this Operator is assigned to a Trading Post, for every {"" if match_every == "1" else f'{match_every} '}<${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator in the same Trading Post, order acquisition efficiency <@cc.vup>{match_spd}</>'
                case "workshop":
                    # Cost reduce morale
                    re_workshop_formula_cost = r'^进驻加工站加工<@cc\.kw>([^<]*)<\/>时，心情消耗为<@cc\.kw>([0-9]*)<\/>的配方全部<@cc\.vup>([\+\-0-9]*)<\/>心情消耗$'
                    if re.match(re_workshop_formula_cost, desc_sub):
                        desc_match          = re.match(re_workshop_formula_cost, desc_sub)
                        match_mat           = riic_match_tl(desc_match.group(1), "item")
                        match_cost          = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        return f'When this Operator is assigned to the Workshop to process <@cc.kw>{match_mat}</>, reduces the Morale consumed by all corresponding formulas that cost <@cc.kw>{match_cost}</> Morale by <@cc.vup>{match_morale}</>'
                case "train":
                    # Train Class Morale Down
                    re_train_cost_profession = r'^进驻训练室协助<@cc\.kw>([^<]*)<\/>干员训练专精技能至<@cc\.vup>([1-3])<\/>级时，心情每小时消耗<@cc\.vdown>([\+\-0-9]*)<\/>$'
                    if re.match(re_train_cost_profession, desc_sub):
                        desc_match          = re.match(re_train_cost_profession, desc_sub)
                        match_class         = class_parse[desc_match.group(1)]
                        match_spec          = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        return f'When this Operator is assigned to be the Trainer in the Training Room, Morale consumed per hour <@cc.vdown>{match_morale}</> when training a <@cc.kw>{match_class}</> Operator\'s skill to Specialization Level <@cc.vup>{match_spec}</>'
                    # Train Skill point
                    re_train_spd_bd = r'^进驻训练室协助位时，心情每小时消耗<@cc\.vdown>([\+\-0-9]*)<\/>，每<@cc\.vup>([0-9]*)<\/>点<\$(cc\.[^>]*)><@cc\.rem>[^<]*<\/><\/><@cc\.vup>([\+0-9%]*)<\/>专精技能训练速度$'
                    if re.match(re_train_spd_bd, desc_sub):
                        desc_match          = re.match(re_train_spd_bd, desc_sub)
                        match_morale        = desc_match.group(1)
                        match_every         = desc_match.group(2)
                        match_skill_id      = desc_match.group(3)
                        match_skill_name    = riic_match_tl(match_skill_id)
                        match_spd           = desc_match.group(4)
                        return f'When this Operator is assigned to be the Trainer in the Training Room, Morale consumed per hour <@cc.vdown>{match_morale}</>, Operators\' Specialization training speed <@cc.vup>{match_spd}</> for every <@cc.vup>{match_every}</> <${match_skill_id}><@cc.rem>{match_skill_name}</></>'
                    # Train Class Specialize
                    re_train_spd_profession = r'^进驻训练室协助位时，<@cc\.kw>([^<]*)<\/>干员的专精技能训练速度<@cc\.vup>([\+0-9%]*)<\/>，如果本次训练专精技能至<@cc\.vup>([1-3])<\/>级，则训练速度额外<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_train_spd_profession, desc_sub):
                        desc_match          = re.match(re_train_spd_profession, desc_sub)
                        match_class         = class_parse[desc_match.group(1)]
                        match_speed1        = desc_match.group(2)
                        match_spec          = desc_match.group(3)
                        match_speed2        = desc_match.group(4)
                        return f'When this Operator is assigned to be the Trainer in the Training Room, <@cc.kw>{match_class}</> Operators\' Specialization training speed <@cc.vup>{match_speed1}</>; if training this skill to Specialization Level <@cc.vup>{match_spec}</>, training speed will be further increased by <@cc.vup>{match_speed2}</>'
                case "dorm":
                    # Dorm morale by Empty Recruit slot
                    re_dorm_hireToRecAll = r'^进驻宿舍时，该宿舍内所有干员心情每小时恢复<@cc\.vup>([\+\-\.0-9]*)<\/>，同时每个招募位（不包含初始招募位）额外<@cc\.vup>([\+\-\.0-9]*)<\/>恢复效果（叠加后的最终值同种效果取最高）$'
                    if re.match(re_dorm_hireToRecAll, desc_sub):
                        desc_match          = re.match(re_dorm_hireToRecAll, desc_sub)
                        match_morale1       = desc_match.group(1)
                        match_morale2       = desc_match.group(2)
                        return f'When this Operator is assigned to a Dormitory, restores <@cc.vup>{match_morale1}</> Morale per hour to all Operators assigned to that Dormitory, and every recruit slot (excluding initial slot), restores another <@cc.vup>{match_morale2}</> (Only the strongest stacked effect of this type takes place)'
                    # Dorm group addition morale
                    re_dorm_rec_single_power = r'^进驻宿舍时，使该宿舍内除自身以外心情未满的某个干员每小时恢复<@cc\.vup>([\+\.0-9]*)<\/>（同种效果取最高），如果目标是<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员，则恢复效果额外<@cc\.vup>([\+\.0-9]*)<\/>$'
                    if re.match(re_dorm_rec_single_power, desc_sub):
                        desc_match          = re.match(re_dorm_rec_single_power, desc_sub)
                        match_morale1       = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_morale2       = desc_match.group(3)
                        return f'When this Operator is assigned to a Dormitory, restores <@cc.vup>{match_morale1}</> Morale per hour to another Operator assigned to that Dormitory whose Morale is not full (Only the strongest effect of this type takes place); if the target is a <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator, further increases Morale restored by <@cc.vup>{match_morale2}</>'
                    re_dorm_rec_all_group = r'^进驻宿舍时，基建内（不包含副手及活动室使用者）每名<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员为该宿舍内所有干员心情每小时恢复速度<@cc\.vup>([\+\.0-9]*)<\/>（最多生效<@cc\.kw>([0-9]*)<\/>名，且同种效果取最高）$'
                    # Dorm all morale by faction
                    if re.match(re_dorm_rec_all_group, desc_sub):
                        desc_match          = re.match(re_dorm_rec_all_group, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_morale        = desc_match.group(2)
                        match_cap           = desc_match.group(3)
                        return f'When this Operator is assigned to a Dormitory, Morale recovery per hour of all Operators in that Dormitory <@cc.vup>{match_morale}</> for each <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator in the Base (excluding Assistants and Activity Room users, caps at <@cc.kw>{match_cap}</> Operators, strongest effect of the same type applies)'
                case "hire":
                    # Speed Morale
                    re_hire_spd_cost = r'^进驻人力办公室时，人脉资源的联络速度<@cc\.vup>([\+0-9%]*)<\/>，心情每小时消耗<@cc\.vdown>([\+\-\.[0-9]*)<\/>$'
                    if re.match(re_hire_spd_cost, desc_sub):
                        desc_match          = re.match(re_hire_spd_cost, desc_sub)
                        match_spd           = desc_match.group(1)
                        match_morale        = desc_match.group(2)
                        return f'When this Operator is assigned to the HR Office, HR contacting speed <@cc.vup>{match_spd}</>, Morale consumed per hour <@cc.vup>{match_morale}</>'
                case "meet":
                    # Speed by Recruit slot
                    re_meet_spd_clue = r'^进驻会客室时，每个招募位（不包含初始招募位）提升<@cc\.vup>([0-9%]*)<\/>线索搜集速度$'
                    if re.match(re_meet_spd_clue, desc_sub):
                        desc_match          = re.match(re_meet_spd_clue, desc_sub)
                        match_spd           = desc_match.group(1)
                        return f'When this Operator is assigned to the Reception Room, for every Recruit slot (Default slots do not count) increases Clue search speed by <@cc.vup>{match_spd}</>'
                    # Speed by op in Dorm ? [meet_spd_ext&P[000]]
                    re_meet_spd_ext_P = r'^进驻会客室时，如果<@cc\.kw>([^<]*)<\/>进驻在宿舍，则线索搜集速度额外提升<@cc\.vup>([0-9%]*)<\/>$'
                    if re.match(re_meet_spd_ext_P, desc_sub):
                        desc_match          = re.match(re_meet_spd_ext_P, desc_sub)
                        match_op            = riic_match_tl(desc_match.group(1), "op")
                        match_spd           = desc_match.group(2)
                        return f'When this Operator is assigned to the Reception Room, if <@cc.kw>{match_op}</> is assigned to a Dormitory, increases Clue search speed by an additional <@cc.vup>{match_spd}</>'
                    # Speed not own when exchange
                    re_meet_spd_notOwned_exchange = r'^进驻会客室时，处于线索交流时更容易获得线索板上尚未拥有的线索$'
                    if re.match(re_meet_spd_notOwned_exchange, desc_sub):
                        return f'When this Operator is assigned to the Reception Room, if in Clue Exchange, increases the likelihood of obtaining clues that are not on the Clue Board'
                    # Speed faction
                    re_meet_spd_sami = r'^进驻会客室时，线索搜集速度提升<@cc\.vup>([\+0-9%]*)<\/>，与其他<\$(cc\.[^>]*)><@cc.kw>黑钢国际干员<\/><\/>进驻会客室一起工作时，线索搜集速度额外提升<@cc\.vup>([\+0-9%]*)<\/>(，自身心情每小时消耗<@cc\.vdown>([\+\-\.0-9]*)<\/>|)$'
                    if re.match(re_meet_spd_sami, desc_sub):
                        desc_match          = re.match(re_meet_spd_sami, desc_sub)
                        match_spd1          = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_spd2          = desc_match.group(3)
                        match_morale        = desc_match.group(5) if desc_match.group(4) else ""
                        return f'When this Operator is assigned to the Reception Room, increases Clue search speed by <@cc.vup>{match_spd1}</>, and when assigned together with another <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator, increases Clue search speed by an additional <@cc.vup>{match_spd2}</>{f' while self Morale loss per hour <@cc.vdown>{match_morale}</>' if match_morale else ""}'
                case _ :
                    printr(f'{R}How did you get here BAKA !!! {RE}: mode = {R}{mode}')   
            
            return desc_sub
        
        def riic_match_tl(desc : str, extra : str = "") -> str:
            '''
                desc = Description to TL
                
                extra = Extra parameter for certain things
                
                ---
                
                **Desc - Extra**
                
                **cc.g.([^<]*)** - group skill
                    - default name
                    
                **<@cc.kw>([^<]*)</>** - keyword
                    - **item** -> for item name
                    - **op** -> for operator name
            '''
            # Base skill term (cc)
            if re.match(r'^cc\.([\.A-Za-z0-9]*)$', desc):
                return json_gamedataEN["termDescriptionDict"][desc]["termName"] if desc in json_gamedataEN["termDescriptionDict"].keys() else desc.split(".")[-1].capitalize()
            else:
                match extra:
                    case "item":
                        mat_tl = {
                                    "任意类材料"    : "any material",
                                    "作战记录"      : "Battle Record",
                                    "贵金属"        : "Precious Metal",
                        }
                        if desc in mat_tl:
                            return mat_tl[desc]
                        else:
                            printr(f'riic_match_tl : {Y}"item"{RE} case - {Y}{desc}')
                    case "op":
                        return [json_character[op_key]["appellation"] for op_key in json_character.keys() if desc == json_character[op_key]["name"]][0]
                    case _:
                        printr(f'riic_match_tl : {R}new case{RE} - {Y}{desc}')
            return desc.replace("；", "; ")
        
        return riic_mode_tl(desc, mode)

    riic_tl_dict = riic_en_dict()

    for riic in json_building["buffs"].keys(): # [key for key in json_building["buffs"].keys() if key not in json_buildingEN["buffs"].keys()]
        riic_value : dict[str, str] = json_building["buffs"][riic]
        if riic not in json_riicTL.keys(): # if riic not in json_riicTL.keys() and not riic_tl_dict.get(riic_value["description"], None):
            json_riicTL["buffs"][riic] = {
                                    "buffName"      :   json_buildingEN["buffs"][riic]["buffName"] if riic in json_buildingEN["buffs"].keys() else riic_value["buffName"],
                                    "skillIcon"     :   json_building["buffs"][riic]["skillIcon"],
                                    "desc"          :   riic_value["description"],
                                    "description"   :   riic_tl_dict.get(riic_value["description"], riic_tl(riic_value["description"], riic.split("_")[0]))
                                }
    
    script_result(json_riicTL, show)
    with open("json/puppiiz/riic_data.json", "w", encoding = "utf-8") as filepath :
        json.dump(json_riicTL, filepath, indent = 4, ensure_ascii = False)

template = '''
                    re_ = r'^$'
                    if re.match(re_, desc_sub):
                        desc_match          = re.match(re_, desc_sub)
                        match_= desc_match.group(1)
                        match_= desc_match.group(2)
                        match_= desc_match.group(3)
                        return f''
'''

if __name__ == "__main__":
    riic_tl_json()
    print(template)