def einlesen(input_path):
    file_handler = open(input_path, "r")
    input_data_lines = file_handler.readlines()
    list_of_input_lines = []
    
    for line in input_data_lines:
        new_line_input = line.replace(' ', '\n')
        list_of_input_lines.append(new_line_input)
    #print(list_of_input_lines)

    raw_records = []
    record_akku = ""
    for input_line in list_of_input_lines:
        if input_line != '\n':
            record_akku += input_line # string concatination
        else:
            raw_records.append(record_akku)
            record_akku = ""
    records = []        
    for raw_record in raw_records:
        splitted_record = raw_record.split('\n')
        akku_dictionary = {}
        for raw_entry in splitted_record:
            if len(raw_entry) != 0:
                splitted_entry = raw_entry.split(':')
                key = splitted_entry[0]
                value = splitted_entry[1]
                akku_dictionary[key] = value
        records.append(akku_dictionary)
    return records

def check_passport1(record, list_of_entry_keys):
    entry_ok = 0
    for entry_key in list_of_entry_keys:
        if entry_key in record:
            entry_ok += 1
    print(entry_ok)
    if len(list_of_entry_keys) != entry_ok:
        return False
    return True

def is_in_boundary(value, lower, higher):
    if value <= higher and value >= lower:
        return True
    return False

def check_birth_year(value):
    if is_in_boundary(int(value),1920,2002):
        return True
    return False

def check_issue_year(value):
    if is_in_boundary(int(value),2010,2020):
        return True
    return False

def check_expiration_year(value):
    if is_in_boundary(int(value), 2020, 2030):
        return True
    return False

def check_height(value):
    height_split_in = value.split('i')
    height_split_cm = value.split('c')

    if len(height_split_in) == 2:  # is inch?
        if height_split_in[1] == 'n': # is in at end
            int_value = 0
            try:
                int_value = int(height_split_in[0])
            except ValueError:
                return False
            if is_in_boundary(int_value,59,76):
                return True
            return False
    if len(height_split_cm) == 2:  # is cm?
        if height_split_cm[1] == 'm':  # is cm at end
            int_value = 0
            try:
                int_value = int(height_split_cm[0])
            except ValueError:
                return False    
            if is_in_boundary(int_value,150,193):
                return True
            return False
    return False    

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def check_haircolor(value):
    haircolor_split = value.split('#')
    if len(haircolor_split) == 2:
        if len(haircolor_split[1]) == 6:
            if is_hex(haircolor_split[1]):
                return True
    return False

def check_eyecolor(value):
    eyecolors = ['amb','blu','brn','gry','grn','hzl','oth']
    if value in eyecolors:
        return True
    return False

def check_passportid(value):
    if len(value) == 9:
        int_value = 0
        try:
            int_value = int(value)
        except ValueError:
            return False
        # if len(str(int_value)) == 9:
        #    print("false2")
        #    return False
        return True
    return False

def check_passport2(record, list_of_entry_keys, key_check_functions):
    entry_ok = 0
    for entry_key in list_of_entry_keys:
        if entry_key in record:
            value =  record[entry_key]
            check_function = key_check_functions[entry_key]
            if check_function(value):
                entry_ok += 1
    if len(list_of_entry_keys) != entry_ok:
        return False
    return True

def main():
    records = einlesen("input.txt")
    list_of_entry_keys = ["ecl","pid","eyr","hcl","byr","iyr","hgt"]
     
    valid_records = 0

    key_check_functions = {"ecl": check_eyecolor,
                           "pid": check_passportid,
                           "eyr": check_expiration_year,
                           "hcl": check_haircolor,
                           "byr": check_birth_year,
                           "iyr": check_issue_year,
                           "hgt": check_height}

    for record in records:
        is_valid = check_passport2(record, list_of_entry_keys, key_check_functions)
        if is_valid == True:
            valid_records += 1
    print(valid_records)
            

if __name__ == "__main__":
    main()
