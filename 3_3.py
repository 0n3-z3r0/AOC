import sys

liste = []
counter_right = 0
counter_down = 0
counter_tree = 0
slope_counter = 0
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counter_loops = 0

result = []

def next_round():
    global slopes
    global counter_down
    counter_down = counter_down + slopes[slope_counter][1]
    global counter_right
    counter_right = counter_right + slopes[slope_counter][0]

def next_slope():
    global slope_counter
    slope_counter += 1

def counter_reset():
    global counter_down
    global counter_right
    global counter_tree
    global counter_loops

    counter_tree = 0
    counter_loops = 0
    counter_right = 0
    counter_down = 0

with open("input_3") as file:
    for line in file:
        liste.append(line.strip())
    for slope in slopes:
        print("slope")
        print(counter_tree)
        counter_reset()
        for element in liste:
            if counter_loops == 0:
                counter_loops += 1
                next_round()
                continue
            if element != liste[counter_down]:
                continue
            else:
                if counter_right >= len(element):
                    counter_right = counter_right - len(element)
                if counter_down >= len(liste):
                    break
                if element[counter_right] == "#":
                    next_round()
                    counter_tree += 1
                else:
                 #   print(slope_counter)
                 #   print(counter_right)
                    next_round()
        result.append(counter_tree)
        next_slope()

    print(result)

    x = 1

    for i in result:
        if i != 0:
            x = x*i

    print(x)
