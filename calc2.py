
# another calculator
print("""Your choices are:
addition '+'
subtraction '-'
multiplication '*'
division '/'
powers '**'
""")

class Calc:

    operations = ('+', '-', '*', '/', '**')

    def __init__(self):
        self.x = None
        self.y = None
        self.op = None

    def run(self):
        self.prompt_op()
        self.prompt_x()
        self.prompt_y()

        if self.op == '+':
            return self.add()
        elif self.op == '-':
            return self.sub()
        elif self.op == '*':
            return self.mult()
        elif self.op == '/':
            return self.div()
        elif self.op == '**':
            return self.pow()
        else:
            raise ValueError("Wrong operation... %s" % self.op)


    def prompt_op(self):

        while self.op not in Calc.operations:
            self.op = input("Enter an operation " + ', '.join(Calc.operations) + ': ')

        # self.op = Calc.operations
        # self.op = input("Enter an operation: " + ', '.join(Calc.operations))
        # if self.op not in Calc.operations:
        #     raise ValueError("Sorry, wrong operation")
        # return self.op


    def prompt_x(self):

        while True:
            try:
                self.x = int(input("Enter a number: "))
            except ValueError:
                print("Sorry, wrong value. Try again... ")

        # try:
        #     int(input('Enter the first number: '))
        # except ValueError:
        #     print('Sorry, wrong value')
        # return self.x

    def prompt_y(self):

        while True:
            try:
                self.y = int(input("Enter a second number: "))
            except ValueError:
                print("Sorry, wrong value. Try again... ")
        # try:
        #     int(input('Enter a second number: '))
        # except ValueError:
        #     print('Sorry, wrong value')
        # return self.y


    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mult(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

    def pow(self):
        return self.x ** self.y


Calculator = Calc()
print(Calculator.run())
