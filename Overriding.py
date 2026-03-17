class Calculator:
    @staticmethod
    def add(*args):
        print(sum(args))

Calculator.add(2,3)
Calculator.add(2,3,4)
Calculator.add(2,3,4,5)
