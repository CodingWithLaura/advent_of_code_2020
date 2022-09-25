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
        index = i+window_size    
        number = numbers[index]
        isok = check_number_in_window(window,number)
        if isok == False:
            return ((number, index))
        i += 1
    return (0, 0)

def is_number_sum_of_contiguous_numbers(number, numbers, index):
    for i in range(0, len(numbers) - 1):
        sum = numbers[i]
        j = 1
        while (sum < number):
            if (i+j) == index :
                continue
            sum += numbers[i + j]
            if (sum == number):
                print("gewonnen")
                return ((i, j))
            j += 1
            if (i+j) > len(numbers):
                break
            
    return (-1,-1)         
    

def main():
    numbers = einlesen("input.txt")
    window_size = 25
    (number, index) = is_number_a_sum_of_window_numbers(numbers, window_size)
    print("number: {}, index: {}".format(number, index))
    (start_index, offset) = is_number_sum_of_contiguous_numbers(number, numbers, index)
    print("startindex: {}, offset: {}".format(start_index, offset))
    if start_index > -1:
        print("contigues set: {}".format(numbers[start_index : start_index+offset+1]))
    numbers_range = numbers[start_index : start_index + offset + 1]
    min_number_of_range = min(numbers_range)
    max_number_of_range = max(numbers_range)
    result = min_number_of_range + max_number_of_range
    print("The result of part two is: {}".format(result))
    
    
if __name__ == "__main__":
    main()
