import json
import re
from pyfunction import printr, script_result, json_load, R, G, B, Y, RE

def audio_json(show : bool = False):
    def charWords_trim(charWords : dict) -> dict:
        trimming = ["charWordId", "voiceIndex", "voiceType", "unlockType", "unlockParam", "lockDescription", "placeType"]
        for key in trimming:
            charWords.pop(key)
        return charWords
    
    def voiceLangDict_trim(voiceLangDict : dict) -> tuple[dict, str]:
        temp_voiceLangDict : dict = {}
        temp_LINKAGE : str = ""
        for lang in voiceLangDict.keys():
            cvName = voiceLangDict[lang]["cvName"][0]
            temp_voiceLangDict[lang] = json_tl_artist["VA"].get(cvName, cvName)
            if lang == "LINKAGE":
                temp_LINKAGE = voiceLangDict[lang]["voicePath"].split("/")[2]
        return temp_voiceLangDict, temp_LINKAGE
            
    json_charWords      =   json_load("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/charword_table.json")
    json_charWordsEN    =   json_load("json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/charword_table.json")
    
    json_tl_artist      =   json_load("json/tl-artist.json")
    
    json_audio = {"charWords" : {}, "voiceLangDict" : {}}
    skin_word = []
    audio_wordkey = []
    linkage_folder = {}
    json_test = []
    
    # charWords
    for key in json_charWords["charWords"].keys():
        if not re.match(r'char_[\d]*_[a-z]*(?:[\d]|)_(?:[a-z]*\#[\d]*_|)CN_[\d]{3}', key):
            continue
        elif key in json_charWordsEN["charWords"].keys():
            json_audio["charWords"][key] = charWords_trim(json_charWordsEN["charWords"][key])
        else :
            json_audio["charWords"][key] = charWords_trim(json_charWords["charWords"][key])
        
        wordKey = json_charWords["charWords"][key]["wordKey"]
        if wordKey not in audio_wordkey:
            audio_wordkey.append(wordKey)
        
        if re.match(r'char_[\d]*_[a-z]*(?:[\d]|)_(?:[a-z]*\#[\d]*_)CN_[\d]{3}', key):
            skin_word.append(json_charWords["charWords"][key]["wordKey"])
    
    # voiceLangDict
    for char in json_charWords["voiceLangDict"].keys():
        if char not in audio_wordkey:
            continue
        char_voice = json_charWords["voiceLangDict"][char]
        
        if char in json_charWordsEN["voiceLangDict"].keys():
            char_voice["dict"].update(json_charWordsEN["voiceLangDict"][char]["dict"])
        
        json_audio["voiceLangDict"][char], linkage = voiceLangDict_trim(char_voice["dict"])

        if linkage:
            linkage_folder[char] = linkage
            
    json_audio["skinWords"] = sorted(list(set(skin_word)))
    json_audio["LINKAGE"] = linkage_folder
    
    return json_audio

if __name__ == "__main__":
    script_result(audio_json(), True)
else:
    with open("json/puppiiz/charword_table.json", "w", encoding = "utf-8") as filepath :
        json.dump(audio_json(), filepath, indent = None, ensure_ascii = False)