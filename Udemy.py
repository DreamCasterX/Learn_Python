#!/usr/bin/env python3
# while的用法類似if, 但是while執行到句子的尾巴時會"重新"跳回開頭檢查條件
# 遇到continue時, 會直接跳回while開頭, 而不往下繼續
# 陷入無限迴圈時, 可下一個"break" 中止讓程式繼續往後

"""
A = 0
while A < 5:
    A += 1
    if A == 3:
        continue
    print("This is loop #" + str(A))
"""
import os

# for迴圈可指定執行次數, 從"0"開始
"""
for i in range(5):
    print("迴圈測試 #" + str(i))
"""

# 從0加到100
"""
total = 0
for num in range(101):  #101代表次數  但並"不包含"101這個次數
    total = total + num
print(total)
"""
# while可以作到跟for相同的事, 只是for更為簡潔, 且可以隨意制定range的指定範圍
# 例如for i in range(12, 16, 1),  會執行12~ 15 (12, 13, 14, 15) 這四個範圍, 然後每次增加單位是1

# 內建函式 = build-in (basic) function
# 使用非內建函式時, 需要呼叫(import)
# 使用pip安裝 3rd-party module 模組  => sudo apt-get install python3-pip
"""
import random  #呼叫random module
print(random.randint(1, 100))   #module.function

import sys
print("Hello")
sys.exit()
print("Goodbye")
"""

"""
import pyperclip
pyperclip.copy("Hello World")
pyperclip.paste()
"""

"""
city = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
"""
"""
def hello(name):   #此處的name 稱為parameter(參數) 也就是函式裡的變數
    print("Hello " + name)
hello("Mike")  #此處的Mike/Elin  稱為arguments (引數)
hello("Elin")
"""
# 每個函式(function) 都會有return value, 預設是None
# input = arguments  , arguments會傳到parameter裡
# output = return

# print函式使用逗號會自動產生空隔
"""
print("Hello", "Mike", "!")
"""
# 變數無法同時成為全域或是局部, 只能其一
"""
spam = 42 #這個是global variable 全域變數, 會一直持續到整個程式碼結束
def egg():
    spam = 42  #這個是local variable 局部變數, 只有函式被呼叫時出現,跑完return就消失
"""
# 下面這段程式碼會出錯, 因為沒有定義全域變數
"""
def spam():
    eggs = 99
spam() #局部變數已消失
print(eggs) #沒有定義全域變數, eggs沒有被定義
"""
# 函式A的局部變數 也不能 跟B函式的局部變數共用, 各自獨立
# 函式裡如果出現變數, python會先檢查他是不是local var,  如果不是才會再檢查是不是global var
"""
def spam():
    eggs = "Hello"
    print(eggs)
eggs = 42
spam()
print(eggs)
"""
# 上面會先印出 Hello  然後是 42
# 如果要強制函式使用global var, 可在變數前加上global, 這樣函式只會取用global直接忽略local
"""
def spam():
    global eggs  # 這裡強制把函式內的eggs轉為global全域變數
    eggs = "Hello"
    print(eggs)
eggs = 42
spam()
print(eggs)
"""
# 上面會先印出 Hello  然後是 Hello

# try except用法, 可以讓程式運行時產生的error消失, 也不會讓程式執行到一半crash
"""
print("How many cats do you have?")
num = input()
try:  #額外加上try
    if int(num) >= 4:
        print("That's a lot of cats.")
    else:
        print("That's not that many cats.")
except ValueError:  #額外加上except ,遇到error時的處理
    print("You did not enter a number")
"""

# 猜數字遊戲
"""
import random
print("請問你的名字是?")
name = input()
print("你好, " + name + " 請從1~20之間猜一個我正在想的數字")
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print("猜猜看~")
    guess = int(input())

    if guess < secretNumber:
        print("你猜的數字太低了")
    elif guess > secretNumber:
        print("你猜的數字太高了")
    else:
        break #答對 do nothing , 繼續往下進行程式

if guess == secretNumber:
    print("太棒了, " + name + "! 你在第" + str(guessTaken) + "回猜到我的數字了")
else:
    print("猜錯太多次囉, 我想的數字是" + str(secretNumber) + "啦")
"""
# import module 模組
"""
import sys as s   # as後面可自取別名
print(s.platform)
print(s.path)  #顯示module搜尋的位置

sys.path.append("modules")  #更改模組的位置
import geometry
print(geometry.slope(1,2,5,6))
print(s.path)
"""

