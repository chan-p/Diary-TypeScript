# coding: utf-8
from google.cloud import datastore
import os
import subprocess as sb

credentials_json = './key.json'  # BigQuery設定時の鍵へのパス
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_json
project_id = "idap-gcp-dev"

# クライアントの設定
client = datastore.Client(project=project_id, namespace="Diary")

def rest(string):
    return "'{}'".format(string)

query = client.query(kind="day_info")

for i in range(1, 32):
    query = client.query(kind="day_info")
    query.add_filter("date", "=", "12月{}日".format(i))
    res = list(query.fetch())
    if len(res) == 0:
        continue
    else:
        res = res[0]
        print(res)
        cmd = 'bq query --nouse_legacy_sql "insert into hayashi_private.daily_info values ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})"'.format(rest(res["date"].encode("utf-8")), rest(res["detail"].encode("utf-8")), rest(res["shokuji"].encode("utf-8")), rest(res["sick"].encode("utf-8")), rest(res["status"].encode("utf-8")), rest(str(res["taion_select"]).encode("utf-8")), rest(res["text"].encode("utf-8").replace("\'", "\"")).replace("\n", ","), rest(res["toilet"].encode("utf-8")), int(res["hour"]), rest(res["date_"]))
        sb.check_output(cmd, shell=True)
