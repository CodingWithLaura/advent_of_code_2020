def einlesen(input_path):
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()
    list_of_input_lines = []

    for line in input_data_lines:
        new_line_input = line.split('\n')
        list_of_input_lines.append(new_line_input[0])
    return list_of_input_lines
    

def calc_seat_id(input_string):
    lower_bound = 0
    upper_bound = 127

    for char in input_string[0:7]:
        schritte = upper_bound - lower_bound
        mitte = int((schritte - 1)/ 2) + lower_bound
        if char == 'F':
            upper_bound = mitte
        if char == 'B':
            lower_bound = mitte + 1
    first_value = lower_bound

    lower_bound = 0
    upper_bound = 7

    for char in input_string[7:]:
        schritte = upper_bound - lower_bound
        mitte = int((schritte - 1)/2) + lower_bound
        if char == 'L':
            upper_bound = mitte
        if char == 'R':
            lower_bound = mitte + 1
    second_value = lower_bound
    seat_id = first_value * 8 + second_value
    return seat_id


def max_seat_id(input):
    max_seat_id = 0
    for row_string in input:
        seat_id = calc_seat_id(row_string)
        #max seat id
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id    


def get_seat_id_list(input):
    seat_id_list = []
    for row_string in input:
        seat_id = calc_seat_id(row_string)
        seat_id_list.append(seat_id)
    return seat_id_list    

def find_seat(liste_seats):
    my_seat = 0 
    for i in range(0,len(liste_seats) - 1):
        if liste_seats[i+1] - liste_seats[i] != 1:
            my_seat = liste_seats[i] + 1
            return my_seat
    return -1        

def main():
    input = einlesen("input.txt")
    max_seat = max_seat_id(input)
    print("aufgabe1: max_seat_id: {}".format(max_seat))

    liste_seats = get_seat_id_list(input)
    liste_seats.sort()
    my_seat = find_seat(liste_seats)
    print(my_seat)

        
if __name__ == "__main__":
    main()