# List 列表  用中括號顯示
"""
print([1,2,3] + [4,5,6]) #會變成[1,2,3,4,5,6]
grades = [60,70,80,90,100]   # 60=index 0     70=index 1   80=index 2   90=index 3   100=index 4
print(grades[1])  #會印出index 1 = 70
print(grades[1:3])  #會印出index 1到index 2之間連續的數值= 70,80    #注意這邊的3不是index 3 反而是index 2(第二輪), 跟for迴圈第二個值的意思一樣
print(grades[1:])  #會印出index 1和它之後全部的東西= 70, 80, 90, 100
print(grades[:3])  #會印出index 0 到 index 2 之間全部的東西 = 60, 70, 80
del grades[4]  #刪除index 4 (100)
print(grades) #印出來會少掉index 4 (100) = 60, 70, 80, 90
"""
"""
spam = [["a","b","c"],[10,20,30,40]]
print(spam[1][3])  #會印出第index 1 (第二個list)中的 index 3 (第4個) = 40
"""
# range(4) 實際上代表的是[0,1,2,3]這個list
# 可用list函式檢查   list(range(4)) = [0,1,2,3]
# print(list(range(0,100,2)))  # 會印出0~98 (不包含100) 之間所有的偶數
"""
students = ["Mike","Elin","Brian","Kevin","Molly"]
for i in (range(len(students))):   # 用len取得List的長度
   print("班上第" + str(i+1) + "位同學的名字是" + students[i])  # 用i+1是因為要略過第0位   後面的[i]會擷取對應index的姓名
"""
# 可利用List 來實現Multiple Assignment 多重指定
"""
cat = ["Fat","White","Loud"]
size, color, temper = cat
print(size)
print(color)
print(temper)
"""
# Tuple ( ) 的用法跟List [ ]相同, 差別在別Tuple的資料無法被變動
"""
# List
data = [3,4,5]
data[0] = 6
print(data)    # 會印出[6,4,5]
# Tuple
data = (3,4,5)
data[0] = 6
print(data)  # 印不出來, 因為Tuple的"原始資料"不能被更動 (加入新的資料可以)
"""

# Method方法   (Class類別,  Object物件, Attribute屬性, Constructor建構式)
# 用print(dir(函式)) 可查看該函式有哪些method可用
"""
name = ["Mike", "Elin", "Molly"]
print(name.index("Elin"))   # 使用List的method => index  回傳index值

name.append("Elin") # 使用List的method => append  追加一個新的字串在後面
print(name)

name.insert(1, "Kevin") # 使用List的method => insert  追加一個新的字串在指定的index
print(name)

name.remove("Mike") # 使用List的method => remove  刪除指定的index
print(name)
"""

"""
num = [5, 8, 2, 4.1, -8, 9]
num.sort()   # 使用List的method => sort 自動由小至大排序(字母也可)
print(num)
num.sort(reverse=True)   # 變成由大至小
print(num)
"""
"""
# String 跟 Tuple的值都是不可變動的(immutable), 只能用新的值取代掉
a = 100
b = a
a = 10    # a已經被賦予全新的值, 所以a已經不是原本的a了  但是b並"沒有"被變動!!   因為a跟b是分開的東西
print(a)
print(b)
# 會印出 10   100

c = [1, 2, 3, 4]
d = c
c[3] = 100
print(c)  # c已經被賦予全新的值, 但是d卻跟著變動了!!  也就是說c跟d是共用相同的東西
print(d)
# 會印出 [1,2,3,100]  [1,2,3,100]

def eggs(cheese):
    cheese.append("Hello")
spam = [1,2,3]
eggs(spam)  # spam沒有被global var蓋掉, 依然吃到local env!!  也就是說List是共用同一份的
print(spam)  # 會印出 [1,2,3,'Hello']
"""
"""
import copy   # 使用copy這個函式可建立新的List
spam = [1,2,3]
cheese = copy.deepcopy(spam)  # 建立一個新的List 而不是跟原本的List共用
cheese[1] = 42
print(cheese)  # 會印出 [1,42,3]
print(spam)    # 會印出 [1,2,3]  不再跟cheese 共用相同List
"""

