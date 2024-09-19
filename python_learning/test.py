def process(input_string: str) -> str:
    above_zero = 0
    below_zero = 0
    equal_zero = 0

    input_list = input_string.split()
    for item in input_list:
        if item.isdigit():
            if int(item) > 0:
                above_zero += 1
            elif int(item) < 0:
                below_zero += 1
            elif int(item) == 0:
                equal_zero += 1

    return f'выше нуля: {above_zero}, ниже нуля: {below_zero}, равна нулю: {equal_zero}'

#process('5 -2 0 0 7 8 -1')
input_string = input()
output_string = process(input_string)
print(output_string)
