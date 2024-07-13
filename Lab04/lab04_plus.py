nums_list = []
nums_string = input("輸入的list為:") #例如:輸入[3, 2, 2, 3, 6, 5, 4, 3, 2, 1]
del_num = int(input("要刪除的數字是:"))
print(f"輸入的list為:{nums_string}, 要刪除的數字是:{del_num}")

for i in nums_string[1:len(nums_string)-1].split(","):
    if(i!=""):
        nums_list.append(int(i))
    
print()
print("刪除後!")
print()

while(nums_list.count(del_num)):
    nums_list.remove(del_num)
        
print(f"list長度剩下:{len(nums_list)}, list變成:{nums_list}")
