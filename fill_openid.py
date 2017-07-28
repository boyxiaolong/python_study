# -*- coding: utf-8 -*-
import pandas as pd
filename = 'id_for_vote.csv'
encoding = "GB2312"
col_name = "id"

json_file_name = "OpenIdToPlayerIdMap.json"
mongo_bson = pd.read_json(json_file_name, lines=True)

id_map = {}

class Info:
    openId = ""
    playerName = ""

    def __init__(self, id, name):
        self.openId = id
        self.playerName = name

for index, row in mongo_bson.iterrows():
    playerId = row["playerId"]
    playerName = row["playerName"]
    openId = row["_id"]
    id_map[playerId] = Info(openId, playerName)

del mongo_bson

id_csv = pd.read_csv(filename, encoding="utf-8")
for index, row in id_csv.iterrows():
    playerId = row["id"]
    if playerId in id_map:
        info = id_map[playerId]
        id_csv.loc[index, "openid"] = info.openId
        id_csv.loc[index, "name"] = info.playerName
        print(row)

id_csv.to_csv("test.csv")
