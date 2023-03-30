import requests as req
import json
from datetime import datetime
import os
import csv
import pandas as pd

url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-A0021-001?Authorization=CWB-EEAE175C-976B-4CB3-BF1F-C3091DB5D2C2&downloadType=WEB&format=JSON'

# 設定相對路徑
# dir_path = './data_record/json'
csv_path = './data_record/csv'

# 取得當前目錄
current_path = os.getcwd()

# 目標資料夾路徑
target_path = os.path.join(
    current_path, 'python_tide', 'success', 'data_record', 'json')

# 如果沒有資料夾，則建立
if not os.path.exists(target_path):
    # os.makedirs(dir_path, exist_ok=True)
    os.makedirs(csv_path, exist_ok=True)

# time
now_str = datetime.now().strftime("%Y-%m-%d %H(%I)%M%S")

# get方法抓
res = req.get(url)

# 建json資料、匯出json
# with open(f'{dir_path}/{now_str}-origin-source.json', 'w', encoding='utf-8') as f:
#     f.write(res.text)
#     f.close()

info = json.loads(res.text)

# 將JSON資料轉換為DataFrame物件
df = pd.json_normalize(info, ['cwbopendata', 'dataset', 'location'], [
                       'cwbopendata.identifier', 'cwbopendata.sent'], errors='ignore')

# 取得"locationName"、"latitude"和"longitude"的值、顯示結果
# print(df['locationName'])
# print(df['latitude'])
# print(df['longitude'])

# 建立csv欄位
dfAll = {
    'locationName': df['locationName'],
    'latitude': df['latitude'],
    'longitude': df['longitude'],
}


# 將資料匯出為CSV檔案
dfA = pd.DataFrame(dfAll)
dfA.to_csv(
    f'{csv_path}/{now_str}-resule.csv', encoding='utf-8-sig', index=False)
