# 建立一個 Animal 的 class
class Animal():
    # 設定 Animal constuctor ()裡面可以設定的初始值
    def __init__(self, weight, mood):
        self.weight = weight
        self.mood = mood
    
    # feed, walk, bath 計算動物改變的 weight 和 mood
    def feed(self, n, c_weight, c_mood):
        self.weight += c_weight * n 
        self.mood += c_mood * n
        
    def walk(self, n, c_weight, c_mood):
        self.weight += c_weight * n 
        self.mood += c_mood * n
    
    def bath(self, n, c_weight, c_mood):
        self.weight += c_weight * n 
        self.mood += c_mood * n
    
# 建立一個 Dogs 的 class 繼承 Animal
class Dogs(Animal):
    def __init__(self, weight, mood):
        # 繼承 Animal 的 __init__ method
        super().__init__(weight, mood)
    
    # feed, walk, bath 個別繼承 Animal 的 feed, walk, bath，並傳入改變的 weight 和 mood
    def feed(self, n):
        super().feed(n,0.2,1)
       
        
    def walk(self, n):
        super().walk(n,-0.2,2)
        
    def bath(self, n):
        super().bath(n,0,-2)
        
    # self 後面的變數傳入各動作執行的次數，最後輸出結果
    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print(f"狗狗現在的體重= {self.weight} kg, 心情 {self.mood}")

# 建立 Cats class 並繼承 Aniaml 
class Cats(Animal):
    def __init__(self, weight, mood):
        # 繼承 Animal 的 __init__ method
        super().__init__(weight, mood)

    # feed, walk, bath 個別繼承 Animal 的 feed, walk, bath，並傳入改變的 weight 和 mood
    def feed(self, n):
        super().feed(n,0.1,1)
       
        
    def walk(self, n):
        super().walk(n,-0.1,-1)
        
    def bath(self, n):
        super().bath(n,0,-2)
        
    # self 後面的變數傳入各動作執行的次數，最後輸出結果
    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print(f"貓貓現在的體重= {self.weight} kg, 心情 {self.mood}")

# 使用 Dogs class 建立 dog object
dog = Dogs(4.8, 65) 
#使用 Dog 裡面的 instance method
dog.printf(18, 10, 4) 

# 使用 Cats class 建立 dog object
cat = Cats(8.2, 60) 
#使用 cat 裡面的 instance method
cat.printf(40, 7, 1) 