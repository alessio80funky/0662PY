#比較演算子

a = 10
b = 20

print(a == b)  # 等しいかどうか -> False
print(a != b)  # 等しくないかどうか -> True
print(a > b)   # aがbより大きいかどうか -> False
print(a < b)   # aがbより小さいかどうか -> True
print(a >= b)  # aがb以上かどうか -> False
print(a <= b)  # aがb以下かどうか -> True

#論理演算子

print(a > 5 and b < 30)  # aが5より大きく、かつbが30より小さいかどうか -> True
print(a > 5 and b > 30)  # aが5より大きく、かつbが30より小さいかどうか -> False

print(a > 5 or b < 10)   # aが5より大きい、またはbが10より小さいかどうか -> True
print(a < 5 or b < 10)   # aが5より小さい、またはbが10より小さいかどうか -> False


print(not(a > 5))        # aが5より大きくないかどうか -> False


age = 17
score = 80

if age >= 18 and score >= 70:
    print("合格")

if age < 18 or score < 70:
    print("不合格")