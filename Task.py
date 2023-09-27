class Tasks:

    def find_max_average(self, numbers1: list, numbers2: list):
        if not isinstance(numbers1, list) or not isinstance(numbers2, list):
            raise TypeError("Введите список.")
        if numbers1 and numbers2:
            if (sum(numbers1) / len(numbers1)) > (sum(numbers2) / len(numbers2)):
                return 'Первый список имеет большее среднее значение'
            elif (sum(numbers1) / len(numbers1)) < (sum(numbers2) / len(numbers2)):
                return 'Второй список имеет большее среднее значение'
            elif (sum(numbers1) / len(numbers1)) == (sum(numbers2) / len(numbers2)):
                return 'Средние значения равны'
        else:
            return 0
