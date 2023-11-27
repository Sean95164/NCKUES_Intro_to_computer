from flask import Flask, render_template, request, redirect, url_for


def define_route(app, data):

    # 建立初始頁面, 並套用 lab10_plus.html
    @app.route("/")
    def index():
        return render_template("lab10_plus.html", data=data)

    # 建立 /set route, 用來接收表單資料
    @app.route("/set", methods = ['POST'])
    def submit():
        # 接收特定表單欄位的資料
        name = request.form["name"]
        score = request.form["score"]
        newdata = {"store_name" : name, "score" : score}
        # 存入 dict
        data[name] = score

        print(f"\nuser input data : {newdata}\n")
        print(f"Data on server : {data}\n") 

        # 重新回到主頁面, url_for() 的參數為 function name, 會傳回該函式所在 route 的絕對路徑
        return redirect(url_for("index"))

    # 建立 /reset/<confirm> route, 其中 confirm 可傳入 fumction 作為轉換為變數
    @app.route("/reset/<confirm>")
    def cls_data(confirm):
        if confirm == "y":
            # 清空資料
            data.clear()
            print(f"\nData on server : {data}\n") 
            # 套用 reset.html, url 以 index function 所在的路徑傳入
            return render_template("reset.html", url=url_for("index"))
        else:
            # 若 confirm 不為 y, 則回到主頁面
            return redirect(url_for("index"))

def main():
    # 建立 dict 儲存資料
    data = dict()
    # 建立 flask 物件
    app = Flask(__name__)
    # 建立網頁的路徑, 以及執行指令
    define_route(app, data)
    # 執行 server
    app.run(host="0.0.0.0", port=3000, debug = True)

main()
