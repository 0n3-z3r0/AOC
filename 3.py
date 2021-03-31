liste = []
counter_right = 0
counter_down = 0
counter_tree = 0
counter_loops = 0

def next_round():
    global counter_down
    counter_down = counter_down + 2
    global counter_right
    counter_right = counter_right +1

with open("input_3") as file:
    for line in file:
        liste.append(line.strip())

    for element in liste:
        if counter_loops == 0:
            counter_loops =+ 1
            next_round()
            continue
        if element != liste[counter_down]:
            continue
        else:
            if counter_right >= len(element):
                counter_right = counter_right - len(element)
            if element[counter_right] == "#":
                next_round()
                counter_tree += 1
            else:
                next_round()
    print(counter_tree)
