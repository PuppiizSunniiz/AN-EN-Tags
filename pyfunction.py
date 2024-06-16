from datetime import datetime

def epoch(time) -> str:
    def TimeReturn(self):  # return Date as Y M D H M or S
        if self.days > 365:
            return str(self.days // 365) + ' Year(s)'
        elif self.days > 31:
            return str(self.days // 30) + ' Month(s)'
        elif self.days > 0:
            return str(self.days) + ' Day(s)'
        elif self.seconds > 3600:
            return str(self.seconds // 3600) + ' Hour(s)'
        elif self.seconds > 60:
            return str(self.seconds // 60) + ' Minute(s)'
        else:
            return str(self.seconds) + ' Second(s)'

    def TimeDiff(self):  # Time different Before(ago) or After(in)
        if self < datetime.now():
            return TimeReturn(datetime.now() - self) + ' ago'
        else:
            return 'in ' + TimeReturn(self - datetime.now())

    def TimeFormat(self):
        return self.strftime('%d %b %Y %H:%M:%S')

    return TimeFormat(datetime.fromtimestamp(time))+" is "+TimeDiff(datetime.fromtimestamp(time))

def CharReady(JSON,mode=0):
    '''
        Get character_table -> Return Code2Name Name2Code dict
        
        Mode 1 : ["Code2Name"]
        Mode 2 : ["Name2Code"]
        Mode 3 : ["Exclude"]
        Default : All
    '''

    Chars={"Code2Name":{},"Name2Code":{}}
    OpsExclude=[] # "isNotObtainable": true
    for key in JSON.keys():
        if "char_" in key:
            Chars["Code2Name"][key]=Charname(JSON,key)
            Chars["Name2Code"][Charname(JSON,key)]=key
            if JSON[key]["isNotObtainable"]:
                OpsExclude.append([key,Charname(JSON,key)])
    Chars["Exclude"]=OpsExclude
    match mode :
        case 1 :
            return Chars["Code2Name"]
        case 2 :
            return Chars["Name2Code"]
        case 3 :
            return Chars["Exclude"]
        case _ :
            return Chars
        
def Charname(JSON,key) -> str:
    return NameCheck(JSON[key]["appellation"])

def NameCheck(appellation) -> str:
    Russian = {'Гум': 'Gummy', 'Зима': 'Zima', 'Истина': 'Istina', 'Позёмка': 'Pozëmka', 'Роса': 'Rosa','Лето':'Leto'}
    if appellation in Russian.keys():
        return Russian[appellation]
    else:
        return appellation