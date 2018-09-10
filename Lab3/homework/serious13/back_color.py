from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    r = choice(shapes)
    r1 = choice(shapes)
    return [
                r['text'],
                r1['color'],
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    click = ""
    code = ''
    if 20 <= x <= 120 and 60 <= y <= 160:
        click = "blue"
        code = 'blue'
    elif 140 <= x <= 240 and 60 <= y <= 160:
        click = "red"
        code = '#C62828'
    elif 140 <= x <= 240 and 180 <= y <= 280:
        click = "green"
        code = '#4CAF50'
    elif 20 <= x <= 120 and 180 <= y <= 280:
        click = "yellow"
        code = '#FFD600'

    if quiz_type == 0 and click == text:
        return True
    elif quiz_type == 1 and code == color:
        return True
    else:
        return False

    return True
