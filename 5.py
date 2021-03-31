import sys

binary = []
row = []
columns = []
for i in range(0, 128):
    row.append(i)

for i in range(0, 8):
    columns.append(i)

def split_list(self):
    half = len(self)//2
    return self[:half], self[half:]

def seatfinder(self):

    if len(self) == 7:
        i = row
    else:
        i = columns

    for bit in self:

        if bit == 0:
            i = split_list(i)[0]
        else:
            i = split_list(i)[1]
    return(i)

with open("input_5")as file:
    for line in file:
        binary_tmp = []
        binary.append(binary_tmp)
        print (line)
        for data in line:
            data = data.strip()

            if data == "F" or data == "B":

                if data == "F":
                    binary_tmp.append(0)
                elif data == "B":
                    binary_tmp.append(1)
            else:
                if data == "L":
                    binary_tmp.append(0)
                elif data == "R":
                    binary_tmp.append(1)
        print(binary_tmp)

    seats_taken = []

    print(binary)

    for data in binary:
        seatrow = seatfinder(data[0:7])
        seatcolumn = seatfinder(data[7:])
        print(seatcolumn)

        seat_id = int(seatrow[0]) *8 + seatcolumn[0]

        seats_taken.append(seat_id)

    print(seats_taken)
    print(max(seats_taken))

    print(sorted(seats_taken))

    for element in range(0, 915):
        if element in seats_taken:
            continue
        else:
            print(element)

