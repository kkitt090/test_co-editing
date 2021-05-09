num = 1
num01 = 2.21

print(type(num))
print(type(num01))

string_a = "hello world"

print(string_a)
print(type(string_a))

num02 = 3

a = [["a","b",],["c","d"]]
print(a[0][0]) #一つ目のリストの１番目の変数
print(a[1][1])
print(a[0][1])

print(num + num01)
print(num * num01)
print(num / num01)
print(num % num01)

print(num == num01)
print(num != num01) #ノットイコール

x = 1
print(x)
x +=10 #Xに１０を追加して変数を更新
# X +10だとxは1のまま
print(x)

if x == 1:
    print("true")
else:
    print("false")

for i in range(5):
    if i == 3:
        break
    print(i)

for t in range(5):
    if t == 3:
        continue
    print(t)

arr = [2,4,6,8,10]
for d in arr:
    for a in arr:
        sum = 0
        sum += a+d
        print(sum)

def say_hello(): #自分で関数を定義できる
    print("hello")

def add(num01,num02,num03):
        return (num01 + num02 + num03)/3
add_result=add(9,4,3)
print (add_result)

class student:

    def __init__(self): #コンストラクタ:メソッドを定義する場合は、必ずselfを記述する
        self.name = ""  #アトリビュート(クラス内で定義された変数）：インスタンスには必ずトリビュートが必要になるので、とりあえず空白を返すという処理


    def ave(self,math,english): #メソッド（クラス内の関数）；返す引数がない場合はselfと記述する慣習
        print((math + english)/2)
a001 = student() #←インスタンス化（実体化）作業。これで初めて使えるようになる
a001.name = "sato"
print(a001.name)

a002 = student() 
print(a002.name)

class student:

    def __init__(self,name):
        self.name = name
    def cal_ave(self,date):
        sum = 0

        for num in date:
            sum += num
        
        ave = sum/len(date)
        return ave

    def jedge(selfe,ave):

        if(ave >= 60):
            result = "passed"
        else:
            result = "failed"
        return result

a001 = student("sato")
date =[70,65,50,90,30]
ave = a001.cal_ave(date)
result = a001.jedge(ave)

print(ave)
print(a001.name+" "+result)

print("ヤッホー")

print("ヤッホー")

print("ヤッホー")

