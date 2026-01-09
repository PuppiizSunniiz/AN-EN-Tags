import json
import re
from pyfunction import printr, script_result, json_load, R, G, B, Y, RE

def riic_tl_json(show : bool = False):
    json_building   =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/building_data.json")
    json_buildingEN =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/building_data.json")
    
    json_character  =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/character_table.json")
    
    json_term_effect=   json_load("json/named_effects.json")
    
    json_riicTL = {"buffs" : {}, "chars" : {char:{"buffChar":json_building["chars"][char]["buffChar"]} for char in json_building["chars"].keys()}}
    
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
                    # Control dorm 1 "Misumi Uika" - Ave Mujica
                    re_control_dorm_bd = r'^进驻控制中枢时，宿舍内每有<@cc\.vup>([0-9]*)<\/>名干员，<\$(cc\.[^>]*)><@cc\.rem>[^<]*<\/><\/><@cc\.vup>([\+0-9]*)<\/>$'
                    if re.match(re_control_dorm_bd, desc_sub):
                        desc_match          = re.match(re_control_dorm_bd, desc_sub)
                        match_count         = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_value         = desc_match.group(3)
                        return f'When this Operator is assigned to the Control Center, for every <@cc.kw>{match_count}</> operator in the Dormitory, <${match_faction_skill}><@cc.rem>{match_faction_name}</></><@cc.vup>{match_value}</>'
                    # Control tag - Dorm Recover
                    re_control_dorm_rec_tag = r'^进驻控制中枢时，所有宿舍内<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>的心情每小时恢复<@cc\.vup>([\+\.0-9]*)<\/>（同种效果取最高）$'
                    if re.match(re_control_dorm_rec_tag, desc_sub):
                        desc_match          = re.match(re_control_dorm_rec_tag, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_morale        = desc_match.group(2)
                        return f'When this Operator is assigned to the Control Center, all <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operators in Dormitories recover <@cc.vup>{match_morale}</> Morale per hour (strongest effect of the same type applies)'
                    # Control dorm 2 "Misumi Uika" - Ave Mujica
                    re_control_dorm_rec2 = r'^进驻控制中枢时，所有宿舍内所有干员的心情每小时恢复<@cc\.vup>([\+\.0-9]*)<\/>（同种效果取最高）；当与<@cc\.kw>([^<]*)<\/>一起进驻控制中枢时，<@cc\.kw>([^<]*)<\/>的心情每小时恢复<@cc\.vup>([\+\.0-9]*)<\/>$'
                    if re.match(re_control_dorm_rec2, desc_sub):
                        desc_match          = re.match(re_control_dorm_rec2, desc_sub)
                        match_morale_1      = desc_match.group(1)
                        match_op_1          = riic_match_tl(desc_match.group(2), "op")
                        match_op_2          = riic_match_tl(desc_match.group(3), "op")
                        match_morale_2      = desc_match.group(4)
                        return f'When this Operator is assigned to the Control Center, all Operators in Dormitories recover <@cc.vup>{match_morale_1}</> Morale per hour (strongest effect of the same type applies); When this Operator is assigned together with <@cc.kw>{match_op_1}</> to the Control Center, <@cc.kw>{match_op_2}</>\'s Morale recovered per hour <@cc.vup>{match_morale_2}</>.'
                    # Control hire "Yahata Umiri" - Ave Mujica
                    re_control_hire_spd_bd = r'^进驻控制中枢时，<\$(cc\.[^>]*)><@cc\.rem>[^<]*<\/><\/><@cc\.vup>([\+0-9]*)<\/>；人脉资源的联络速度<@cc\.vup>([\+0-9%]*)<\/>（同种效果取最高）$'
                    if re.match(re_control_hire_spd_bd, desc_sub):
                        desc_match          = re.match(re_control_hire_spd_bd, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_point         = desc_match.group(2)
                        match_spd           = desc_match.group(3)
                        return f'When this Operator is assigned to the Control Center, <${match_faction_skill}><@cc.rem>{match_faction_name}</></><@cc.vup>{match_point}</>; HR contacting speed <@cc.vup>{match_spd}</> (strongest effect of the same type applies)'
                    # control_meeting&mp_cost[000]/[100] // char_4166_varkis
                    re_control_meeting__mp_cost = r'进驻控制中枢时，基建内（不包含副手及活动室使用者）每有1名<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员，会客室线索搜集速度<@cc\.vup>([\+0-9%]*)<\/>（最多<@cc\.vup>([\+0-9%]*)<\/>，同种效果取最高）；当与<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员进驻控制中枢一起工作时，自身心情每小时消耗<@cc\.vdown>([\+\.0-9]*)<\/>'
                    if re.match(re_control_meeting__mp_cost, desc):
                        desc_match          = re.match(re_control_meeting__mp_cost, desc_sub)
                        match_faction_skill1= desc_match.group(1)
                        match_faction_name1 = riic_match_tl(match_faction_skill1)
                        match_spd           = desc_match.group(2)
                        match_spd_max       = desc_match.group(3)
                        match_faction_skill2= desc_match.group(4)
                        match_faction_name2 = riic_match_tl(match_faction_skill2)
                        match_mood          = desc_match.group(5)
                        return f'When this Operator is assigned to the Control Center, for each <${match_faction_skill1}><@cc.kw>{match_faction_name1}</></> Operator in the Base (excluding Assistants and Activity Room users), increases Clue collection speed in the Reception Room by <@cc.vup>{match_spd}</> (up to a maximum of <@cc.vup>{match_spd_max}</>, strongest effect of the same type applies); When this Operator is assigned together with other <${match_faction_skill2}><@cc.kw>{match_faction_name2}</></> Operators to the Control Center, self Morale loss per hour <@cc.vdown>{match_mood}</>'
                    # Control meeting "Yūtenji Nyamu" - Ave Mujica
                    re_control_meeting_spd_bd = r'^进驻控制中枢时，<\$(cc\.[^>]*)><@cc\.rem>[^<]*<\/><\/><@cc\.vup>([\+0-9]*)<\/>；会客室线索搜集速度提升<@cc\.vup>([\+0-9%]*)</>（同种效果取最高）$'
                    if re.match(re_control_meeting_spd_bd, desc_sub):
                        desc_match          = re.match(re_control_meeting_spd_bd, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_point         = desc_match.group(2)
                        match_spd           = desc_match.group(3)
                        return f'When this Operator is assigned to the Control Center, <${match_faction_skill}><@cc.rem>{match_faction_name}</></><@cc.vup>{match_point}</>; Clue search speed in Reception Room increases by <@cc.vup>{match_spd}</> (strongest effect of the same type applies)'
                    # Control trade "Wakaba Mutsumi" - Ave Mujica
                    re_control_mp_bd_trade = r'^进驻控制中枢时，<\$(cc\.[^>]*)><@cc\.rem>[^<]*<\/><\/><@cc\.vup>([\+0-9]*)<\/>；每有<@cc\.vup>([0-9]*)<\/>点<\$(cc\.[^>]*)><@cc\.rem>[^<]*<\/><\/>，自身心情每小时消耗<@cc\.vdown>([\+\.0-9]*)<\/>，所有贸易站订单效率<@cc\.vup>([\+0-9%]*)<\/>（同种效果取最高）$'
                    if re.match(re_control_mp_bd_trade, desc_sub):
                        desc_match            = re.match(re_control_mp_bd_trade, desc_sub)
                        match_faction_skill_1 = desc_match.group(1)
                        match_faction_name_1  = riic_match_tl(match_faction_skill_1)
                        match_point           = desc_match.group(2)
                        match_count           = desc_match.group(3)
                        match_faction_skill_2 = desc_match.group(4)
                        match_faction_name_2  = riic_match_tl(match_faction_skill_1)
                        match_morale          = desc_match.group(5)
                        match_eff             = desc_match.group(6)
                        return f'When this Operator is assigned to the Control Center, <${match_faction_skill_1}><@cc.rem>{match_faction_name_1}</></><@cc.vup>{match_point}</>; for every <@cc.vup>{match_count}</> points <${match_faction_skill_2}><@cc.rem>{match_faction_name_2}</></>,  decreases own morale consumption by <@cc.vdown>{match_morale}</>, all Trading Posts\' order efficiency <@cc.vup>{match_eff}</> (Only the strongest effect of this type takes place)'
                    # Control morale point "Togawa Sakiko" - Ave Mujica
                    re_control_mp_cost_bd3 = r'^进驻控制中枢时，([^<]*)处于<@cc\.kw>([0-9]*)<\/>点及以上时，自身心情每小时消耗<@cc\.vdown>([\+\.0-9]*)<\/>$'
                    if re.match(re_control_mp_cost_bd3, desc_sub):
                        desc_match          = re.match(re_control_mp_cost_bd3, desc_sub)
                        match_skill         = desc_match.group(1)
                        match_point         = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        return f'When this Operator is assigned to the Control Center, if {match_skill} more than <@cc.kw>{match_point}</> points, decreases own morale consumption by<@cc.vdown>{match_morale}</>'
                    # Control morale point "Wakaba Mutsumi" - Ave Mujica
                    re_control_mp_cost_reset = r'^当与<@cc\.kw>([^<]*)<\/>一起进驻控制中枢时，消除自身心情消耗的影响$'
                    if re.match(re_control_mp_cost_reset, desc_sub):
                        desc_match          = re.match(re_control_mp_cost_reset, desc_sub)
                        match_op            = riic_match_tl(desc_match.group(1), "op")
                        return f'When this Operator is assigned together with <@cc.kw>{match_op}</> to the Control Center, remove any self Morale reduction effects'
                    # Control meeting "Yūtenji Nyamu" - Ave Mujica
                    re_control_mp_meet_spd = r'^当与<@cc\.kw>([^<]*)<\/>一起进驻控制中枢时，<@cc\.kw>([^<]*)</>心情每小时消耗<@cc\.vdown>([\+\.0-9]*)<\/>，会客室线索搜集速度额外提升<@cc\.vup>([\+\.0-9%]*)</>（同种效果取最高）$'
                    if re.match(re_control_mp_meet_spd, desc_sub):
                        desc_match          = re.match(re_control_mp_meet_spd, desc_sub)
                        match_op_1          = riic_match_tl(desc_match.group(1), "op")
                        match_op_2          = riic_match_tl(desc_match.group(2), "op")
                        match_morale        = desc_match.group(3)
                        match_spd           = desc_match.group(4)
                        return f'When this Operator is assigned together with <@cc.kw>{match_op_1}</> to the Control Center, <@cc.kw>{match_op_2}</> Morale loss per hour <@cc.vdown>{match_morale}</> and increases Clue search speed in Reception Room by an additional <@cc.vup>{match_spd}</> (Only the strongest effect of this type takes place)'
                    # Control point "Togawa Sakiko" - Ave Mujica
                    re_control_prod_bd_spd = r'^进驻控制中枢时，所有生产<@cc\.kw>([^<]*)<\/>类配方的制造站生产力<@cc\.vup>([\+\.0-9%]*)<\/>，每有<@cc\.vup>([0-9]*)<\/>点<\$(cc\.[^>]*)><@cc\.rem>[^<]*<\/><\/>，所有生产<@cc\.kw>([^<]*)<\/>类配方的制造站生产力<@cc\.vup>([\+\.0-9%]*)<\/>$'
                    if re.match(re_control_prod_bd_spd, desc_sub):
                        desc_match          = re.match(re_control_prod_bd_spd, desc_sub)
                        match_mat_1         = riic_match_tl(desc_match.group(1), "item")
                        match_prod_1        = desc_match.group(2)
                        match_point         = desc_match.group(3)
                        match_faction_skill = desc_match.group(4)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_mat_2         = riic_match_tl(desc_match.group(5), "item")
                        match_prod_2        = desc_match.group(6)
                        return f'When this Operator is assigned to the Control Center, all Factories\' productivity <@cc.vup>{match_prod_1}</> towards <@cc.kw>{match_mat_1}</>; for every <@cc.vup>{match_point}</> <${match_faction_skill}><@cc.kw>{match_faction_name}</></> points, all Factories\' productivity <@cc.vup>{match_prod_2}</> towards <@cc.kw>{match_mat_2}</>'
                    # Control tag - Production Speed
                    re_control_token_prod_spd = r'^当与<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员进驻控制中枢一起工作时，所有制造站生产力<@cc\.vup>([\+\.0-9%]*)<\/>（同种效果取最高）$'
                    if re.match(re_control_token_prod_spd, desc_sub):
                        desc_match          = re.match(re_control_token_prod_spd, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_prod          = desc_match.group(2)
                        return f'When this Operator is assigned together with other <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operators to the Control Center, all Factories\' productivity <@cc.vup>{match_prod}</> (Only the strongest effect of this type takes place)'
                    # Control trade "Yahata Umiri" - Ave Mujica
                    re_control_tra_limit_spd2 = r'^进驻控制中枢时，每个进驻在贸易站的<\$(cc\.[^>]*)><@cc\.kw>[^>]*</></>干员，订单获取效率<@cc\.vup>([\+\.0-9%]*)<\/>$'
                    if re.match(re_control_tra_limit_spd2, desc_sub):
                        desc_match          = re.match(re_control_tra_limit_spd2, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_spd           = desc_match.group(2)
                        return f'When this Operator is assigned to the Control Center, all <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operators assigned to Trading Posts gain order acquisition efficiency <@cc.vup>{match_spd}</>'
                    # Control trade "SilverAsh the Reignfrost"
                    re_control_tra_limit_spd3 = r'^进驻控制中枢时，每个存在<@cc\.vup>([0-9]*)<\/>名<\$(cc\.[^>]*)><@cc\.kw>[^>]*</></>干员的贸易站，订单获取效率<@cc\.vup>([\+\.0-9%]*)<\/>$'
                    if re.match(re_control_tra_limit_spd3, desc_sub):
                        desc_match          = re.match(re_control_tra_limit_spd3, desc_sub)
                        match_every         = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_spd           = desc_match.group(3)
                        return f'When this Operator is assigned to the Control Center, Trading Posts with {match_every} <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operators assigned, gain order acquisition efficiency <@cc.vup>{match_spd}</>'
                case "power":
                    # Speed faction
                    re_power_rec_spd_ext_faction = r'^进驻发电站时，如果其他<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员进驻在发电站，则无人机充能速度<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_power_rec_spd_ext_faction, desc_sub):
                        desc_match          = re.match(re_power_rec_spd_ext_faction, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_power         = desc_match.group(2)
                        return f'When this Operator is assigned to a Power Plant, if another <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator is assigned to a Power Plant, drone charging speed <@cc.vup>{match_power}</>'
                case "manu":
                    # Speed cost
                    re_manu_formula_spd__cost_bd = r'进驻制造站时，基建内（不包含副手及活动室使用者）每有1名<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员（最多<@cc\.kw>(\d+)<\/>名），<@cc\.kw>([^<]*)<\/>类配方的生产力<@cc\.vup>([\+\-\.0-9]*%)<\/>'
                    if re.match(re_manu_formula_spd__cost_bd, desc_sub):
                        desc_match          = re.match(re_manu_formula_spd__cost_bd, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_cap           = desc_match.group(2)
                        match_mat           = riic_match_tl(desc_match.group(3), "item")
                        match_spd           = desc_match.group(4)
                        return f'When this Operator is assigned to a Factory, for each <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator in the Base (excluding Assistants and Activity Room users, caps at <@cc.kw>{match_cap}</>), <@cc.kw>{match_mat}</> productivity <@cc.vup>{match_spd}</>'
                    # Speed & Morale
                    re_manu_formula_spd_limit_cost = r'^进驻制造站时，<@cc\.kw>([^<]*)<\/>类配方的生产力<@cc\.vup>([\+0-9%]*)<\/>，心情每小时消耗<@cc\.vup>([\+\-\.0-9]*)<\/>$'
                    if re.match(re_manu_formula_spd_limit_cost, desc_sub):
                        desc_match          = re.match(re_manu_formula_spd_limit_cost, desc_sub)
                        match_mat           = riic_match_tl(desc_match.group(1), "item")
                        match_spd           = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        return f'When this Operator is assigned to a Factory, <@cc.kw>{match_mat}</> formula related productivity <@cc.vup>{match_spd}</> and Morale consumed per hour <@cc.vup>{match_morale}</>'
                    # Speed together with
                    re_manu_prod_spd_double = r'^进驻制造站时，当与<@cc\.kw>([^<]*)</>在同一个制造站时，<@cc\.kw>([^<]*)</>类配方的生产力<@cc\.vup>([\+0-9%]*)</>$'
                    if re.match(re_manu_prod_spd_double, desc_sub):
                        desc_match          = re.match(re_manu_prod_spd_double, desc_sub)
                        match_op            = riic_match_tl(desc_match.group(1), "op")
                        match_mat           = riic_match_tl(desc_match.group(2), "item")
                        match_prod          = desc_match.group(3)
                        return f'When this Operator is assigned to a Factory, <@cc.kw>{match_mat}</> formula productivity <@cc.vup>{match_prod}</> when <@cc.kw>{match_op}</> is assigned to the same Factory'
                    # Speed Morale
                    re_manu_prod_spd_limit_cost = r'^进驻制造站时，生产力<@cc\.vup>([\+0-9%]*)</>，心情每小时消耗<@cc\.(vdown|vup)>([\-\+\.0-9]*)</>$'
                    if re.match(re_manu_prod_spd_limit_cost, desc_sub):
                        desc_match          = re.match(re_manu_prod_spd_limit_cost, desc_sub)
                        match_prod          = desc_match.group(1)
                        match_morale_desc   = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        return f'When this Operator is assigned to a Factory, Productivity <@cc.vup>{match_prod}</> and Morale consumed per hour <@cc.{match_morale_desc}>{match_morale}</>'
                    # Speed & Cap
                    re_manu_prod_spd_limit_cost_down = r'^进驻制造站时，生产力<@cc\.vup>([\+0-9%]*)</>，仓库容量上限<@cc\.(vdown|vup)>([\-\+0-9]*)</>$'
                    if re.match(re_manu_prod_spd_limit_cost_down, desc_sub):
                        desc_match          = re.match(re_manu_prod_spd_limit_cost_down, desc_sub)
                        match_prod          = desc_match.group(1)
                        match_cap_desc      = desc_match.group(2)
                        match_cap           = desc_match.group(3)
                        return f'When this Operator is assigned to a Factory, Productivity <@cc.vup>{match_prod}</> and capacity limit <@cc.{match_cap_desc}>{match_cap}</>'
                    # (manu_prod_spd&manu) #1
                    re_manu_prod_spd_manu_1 = r'^进驻制造站时，当前制造站内其他干员提供的生产力<@cc\.vdown>全部归零<\/>（不包含根据设施数量提供加成的生产力），每个当前制造站内干员为当前制造站仓库容量上限<@cc\.vup>([+0-9]*)<\/>$'
                    if re.match(re_manu_prod_spd_manu_1, desc_sub):
                        desc_match          = re.match(re_manu_prod_spd_manu_1, desc_sub)
                        match_cap           = desc_match.group(1)
                        return f'When this Operator is assigned to a Factory, the productivity contributed by all other Operators in that Factory <@cc.vdown>becomes 0</> (excluding productivity granted based on facility count), each Operators in that factory capacity limit <@cc.vup>{match_cap}</>'
                    # (manu_prod_spd&manu) #2
                    re_manu_prod_spd_manu_2 = r'^进驻制造站时，当前制造站内其他干员提供的生产力<@cc\.vdown>全部归零<\/>（不包含根据设施数量提供加成的生产力），每个当前制造站内干员为当前制造站<@cc\.vup>([+0-9%]*)<\/>生产力，仓库容量上限<@cc\.vup>([+0-9]*)<\/>$'
                    if re.match(re_manu_prod_spd_manu_2, desc_sub):
                        desc_match          = re.match(re_manu_prod_spd_manu_2, desc_sub)
                        match_prod          = desc_match.group(1)
                        match_cap           = desc_match.group(2)
                        return f'When this Operator is assigned to a Factory, the productivity contributed by all other Operators in that Factory <@cc.vdown>becomes 0</> (excluding productivity granted based on facility count), each Operators in that factory productivity <@cc.vup>{match_prod}</> and capacity limit <@cc.vup>{match_cap}</>'
                    # Cap by skill
                    re_manu_skill_limit = r'^进驻制造站时，当前制造站内每个<\$(cc\.[\.A-Za-z0-9]*)><@cc\.kw>(.+?)</></>技能为自身<@cc\.vup>([\+0-9]*)<\/>的仓库上限容量$'
                    if re.match(re_manu_skill_limit, desc_sub):
                        desc_match          = re.match(re_manu_skill_limit, desc_sub)
                        match_skill_id      = desc_match.group(1)
                        match_skill_name    = riic_match_tl(match_skill_id)
                        match_mat           = riic_match_tl(desc_match.group(1))
                        match_cap           = desc_match.group(3)
                        return f'When this Operator is assigned to a Factory, all <${match_skill_id}><@cc.kw>{match_skill_name}</></> skills in the Factory, capacity limit <@cc.vup>{match_cap}</>'
                        
                    # Speed by Power Plants Robot
                    re_manu_token_prod_spd = r'^进驻制造站时，每有<@cc\.vup>([0-9]*)<\/>台<\$(cc\.[\.A-Za-z0-9]*)><@cc\.kw>[^<]*<\/><\/>进驻发电站，<@cc\.kw>([^<]*)<\/>类配方的生产力<@cc\.vup>([\+0-9%]*)</>$'
                    if re.match(re_manu_token_prod_spd, desc_sub):
                        desc_match          = re.match(re_manu_token_prod_spd, desc_sub)
                        match_every         = desc_match.group(1)
                        match_skill_id      = desc_match.group(2)
                        match_skill_name    = riic_match_tl(match_skill_id)
                        match_mat           = riic_match_tl(desc_match.group(3), "item")
                        match_prod          = desc_match.group(4)
                        return f'When this Operator is assigned to a Factory, <@cc.kw>{match_mat}</> productivity <@cc.vup>{match_prod}</> for {f'every <@cc.vup>{match_every}</>' if int(match_every) > 1 else "<@cc.vup>every</>"} <$cc.{match_skill_id}><@cc.kw>{match_skill_name}</></> assigned to a Power Plant'
                case "trade":
                    # Trade together with (Exuter : trade_ord_spd&multiPar[100]) 
                    re_trade_ord_spd_multiPar = r'^进驻贸易站时，订单获取效率<@cc\.vup>([\+0-9%]*)<\/>；当与<@cc\.kw><\$(cc\.[\.A-Za-z0-9]*)>([^<]*)<\/><\/>在同一个贸易站时，订单获取效率额外<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_trade_ord_spd_multiPar, desc_sub):
                        desc_match          = re.match(re_trade_ord_spd_multiPar, desc_sub)
                        match_spd_1         = desc_match.group(1)
                        match_term          = desc_match.group(2)
                        if match_term in json_term_effect["termDescriptionDict"].keys():
                            match_with      = riic_match_tl(match_term)
                        else :
                            match_op        = desc_match.group(3)
                            match_with      = riic_match_tl(match_op, "op")
                        match_spd_2         = desc_match.group(4)
                        return f'When this Operator is assigned to a Trading Post, order acquisition efficiency <@cc.vup>{match_spd_1}</>; if <${match_term}><@cc.kw>{match_with}</></> is assigned to the same Trading Post, additionally order acquisition efficiency <@cc.vup>{match_spd_2}</>'
                    # Trade faction
                    re_trade_ord_spd_par = r'^进驻贸易站时，同个贸易站中每有([0-9]*)名<\$(cc\.[^>]*)><@cc\.kw>拉特兰<\/><\/>干员，当前贸易站订单获取效率<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_trade_ord_spd_par, desc_sub):
                        desc_match          = re.match(re_trade_ord_spd_par, desc_sub)
                        match_every         = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_spd           = desc_match.group(3)
                        return f'When this Operator is assigned to a Trading Post, for every {"" if match_every == "1" else f'{match_every} '}<${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator in the same Trading Post, order acquisition efficiency <@cc.vup>{match_spd}</>'
                    # Trade share speed
                    re_trade_ord_spd_share = r'^进驻贸易站时，贸易站内除自身以外每名处于工作状态的干员<@cc\.vup>([\+0-9%]*)</>订单获取效率$'
                    if re.match(re_trade_ord_spd_share, desc_sub):
                        desc_match          = re.match(re_trade_ord_spd_share, desc_sub)
                        match_spd           = desc_match.group(1)
                        return f'When this Operator is assigned to a Trading Post, other Operators working in the Trading Post have <@cc.vup>{match_spd}</> order acquisition efficiency'
                    # (trade_ord_spd&tag)
                    re_trade_ord_spd_tag = r'^进驻贸易站时，订单获取效率<@cc\.vup>([+0-9%]*)<\/>，基建内（不包含副手及活动室）每有一间进驻<\$(cc\.[^>]*)><@cc\.kw>精英干员<\/><\/>的设施，订单获取效率额外<@cc\.vup>([+0-9%]*)<\/>（最多<@cc\.kw>([0-9]*)<\/>间）$'
                    if re.match(re_trade_ord_spd_tag, desc_sub):
                        desc_match          = re.match(re_trade_ord_spd_tag, desc_sub)
                        match_eff           = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_eff_add       = desc_match.group(3)
                        match_facility      = desc_match.group(4)
                        return f'When this Operator is assigned to a Trading Post, order acquisition efficiency <@cc.vup>{match_eff}</>, each facility that <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator is stationed (excluding Assistants and Activity Room users), additional order acquisition efficiency <@cc.vup>{match_eff_add}</> (up to <@cc.kw>{match_facility}</> facilities)'
                case "workshop":
                    # Cost reduce morale
                    re_workshop_formula_cost = r'^进驻加工站加工<@cc\.kw>([^<]*)<\/>时，心情消耗为<@cc\.kw>([0-9]*)<\/>的配方全部<@cc\.vup>([\+\-0-9]*)<\/>心情消耗$'
                    if re.match(re_workshop_formula_cost, desc_sub):
                        desc_match          = re.match(re_workshop_formula_cost, desc_sub)
                        match_mat           = riic_match_tl(desc_match.group(1), "item")
                        match_cost          = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        return f'When this Operator is assigned to the Workshop to process <@cc.kw>{match_mat}</>, reduces the Morale consumed by all corresponding formulas that cost <@cc.kw>{match_cost}</> Morale by <@cc.vup>{match_morale}</>'
                    # (workshop_formula_cost5)
                    re_workshop_formula_cost5 = r'^进驻加工站加工<@cc\.kw>([^<]*)<\/>材料时，心情消耗为<@cc\.kw>([0-9]*)<\/>的配方全部<@cc\.vup>([\+\-0-9]*)<\/>心情消耗$'
                    if re.match(re_workshop_formula_cost5, desc_sub):
                        desc_match          = re.match(re_workshop_formula_cost5, desc_sub)
                        match_mat           = riic_match_tl(desc_match.group(1), "item")
                        match_cost          = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        return f'When this Operator is assigned to the Workshop to process <@cc.kw>{match_mat}</>-type materials, reduces the Morale consumed by all corresponding formulas that cost <@cc.kw>{match_cost}</> Morale by <@cc.vup>{match_morale}</>'
                    # (re_workshop_formula_device)
                    re_workshop_formula_device = r'^进驻加工站加工<@cc\.kw>([^<]*)<\/>材料时，副产品的产出概率提升<@cc\.vup>([0-9%]*)<\/>$'
                    if re.match(re_workshop_formula_device, desc_sub):
                        desc_match          = re.match(re_workshop_formula_device, desc_sub)
                        match_mat           = riic_match_tl(desc_match.group(1), "item")
                        match_byproduct     = desc_match.group(2)
                        return f'When this Operator is assigned to a Workshop to process <@cc.kw>{match_mat}</>-type materials, the production rate of byproduct increases by <@cc.vup>{match_byproduct}</>'
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
                        return f'When this Operator is assigned to be the Trainer in the Training Room, Morale consumed per hour <@cc.vdown>{match_morale}</>, and every <@cc.vup>{match_every}</> <${match_skill_id}><@cc.rem>{match_skill_name}</></> gives <@cc.vup>{match_spd}</> Specialization training speed'
                    # Train Class Specialize
                    re_train_spd_profession2 = r'^进驻训练室协助位时，<@cc\.kw>([^<]*)<\/>干员的专精技能训练速度<@cc\.vup>([\+0-9%]*)<\/>，如果本次训练专精技能至<@cc\.vup>(\d)<\/>级，则训练速度额外<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_train_spd_profession2, desc_sub):
                        desc_match          = re.match(re_train_spd_profession2, desc_sub)
                        match_class         = class_parse[desc_match.group(1)]
                        match_speed_1       = desc_match.group(2)
                        match_spec          = desc_match.group(3)
                        match_speed_2       = desc_match.group(4)
                        return f'When this Operator is assigned to be the Trainer in the Training Room, increases the Specialization training speed of <@cc.kw>{match_class}</> Operators by <@cc.vup>{match_speed_1}</>, and further increases this speed by <@cc.vup>{match_speed_2}</> if training the skill to Specialization Level <@cc.vup>{match_spec}</>'
                case "dorm":
                    # Dorm morale by Empty Recruit slot
                    re_dorm_hireToRecAll = r'^进驻宿舍时，该宿舍内所有干员心情每小时恢复<@cc\.vup>([\+\-\.0-9]*)<\/>，同时每个招募位（不包含初始招募位）额外<@cc\.vup>([\+\-\.0-9]*)<\/>恢复效果（叠加后的最终值同种效果取最高）$'
                    if re.match(re_dorm_hireToRecAll, desc_sub):
                        desc_match          = re.match(re_dorm_hireToRecAll, desc_sub)
                        match_morale_1      = desc_match.group(1)
                        match_morale_2      = desc_match.group(2)
                        return f'When this Operator is assigned to a Dormitory, restores <@cc.vup>{match_morale_1}</> Morale per hour to all Operators assigned to that Dormitory, and every recruit slot (excluding initial slot), restores another <@cc.vup>{match_morale_2}</> (Only the strongest stacked effect of this type takes place)'
                    # dorm_rec_all&tired[100] // char_1022_flwr2
                    re_dorm_rec_all__tired = r'进驻宿舍时，该宿舍内心情<@cc\.vup>([0-9]*)<\/>以下的干员恢复效果额外<@cc\.vup>([\+\-\.0-9]*)<\/>（同种效果取最高）'
                    if re.match(re_dorm_rec_all__tired, desc_sub):
                        desc_match          = re.match(re_dorm_rec_all__tired, desc_sub)
                        match_morale_1      = desc_match.group(1)
                        match_morale_2      = desc_match.group(2)
                        return f'When this Operator is assigned to a Dormitory, restores an additional <@cc.vup>{match_morale_2}</> Morale per hour to all Operators whose Morale is below <@cc.vup>{match_morale_1}</> (Only the strongest effect of this type applies)'
                    # Dorm group addition morale
                    re_dorm_rec_single_power = r'^进驻宿舍时，使该宿舍内除自身以外心情未满的某个干员每小时恢复<@cc\.vup>([\+\.0-9]*)<\/>（同种效果取最高），如果目标是<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员，则恢复效果额外<@cc\.vup>([\+\.0-9]*)<\/>$'
                    if re.match(re_dorm_rec_single_power, desc_sub):
                        desc_match          = re.match(re_dorm_rec_single_power, desc_sub)
                        match_morale_1      = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_morale_2      = desc_match.group(3)
                        return f'When this Operator is assigned to a Dormitory, restores <@cc.vup>{match_morale_1}</> Morale per hour to all other Operators assigned to that Dormitory whose Morale is not full (Only the strongest effect of this type takes place); if the target is a <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator, further increases Morale restored by <@cc.vup>{match_morale_2}</>'
                    # Dorm all morale by faction
                    re_dorm_rec_all_group = r'^进驻宿舍时，基建内（不包含副手及活动室使用者）每名<\$(cc\.[^>]*)><@cc\.kw>[^<]*<\/><\/>干员为该宿舍内所有干员心情每小时恢复速度<@cc\.vup>([\+\.0-9]*)<\/>（最多生效<@cc\.kw>([0-9]*)<\/>名，且同种效果取最高）$'
                    if re.match(re_dorm_rec_all_group, desc_sub):
                        desc_match          = re.match(re_dorm_rec_all_group, desc_sub)
                        match_faction_skill = desc_match.group(1)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_morale        = desc_match.group(2)
                        match_cap           = desc_match.group(3)
                        return f'When this Operator is assigned to a Dormitory, Morale recovery per hour of all Operators in that Dormitory <@cc.vup>{match_morale}</> for each <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator in the Base (excluding Assistants and Activity Room users, caps at <@cc.kw>{match_cap}</> Operators, strongest effect of the same type applies)'
                    # 
                    re_dorm_rec_all__lv = r'进驻宿舍时，该宿舍内所有干员的心情每小时恢复<@cc\.vup>([\+\.0-9]*)<\/>，同时当前宿舍每级为恢复效果额外<@cc\.vup>([\+\.0-9]*)<\/>（叠加后的最终值同种效果取最高）'
                    if re.match(re_dorm_rec_all__lv, desc_sub):
                        desc_match          = re.match(re_dorm_rec_all__lv, desc_sub)
                        match_morale        = desc_match.group(1)
                        match_morale_extra  = desc_match.group(2)
                        return f'When this Operator is assigned to a Dormitory, restores <@cc.vup>{match_morale}</> Morale per hour to all Operators assigned to that Dormitory. Additionally, for every level of the current Dormitory, restores another <@cc.vup>{match_morale_extra}</> (Only the strongest stacked effect of this type takes place)'
                case "hire":
                    # Speed Morale
                    re_hire_spd_cost = r'^进驻人力办公室时，人脉资源的联络速度<@cc\.vup>([\+0-9%]*)<\/>，心情每小时消耗<@cc\.vdown>([\+\-\.[0-9]*)<\/>$'
                    if re.match(re_hire_spd_cost, desc_sub):
                        desc_match          = re.match(re_hire_spd_cost, desc_sub)
                        match_spd           = desc_match.group(1)
                        match_morale        = desc_match.group(2)
                        return f'When this Operator is assigned to the HR Office, HR contacting speed <@cc.vup>{match_spd}</> and Morale consumed per hour <@cc.vdown>{match_morale}</>'
                    # Speed Morale Char
                    re_hire_spd_cost = r'^进驻人力办公室时，人脉资源的联络速度<@cc\.vup>([\+0-9%]*)<\/>，心情每小时消耗<@cc\.(vdown|vup)>([\+\-\.[0-9]*)<\/>，如果<@cc\.kw>(.+?)<\/>进驻在<@cc\.kw>(.+?)<\/>，则人脉资源的联络速度额外<@cc\.vup>([\+0-9%]*)<\/>$'
                    if re.match(re_hire_spd_cost, desc_sub):
                        desc_match          = re.match(re_hire_spd_cost, desc_sub)
                        match_spd_1         = desc_match.group(1)
                        match_morale_desc   = desc_match.group(2)
                        match_morale        = desc_match.group(3)
                        match_op            = riic_match_tl(desc_match.group(4), "op")
                        match_room          = riic_match_tl(desc_match.group(5), "room")
                        match_spd_2         = desc_match.group(6)
                        return f'When this Operator is assigned to the HR Office, HR contacting speed <@cc.vup>{match_spd_1}</> and Morale consumed per hour <@cc.{match_morale_desc}>{match_morale}</>. if <@cc.kw>{match_op}</> is assigned to the <@cc.kw>{match_room}</>, increase contacting speed by an additional <@cc.vup>{match_spd_2}</>'
                case "meet":
                    # Speed by Recruit slot
                    re_meet_spd_clue = r'^进驻会客室时，每个招募位（不包含初始招募位）提升<@cc\.vup>([0-9%]*)<\/>线索搜集速度$'
                    if re.match(re_meet_spd_clue, desc_sub):
                        desc_match          = re.match(re_meet_spd_clue, desc_sub)
                        match_spd           = desc_match.group(1)
                        return f'When this Operator is assigned to the Reception Room, every Recruit slot (Default slots do not count) increases Clue search speed by <@cc.vup>{match_spd}</>'
                    # Speed by op in Dorm ? [meet_spd_ext&P[000]]
                    re_meet_spd_ext_P = r'^进驻会客室时，如果<@cc\.kw>([^<]*)<\/>进驻在宿舍，则线索搜集速度额外提升<@cc\.vup>([0-9%]*)<\/>$'
                    if re.match(re_meet_spd_ext_P, desc_sub):
                        desc_match          = re.match(re_meet_spd_ext_P, desc_sub)
                        match_op            = riic_match_tl(desc_match.group(1), "op")
                        match_spd           = desc_match.group(2)
                        return f'When this Operator is assigned to the Reception Room, if <@cc.kw>{match_op}</> is assigned to a Dormitory, Clue search speed increases by <@cc.vup>{match_spd}</>'
                    # Speed not own when exchange
                    re_meet_spd_notOwned_exchange = r'^进驻会客室时，处于线索交流时更容易获得线索板上尚未拥有的线索$'
                    if re.match(re_meet_spd_notOwned_exchange, desc_sub):
                        return f'When this Operator is assigned to the Reception Room, if in Clue Exchange, increases the likelihood of obtaining clues that are not on the Clue Board'
                    # Speed faction
                    re_meet_spd_sami = r'^进驻会客室时，线索搜集速度提升<@cc\.vup>([\+0-9%]*)<\/>，与其他<\$(cc\.[^>]*)><@cc\.kw>黑钢国际干员<\/><\/>进驻会客室一起工作时，线索搜集速度额外提升<@cc\.vup>([\+0-9%]*)<\/>(，自身心情每小时消耗<@cc\.vdown>([\+\-\.0-9]*)<\/>|)$'
                    if re.match(re_meet_spd_sami, desc_sub):
                        desc_match          = re.match(re_meet_spd_sami, desc_sub)
                        match_spd_1         = desc_match.group(1)
                        match_faction_skill = desc_match.group(2)
                        match_faction_name  = riic_match_tl(match_faction_skill)
                        match_spd_2         = desc_match.group(3)
                        match_morale        = desc_match.group(5) if desc_match.group(4) else ""
                        return f'When this Operator is assigned to the Reception Room, increases Clue search speed by <@cc.vup>{match_spd_1}</>, and when assigned together with another <${match_faction_skill}><@cc.kw>{match_faction_name}</></> Operator, increases Clue search speed by an additional <@cc.vup>{match_spd_2}</>{f' while self Morale loss per hour <@cc.vdown>{match_morale}</>' if match_morale else ""}'
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
                    - **room** -> for RIIC room type
            '''
            # Base skill term (cc)
            if re.match(r'^cc\.([\.\_A-Za-z0-9]*)$', desc):
                return json_term_effect["termDescriptionDict"][desc]["termName"] if desc in json_term_effect["termDescriptionDict"].keys() else desc.split(".")[-1].capitalize()
            else:
                match extra:
                    case "item":
                        mat_tl = {
                                    "任意类材料"    : "any material",
                                    "作战记录"      : "Battle Record",
                                    "贵金属"        : "Precious Metal",
                                    "精英材料"      : "Elite materials",
                                    "芯片"          : "Chips",
                                    "技巧概要"      : "Skill Summaries",
                                    "基建材料"      : "Building material",
                                    
                                    "异铁组"        : "Oriron",
                                    "炽合金块"      : "Incandescent Alloy Block",
                        }
                        if desc in mat_tl:
                            return mat_tl[desc]
                        else:
                            printr(f'riic_match_tl : {Y}"item"{RE} case - {Y}{desc}')
                    case "op":
                        return [json_character[op_key]["appellation"] for op_key in json_character.keys() if desc == json_character[op_key]["name"]][0]
                    case "room":
                        room_tl = {
                                    "控制中枢"  : "Control Center",
                                    "发电站"    : "Power Plant",
                                    "制造站"    : "Factory",
                                    "贸易站"    : "Trading Post",
                                    "宿舍"      : "Dormitory",
                                    "活动室"    : "Activity Room",
                                    "加工站"    : "Workshop",
                                    "办公室"    : "Office",
                                    "训练室"    : "Training Room",
                                    "会客室"    : "Reception Room",
                                    "电梯间"    : "Elevator",
                                    "走廊"      : "Corridor"
                                }
                        if desc in room_tl:
                            return room_tl[desc]
                        else:
                            printr(f'riic_match_tl : {Y}"room"{RE} case - {Y}{desc}')
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
    
    return json_riicTL

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
    script_result(riic_tl_json(), True)
    print(template)
else:
    with open("json/puppiiz/riic_data.json", "w", encoding = "utf-8") as filepath :
        json.dump(riic_tl_json(), filepath, indent = 4, ensure_ascii = False)