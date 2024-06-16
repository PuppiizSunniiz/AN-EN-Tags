import json
from pyfunction import epoch

#########################################################################################################
# JSON
#########################################################################################################
json_char       =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/character_table.json").read())
json_char_patch =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/char_patch_table.json").read())
json_mod        =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/uniequip_table.json").read())
json_range      =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/range_table.json").read())

#########################################################################################################
# Function
#########################################################################################################
def msgbox(self) -> str:
    if isinstance(self,str):
        repeat=len(self)+8
        return "#"*repeat+"\n#   "+self+"   #\n"+"#"*repeat
    elif isinstance(self,list):
        repeat=max(map(lambda x: len(x),self))+15
        return "#"*repeat+("\n#    ").join(self)+"\n"+"#"*repeat

def Continue() -> bool:
    print(msgbox("Continue ? (Y/N)"))
    con=input()
    match con.lower():
        case "n":
            return False
        case "y":
            return True
        case default:
            return Continue()

def Charname(self) -> str:
    '''
        Get self as Char key
        Check if appellation in Russian
        Return as Eng name
        
        # Russian = {'Гум': 'Gummy', 'Зима': 'Zima', 'Истина': 'Istina', 'Позёмка': 'Pozëmka', 'Роса': 'Rosa'}
        
        return NameCheck(json_char[self]["appellation"])
    '''
    def NameCheck(self):
        Russian = {'Гум': 'Gummy', 'Зима': 'Zima', 'Истина': 'Istina', 'Позёмка': 'Pozëmka', 'Роса': 'Rosa','Лето':'Leto'}
        if self in Russian.keys():
            return Russian[self]
        else:
            return self
        
    return NameCheck(json_char[self]["appellation"])

def Charcheck():
    def Charout(text,mode):
        print(msgbox("What "+text+" to check ?"))
        charin=input()
        
        chars=[]
        for key in DB["Char"][mode].keys():
            if charin.lower() in key.lower():
                chars.append([key,DB["Char"][mode][key]])
        if len(chars):
            print("Result :")
            for x in range(len(chars)):
                print(chars[x])
            print("Search result :",len(chars))
        else:
            print(f"No Char Code with \"{charin}\" exist")
        
    print(msgbox(["\n#  Select Mode",
          "1 : Char Name from Char Code",
          "2 : Char Code from Char Name",
          "0 : Exit"
          ]))
    char=input()
    match char:
        case "0":
            return False
        case "1":
            Charout("Char Code","Code2Name")
        case "2":
            Charout("Char Name","Name2Code")
        case default:
            Charcheck()
        
    return Continue()

def Modcheck():
    print(msgbox("What Module Num to check ? (1/2/3 or 0 : Exit)" ))
    modnum=int(input())
    
    if modnum =="0":
        return False
    elif modnum not in [1,2,3]:
        Modcheck()
    
    mod=[]
    for key in json_mod["charEquip"].keys():
        if len(json_mod["charEquip"][key])>modnum:
            mod.append(Charname(key)+" -- "+key)
    sorted(mod)
    mod.append("Search result :"+str(len(mod)))
    print("\n".join(mod))
    return Continue()

def Rangecheck():
    print(msgbox("What Range to check ? (S: Show All Range | 0 : Exit)" ))
    rangeid=input()
    
    if rangeid == "0":
        return False
    elif rangeid.lower() == "s":
        print(list(DB["Range"].keys()))
        return True
    elif rangeid.lower() not in DB["Range"].keys():
        print(rangeid,"is not Range ID")
        return Continue()
    else :
        print("\n".join(DB["Range"][rangeid]))
        return Continue()
    
def Timecheck():
    print(msgbox("What Epoch time to check ? (0 : Exit)" ))
    time=int(input())
    
    if time == "0":
        return False
    else :
        print("\nEpoch ",time," = ",epoch(time))
        return Continue()

'''
    def Tagcheck():
        print(msgbox("What Tag(s) to check ? (up to 5 tags | 0 : Exit)"))
        tags=input()
    
        if tags=="0":
            return False
        else :
            tagscheck(tags)
    
        def tagscheck(tags):
            tags = tags.split(" ")
            for i in range(len(tags)):
                match tags[i]:
					case "guard":
					    tags[i] = 近卫干员		#Guard
					case "sni":
					    tags[i] = 狙击干员		#Sniper
					case "defender":
					    tags[i] = 重装干员		#Defender
					case "medic":
					    tags[i] = 医疗干员		#Medic
					case "sup":
					    tags[i] = 辅助干员		#Supporter
					case "caster":
					    tags[i] = 术师干员		#Caster
					case "spec":
					    tags[i] = 特种干员		#Specialist
					case "van":
					    tags[i] = 先锋干员		#Vanguard
					case "melee":
					    tags[i] = 近战位		#Melee
					case "range":
					    tags[i] = 远程位		#Ranged
					case "top":
					    tags[i] = 高级资深干员	#Top Operator
					case "cc":
					    tags[i] = 控场			#Crowd-Control
					case "nuker":
					    tags[i] = 爆发			#Nuker
					case "senior":
					    tags[i] = 资深干员		#Senior Operator
					case "heal":
					    tags[i] = 治疗			#Healing
					case "support":
					    tags[i] = 支援			#Support
					case "starter":
					    tags[i] = 新手			#Starter
					case "dp":
					    tags[i] = 费用回复		#DP-Recovery
					case "dps":
					    tags[i] = 输出			#DPS
					case "survival":
					    tags[i] = 生存			#Survival
					case "aoe":
					    tags[i] = 群攻			#AoE
					case "defense":
					    tags[i] = 防护			#Defense
					case "slow":
					    tags[i] = 减速			#Slow
					case "debuff":
					    tags[i] = 削弱			#Debuff
					case "frd":
					    tags[i] = 快速复活		#Fast-Redeploy
					case "shift":
					    tags[i] = 位移			#Shift
					case "summon":
					    tags[i] = 召唤			#Summon
					case "robot":
					    tags[i] = 支援机械		#Robot
					case "male":
					    tags[i] = 男性干员		#Male
					case "female":
					    tags[i] = 女性干员		#Female
            recruitment()
'''
#########################################################################################################
# Ready
#########################################################################################################
DB={}

