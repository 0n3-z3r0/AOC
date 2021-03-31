import sys
group_answers = []
answers = []
lettercount = []
tbsum = []


#for letter in self[counter]:
#    print(letter)


def recursive_check(self,iterable, counter, max):
        print("start_recursion")
        #print(iterable)
        #print(self)
        #print(max)

        #print(counter)
        #print(self in iterable[counter])

        if self in iterable[counter]:
         #   print("again")
            counter += 1

            if counter == max:
          #      print("out")
                return self
            else:
                return recursive_check(self, iterable, counter, max)

def lettercheck_simple(self):
    letters = []
    for data in self:
        for letter in data:
            if letter in letters:
                continue
            else:
                letters.append(letter)
    return(letters)

def lettercheck_adv(self):
    iterable_answers = len(self)
    # print(iterable_answers)
    checked = []
    #print(iterable_answers)
    for data in self:
      #  print(data)
        for letter in data:
       #     print(letter)
            x = recursive_check(letter, self, 0, iterable_answers)
            print(x)
            checked.append(x)

    for letter_checked in checked:



    return checked



list=['su', 'egu']

print(lettercheck_adv(list))











sys.exit()
with open("input_6") as file:
    for line in file:
        line = line.strip()

        #print(line)

        if line == "":
            group_answers.append(answers)

            answers = []
            continue
        else:
            answers.append(line)
            #print(answers)
    group_answers.append(answers)
    #print(group_answers)
    counter = 0
    print(group_answers)
    for group in group_answers:
        print(lettercheck_adv(group))


