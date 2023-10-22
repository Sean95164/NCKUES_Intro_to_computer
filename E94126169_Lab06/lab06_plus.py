"""
遞迴+窮舉，暴力樹狀展開所有解
By the way: 好像寫太複雜了@@
"""
# ans list 用來儲存答案
ans = []
# input 一個要排列的陣列
input_string = input("輸入一個字串：")
# 開一個 used 陣列紀錄原本的 string 哪些位置使用過
used = [0 for i in range(len(input_string))]


# 定義一個函數求排列，參數為一個原本的 string 和 後來要生成排列的 string
def function(raw_string, temp_string):
    # use to debug ===================================
    # print(temp_string,used.count(1))
    # ================================================

    # 終止條件：當原本的陣列每個元素都被使用時，結束遞迴並儲存答案
    if used.count(1) == len(raw_string):
        ans.append(temp_string)
        return

    # 嘗試每一種未被嘗試的可能
    for i in range(len(raw_string)):
        # 如果沒有用過的話就選擇
        if used[i] == 0:
            # 將當前使用的元素設成"已使用"
            used[i] = 1

            # 加入 temp_string 中
            temp_string += raw_string[i]

            # 遞迴嘗試其他可能
            function(raw_string, temp_string)

            # 將目前使用過的元素設成未使用，給前一個元素使用
            used[i] = 0

            # 退回前一個可能性
            temp_string = temp_string[0 : len(temp_string) - 1]


function(input_string, "")
print(ans)
