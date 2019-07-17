#coding:utf-8
import math

# 経路クラス
class Path:
    def __init__(self,cost,city):
        self.cost = cost
        self.next_city = city

# 都市クラス
class City:
    def __init__(self, name):
        self.name = str(name)
        self.nextPathNum = 0
        self.path_list = list()

    def setNextPath(self,cost,next_city):
        self.nextPathNum += 1
        path = Path(cost,next_city)
        self.path_list.append(path)

########################################
##               main                 ##
########################################
if __name__ == '__main__':
    ## 都市それぞれのインスタンス化
    osaka    = City('大阪') #大阪
    tokyo    = City('東京') #東京
    yokohama = City('横浜') #横浜
    sendai   = City('仙台') #仙台
    okinawa  = City('沖縄') #沖縄

    ## 次の都市への経路の設定
    osaka.setNextPath(2980,tokyo)
    osaka.setNextPath(3800,yokohama)
    osaka.setNextPath(6000,sendai)

    tokyo.setNextPath(7390,okinawa)
    yokohama.setNextPath(7970,okinawa)
    sendai.setNextPath(18550,okinawa)

    ## 探索部分
    min_cost = math.inf  #最小の費用
    city_names = list()  #最小で行った時の都市の順番
    # 大阪の次の都市への経路(Path)でループ
    for i in osaka.path_list:
        print(osaka.name, end=' -- ')   #「大阪 -- 」を表示
        print( i.cost , end=' --> ')  #「(値段) --> 」を表示
        print( i.next_city.name, end=' -- ')
        tmp_names = [osaka.name ,i.next_city.name] # 一時的に、今いるの都市名前を入れるリスト

        # 東京、横浜、仙台からの経路(Path)でループ
        for j in i.next_city.path_list:
            tmp = j.cost # あとで費用を足し合わせるために一時的に保存
            tmp_names.append(j.next_city.name) # 50行目のリストに都市を追加
            print(j.cost, end=' --> ') 
            print(j.next_city.name)
        
        # 2つの費用を足し算
        tmp += i.cost
        # もし費用が最小ならmin_costに値を代入する
        if min_cost > tmp:
            min_cost = tmp # 最小の費用を代入
            city_names = tmp_names # 費用最小の場合の都市の名前を代入
        
        # print(tmp, end='\t')
        # print(tmp_names)
    
    print() # 改行用
    print("最小の費用\t",min_cost)

    for i in city_names:
        print(i,end= '\t')
    print()
    