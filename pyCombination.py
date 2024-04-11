import json

###
# json
###

Server = "zh_CN" # "zh_CN" / "en_US"

jsonlist = json.loads(open("json/gamedata/"+Server+"/gamedata/excel/activity_table.json").read())

formulas = jsonlist["activity"]["TYPE_ACT29SIDE"]["act29side"]["formDataMap"]
'''
    notes = jsonlist["activity"]["TYPE_ACT29SIDE"]["act29side"]["fragDataMap"]

    parse = {}
    for note in notes.keys():
        parse[note]=notes[note]["fragName"]

    mood={"乐":"Happy","怒":"Fury","哀":"Sorrow","惧":"Fear"}

    color={"乐":"🟨","怒":"🟥","哀":"🟦","惧":"🟩"}

    #for i in formulas.keys():
        #print(formulas[i]["formDesc"],[parse[x] for x in formulas[i]["fragIdList"]])
        #print([mood[parse[x]] for x in formulas[i]["fragIdList"]])
        #print(formulas[i]["formDesc"],[parse[x] for x in formulas[i]["fragIdList"]],"".join([color[parse[x]] for x in formulas[i]["fragIdList"]]))
'''    
groups= jsonlist["activity"]["TYPE_ACT29SIDE"]["act29side"]["productGroupDataMap"]

colors={"act29side_frag_1":"🟨","act29side_frag_2":"🟥","act29side_frag_3":"🟦","act29side_frag_4":"🟩"}

print('tone\tmood\tformula')

for group in groups.keys():
    for formula in groups[group]["formList"]:
        print (groups[group]["groupSmallName"],'\t',formulas[formula]["formDesc"],("").join([colors[x] for x in formulas[formula]["fragIdList"]]))
    print("\n")