class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.title = "君" if age <= 19 else "さん"

    def getInfo(self):
        return self.name + self.title + "は" + str(self.age) + "歳てす。"

a = Person("なかむら", 38)
b = Person("たけし", 12)

print(a.getInfo())
print(b.getInfo())
