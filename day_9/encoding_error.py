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
            #print(window[i])
            #print(window[j])
            new_number = window[i] + window[j]
            if new_number == number_to_check:
                results.append(True)
            else:
                results.append(False)
    if True in results:
        return True
    else:
        return False

def is_number_a_sum_of_window_numbers(numbers):
    i = 0
    while i < (len(numbers)-5):
        x1 = numbers[i]
        x2 = numbers[i+1]
        x3 = numbers[i+2]
        x4 = numbers[i+3]
        x5 = numbers[i+4]
        window = [x1,x2,x3,x4,x5]
        number = numbers[i+5]
        isok = check_number_in_window(window,number)
        if isok == False:
            print(number)
        i += 1
    

def main():
    numbers = einlesen("small_input.txt")
    result = is_number_a_sum_of_window_numbers(numbers)
            
if __name__ == "__main__":
    main()
