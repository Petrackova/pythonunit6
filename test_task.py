"""Модуль, предоставляющий функцию печати версии python."""
from unittest import TestCase
import pytest
from task import Tasks


class TestAverage(TestCase):
    """Проверка тестов для task"""
    average = Tasks()

    def test_find_average(self):
        """Средние значения списков равны"""
        assert self.average.find_max_average([10,
                                              20,
                                              30,
                                              40,
                                              50],
                                             [10,
                                              20,
                                              30,
                                              40,
                                              50]) == 'Средние значения равны'

    def test_find_average_1(self):
        """Среднее значение второго списка больше """
        assert self.average.find_max_average([10,
                                              20,
                                              30,
                                              40],
                                             [10,
                                              20,
                                              30,
                                              40,
                                              50]) == 'Второй список имеет большее среднее' \
                                                                      ' значение'

    def test_find_average_2(self):
        """Среднее значение первого списка больше """
        assert self.average.find_max_average([10,
                                              20,
                                              30,
                                              40,
                                              50],
                                             [10,
                                              20,
                                              30,
                                              40]) == 'Первый список имеет большее среднее' \
                                                                  ' значение'

    def test_find_average_3(self):
        """Ошибка типа данных """
        with pytest.raises(TypeError):
            assert self.average.find_max_average('Не лист', "Not a list")

    def test_find_average_4(self):
        """Пустой список 1 """
        assert self.average.find_max_average([], [10, 20, 30, 40]) == 'Пустой список'

    def test_find_average_5(self):
        """Пустой список 2 """
        assert self.average.find_max_average([10, 20, 30, 40, 50], []) == 'Пустой список'

    def test_find_average_6(self):
        """Пустые списки"""
        assert self.average.find_max_average([], []) == 'Пустой список'

    def test_find_average_7(self):
        """Второй список имеет большее среднее значение"""
        assert self.average.find_max_average([0],
                                             [5]) == 'Второй список имеет большее среднее значение'

    def test_find_average_8(self):
        """Средние значения списков равны"""
        assert self.average.find_max_average([5], [5]) == 'Средние значения равны'

    def test_find_average_9(self):
        """Ошибка типа данных"""
        with pytest.raises(TypeError):
            assert self.average.find_max_average(5, 5)
