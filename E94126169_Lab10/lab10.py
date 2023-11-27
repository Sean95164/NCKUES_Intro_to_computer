from flask import Flask, render_template, request
import random

# 電腦隨機出拳  
def computer_choice():
    ways = ["r", "s","p"]
    choice = random.choice(ways)
    return choice

# 運行剪刀石頭布遊戲
def game(user):
    computer = computer_choice()

    print(f"\ncomputer : {computer}  user : {user}")

    if(user == computer): # 平手的情況
        return "It's Tie !"
    elif (user, computer) in [("r", "s"), ("s", "p"), ("p", "r")]: # 玩家贏的情況
        return "You win !"
    else:
        return "Computer win !" #剩餘的情況為電腦贏的情況

def define_route(app):

    # 建立初始頁面
    @app.route("/")
    def index():
        # 套用 lab10.html 
        return render_template("lab10.html")

    # 建立 /student_data route, 並設定可以處理的 HTTP methods
    @app.route("/student_data", methods = ['POST'])
    def submit():
        # 取得表單資料
        name = request.form["name"]
        student_id = request.form["id"]

        print(f"\nname : {name}")
        print(f"student_id : {student_id}\n")
        return "ok"

    # 建立 /rsp 剪刀石頭布的遊戲運行 route
    @app.route("/rsp")
    def play():
        # 取得使用者樹輸入的 ?choice
        user_input = request.args.get("choice")
        # 回傳遊戲的結果
        result = game(user_input)
        return result
        

def main():
    # 建立 flask 物件
    app = Flask(__name__)
    # 建立網頁 route
    define_route(app)
    # 運行 server
    app.run(host="0.0.0.0", port=3000, debug = True)

main()