# Dictionary Data字典  使用大括號{ }  裡面包含keys + values
# Dict 不重視順序, 即使兩個不同的Dict有相同數值但排序不同, 也會被視作是相同的Dict
"""
MyCat = {"size": "fat", "color": "blue", "temper": "loud"}  # keys = size/color/temper   values = fat/blue/loud
print(MyCat["size"])  # 會印出fat
# print(MyCat["shape"])  # 會產生KeyError
print("size" in MyCat) # 會印出True
print("fat" in MyCat)   # 會印出False  因為in只會檢查keys  不檢查values

del MyCat["color"]  # 使用del  可把color這個key和value整個一起刪除
print(MyCat)  # 會印出{"size": "fat", "temper": "loud"}
"""
# Dictionary 有三種基本Method可用: keys, values, items  (如同List有index, append, insert, sort的Method可用)
"""
print(list(MyCat.keys()))
print(list(MyCat.values()))
print(list(MyCat.items()))
print("size" in MyCat.keys()) # 會印出True
print("fat" in MyCat.values()) # 會印出True
"""
# 使用"get" Method  可檢查該keys 是否存在, 若無則return後面自定義的內容 (比用if判斷式更快更方便)
"""
print(MyCat.get("color", "non-existent"))  # 會直接印出該key的value: blue
print(MyCat.get("shape", "non-existent"))  # 會印出non-existent
"""
# 使用"setdefault" Method  可以加入一組不存在的keys + values組合進去dict (若已存在key, 則無法修改或加入)
"""
MyCat.setdefault("weight", 10)
print(MyCat)  # 會印出{'size': 'fat', 'color': 'blue', 'temper': 'loud', 'weight': 10}
"""

# 列出一個句子裡面 每個字母出現幾次
# 使用pprint module可以把dict印的更整齊漂亮
"""
import pprint
message = "I am Mike. How are you doing?"
count = {}
for letter in message:
    count.setdefault(letter, 0)
    count[letter] = count[letter] + 1  # 這裡+1的會是values 而不是keys
pprint.pprint(count)
"""

# 將List轉換成Dict的一個小技巧
"""
dic = {x:x*2 for x in [3,4,5]}   # 從列表的資料產生字典
print(dic)   # 會印出 {3: 6, 4: 8, 5: 10}
"""

# 所有的函式都有return value, 即使像是print()函式 也會return "None", 只是不顯示
# 函式預設的return value都是None
"""
print("cat","dog","cow", end=" ")  # 會用空白跟下面的print做連結   end可稱為"keyword argument"
print("pig")
print("cat","dog","cow", sep="---")  # 會用---區隔開來   sep可稱為"keyword argument"
"""

# 字串的Methods

# print("Hello".isalpha())  # 檢查是否為字母 (非數字或符號空格)
# print("Hello".isalnum())  # 檢查是否為字母或數字 (非符號或空格)
# print("Hello Mike"[5].isspace())  # 檢查是否為空格
#
# print("Hello, Mike".startswith("He")) # 檢查開頭的字串是否符合指定的字
# print("Hello, Mike".endswith("ike")) # 檢查開頭的字串是否符合指定的字
#
# print("\n".join(["(1)","(2)","(3)"])) # 把\n 這個字串加入到後面的list中, 會印出 (1)\n(2)\n(3)
# print("My name is Mike".split())  # 與.join()相反  把字串切割開來, 會印出 ["My", "name", "is", "Mike"]     # 把字串變成List的方法
# print("My name is Mike".split("e"))  # 指定e為切割點  只要看到e就刪除並分段, 會印出 ["My nam", " is Mik", ""]   # 把字串變成List的方法


# 字串 + .rjust = 向右移動指定的長度    .ljust = 向左移動指定的長度   .center = 置中
# 預設是空白可自己填入想要的字串
"""
a = " Hello ".center(15, "*")
print(a)

# 字串 + .rstrip = 刪除右邊指定的字串(預設是空白)   .lstrip = 刪除左邊指定的字串   .strip = 刪除所有指定的字串
a = "Hello".strip("o")
print(a)

# 字串 + .replace("xx","yy")   把字串裡的xx換成yy
a = "Hello".replace("lo", "p~!")
print(a)
"""
# Conversion specifiers    %s = placeholder for "String"     %d = placeholder for "Digital character"
# 如果string當中有很多變數, 可使用 %s 取代所有的變數, 放在後頭解釋更易讀
"""
name = "Mike"
place = "park"
time = 6
food = "chicken"
print ("Hello %s, you are invited to %s at %d pm. Please bring your %s, thanks!" % (name, place, time, food))
"""

