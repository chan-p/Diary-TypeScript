# coding: utf-8
if __name__=='__main__':
    from google.cloud import datastore
    import json
    import os

    credentials_json = './key.json'  # BigQuery設定時の鍵へのパス
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_json
    project_id = "idap-gcp-dev"

    # クライアントの設定
    client = datastore.Client(project=project_id, namespace="Diary")

    with open("input.csv") as f:
        for line in f:
            info = line[:-1].split(',')
            print(info)
            # kindにエンティティ種類名を指定
            key = client.key("day_info", int(info[1]))
            entity = client.get(key)
            entity[info[2]] = str(info[3])
            print(entity)
            client.put(entity)

