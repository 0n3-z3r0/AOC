passport = {}

valid = 0




with open("input_4") as file:
    file = file.readlines()
    for line in file:
        line = line.strip().split(" ")

        if line == ['']:

            if passport.keys() >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
            #    print(passport.keys())
                valid += 1
                print(valid)

            else:
                pass
            #    print(passport.keys())
            passport = {}

        else:
            for data in line:
                data = data.split(":")
                passport[data[0]] = data[1]
           #     print(passport)







       # print(passport)