# 在Windows / Linux 執行.py的方式
# Windows:
# (1) 打開cmd,v輸入py.(exe) xxxxx.py   (exe可省略)    如果此程式碼不需要跳出CMD視窗給user, 可改為pyw xxxxx.py
# (2) Win+R, 直接執行py.(exe) xxxxx.py   (exe可省略)
# (3) 寫成batch:
#     @py C:\user\xxx\xxx.py %*    (執行時不顯示cmdline, %*代表把所有命令行參數都丟給python)
#     @pause   (Windows內建暫停指令)
# Linux:
# (1) 更改.py檔案權限 ==> chmod +x xxxx.py
# (2) 打開Terminal執行  ./xxxx.py

# regular expression   (簡稱Regex 正規表達式)   類似Linux裡grep 和 sed的概念
# wiki: 一種用來描述字串 符合某個語法規則的模型, 可用來做文字的搜尋,比對,替代,轉換
# 使用強大的re模組來 搜尋或是處理字串符, 可省時省力
# 比較慢的方法(未使用re...要一個字一個字定義)  例如要判斷一段字串裡面是否存在電話號碼:
"""
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
         return False
    return True
print(isPhoneNumber("415-555-0000"))
"""
# 使用re, 可直接定義整排字串格式
"""
import re
message = "Please call me 415-555-0000 tomorrow, or at 415-555-9999 for office."
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")   # re.compile method 可定義格式   \d代表任何數字(Digital character)
mo = phoneNumRegex.search(message) # search第一筆符合的字串  Matched object
mo2 = phoneNumRegex.findall(message)  # search全部符合的字串並顯示為List
print(mo.group())    # group method 可顯示actual text
print(mo2)
"""
# 使用( )可以再定義區塊   小括號在正規表達式可用來分割區塊
"""
import re
message = "Please call me 415-555-0000 tomorrow, or at 415-555-9999 for office."
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")   # 定義了區塊1 和 區塊2
mo = phoneNumRegex.search(message)
print(mo.group(2))  # 只要區塊2
"""
# 使用問號 ？ 可以篩選出有出現0次或1次的字串,也就是前面小括號()內的字串可以是optional
# 使用星號 *  可以篩選出有出現0次或N次的字串,也就是前面小括號()內的字串可以是optional
# 使用加號 +  可以篩選出有出現1次或N次的字串,也就是前面小括號()內的字串可以是optional
"""
import re
message = "The Adventures of Batwoman"
batRegex = re.compile(r"Bat(wo)?man")  #    "?" 可代表前面的( )內可出現0或1次
mo = batRegex.search(message)
print(mo.group())   # 會印出 Batwoman

import re
message = "Please call me 555-666-555-1111 tomorrow, or at 777-888-555-2222 for office."
phoneNumRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")  # 定義(d\d\d-)這個區塊可以出現0或1次
mo = phoneNumRegex.search(message)
print(mo.group())  # 會印出 666-555-1111

message = "Please call me 555-666-555-1111 tomorrow, or at 777-888-555-2222 for office."
phoneNumRegex = re.compile(r"(\d\d\d-)*\d\d\d-\d\d\d\d")  # 定義(d\d\d-)這個區塊可以出現0或多次
mo = phoneNumRegex.search(message)
print(mo.group())  # 會印出 555-666-555-1111   # 有兩筆字串都符合\d\d\d格式  所以全部都印出

message = "Please call me 555-1111 tomorrow, or at 777-888-555-2222 for office."
phoneNumRegex = re.compile(r"(\d\d\d-)+\d\d\d-\d\d\d\d")  # 定義(d\d\d-)這個區塊可以出現1或多次
mo = phoneNumRegex.search(message)
print(mo.group())  # 會印出 777-888-555-2222   # 有兩筆字串都符合\d\d\d格式  所以全部都印出
"""

