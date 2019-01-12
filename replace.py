# ["佐藤", "鈴木", "山田"]の配列を作成し、
# 「佐藤」という文字列の要素のみ、「斎藤」に変更した新しい配列を作成してください。

names = ["佐藤", "鈴木", "山田"]

for i in range(len(names)):
    names[i] = "斉藤" if names[i] == "佐藤" else names[i]

print(names)

names = ["佐藤", "鈴木", "山田"]

new_names = [("斉藤" if name == "佐藤" else name) for name in names ]

print(new_names)
