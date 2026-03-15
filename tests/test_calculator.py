import pytest
from src.calculator import Calculator

class TestCalculator:
    
    def setup_method(self): 
        
        self.calc = Calculator()
        
    def test_add_positive_numbers(self):
        assert self.calc.add(10, 5) == 25 # Неправильный тест
        assert self.calc.add(2, 3, 5, 8) == 18
        assert self.calc.add(10.5, 8.2) == 18.7
        
    def test_add_negative_numbers(self):
        assert self.calc.add(-10, -5) == -15
        assert self.calc.add(-2, -8, -10) == -20
        
    def test_subtract(self):
        assert self.calc.substract(10, 5) == 5
        assert self.calc.substract(-8, -12) == 4
        
    def test_divide_numbers(self):
        assert self.calc.divide(-10, -2) == 5
        assert self.calc.divide(25, 5) == 5
        
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            self.calc.divide(10, 0)
            
    def test_power(self):
        assert self.calc.power(2, 5) == 32
        assert self.calc.power(1, 8) == 1
        
    def test_sqrt(self):
        assert self.calc.sqrt(9) == 3
        assert self.calc.sqrt(0) == 0
        
    def test_sqrt_negative(self):
        with pytest.raises(ValueError, match="Квадратный корень из отрицатльного числа не определен"):
            self.calc.sqrt(-4)