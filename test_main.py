import unittest
from unittest.mock import patch
from main import (
    Train,
    quantity_input,
)


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train()

    def test_initial_variables(self):
        self.assertEqual(self.train.position, 0)

    def test_mover_valid_commands(self):
        position = self.train.move(["DIREITA", "ESQUERDA", "DIREITA"])
        self.assertEqual(position, 1)

    def test_consecutive_movements_limit(self):
        position = self.train.move(["DIREITA"] * 21)
        self.assertLessEqual(self.train.consecutive_movements, 21)
        self.assertEqual(position, 20)

    def test_movement_limit(self):
        position = self.train.move(
            [
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "ESQUERDA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
                "DIREITA",
            ]
        )
        self.assertLessEqual(self.train.movements, 50)
        self.assertEqual(position, 10)


class TestQuantityInput(unittest.TestCase):
    def test_invalid_integer(self):
        # Testar se a função aceita apenas números válidos
        with patch("builtins.input", side_effect=["abc", "", "-1", "5"]):
            self.assertEqual(quantity_input(), 5)


if __name__ == "__main__":
    unittest.main()

# python -m unittest test_main.py