# 集合 {   }    不用像Dict需要Key:Value
"""
s1 = {3,4,5}
s2 = {4,5,6}
print(6 in s1)   # 可用in來檢查是否在集合中, 此範例會回傳False
print(6 not in s1)   # 可用in來檢查是否不在集合中, 此範例會回傳True
s3 = s1 & s2  # 交集
print(s3)  #  使用& 來取得交集的部份, 此範例會回傳{4, 5}
s4 = s1 | s2  # 聯集
print(s4)  #  使用 | 來取得聯集的部份,但不重複取 此範例會回傳{3, 4, 5, 6}
s5 = s1 - s2  # 差集
print(s5)  #  使用 - 來取得差集的部份,此範例會回傳{3}
s6 = s1 ^ s2  # 反交集
print(s6)  #  使用 ^ 來取得兩個集合中 不交集的部份,此範例會回傳{3, 6}
# set(字串)  可將字串拆解為集合
"""
"""
# 定義函式結束後, return可用來強制結束函式, 會回傳None(預設)
def say(msg):
    print(msg)
    return  # 若不寫return也可以, 預設的回傳就是None
value = say("Hi Mike")
print(value)   # 會印出None

def add(n1, n2):
    result = n1 + n2
    return "Done!"   # 可自定義
value = add(3, 4)
print(value)   # 會印出整個函式執行完後的回傳值 = Done!

# 無限參數 (參數前面加一個星星) 則參數的數量可不受限, 會被當作Tuple的資料型態處理
def add(*numbers):
    for i in numbers:  # 這邊的numbers會變成一個Tuple被處理
        print(i)
add("Mike", "Elin", "Ryan", "Tony", "Molly")  # 給幾筆都沒關係, 因為參數可無限
"""
# 自己定義一個函式, 可放任意數字進去當參數使用, 最後自動計算出平均值
# 其實功能就是statistics.mean() ,  後來才教到
"""
def avg(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    print(total / len(numbers))
avg(10,90,-1)   # 取得平均值為33
"""

# 封包資料夾 一定要有一個 __init__.py

# 數據分析
# random module 使用大全   (python內建的亂數模組)
"""
import random
a = random.choice([0,1,5,8])  # 從List中隨機選取1筆資料
b = random.sample([0,1,5,8], 2)  # 從List中隨機選取n筆資料 (choice的進階板)
print(a)
print(b)

data =[0,1,5,8]
random.shuffle(data)  # 將List中的值隨機調換(洗牌)
print(data)

c = random.random()   # 在0.0 ~ 1.0之間取得隨機亂數
print(round(c*100))

d = random.uniform(1, 100)  # 可自行定義一個範圍內隨機取float (random.random的加強板)
print(round(d))

e = random.randint(1, 100) # 可自行定義一個範圍內隨機取int (輸出就是整數, 更方便好用)
"""

# statistics module 使用大全   (python內建的統計模組)
"""
import statistics as stat
stat.mean([1,4,5,8])  # 計算List中的平均數  , 會印出4.5
stat.median([1,2,3,4,5,8,100])  # 計算List中的中位數, 會忽略掉極端的數值,  會印出4
stat.stdev([1,4,6,9])  # 計算List中的標準差（standard deviation)
"""

# try...except...finally 用法
# 可針對各種錯誤 做出排解回應, 而不讓程式出現error中斷
"""
try:
    print(1/2)  # 可正常印出 0.5
    print(1/0)  # 這邊出現error了, 所以會直接跳到except去處理error的問題
    print(2/1)  # 因為上一句出現error, 這邊會被中斷不執行
except Exception:
    print("Zero can't be divided")
"""
"""
try:
    a = 1/2
    print(a)  # 可正常印出 0.5
    print(QQ)  # 因為m這個變數沒有被定義, 會跳出NameError
    b = 1/0  # 上面已報錯, 後面都中斷不執行
    print(b)
    c = 2/1
    print(c)
except NameError:
    print("Oops!") # 對應到NameError, 這邊會印出來
except ZeroDivisionError:
    print("Wrong math!") # 沒有error, 不被印
except:  # 出現除了上述以外的error, 才會被執行
    print("Error") # 因為已經error, 不被印
else: # 都沒有任何error就執行這句
    print("No error! Yeah~")
finally:   # 不管有沒有error 都執行這句
    print("Successful!")
"""
# with....as  為簡化板的try except finally語句
# 結構: with expression [as 變數]:
#        with-block

