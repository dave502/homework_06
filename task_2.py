
class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        """
        :param length: длина (м)
        :param width:  ширина (м)
        """
        self._length = length
        self._width = width

    def get_asphalt_weight(self, weight_1m=25, depth=5):
        """
        расчет массы асфальта, необходимого для покрытия всего
        дорожного полотна
        :param weight_1m: int - вес одного метра асфальта (кг)
        :param depth: int - толщина слоя асфальта (см)
        :return: int - вес асфальта (тонны)
        """
        return self._length * self._width * weight_1m * depth / 1000


road = Road(width=20, length=5000)
print(f'{road.get_asphalt_weight()} т')
