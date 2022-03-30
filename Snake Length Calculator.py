import sys

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")
values = inputFile.read().split(" ")
for i in range(len(values)):
    try:
        values[i] = int(values[i])
    except ValueError:
        outputFile.write("Invalid data")
        sys.exit()

WIDTH, HEIGHT, X, Y = values

if 1 > WIDTH or HEIGHT > 20000 or 0 > X or X > WIDTH or 0 > Y or Y > HEIGHT:
    outputFile.write("Invalid data")
    sys.exit()

def get_next_cell(current_cell, direction):
    next_cell = [current_cell[0], current_cell[1]]
    if direction == "right":
        next_cell[0] = current_cell[0] + 1
        return next_cell
    if direction == "down":
        next_cell[1] = current_cell[1] + 1
        return next_cell
    if direction == "left":
        next_cell[0] = current_cell[0] - 1
        return next_cell
    if direction == "up":
        next_cell[1] = current_cell[1] - 1
        return next_cell

def change_direction(current_direction):
    directions = ["right", "down", "left", "up"]
    return directions[(directions.index(current_direction) + 1) % len(directions)]

direction = "right"
checked_cells = []
current_cell = [0, 0]

while current_cell != [X, Y]:
    checked_cells.append([current_cell[0], current_cell[1]])
    if current_cell[0] == WIDTH - 1 and direction == "right" or current_cell[0] == 0 and direction == "left" or current_cell[1] == HEIGHT - 1 and direction == "down" or current_cell[1] == 0 and direction == "up":
        direction = change_direction(direction)
    if get_next_cell(current_cell, direction) not in checked_cells:
        current_cell = get_next_cell(current_cell, direction)
    else:
        direction = change_direction(direction)
        current_cell = get_next_cell(current_cell, direction)

checked_cells.append([current_cell[0], current_cell[1]])
outputFile.write(f"{len(checked_cells)}")