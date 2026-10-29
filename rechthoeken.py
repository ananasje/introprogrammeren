def is_same_rectangle(ax_length: int, ay_length: int,
                      bx_length: int, by_length: int) -> bool:
    """
    Controleert of de lengtes van de zijdes gelijk zijn.

    >>> is_same_rectangle(3, 2, 3, 2)
    True
    >>> is_same_rectangle(7, 8, 6, 7)
    False
    """
    return ax_length == bx_length and ay_length == by_length


def is_same_square(ax_length: int, ay_length: int,
                   bx_length: int, by_length: int) -> bool:
    """
    >>> is_same_square(7, 7, 7, 7)
    True
    >>> is_same_square(7, 4, 7, 4)
    False
    """
    return (is_same_rectangle(ax_length, ay_length, bx_length, by_length)
        and ax_length == ay_length )

def calculate_length(c1: int, c2: int) -> int:
    """
    >>> calculate_length(0, 2)
    2
    >>> calculate_length(5, 3)
    2
    """
    return abs(c2 - c1)


if __name__ == '__main__':
    ax1 = int(input("Geef de x1 van A: "))
    ax2 = int(input("Geef de x2 van A: "))
    ay1 = int(input("Geef de y1 van A: "))
    ay2 = int(input("Geef de y2 van A: "))

    bx1 = int(input("Geef de x1 van B: "))
    bx2 = int(input("Geef de x2 van B: "))
    by1 = int(input("Geef de y1 van B: "))
    by2 = int(input("Geef de y2 van B: "))

    ax_length = calculate_length(ax1, ax2)
    ay_length = calculate_length(ay1, ay2)
    bx_length = calculate_length(bx1, bx2)
    by_length = calculate_length(by1, by2)

    if is_same_rectangle(ax_length, ay_length, bx_length, by_length):
        print("De rechthoeken zijn gelijk!")

        if is_same_square(ax_length, ay_length, bx_length, by_length):
            print("En ze zijn ook nog vierkant!")
    else:
        print("Er is niks aan :(")