# 要打開一個文件 再讀取 再關閉的寫法如下:
# file = open("/tmp/TEST.txt")
# data = file.read()
# file.close()
#
# 避免過程中出現異常, 改良後
# file = open("/tmp/TEST.txt")
# try:
#     data = file.read()
# finally:
#     file.close()
#
# 精簡化加強版(更優雅)
# with open("/tmp/TEXT.txt") as file:  # 把with後面做的事產生的return value 傳給後面的變數
#     data = file.read()              # 然後再執行finally的工作, 不論前面是否成功都會被執行, 且執行完會自動close

"""
import datetime
with open("dateInfo.txt", "a") as outFile:  # 將前面的函式的返回值 丟給後面的變數
    outFile.write("\n" + str(datetime.datetime.now()))
"""

# datetime: 顯示當前時間的函式
"""
import datetime
now = datetime.datetime.now()
nowformat = now.strftime("%Y/%m/%d %H:%M:%S")  # 自定義時間格式
print(nowformat)
"""

# getsizeof : 查看內存大小的函式
"""
from sys import getsizeof
sum = range(100)
sum2 = list(sum)
print(getsizeof(sum))
print(getsizeof(sum2))
"""

# class 類別的概念與用法    class可以同時包裝 變數 & 函式(method)
# 結構: #class Test:
#          x=3         #定義變數
#          def say():  #定義函式
#            print("Hello")
# 用法一:  類別名稱.屬性名稱     class + 實體屬性(Instance Attribute)
"""
class fruit:
    select = ["apple", "banana", "orange", "strawberry"]
    def choice(x):
        if x in (fruit.select[0]):
            print("$10")
        elif x in (fruit.select[1]):
            print("$20")
        elif x in (fruit.select[2]):
            print("$30")
        elif x in (fruit.select[3]):
            print("$40")
        else:
            print("Please choose again")
# 使用class   fruit.select
print(fruit.select)      # 會印出 ['apple', 'banana', 'orange', 'strawberry']
fruit.choice("apple")    # 會印出 $10
fruit.choice("egg")      # 會印出 Please choose again
"""

# 用法二:  實體物件基本語法
# class 類別名稱:
#     def __init__(self):     # 先建立一個初始化函式,  透過操作self來定義實體屬性
# obj = 類別名稱()    # 呼叫初始化函式   建立實體物件, 放入變數obj中

# class Point:
#     def __init__(self, x, y):  # 先建立一個初始化函式  傳入x.y
#         self.mike = x          # 在這個初始化函式中, 把實體屬性(instance attribute)定義好
#         self.elin = y          # 在這個初始化函式中, 把實體屬性(instance attribute)定義好
# p = Point(1, 5)                # 呼叫這個物件 傳入1, 5  給x,y使用 並存為變數
# print(p.mike) # 會印出1     # class + 實體屬性
# print(p.elin) # 會印出5
#
# class Point:
#     def __init__(self, x, y):     # 先建立一個初始化函式  傳入x.y
#         self.mike = x             # 在這個初始化函式中, 把實體屬性(instance attribute)定義好
#         self.elin = y             # 在這個初始化函式中, 把實體屬性(instance attribute)定義好
# p1 = Point(3,4)                   # 呼叫這個物件 傳入3, 4  給x,y使用 並存為變數
# print(p1.mike, p1.elin)  # 會印出 3 4
# p2 = Point(5,6)
# print(p2.mike, p2.elin)  # 會印出 5 6

# 實體方法的語法
# class 類別名稱:
#     def __init__(self):     # 定義初始化函式,  透過操作self來定義實體屬性
#         定義實體屬性
#     定義實體方法/函式
# obj = 類別名稱()

# 定義實體方法/函式
#   def 方法名稱(self, 更多自訂參數):
#       方法主體, 夠過self操作實體物件


