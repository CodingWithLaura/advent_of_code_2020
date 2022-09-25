def einlesen(input_path):
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()

    numbers_to_check = []
    for line in input_data_lines:
        new_number = int(line.replace("\n",""))
        numbers_to_check.append(new_number)
    return numbers_to_check

def check_number_in_window(window, number_to_check):
    results = []
    for i in range(0,len(window)):
        for j in range(i+1,len(window)):
            new_number = window[i] + window[j]
            if new_number == number_to_check:
                return True
    return False

def is_number_a_sum_of_window_numbers(numbers,window_size):
    i = 0
    while i < (len(numbers)-window_size):
        window = []
        for j in range(0,window_size):
            x = numbers[i + j]
            window.append(x)
        number = numbers[i+window_size]
        isok = check_number_in_window(window,number)
        if isok == False:
            print(number)
        i += 1

def main():
    numbers = einlesen("input.txt")
    result = is_number_a_sum_of_window_numbers(numbers,25)
            
if __name__ == "__main__":
    main()
