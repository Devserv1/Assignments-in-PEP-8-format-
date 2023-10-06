#!/usr/bin/env python
# coding: utf-8

# # QUESTION 3:


class BankAccount():
    def __init__(self,name,initial_amount):
        self.name=name
        self.initial_amount=initial_amount
    def Display_balance(self):
        print(f"{self.name}:{self.initial_amount}")
              
    def Deposit(self,new_amount):
              initial_amount+=new_amount
              self.Display_balance()
              
    def Withdraw (self,withdrawal_amount):
        if withdrawal_amount <= initial_amount:
              initial_amount-= withdrawal_amount
        else:
              raise ValueError(" Insufficient balance in account")
              
    def Transfer(self,second_account,transfer_amount):
        if transfer_amount <= initial_amount:
              second_account.initial_amount+=transfer_amount
              self.initial_amount-=transfer_amount
              second_account.Display_balance()
              self.Display_balance()
        else:
              raise ValueError(" Insufficient amount in sender's account")
              
              
              
        
class InterestRewardAcc(BankAccount):
    def __init__(self,name,initial_amount):
        super().__init__(name,initial_amount)
        
    def add_benefit(self):
        interest=self.initial_amount*0.05
        initial_amount+=interest
        
    def deposit(self,new_amount):
        super().Deposit(new_amount)
        self.add_benefit()
    


class SavingsAcc(InterestRewardAcc):
    def __init__(self,name,initial_amount):
        super().init(name,initial_amount)
        
        
    
        
    def withdraw(self,withdrawal_amount):
        super().withdraw(withdrawal_amount-5)
        
        
    
        
# # QUESTION 2


class M():
    def process(self):
        print("M Process")
    pass

class A(M):
    def process(self):
        print("A Process")
    pass

class B(M):
    def process(self):
        print("B Process")
    pass

class X(A):
    def process(self):
        print("X Process")
    pass

class Y(A,B):
    def process(self):
        print("Y Process")
    pass

class Z(B,M):
    def process(self):
        print("Z Process")
    pass

class Final(X,Y,Z):
    def process(self):
        print("Final Process")
    pass

obj=Final()
obj.process()


# Above is the MRO created for part 1.Only condition when it can fail is if we dont have any attribute in class M(the base class).



class C():
    def process(self):
        print("C process")
    pass

class B(C):
    def process(self):
        print("B process")
    pass

class A(B,C):
    def process(self):
        print("A process")
    pass

obj=A()
obj.process()
    


# Above is the MRO for part 2. Only condition in which MRO can not be created is when there is no attribute in base class(class C)
# 

# # QUESTION 1



import math
def complex_mathematics(a,b,c,d):
    real_sum=round(a+c,2)
    imaginary_sum=round(b+d,2)
    print(f"Addition: {real_sum}+{imaginary_sum}i")
    
    real_subtract=round(a-c,2)
    imaginary_subtract=round(b-d,2)
    print(f"Subtraction: {real_subtract}+{imaginary_subtract}i")
    
    real_multiply=round(a*c-b*d,2)
    imaginary_multiply=round(a*d+b*c,2)
    print(f"multiplication: {real_multiply}+{imaginary_multiply}i")
    
    denominator = c**2 + d**2
    real_divide = round((a * c + b * d) / denominator, 2)
    imaginary_divide = round((b * c - a * d) / denominator, 2)
    print(f"Division: {real_divide} + {imaginary_divide}i")
    
    modulus_1 = round(math.sqrt(a**2 + b**2), 2)
    modulus_2 = round(math.sqrt(c**2 + d**2), 2)
    print(f"Modulus: {modulus_1}")
    print(f"Modulus: {modulus_2}")


# # QUESTION 4


class FormulaError(Exception):
    pass

def parse_input(user_input):
    inputs_part=user_input.split()
    
    if len(inputs_part)!=3:
        raise FormulaError("Invalid input. Please provide a formula with 3 elements.")
    
    n1, op, n2 = inputs_part
    
    try:
        n1=float(n1)
        n2=float(n2)
    except ValueError:
        raise FormulaError("Error. First and third input should be integer")
    
    if op not in ['+', '-']:
        raise FormulaError("Error. Only '+' or '-' operators allowed.")
    
    return n1, op, n2

def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2


while True:
    user_input = input('>>> ')
    if user_input == 'quit':
        break
    
    try:
        n1, op, n2 = parse_input(user_input)
        result = calculate(n1, op, n2)
        print(result)
    except FormulaError as e:
        print(f"Error: {e}")
        
   




