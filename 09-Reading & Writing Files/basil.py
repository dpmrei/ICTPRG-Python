with open("names.txt","r") as reader, open("names_formatted.txt", "w") as output:
    lines = reader.readlines()
    count = 0
    for line in lines:
        count += 1
        statement  = "{}: {}".format(line.strip(), line.strip().title()) + "\n"
        output.write(statement)
        print(statement)