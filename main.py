import json


class Rect():
    """Четырехугольник с полями-координатами"""

    def __init__(self, x1, x2, y1, y2):
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)

    def set_coordinate(self, x1, x2, y1, y2):
        """изменение координат (не используется)"""
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)

    def print(self):
        """вывод полей координат"""
        print(self.x1, self.x2, self.y1, self.y2, sep=', ')

    def intersection(self, rec):
        """пересечение с переданным четырехугольником"""
        inter = Rect(0, 0, 0, 0)  # результат пересечения
        # по оси Ох
        if self.x1 >= rec.x1 and self.x1 <= rec.x2 and rec.x2 >= self.x1 and rec.x2 <= self.x2:
            inter.x1 = self.x1
            inter.x2 = rec.x2
        elif self.x2 >= rec.x1 and self.x2 <= rec.x2 and rec.x1 >= self.x1 and rec.x1 <= self.x2:
            inter.x1 = rec.x1
            inter.x2 = self.x2
        elif self.x1 >= rec.x1 and self.x1 <= rec.x2 and self.x2 >= rec.x1 and self.x2 <= rec.x2:
            inter.x1 = self.x1
            inter.x2 = self.x2
        elif rec.x1 >= self.x1 and rec.x1 <= self.x2 and rec.x2 >= self.x1 and rec.x2 <= self.x2:
            inter.x1 = rec.x1
            inter.x2 = rec.x2
        else:
            return None
        # по Оси Оу
        if self.y1 >= rec.y1 and self.y1 <= rec.y2 and rec.y2 >= self.y1 and rec.y2 <= self.y2:
            inter.y1 = self.y1
            inter.y2 = rec.y2
        elif self.y2 >= rec.y1 and self.y2 <= rec.y2 and rec.y1 >= self.y1 and rec.y1 <= self.y2:
            inter.y1 = rec.y1
            inter.y2 = self.y2
        elif self.y1 >= rec.y1 and self.y1 <= rec.y2 and self.y2 >= rec.y1 and self.y2 <= rec.y2:
            inter.y1 = self.y1
            inter.y2 = self.y2
        elif rec.y1 >= self.y1 and rec.y1 <= self.y2 and rec.y2 >= self.y1 and rec.y2 <= self.y2:
            inter.y1 = rec.y1
            inter.y2 = rec.y2
        else:
            return None
        return inter


def create_json_result_file(result_rec):
    """Создание выходного json-файла"""
    data = {}
    if result_rec:
        data['rects'] = []
        data['rects'].append({
            'x1': result_rec.x1,
            'x2': result_rec.x2,
            'y1': result_rec.y1,
            'y2': result_rec.y2
        })
    else:
        data['rects'] = []
        data['rects'].append({
            'x1': 'empty',
            'x2': 'empty',
            'y1': 'empty',
            'y2': 'empty'
        })
    with open('data_result.txt', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    try:
        with open('data_input.txt') as json_file:
            data = json.load(json_file)

            if data['rects'][0]['x1'] == data['rects'][0]['x2'] or data['rects'][0]['y1'] == data['rects'][0]['y2']:
                raise Exception('Несуществующий четерыхугольник!!!')

            result_rec = Rect(data['rects'][0]['x1'], data['rects'][0]['x2'], data['rects'][0]['y1'],
                              data['rects'][0]['y2'])
            for rec in data['rects']:
                if rec['x1'] == rec['x2'] or rec['y1'] == rec['y2']:
                    raise Exception('Несуществующий четерыхугольник!!!')
                result_rec = result_rec.intersection(Rect(rec['x1'], rec['x2'], rec['y1'], rec['y2']))
                if not (result_rec):
                    break
        create_json_result_file(result_rec)

    except Exception as ex:
        print("Ошибка открытия json-файла")
        print(ex)
