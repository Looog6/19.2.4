import pytest
from Calculator.app.calc import Calculator


# def test_sum():              #тест
#     assert 2 + 2 == 4

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_success(self):
        assert self.calc.multiply(5, 5) == 25

    def test_division_success(self):
        assert self.calc.division(10, 5) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(5, 1) == 4

    def test_adding_success(self):
        assert self.calc.adding(2, 2) == 4

    def test_multiply_unsuccess(self):
        assert self.calc.multiply(5, 5) == 20

    def test_division_unsucces(self):
        assert self.calc.division(10, 5) == 5

    def test_subtraction_unsuccess(self):
        assert self.calc.subtraction(5, 1) == 5

    def test_adding_unsuccess(self):
        assert self.calc.adding(2, 2) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
