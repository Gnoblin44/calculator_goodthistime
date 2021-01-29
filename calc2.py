
# second calculator
print("""Your choices are:
addition '+'
subtraction '-'
multiplication '*'
division '/'
powers '**'
""")

class Calc:

    op = ('+', '-', '*', '/', '**')

    def __init__(self):
        self.x = None
        self.y = None

    def run(self):
        while True:
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
                raise ValueError("Wrong operation, try again... ")

    def prompt_x(self):
        try:
            int(input('Enter the first number: '))
        except:
            print('Sorry, wrong value')
        return self.x

    def prompt_y(self):
        try:
            int(input('Enter a second number: '))
        except:
            print('Sorry, wrong value')
        return self.y


    def add(self):
        self.x + self.y































