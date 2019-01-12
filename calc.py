class Calc(object):
    def __init__(self, operand="+"):
        calcs = {
            "+":self.add,
            "-":self.sub,
            "*":self.multi,
            "/":self.div,
        }
        self.calc = calcs[operand]

    def add(self, a,b):
        return a+b

    def sub(self, a,b):
        return a-b

    def multi(self, a,b):
        return a*b

    def div(self, a,b):
        return a/b

def main():
    calc = Calc(input("input operator : "))
    a = float(input("input number a : "))
    b = float(input("input number b : "))
    print(calc.calc(a,b))

if __name__ == '__main__':
    main()