# class Point:
#     def __init__(self, x, y):     # 先建立一個初始化函式  傳入x.y
#         self.mike = x             # 在這個初始化函式中, 把實體屬性(instance attribute)定義好
#         self.elin = y             # 在這個初始化函式中, 把實體屬性(instance attribute)定義好
#
#     def show(self):               # 定義實體方法(method)
#         print(self.mike, self.elin)
# p = Point(3,4)                   # 建立實體物件, 呼叫初始化函式
# p.show()                         # 呼叫實體方法/函式   會印出 3  4
#
# # 實體物件設計,包裝檔案讀取的程式
#
# class File:
#     def __init__(self, name):                     # 建立一個初始化函式
#         self.name = name
#         self.file = None    # 尚未開啟檔案, 初期是None
#     def open(self):   # 定義第一個實體方法(method)
#         self.file = open(self.name, mode="r", encoding="utf-8")  # 此處為Python內建的函式
#     def read(self):    # 定義第二個實體方法(method)
#         return self.file.read()
#
# f1 = File("data1.txt")        # 建立File的實體物件, 呼叫初始化函式
# f1.open()                     # 利用f1代表實體物件  呼叫實體方法open
# data = f1.read()              # 呼叫實體方法read
# print(data)      # 會印出data.txt的內容


# class CuteCat:
# #     def __init__(self):
#         self.name = "Mike"
# cat1 = CuteCat()
# print(cat1.name)  # 會印出Mike
#
#
# class CuteCat:
#     def __init__(self, cat_name):
#         self.name = cat_name
# cat1 = CuteCat("Mike")
# print(cat1.name)  # 會印出Mike
#
#
# class CuteCat:
#     def __init__(self, cat_name, cat_age, cat_color):  # cat_name, cat_age, cat_color都只是一般的變數而已
#         self.name = cat_name
#         self.age = cat_age
#         self.color = cat_color     # .name .age  .color 都是綁定實體物件的屬性
#     def speak(self):
#         print("Meow" * self.age)
#
# cat1 = CuteCat("Mike", 5, "orange")
# print(f"My cat {cat1.name} is {cat1.age} years old, her color is {cat1.color}")
# # 會印出 My cat Mike is 5 years old, her color is orange
# cat1.speak()
# # 會印出 MeowMeowMeowMeowMeow




# 檔案處理 =>  利用os module來處理文件檔案
"""
import os

例如我有一個檔案位置在C:\Windows\System32\drivers\Mike.jpg
a = os.path.join("C:\", "Windows", "System32", "drivers", "Mike.jpg")  # 會根據你目前使用的OS自動判斷

os.getcwd()  # 獲取當前的工作目錄(current working directory)
os.chdir("xxxx")  # 可暫時改變cwd的路徑, (用指定存放檔案的位置)
os.path.exists("/home/mike/Desktop/Pycharm/Udemy/Udemy.py")   # 檢查此路徑或檔案是否存在
os.path.isfile("/home/mike/Desktop/Pycharm/Udemy/Udemy.py")   # 檢查此路徑是否為檔案(True/False)
os.path.isdir("/home/mike/Desktop/Pycharm/wUdemy/Udemy.py")    # 檢查此路徑是否為資料夾(True/False)
os.listdir("/home/mike/Desktop/Pycharm")     # 列出此路徑下所有的資料夾
os.makedirs("/home/mike/Desktop/XYZ")        # 建立資料夾
"""

# 遞迴 (recursive) 函式  (定義函式中 調用自己)
# 填入任意數字  自動幫你連加到1
"""
def num(n):
    if n == 1:
        return 1
    return n + num(n - 1)
print(num(100))   # 印出5050
"""
# lambda表達式 => 用來定義一個匿名函式
# 公式 =>     lambda 變數列表: 表達式
# 意思如同下面:
# def anonymous(變數列表)
#     return 表達式


# def fun(name):
#     return "Hi, " + name
# QQ = fun
# print(QQ("Mike"))   # 會印出 Hi, Mike


# QQ = lambda name: print("Hi, " + name)
# QQ("Mike")  # 會印出 Hi, Mike


# def display(name, greeting):  # 把greeting當作一個函數的變數
#     result = greeting(name)
#     print(result)
# display("Mike", lambda name: f"Hello {name}")  # 直接建立一個lambda的函式拿來用   這個lambda函式的變數就是greeting




# enumerate 函數可取得項目編號(index)      語法 = enumerate(List, 起始值)  起始值沒有填預設是0
# 已測試Dict也能用

