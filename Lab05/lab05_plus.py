# 建立一個空的字典
dict0 = {}

# 輸入資料並儲存至dict
for i in range(4):
    key = input("Enter Keys: ")
    print(f"Enter Keys: {key}")
    # 將輸入的 values 以逗號做分割，並以 list 做儲存
    values = list(input("Enter values: ").split(","))
    print(f"Enter values: {values}")
    # 將 key-value pair 放入 dict 中
    dict0[key] = values
    
# 用 f-string 輸出字典的內容
print(f"dict0 = {dict0}")
