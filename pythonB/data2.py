#list        0        1       2
fruits = ["りんご","バナナ","みかん"]

print(fruits[0])
print(fruits[1])


print(fruits)

fruits.append("ブドウ")

print(fruits)
print(fruits[3])

#dict (辞書型)

student = {
    "name":"佐藤",
    "age":20, 
    "score":85
    }

print(student)

print(student["name"])
print(student["score"])

student["name"] = "アレッシオ"
student["score"] = 90

print(student)

#タプル

colors = ("赤","青","黄色")

print(colors[1])
print(colors[0])

colors[0] = "緑"

print(colors[0])
