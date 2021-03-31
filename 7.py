class Bags:
    def __init__(self):
        self.number = self.split(" ")[0]
        self.type = self.split(" ")[1]
        self.color = self.split(" ")[2]

    print(self.number + self.type + self.color)

 #   _
#    self.counter = self.split(" ")


with open ("input_7") as file:
    for line in file:
        if "shiny gold bag" in line:
            line_splitted = line.strip().split(", ")
            print(line_splitted)
            for element in line_splitted:
                if " contain " in element:
                    element = element.split(" contain ")
                    print(element[0])