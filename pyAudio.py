import json
import re
from pyfunction import printr, script_result, json_load, R, G, B, Y, RE

def audio_json(show : bool = False):
    def charWords_trim(charWords : dict) -> dict:
        charWords = dict(charWords)
        trimming = ["charWordId", "voiceIndex", "voiceType", "unlockType", "unlockParam", "lockDescription", "placeType"]
        for key in trimming:
            charWords.pop(key)
        return charWords
    
    def voiceLangDict_trim(voiceLangDict : dict) -> tuple[dict, str]:
        temp_voiceLangDict : dict = {}
        temp_LINKAGE : str = ""
        for lang in voiceLangDict.keys():
            cvName = " & ".join([cv.strip() for cv in voiceLangDict[lang]["cvName"]])
            temp_voiceLangDict[lang] = json_tl_artist["VA"].get(cvName, cvName)
            if lang == "LINKAGE":
                temp_LINKAGE = voiceLangDict[lang]["voicePath"].split("/")[2]
        return temp_voiceLangDict, temp_LINKAGE
            
    json_charWords      =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/charword_table.json")
    json_charWordsEN    =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/charword_table.json")
    
    json_tl_artist      =   json_load("json/tl-artist.json")
    
    json_birthday       =   json_load(r"temp\birthday_voicelines.json") if birthday_manual else {}
    
    json_audio = {"charWords" : {}, "voiceLangDict" : {}}
    skin_word = []
    audio_wordkey = []
    linkage_folder = {}
    birthday_dict = {"EN" : [], "KR" : []}
    json_test = []
    Xiaohei_string = r'(char_4067_lolxh)(_CN_[\d]{3})'
    
    # charWords
    for key in json_charWords["charWords"].keys():
        if not re.match(r'char_[\d]*_[a-z\d]*(\#1|)_(?:[a-z\d]*\#[\d]*_|)CN_[\d]{3}', key):
            continue
        if key in json_charWordsEN["charWords"].keys():
            json_audio["charWords"][key] = charWords_trim(json_charWordsEN["charWords"][key])
            # Dupe Xiaohei build voiceline
            if re.match(Xiaohei_string, key) and 19 < json_charWordsEN["charWords"][key]["voiceIndex"] < 29:
                Xiaohei_newkey  = re.sub(Xiaohei_string, r'\1#1\2', key)
                json_audio["charWords"][Xiaohei_newkey] = charWords_trim(json_charWordsEN["charWords"][key])
                json_audio["charWords"][Xiaohei_newkey]["wordKey"] = json_audio["charWords"][Xiaohei_newkey]["wordKey"].replace("char_4067_lolxh", "char_4067_lolxh#1")
                json_audio["charWords"][Xiaohei_newkey]["voiceAsset"] = json_audio["charWords"][Xiaohei_newkey]["voiceAsset"].replace("char_4067_lolxh", "char_4067_lolxh#1")
        else :
            json_audio["charWords"][key] = charWords_trim(json_charWords["charWords"][key])
        
        wordKey = json_charWords["charWords"][key]["wordKey"]
        if wordKey not in audio_wordkey:
            audio_wordkey.append(wordKey)
        
        # skinWords
        if re.match(r'char_[\d]*_[a-z\d]*_(?:[a-z\d]*\#[\d]*_)CN_[\d]{3}', key):
            skin_word.append(json_charWords["charWords"][key]["wordKey"])
    
    # voiceLangDict
    for char in json_charWords["voiceLangDict"].keys():
        if char not in audio_wordkey:
            continue
        char_voice = json_charWords["voiceLangDict"][char]
        
        if char in json_charWordsEN["voiceLangDict"].keys():
            char_voice["dict"].update(json_charWordsEN["voiceLangDict"][char]["dict"])
        
        json_audio["voiceLangDict"][char], linkage = voiceLangDict_trim(char_voice["dict"])

        # LINKAGE
        if linkage:
            linkage_folder[char] = linkage
        
        # Birthday
        for global_lang in ["EN", "KR"]:
            if global_lang in json_charWords["voiceLangDict"][char]["dict"]:
                birthday_dict[global_lang].append(char)

    json_audio["charWords"] = {k:json_audio["charWords"][k] for k in sorted(json_audio["charWords"].keys())}
    json_audio["skinWords"] = sorted(list(set(skin_word)))
    json_audio["LINKAGE"] = linkage_folder
    json_audio["Birthday"] = json_birthday if birthday_manual else birthday_dict
    return json_audio

birthday_manual = True

if __name__ == "__main__":
    script_result(audio_json(), True)
else:
    with open("json/puppiiz/charword_table.json", "w", encoding = "utf-8") as filepath :
        json.dump(audio_json(), filepath, indent = None, ensure_ascii = False)