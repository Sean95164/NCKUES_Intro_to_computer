dict0 = {
    "index":["國文","英文","數學","自然","社會"],
    "StuA":[50, 60, 70, 80, 90],
    "StuB":[57, 86, 73, 82, 43],
    "StuC":[97, 96, 86, 97, 83]
}
# 輸出字典 dict0
print(dict0)

#使用 f-string 分別印出 A,B,C 學生的平均成績
print(f"A學生平均成績：{sum(dict0['StuA'])/len(dict0['StuA'])}")
print(f"B學生平均成績：{sum(dict0['StuB'])/len(dict0['StuB'])}")
print(f"C學生平均成績：{sum(dict0['StuC'])/len(dict0['StuC'])}")
print()

#使用 for loop 分別計算各科成績
for i in range(len(dict0["index"])):
    # 將要計算的科目成績放入 score 中
    score = []
    score.append(dict0["StuA"][i])
    score.append(dict0["StuB"][i])
    score.append(dict0["StuC"][i])
    
    #在 f-string 中計算平均並且印出答案
    print(f"{dict0['index'][i]}平均成績：{sum(score)/len(score)}")
    
    