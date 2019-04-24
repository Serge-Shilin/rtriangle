def is_right_angle(x0, y0, x1, y1, x2, y2):
    """декартово произведение 2-х перепендикулярных векторов должно равнятся 0"""
    return (int(x1) - int(x0)) * (int(x2) - int(x0)) + (int(y1) - int(y0)) * (int(y2) - int(y0)) == 0


def test_is_triangle_right(coordinates):
    """параметры координат векторов для 3 углов треугольника"""
    params = [['x0','y0','x1', 'y1', 'x2', 'y2'], ['x1','y1','x0', 'y0', 'x2', 'y2'], ['x2','y2','x1', 'y1', 'x0', 'y0']]
    is_rtriangle = False
    for p in params:
        if is_right_angle(coordinates[p[0]], coordinates[p[1]],coordinates[p[2]], coordinates[p[3]],coordinates[p[4]],
                      coordinates[p[5]]):
            is_rtriangle = True
            break
    assert is_rtriangle, 'Triangle is not right'
