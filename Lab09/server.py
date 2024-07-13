import socket

def fibonacci(n):
    n = int(n)
    nums = [0,1]
    if n != 0 or n != 1:
        # 增加 array 長度直到目標數字
        for i in range(2,n+1):
            nums.append(nums[i-2]+nums[i-1])
    else:
        #若為 0 or 1 直接回傳
        return nums[n]

    return str(nums[n])

def setup_socket(HOST, PORT):

    # 設定 socket 協定
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 將通道重製
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 設定 Server 的連結 ip 和 port
    s.bind((HOST, PORT))

    # 設定最多連接的 client 數量
    s.listen(3)
    return s

def run_server(s):

    while True:
        print("Waiting for connection...")

        # 等待直到 client 連接
        conn, addr = s.accept()
        print(f"Add connection from {conn.getpeername()}")

        while True:

            # 從 client 接收資料
            receive = conn.recv(1024)

            # 若 client 沒有傳送資料 表示 client 關閉連線
            if len(receive) == 0:
                conn.close()
                print("connection closed")
                break

            print(f"Received from {conn.getpeername()}: {receive.decode()}")

            # client 輸入 exit 結束連線
            if receive.decode() == "exit":
                conn.close()
                print("connection closed")
                break

            print(f"Send to {conn.getpeername()}: {fibonacci(receive.decode())}")

            # server 回傳答案給 client
            conn.send(fibonacci(receive.decode()).encode())

def main():
    HOST = "192.168.137.30"
    PORT = 8000
    s = setup_socket(HOST, PORT)
    run_server(s)
    s.close()


main()
