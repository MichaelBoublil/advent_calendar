mapping_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def get_letter_digit(line, start_index):
    for digit in mapping_digits.keys():
        if start_index + len(digit) > len(line):
            continue
        if line[start_index:start_index + len(digit)] == digit:
            return digit

    return None

def get_digit(line, index):
    if line[index].isdigit():
        return line[index]

    letter_digit = get_letter_digit(line, index)
    if letter_digit is not None:
         return mapping_digits[letter_digit]

    return None

def find_calibration_value(line):
    first = None
    last = None
    for i in range(0, len(line)):
        first = get_digit(line, i)
        if first is not None:
            break

    for i in range(len(line) - 1, -1, -1):
        last = get_digit(line, i)
        if last is not None:
            break

    return int(first + last)


sum = 0
with open("inputs/lala.txt", "r") as f:
    for line in f.readlines():
        sum += find_calibration_value(line.strip())

print(sum)