from datetime import datetime
import json
import inspect
import os
import subprocess
from typing import Any

R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
B = '\033[34m'
RE = '\033[0m'

URSUS : dict = {
                    "Гум"           : "Gummy",
                    "Зима"          : "Zima",
                    "Истина"        : "Istina",
                    "Позёмка"       : "Pozëmka",
                    "Роса"          : "Rosa",
                    "Лето"          : "Leto",
                    "Снегурочка"    : "Snegurochka",
                    "Веточки"       : "Vetochki"
                }

def printr(*arg):
    print(f'{R}[:{inspect.currentframe().f_back.f_lineno}]{RE}', *arg, RE) # type: ignore

def json_load(filepath : str):
    with open(filepath, 'r', encoding = 'utf-8') as file:
        return json.load(file)

def epoch(time) -> str :
    return f'{TimeFormat(datetime.fromtimestamp(time))} is {time_diff(datetime.fromtimestamp(time))}'

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

def char_ready(char_json : dict , mode : int = 0) -> dict:
    '''
        Get character_table -> Return Code2Name Name2Code dict
        
        Mode 1 : ["Code2Name"]
        Mode 2 : ["Name2Code"]
        Mode 3 : ["Exclude"]
        Default : All
    '''

    Chars : dict[str, Any] = {"Code2Name":{}, "Name2Code":{}}
    for char_key in char_json.keys() :
        if "char_" in char_key :
            Chars["Code2Name"][char_key] = get_char_name(char_json,char_key)
            Chars["Name2Code"][get_char_name(char_json,char_key)] = char_key
    Chars["Exclude"] = [[char_key, get_char_name(char_json, char_key)] for char_key in char_json.keys() if "char_" in char_key and char_json[char_key]["isNotObtainable"]]
    match mode :
        case 1 :
            return Chars["Code2Name"]
        case 2 :
            return Chars["Name2Code"]
        case 3 :
            return Chars["Exclude"] # type: ignore
        case _ :
            return Chars
        
def get_char_name(char_json : dict[str, dict[str, Any]], char_key : str) -> str :
    return name_check(char_json[char_key]["appellation"])

def name_check(appellation : str) -> str :
    return URSUS.get(appellation, appellation)

def print_header(text : str) -> str:
    length : int = 20
    return f'\n{"#" * length * 3}\n{"#" * length}{text:^{length}}{"#" * length}\n{"#" * length * 3}'

def script_result(text : str | list | set | dict , show : bool = False, indent : int | None = 4, sort_keys : bool = False) -> None:
    '''
        Output result
            STR, LIST   >   TXT
            DICT        >   JSON
    '''
    if isinstance(text, str):
        with open("py/script.txt", "w", encoding = "utf-8") as filepath:
            filepath.write(text)
    elif isinstance(text, list) or isinstance(text, set):
        with open("py/script.txt", "w", encoding = "utf-8") as filepath:
            filepath.write("\n".join(text))
    elif isinstance(text, dict) and indent:
        with open("py/script.json", "w", encoding = "utf-8") as filepath:
            json.dump(text, filepath, indent = indent, ensure_ascii = False, sort_keys = sort_keys)
    else:
        with open("py/script.json", "w", encoding = "utf-8") as filepath:
            json.dump(text, filepath, separators = (",", ":"), ensure_ascii = False, sort_keys = sort_keys)
    
    file = f'py/script.{"json" if isinstance(text, dict) else "txt"}'
    print(f'\n{Y}Script Completed{RE} -> {R}{file}{RE}')
    if show:
        subprocess.run(f'code --reuse-window -g "{os.path.abspath(file)}"', shell = True)