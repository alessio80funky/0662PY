#str
message = "hello python"

print(message)
print(message.upper())
print(message.replace("python","world"))

#int　整数 (integer -> 完全なる)　float 少数　(浮き)

score = 85 
count = 3
height = 170.5 
average = 82.5

result = score / count
res = "{:.0f}".format(result)

print(type(score + 10)) #<class 'int'>
print(type(height))#<class 'float'>
print(res)
print(round(average))#82

#bool  真偽値型

isStudent = True
isAdult = False

age = 17

print(isStudent)
print(isAdult)
print(age >= 18)
print(age < 18)