ClassParse = {"MEDIC": "Medic", "WARRIOR": "Guard", "SPECIAL": "Specialist", "SNIPER": "Sniper",
              "PIONEER": "Vanguard", "CASTER": "Caster", "SUPPORT": "Supporter", "TANK": "Defender"}
for char in json_char_patch["patchChars"].keys():
    json_char_patch["patchChars"][char]["appellation"]=json_char_patch["patchChars"][char]["appellation"]+" ("+ClassParse[json_char_patch["patchChars"][char]["profession"]]+")"
json_char.update(json_char_patch["patchChars"])

CharReady={"Code2Name":{},"Name2Code":{}}
OpsExclude=[] # "isNotObtainable": true
for key in json_char.keys():
    if "char_" in key:
        CharReady["Code2Name"][key]=Charname(key)
        CharReady["Name2Code"][Charname(key)]=key
        if json_char[key]["isNotObtainable"]:
            OpsExclude.append(key)
DB["Char"]=CharReady

RangeReady={} # 🟥🟧🟨🟩🟦🟪🟫⬛⬜🔳
for rangeid in json_range.keys():
    temp =[]
    for grid in json_range[rangeid]["grids"]:
        temp.append([grid["col"],grid["row"]])
    
    maxX=max([x[0] for x in temp])
    minX=min([x[0] for x in temp]+[0])
    maxY=max([y[1] for y in temp])
    minY=min([y[1] for y in temp]+[0])
    
    rangearray=[["⬛" for x in range(maxX-minX+1)] for y in range(maxY-minY+1)]
    
    rangearray[maxY][abs(min(0,minX))]="🔳"

    for userange in temp:
        if userange == [0,0]:
            rangearray[userange[1]+maxY][userange[0]+abs(min(0,minX))]="🟨"
        else:
            rangearray[userange[1]+maxY][userange[0]+abs(min(0,minX))]="🟦"
    
    for i in range(len(rangearray)):
        rangearray[i]=("").join(rangearray[i])
    
    rangearray.append(str(temp))
    RangeReady[rangeid]=rangearray
DB["Range"]=RangeReady

TagReady={}
for char in CharReady["Code2Name"].keys():
    TagReady[CharReady["Code2Name"][char]]=["高级资深干员" for x in range(1) if json_char[char]["rarity"][-1]=="6"]+ \
                                            ["资深干员" for x in range(1) if json_char[char]["rarity"][-1]=="5"]+ \
                                            ["新手" for x in range(1) if json_char[char]["rarity"][-1]=="2"]+ \
                                            ["近战位" for x in range(1) if json_char[char]["position"]=="MELEE"]+ \
                                            ["远程位" for x in range(1) if json_char[char]["position"]=="RANGED"]+ \
                                            json_char[char]["tagList"]
DB["Tag"]=TagReady
jsonout=json.dumps(DB,indent=4, ensure_ascii=False)
with open('py/dict.json','w') as JSON:
    JSON.write(jsonout)

TagReady={}

'''
    json_gacha  =   json.loads(open("json/gamedata/zh_CN/gamedata/excel/gacha_table.json").read())
    json_gachaEN  =   json.loads(open("json/gamedata/en_US/gamedata/excel/gacha_table.json").read())
    gachapon={}
    for tag in json_gacha["gachaTags"]:
        gachapon[tag["tagId"]]={"tagName":tag["tagName"]}
    for tag in json_gachaEN["gachaTags"]:
        gachapon[tag["tagId"]].update({"EN":tag["tagName"]})
    gacha=json.dumps(gachapon,indent=4, ensure_ascii=False)
    with open('temp/tag.json','w') as JSON:
        JSON.write(gacha)
        
    tagstr=[]
    for key in gachapon.keys():
        tagstr.append("\t"*5+"case \""+gachapon[key]["EN"].lower()+"\":\n"+"\t"*6+"tags[i] = "+gachapon[key]["tagName"]+"\t"*round(4-len(gachapon[key]["tagName"])/2)+"#"+gachapon[key]["EN"])
    gachastr=("\n").join(tagstr)
    with open('temp/tag.txt','w') as JSON:
        JSON.write(gachastr)
'''

#########################################################################################################
# Go !!!
#########################################################################################################
while(True):
    #repeat=49
    Boolcheck=True
    text=["\n#  Select Function",
          "1 : Char Name/Code Check",
          "M : Mod Check",
          "R : Range Check",
          "T : Time Epoch",
          "0 : Exit"
          ]
    print(msgbox(text))
    exe=input()
    match exe.lower():
        case "0":
            break
        case "1":
            while(Boolcheck):
                Boolcheck=Charcheck()
        case "m":
            while(Boolcheck):
                Boolcheck=Modcheck()
        case "r":
            while(Boolcheck):
                Boolcheck=Rangecheck()
        case "t":
            while(Boolcheck):
                Boolcheck=Timecheck()
        case default:
            pass