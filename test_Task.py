from unittest import TestCase
import pytest
from Task import Tasks


class TestAverage(TestCase):
    average = Tasks()

    def test_find_average(self):
        assert self.average.find_max_average([10, 20, 30, 40, 50], [10, 20, 30, 40, 50]) == 'Средние значения равны'

    def test_find_average_1(self):
        assert self.average.find_max_average([10, 20, 30, 40],
                                             [10, 20, 30, 40, 50]) == 'Второй список имеет большее среднее значение'

    def test_find_average_2(self):
        assert self.average.find_max_average([10, 20, 30, 40, 50],
                                             [10, 20, 30, 40]) == 'Первый список имеет большее среднее значение'

    def test_find_average_3(self):
        with pytest.raises(TypeError):
            assert self.average.find_max_average('Не лист', "Not a list")

    def test_find_average_4(self):
        assert self.average.find_max_average([], [10, 20, 30, 40]) == 0

    def test_find_average_5(self):
        assert self.average.find_max_average([10, 20, 30, 40, 50], []) == 0

    def test_find_average_6(self):
        assert self.average.find_max_average([], []) == 0

    def test_find_average_7(self):
        assert self.average.find_max_average([0], [5]) == 'Второй список имеет большее среднее значение'

    def test_find_average_8(self):
        assert self.average.find_max_average([5], [5]) == 'Первый список имеет большее среднее значение'

    def test_find_average_9(self):
        with pytest.raises(TypeError):
            assert self.average.find_max_average(5, 5)
