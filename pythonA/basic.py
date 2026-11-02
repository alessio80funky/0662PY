#pythonのターミナルの出力のコマンド
print("hello")
#pythonの変数
name = "アレッシオ"
age = 36

print(name)
print(age)
#pythonのテンプレート文字列
print(f"{name}さんは{age}才です")

#関数
def sayHello():
    print(name)

sayHello()

def tsuika(a, b):
    return a + b

kekka = tsuika(10, 5)

print(kekka)#15