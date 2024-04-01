import pandas as pd
import json
from pyfunction import CharReady

########################################################################################################################
# request JSON
########################################################################################################################
path=['zh_CN','en_US']

json_char=json.loads(open('json/gamedata/'+path+'/gamedata/excel/character_table.json').read())
json_charpatch=json.loads(open('json/gamedata/'+path+'/gamedata/excel/char_patch_table').read())

json_char=json.loads(open('json/gamedata/'+path+'/gamedata/excel/battle_equip_table.json').read())

json_char=json.loads(open('json/gamedata/'+path+'/gamedata/excel/battle_equip_table.json').read())


########################################################################################################################
# request JSON
########################################################################################################################

########################################################################################################################
# request JSON
########################################################################################################################