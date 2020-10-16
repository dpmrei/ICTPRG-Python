
names = open('names.txt', 'w')

names.write('lAchlan velDen\n')
names.write('Frank joe\n')
names.write('dOnAld TRump\n')

names.close()

names = open('names.txt', 'r')

formatted = open('names-formatted.txt', 'w')

for line in names:
    fixed = line.title()
    output = (f'{line.strip()} -> {fixed}\n')
    formatted.write(output)

names.close()
formatted.close()