
# another calculator
print("""
Your choices are:
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
        """
        The self.prompts are taken from the bottom functions and placed in here.
        This is pretty cool as pretty much every programming languages read top to bottom.
        But, the class function is different and this can confuse beginners (which means me).
        """

        self.prompt_op()
        self.x = self.prompt_x()
        self.y = self.prompt_y()

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
        # else:
        #     print("Wrong operation... ")


    def prompt_op(self):

        while self.op not in Calc.operations:
            self.op = input("Enter an operation " + ', '.join(Calc.operations) + ': ')
            if self.op not in Calc.operations:
                print("Wrong operation... ")


        # self.op = Calc.operations
        # self.op = input("Enter an operation: " + ', '.join(Calc.operations))
        # if self.op not in Calc.operations:
        #     raise ValueError("Sorry, wrong operation")
        # return self.op


    def prompt_x(self):
        while True:
            try:
                return int(input("Enter a number: "))
            except ValueError:
                print("Sorry, wrong value. Try again... ")


    def prompt_y(self):
        while True:
            try:
                return int(input("Enter a second number: "))
            except ValueError:
                print("Sorry, wrong value. Try again... ")


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
