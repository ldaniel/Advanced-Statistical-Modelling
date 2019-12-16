import unittest
from src.exercises.exercise_2_cpf_checker import CPFChecker as CPFCheckerClass


class Test_CPF_Checker(unittest.TestCase):
    def test_valid_cpf(self):
        input_cpf = "86282573068"
        cpf_checker = CPFCheckerClass(input_cpf)
        self.assertEqual(cpf_checker.is_valid(), True)

    def test_invalid_cpf(self):
        input_cpf = "86282573067"
        cpf_checker = CPFCheckerClass(input_cpf)
        self.assertEqual(cpf_checker.is_valid(), False)

    def test_invalid_cpf_equal_numbers(self):
        input_cpf = "11111111111"
        cpf_checker = CPFCheckerClass(input_cpf)
        self.assertEqual(cpf_checker.is_valid(), False)

    def test_invalid_cpf_wrong_len(self):
        input_cpf = "1234"
        cpf_checker = CPFCheckerClass(input_cpf)
        self.assertEqual(cpf_checker.is_valid(), False)

    def test_invalid_cpf_only_digits(self):
        input_cpf = "a6282573068"
        cpf_checker = CPFCheckerClass(input_cpf)
        self.assertEqual(cpf_checker.is_valid(), False)


if __name__ == '__main__':
    unittest.main()
