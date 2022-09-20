def einlesen(input_path):
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()

    numbers_to_check = []
    for line in input_data_lines:
        new_number = int(line.replace("\n",""))
        numbers_to_check.append(new_number)
    return numbers_to_check

def check_number_in_window(window, number_to_check):
    for n in range(0, len(window)):
        number_1 = window[n]
        for m in range(0,len(window)):
            number_2 = window[m]
            if number_1 + number_2 == number_to_check:
                return True
            else:
                return False

def is_number_a_sum_of_window_numbers(numbers):
    i = 0
    while i < (len(numbers) - 6):
        x1 = numbers[i]
        x2 = numbers[i+1]
        x3 = numbers[i+2]
        x4 = numbers[i+3]
        x5 = numbers[i+4]
        window = [x1,x2,x3,x4,x5]
        number = numbers[i+5]
        isok = check_number_in_window(window,number)
        print(isok)
        if isok == False:
            print("yeah")
        i += 1
    

def main():
    numbers = einlesen("small_input.txt")
    print(numbers)
    result = is_number_a_sum_of_window_numbers(numbers)
    print(result)

if __name__ == "__main__":
    main()
