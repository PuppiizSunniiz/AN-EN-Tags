from datetime import datetime
import json

def json_load(filepath) :
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def epoch(time) -> str :
    return TimeFormat(datetime.fromtimestamp(time))+" is "+time_diff(datetime.fromtimestamp(time))

def time_to_str(self) -> str :  # return Date as Y M D H M or S
    if self.days > 365 :
        return str(self.days // 365) + ' Year(s)'
    elif self.days > 31 :
        return str(self.days // 30) + ' Month(s)'
    elif self.days > 0 :
        return str(self.days) + ' Day(s)'
    elif self.seconds > 3600 :
        return str(self.seconds // 3600) + ' Hour(s)'
    elif self.seconds > 60 :
        return str(self.seconds // 60) + ' Minute(s)'
    else :
        return str(self.seconds) + ' Second(s)'

def time_diff(self) -> str :  # Time different Before(ago) or After(in)
    if self < datetime.now() :
        return time_to_str(datetime.now() - self) + ' ago'
    else :
        return 'in ' + time_to_str(self - datetime.now())

def TimeFormat(self) -> str :
    return self.strftime('%d %b %Y %H:%M:%S')

def char_ready(char_json,mode=0) :
    '''
        Get character_table -> Return Code2Name Name2Code dict
        
        Mode 1 : ["Code2Name"]
        Mode 2 : ["Name2Code"]
        Mode 3 : ["Exclude"]
        Default : All
    '''

    Chars = {"Code2Name":{}, "Name2Code":{}}
    for char_key in char_json.keys() :
        if "char_" in char_key :
            Chars["Code2Name"][char_key] = get_char_name(char_json,char_key)
            Chars["Name2Code"][get_char_name(char_json,char_key)] = char_key
    Chars["Exclude"] = [[char_key,get_char_name(char_json,char_key)] for char_key in char_json.keys() if "char_" in char_key and char_json[char_key]["isNotObtainable"]]
    match mode :
        case 1 :
            return Chars["Code2Name"]
        case 2 :
            return Chars["Name2Code"]
        case 3 :
            return Chars["Exclude"]
        case _ :
            return Chars
        
def get_char_name(char_json,char_key) -> str :
    return name_check(char_json[char_key]["appellation"])

def name_check(appellation) -> str :
    Russian = {
                'Гум'       : 'Gummy',
                'Зима'      : 'Zima',
                'Истина'    : 'Istina',
                'Позёмка'   : 'Pozëmka',
                'Роса'      : 'Rosa',
                'Лето'      : 'Leto'
            }
    return Russian.get(appellation,appellation)

def print_header(text) :
    length = 20
    return f'\n{"#"*length*3}\n{"#"*length}{text:^{length}}{"#"*length}\n{"#"*length*3}'

#print_header("Error Test")
#print_header("Data Test")