#反復処理

#for文を使った場合

for i in range(5):
    print(i)  # 0,1,2,3,4

#for文を使わない場合

print(0)
print(1)
print(2)
print(3)
print(4)

#for..in

fruits = ["apple", "banana", "orange"]

for x in fruits:
    print(x)  # apple, banana, orange

#while文

count = 0

while count < 5:
    print(count)  # 0,1,2,3,4
    count += 1 