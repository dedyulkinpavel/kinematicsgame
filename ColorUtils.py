import pygame

def to_str(color_int):
    color = int_to_rgb(color_int)
    return f'RGB({color.r}:{color.g}:{color.b})'

def from_str(color_str):
    result = list(map(int, color_str[4:-1].split(':')))
    return rgb_to_int(result[0], result[1], result[2])

def rgb_to_int(r, g, b):
    """Упаковывает RGB в одно целое число"""
    return (r << 16) | (g << 8) | b

def int_to_rgb(color_int):
    """Распаковывает целое число обратно в RGB"""
    r = (color_int >> 16) & 0xFF  #0xFF = 255 в десятичной, 11111111 в двоичной
    g = (color_int >> 8) & 0xFF
    b = color_int & 0xFF
    return pygame.Color(r, g, b)

