nums_1 = []
nums_2 = []
nums_string = input("輸入的list為:") #例如:輸入[3, 2, 2, 3, 6, 5, 4, 3, 2, 1]
del_num = int(input("要刪除的數字是:"))
print(f"輸入的list為:{nums_string}, 要刪除的數字是:{del_num}")

for i in nums_string[1:len(nums_string)-1].split(","):
    nums_1.append(int(i))

print()
print("刪除後!")
print()

for i in nums_1:
    if(i!=del_num):
        nums_2.append(i)
        
print(f"list長度剩下:{len(nums_2)}, list變成:{nums_2}")