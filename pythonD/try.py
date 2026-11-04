
try:
    age = int(input("：あなたの年齢を入力して: "))
    print(f"あなたの年齢は {age} 歳です。")
except ValueError:
    print("無効な入力です。整数を入力してください。")