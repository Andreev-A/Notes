"""Код программы рисования пейзажа"""
import graphics as gr


def main():
    window = gr.GraphWin("My Image", 600, 600)
    draw_image(window)
    window.getMouse()


def draw_image(window):
    house_x, house_y = window.width // 2, window.height * 2 // 3
    house_width = window.width // 3
    house_height = house_width * 4 // 3

    draw_background(window)
    draw_house(window, house_x, house_y, house_width, house_height)


def draw_background(window):
    earth = gr.Rectangle(gr.Point(0, window.height // 2),
                         gr.Point(window.width - 1, window.height - 1))
    earth.setFill("green")
    earth.draw(window)
    scy = gr.Rectangle(gr.Point(0, 0),
                       gr.Point(window.width - 1, window.height // 2))
    scy.setFill("cyan")
    scy.draw(window)


def draw_house(window, x, y, width, height):
    foundation_height = height // 8
    walls_height = height // 2
    walls_width = 7 * width // 8
    roof_height = height - walls_height - foundation_height

    draw_house_foundation(window, x, y, width, foundation_height)
    draw_house_walls(window, x, y - foundation_height,
                     walls_width, walls_height)
    draw_house_roof(window, x, y - foundation_height - walls_height,
                    width, roof_height)


def draw_house_foundation(window, x, y, width, height):
    foundation = gr.Rectangle(gr.Point(x - width // 2, y),
                              gr.Point(x + width // 2, y - height))
    foundation.setFill("brown")
    foundation.draw(window)


def draw_house_walls(window, x, y, width, height):
    walls = gr.Rectangle(gr.Point(x - width // 2, y),
                         gr.Point(x + width // 2, y - height))
    walls.setFill("red")
    walls.draw(window)
    draw_house_window(window, x, y - height // 4,
                      width // 3, height // 2)


def draw_house_window(window, x, y, width, height):
    glass = gr.Rectangle(gr.Point(x - width // 2, y),
                         gr.Point(x + width // 2, y - height))
    glass.setFill("blue")
    line1 = gr.Line(gr.Point(x, y), gr.Point(x, y - height))
    line2 = gr.Line(gr.Point(x - width // 2, y - height // 2),
                    gr.Point(x + width // 2, y - height // 2))
    glass.draw(window)
    line1.draw(window)
    line2.draw(window)
    line1.setOutline("black")
    line2.setOutline("black")
    line1.setWidth(2)
    line2.setWidth(2)


def draw_house_roof(window, x, y, width, height):
    roof = gr.Polygon(gr.Point(x - width // 2, y),
                      gr.Point(x + width // 2, y),
                      gr.Point(x, y - height))
    roof.setFill("green")
    roof.draw(window)


if __name__ == "__main__":
    main()

# Этот программный код нельзя назвать образцовым. Дело в том, что в функциях отсутствуют документ-строки, а
# документирование функций — это очень важно. Однако, в данном уроке нет цели обучить этому навыку. В ущерб
# перфекционизму мы здесь концентрируемся на парадигме структурного программирования, а особенно на навыке декомпозиции
# задачи и итеративном движении сверху-вниз.

def main():
    salary = calculate_salary()
    print(salary)


def calculate_salary():
    """
    Считает зарплату сотрудника ДПС, считывая исходные данные с клавиатуры.

    :returns: зарплата сотрудника
    """
    sum_of_fines = 0
    speed_of_auto, number_of_auto = read_data()
    while not detect_chief(number_of_auto):
        if speed_of_auto > 60:
            sum_of_fines += calculate_fine(number_of_auto)
        speed_of_auto, number_of_auto = read_data()
    return sum_of_fines


def read_data():
    """
    Считывает следущую строку данных.

    :returns: tuple(int, str) - скорость, номер машины
    """
    data = input().split()
    return data


def detect_chief(number_of_auto):
    """
    Проверяет, принадлежит ли данный номер начальнику.

    :param number_of_auto: номер автомобиля
    :returns: True, если номер принадлежит начальнику, иначе False
    """
    return number_of_auto == "A999AA"


def calculate_fine(number_of_auto):
    """
    Считает штраф для автомобиля с конкретным номером.

    :param number_of_auto: номер автомобиля
    :returns: Целое число, размер штрафа
    """
    if is_super_number(number_of_auto):
        return 1000
    elif is_good_number(number_of_auto):
        return 500
    else:
        return 100


def is_super_number(number_of_auto):
    """
    Проверяет, является ли номер «крутым» (совпадение трёх цифр)

    :param number_of_auto: номер автомобиля
    :returns: True, если номер «крутой», иначе False
    """
    return number_of_auto[1] == number_of_auto[2] == number_of_auto[3]


def is_good_number(number_of_auto):
    """
    Проверяет, является ли номер «хорошим» (совпадение двух цифр)

    :param number_of_auto: номер автомобиля
    :returns: True, если номер «хороший», иначе False
    """
    return number_of_auto[1] == number_of_auto[2] or \
           number_of_auto[1] == number_of_auto[3] or \
           number_of_auto[2] == number_of_auto[3]


if __name__ == "__main__":
    main()