# ages = [28, 18, 10, 30]
# for index, age in enumerate(ages, 1):
#     print(f"{index}). {age}")
# 會印出
# 1). 28
# 2). 18
# 3). 10
# 4). 30


"""
# map()函數使用, 公式= map(function, 集合)     返回的是迭代器(iterator)
salary  = [6800, 7000, 5400, 4000]
res = []
for i in salary:
    res.append(i * 2)
print(res)

# 上面的程式可使用map函數簡化成一句就搞定 (替代for迴圈) :
print(list(map(lambda s: s * 2, salary)))  # 用lambda定義一個空函數叫做s , 後面的表答式就是s * 2,  map的集合為salary

# 列表解析  (對一個List 操作產生新的列表)  公式： [輸出表答式 for 變數 in 列表   ]
# 上面的程式還可再使用列表解析 更精簡
print([i*2 for i in salary])
print([i*2 for i in salary if i > 5500])  # 後面可追加if條件語句   會印出 [13600, 14000]

"""


# 好用的招式   (取出每個tuple的年齡)  map搭配lambda使用
# 已測試過 也能針對dict的 key或是value存出新的List

# student = [("Mike", 25),
#            ("Elin", 22),
#            ("Molly", 5),
#            ]
# age = list(map(lambda s: s[1], student))
# print(age)
#
# # Dict
# student = {"Mike": 25,
#            "Elin": 22,
#            "Molly": 5
#            }
# age = list(map(lambda s: s, student.values()))
# print(age)


# filter() 函式 用來過濾掉List中不符合要求的元素, 留下符合的元素, 並生成一個新的集合
# 公式= filter(function, List)     返回的是迭代器(iterator)
# 過濾出高於6500的印出來
# salary = [6800, 7000, 5400, 4000]
# it = filter(lambda x: x > 6500, salary)
# print(list(it))

# 過濾出高於18歲 的印出來
# student = [("Mike", 25),
#            ("Elin", 22),
#            ("Molly", 5),
#            ]
# print(list(filter(lambda x: x[1] > 18, student)))



# filter() 函式    用來提取List"兩筆"資料, 得到的結果再繼續與後面"下一筆"資料作動
# from functools import reduce
# num = [3, 4, 5, 8]
# print(reduce(lambda a, b: a + b, num))   # 會印出  3+4=7   7+5=12   12+8=20

"""
# 檔案處理: 複製 & 移動 & 刪除
import os
import send2trash
import shutil

# 複製檔案
shutil.copy("/home/mike/Desktop/TEST2.txt", "/home/mike/Desktop/TEST/12345.txt")  # 原始檔案位置 + 要複製的地方(可同時重新命名)

# 複製資料夾
shutil.copytree("/home/mike/Desktop/TEST", "/home/mike/Desktop/Mike2")  # 原始檔案位置 + 要複製的地方(可同時重新命名)

# 移動檔案or資料夾 (剪下貼上)   也可當作直接重新命名 用法類似shell的"mv" command
shutil.move("/home/mike/Desktop/TEST2.txt", "/home/mike/Desktop/TEST2")

# 刪除檔案  如果不想永久刪除可使用send2trash module
os.unlink("TEST.txt")   # 永久刪除單一檔案(不會丟垃圾桶)

# 刪除資料夾
os.rmdir("/home/mike/Desktop/TEST2")  # 永久刪除空的資料夾(不會丟垃圾桶)

# 刪除檔案+資料夾
shutil.rmtree("/home/mike/Desktop/TEST")  # 永久刪除全部檔案(不會丟垃圾桶, 小心使用!!)
"""

# 大量文件檔案操作 可使用os.walk 把全部的資料夾擷取出來
import os, shutil
for root_folders, sub_folders, files in os.walk("/home/mike/Desktop/Mike2"):
    print("The Root folder is: " + str(root_folders))
    print("The Sub folder is: " + str(sub_folders))  # 會用list呈現
    print("The file is: " + str(files))   # 會用list呈現
    print()
    # 對特定檔案進行操作,  複製一份並命新名
    for file in files:
        if file.endswith(".py"):   # 指定副檔名稱.py
            shutil.copy(os.path.join(root_folders, file), os.path.join(root_folders, file + ".backup"))  # 複製並改名為.backup

