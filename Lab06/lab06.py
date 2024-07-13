# 求 GCD 使用輾轉相除法
def gcd(a, b):
    # b==0 時，直接 return 0
    if b == 0:
        return 0
    # 當 a mod b == 0 ，表示找到最大公因數 b
    if a % b == 0:
        return b
    # resursion 反覆呼叫 gcd，每次將 b 代入新的 a，a%b 代入新的 b
    return gcd(b, a % b)


# 儲存答案
ans1 = gcd(80, 20)
ans2 = gcd(10, 0)
ans3 = gcd(19, 20)

# 輸出
print(f"80 和 20 的gcd= {ans1}")
print(f"{ans2} 沒有gcd")
if ans3 == 1:
    print("19 和 20 互質")
