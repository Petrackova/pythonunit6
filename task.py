"""Реализация класса."""


class Tasks:
    """Класс Task"""

    def find_max_average(self, numbers1, numbers2):
        """Сравнение среднего значения двух списков"""
        if not isinstance(numbers1, list) or not isinstance(numbers2, list):
            raise TypeError("Введите список.")
        if numbers1 and numbers2:
            if (sum(numbers1) / len(numbers1)) > (sum(numbers2) / len(numbers2)):
                return 'Первый список имеет большее среднее значение'
            if (sum(numbers1) / len(numbers1)) < (sum(numbers2) / len(numbers2)):
                return 'Второй список имеет большее среднее значение'
            return 'Средние значения равны'
        return 'Пустой список'
