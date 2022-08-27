def einlesen(input_path):
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()

    groups = []
    raw_group = []
    for line in input_data_lines:  # <- gruppe und person
        #print(repr(line)) -> prints fileoutput with newlines
        if line != '\n':
            person_raw_data = line.split('\n')
            raw_group.append(person_raw_data[0])
        else :
            groups.append(raw_group)
            raw_group = []
    groups.append(raw_group)        
    return groups


def calc_unique_answers_by_group(input):
    sum = 0
    for group in input:
        group_dict = {}
        for person in group:
            for answer_char in person:
                if not (answer_char in group_dict):
                    group_dict[answer_char] = True
        sum += len(group_dict)
    return sum


def calc_answer_used_by_all_members_of_group(input):
    sum = 0
    for group in input:
        group_dict = {}
        num_person = len(group)
        for person in group:
            for answer_char in person:
                if not (answer_char in group_dict):
                    group_dict[answer_char] = 1
                else:
                    group_dict[answer_char] += 1
        for key in group_dict:
            if (group_dict[key] == num_person):
                sum += 1
    return sum


def main():

    input_test = einlesen("input.txt")
    yes_answers = calc_unique_answers_by_group(input_test)
    yes_for_all_answers = calc_answer_used_by_all_members_of_group(input_test)
    print(yes_answers)
    print(yes_for_all_answers)
if __name__ == "__main__":
    main()
