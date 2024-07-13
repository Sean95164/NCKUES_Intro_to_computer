import socket, sys

def connect_to_server(HOST, PORT):

    # 設定 socket 的使用協定
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 設定要連接到的 server 的 ip, port
    s.connect((HOST, PORT))
    print(f"connect to {HOST}")
    return s

def run_client(s):
    while True:
        messenge = input("The Fabonnaci(n) when n = ")

        # 發送訊息給 server
        s.send(messenge.encode())
        
        # 當輸入 exit 結束程式
        if(messenge == "exit"):

            # 強制結束程式
            sys.exit()

        # 接收 server 回傳的答案
        receive = s.recv(1024)
        if len(receive) == 0:
            s.close()
        print(f"the ans is {receive.decode()}")

def main():
    HOST = "192.168.137.30"
    PORT = 8000
    s = connect_to_server(HOST, PORT)
    run_client(s)

main()
