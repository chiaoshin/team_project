import requests as req
import json
from datetime import datetime
import os

url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-A0021-001?Authorization=CWB-EEAE175C-976B-4CB3-BF1F-C3091DB5D2C2&downloadType=WEB&format=JSON'

# 設定相對路徑
dir_path = './success/data_record/json'

# 取得當前目錄
current_path = os.getcwd()

# 目標資料夾路徑
target_path = os.path.join(
    current_path, 'python_tide', 'success', 'data_record', 'json')

# 如果沒有資料夾，則建立
if not os.path.exists(target_path):
    os.makedirs(dir_path, exist_ok=True)

# time
now_str = datetime.now().strftime("%Y-%m-%d %H(%I)%M%S")

# get方法抓
res = req.get(url)

# 建json資料
with open(f'{dir_path}/{now_str}-origin-source.json', 'w', encoding='utf-8') as f:
    f.write(res.text)
    f.close()
