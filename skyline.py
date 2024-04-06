def process_inputs(input_lists):
    height = []
    left = []
    right = []
    for line in input_lists:
        inputs = line.split(', ')
        height.append(inputs[0])
        left.append ((inputs[1], (-inputs[0])))
        right.append((inputs[2], inputs[0]))

    return height, left, right

def skyline(height, left, right):
    points = []

height, left, right = process_input(input_lists)
points = skyline(height, left_right)
# Hi , Lxi , Rxi
input_lists = [
    (6, 1, 6),
    (8, 3, 5),
    (4, 4, 9),
    (2, 7, 12)
    (7, 11, 14),
]