
class Person(object):
    def __init__(self, firstName = None, lastName = None):
        self.firstName = firstName
        self.lastName = lastName

    def showFullName(self):
        nameElements = [self.firstName, self.lastName]
        if (None in nameElements) or ("" in nameElements):
            print("error!")
        else:
            print(self.firstName + " " + self.lastName)

person1 = Person("Yoshio", "Nakamura")
person1.showFullName()

person2 = Person()
person2.showFullName()

person3 = Person("", "Tanaka")
person3.showFullName()

person4 = Person(firstName = "Yoshito", lastName = "Kamizato")
person4.showFullName()
