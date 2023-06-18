import pytest
from Calculator.app.calc import Calculator


# def test_sum():              #тест
#     assert 2 + 2 == 4

class TestCalc:
    def setup(self):
        self.calc = Calculator()
# Положительные тесты
    def test_multiply_success(self):
        assert self.calc.multiply(7, 7) == 49

    def test_division_success(self):
        assert self.calc.division(20, 5) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(9, 5) == 4

    def test_adding_success(self):
        assert self.calc.adding(2, 2) == 4
# Отрицателные тесты
    def test_multiply_unsuccess(self):
        assert self.calc.multiply(7, 7) == 47

    def test_division_unsucces(self):
        assert self.calc.division(20, 5) == 15

    def test_subtraction_unsuccess(self):
        assert self.calc.subtraction(9, 5) == 5

    def test_adding_unsuccess(self):
        assert self.calc.adding(2, 2) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)

    def teardown(self):
        print('Выполнение метода Teardown')
