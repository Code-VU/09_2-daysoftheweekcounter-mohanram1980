def countDayOfTheWeek():
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print('File cannot be opened:', fname)
        exit()

    dictionary_days = dict()
    for line in fhand:
        words = line.split()
        if len(words) < 3 or words[0] != 'From':
            continue
        else:
            if words[2] not in dictionary_days:
                dictionary_days[words[2]] = 1
            else:
                dictionary_days[words[2]] += 1

    print(dictionary_days)



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
