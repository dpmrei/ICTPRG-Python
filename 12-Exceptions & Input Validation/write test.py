with open ('ages.txt', 'w') as ages:
    for i in range (1,5):
        ages_in = input('input age:\t')
        ages.writelines(f'{ages_in}\n')

