from math import pi

__all__ = ['circle_perimetr', 'circle_area']


def circle_perimetr(default_radius=5):
    return 2 * pi * default_radius


def circle_area(default_radius=5):
    return pi * default_radius ** 2
