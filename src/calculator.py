class Calculator:
    
    @staticmethod
    def add(*args):
        sum = 0
        for i in args:
            sum += i
        
        return sum
    
    @staticmethod
    def multiply(*args):
        res = 1
        for i in args:
            res *= i
        
        return res
    
    @staticmethod
    def substract(a, b):
        return a - b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    @staticmethod
    def sqrt(a):
        if a < 0:
            raise ValueError("Квадратный корень из отрицатльного числа не определен")
        
        return a ** 0.5
    
    