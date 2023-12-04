# 111年臺南市查獲擴大營業遭裁罰之旅宿業名單
# https://data.gov.tw/dataset/161399

import pymysql.cursors
import requests
import json

# 取得 html 上的資料
test = requests.get("https://soa.tainan.gov.tw/Api/Service/Get/2188d74d-b8ec-41ab-a685-dbd174dac870")

# 讀取 json 格式的文字
r = json.loads(test.text)

# 取得字典的 "data" 欄位
data = r["data"]

try:
    # 輸入連結資料庫的相關資料
    connection = pymysql.connect(host='localhost', user='e94126169', password='0000', database='wordpress', cursorclass=pymysql.cursors.DictCursor)
    print("連線成功")
except Exception as err:
    print(err)


with connection:
    with connection.cursor() as cursor:
        # 將資料插入 SQL 的對應資料庫和欄位
        sql = "INSERT INTO `臺南市查獲擴大營業遭裁罰之旅宿業名單` (`序號`, `裁處對象`, `地址`, `樣態`, `法條`) VALUES (%s, %s, %s, %s, %s)"

        for i in range( len(data) ):
            # 執行 SQL 語法, 插入資料到資料庫
            cursor.execute(sql, (data[i]['序號'],data[i]['裁處對象'],data[i]['地址'],data[i]['樣態'],data[i]['法條']))
    connection.commit()
    cursor.close()
