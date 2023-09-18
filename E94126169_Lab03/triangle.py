a = int(input("請輸入第一個邊長："))
b = int(input("請輸入第二個邊長："))
c = int(input("請輸入第三個邊長："))

print(f"請輸入第一個邊長：{a}")
print(f"請輸入第一個邊長：{b}")
print(f"請輸入第一個邊長：{c}")

if(a+b>c and a+c>b and b+c>a):
    if(a == b == c):
        print("這是一個正三角形")
    else:
        print("這是一個一般三角形")
else:
    print("這三個邊長不能構成合法的三角形")